# Security

To report security vulnerabilities, please contact the maintainers privately. Do not open a public issue for security-sensitive information.

Guidelines:
- Use token-based authentication for the listener.
- Default to binding the listener to localhost or a Unix domain socket to avoid remote exposure.
- Validate incoming JSON and cap execution timeouts to avoid long-running or blocking scripts.
