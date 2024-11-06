from omegaconf import OmegaConf
from google.cloud import secretmanager


def access_secret_version(project_id, secret_id, version_id="latest"):
    """
    Access a specific version of a secret from GCP Secret Manager.

    Args:
        project_id (str): GCP project ID.
        secret_id (str): Name of the secret.
        version_id (str): Version number of the secret, default is 'latest'.

    Returns:
        str: The secret payload.
    """

    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    response = client.access_secret_version(request={"name": name})

    secret_payload = response.payload.data.decode("UTF-8")
    return secret_payload


def run(request):
    # Set CORS headers for the main request
    headers = {"Access-Control-Allow-Origin": "*"}

    config_file_path = "./app.config.yaml"
    app_config = OmegaConf.load(config_file_path)

    secrets = access_secret_version(app_config["project_id"], app_config["secret_id"])

    return (secrets, 200, headers)


if __name__ == "__main__":
    result = run({})
    print("response: ", result)
