# Get Credencials API

This API retrieves credentials from a secret manager, which facilitates versioning, decoupling, and secure management of secrets for applications. Using a secret manager helps streamline the process of updating and maintaining sensitive information without embedding it directly in the app.


## Recomendations:
- Credentials API: Should be configured to restrict access exclusively to the web app by enabling CORS (Cross-Origin Resource Sharing) filters, ensuring that only authorized requests from the designated web application are permitted. Additionally, it is recommended to integrate a DDoS (Distributed Denial-of-Service) protection tool to safeguard the API against malicious traffic and prevent potential attacks.
