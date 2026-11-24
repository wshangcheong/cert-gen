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

The script automatically creates an `output/` folder and writes:

- `output/private.pem`: the unencrypted PKCS8 private key
- `output/public.pem`: the PEM-encoded self-signed certificate

The certificate name and validity period can be changed in `cert_gen.py` with the `cert_name` and `cert_validity_days` settings.