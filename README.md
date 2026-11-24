# Certificate Generator

This script generates a self-signed RSA certificate and private key.

## Setup

This project requires Python 3.14 and uses [uv](https://docs.astral.sh/uv/) for environment and dependency management.

From the project directory, create the environment and install dependencies:

```powershell
uv sync
```

## Usage

Run the script through uv:

```powershell
uv run python cert_gen.py
```

Or run the configured uv console script:

```powershell
uv run cert-gen
```

The script automatically creates an `output/` folder and writes:

- `output/private.pem`: the unencrypted PKCS8 private key
- `output/public.pem`: the PEM-encoded self-signed certificate

The certificate name and validity period can be changed in `cert_gen.py` with the `cert_name` and `cert_validity_days` settings.

## Security note

The generated private key is currently written as an unencrypted PEM file. Keep the local `output/` directory and generated key restricted to authorized users and processes, and remove or securely archive the local copy after uploading it to a secure location such as Azure Key Vault or another protected secret store.

Encrypted private-key output and configurable secure-file permissions are future enhancements. Until then, use this tool only in a trusted environment and avoid committing or sharing `private.pem`.