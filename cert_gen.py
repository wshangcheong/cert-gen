from datetime import datetime, timedelta, timezone
from pathlib import Path

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

cert_name = "my-app-cert" # update this
cert_validity_days = 3650  # update this (e.g., 3650 for 10 years)
output_dir = Path(__file__).resolve().parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Certificate subject
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, cert_name),
])

# Build certificate
certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(timezone.utc))
    .not_valid_after(
        datetime.now(timezone.utc) + timedelta(days=cert_validity_days)
    )
    .sign(private_key, hashes.SHA256())
)

# Save private key
with (output_dir / "private.pem").open("wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Save public certificate
with (output_dir / "public.pem").open("wb") as f:
    f.write(
        certificate.public_bytes(
            serialization.Encoding.PEM
        )
    )

print("Generated:")
print(f"  {output_dir / 'private.pem'}")
print(f"  {output_dir / 'public.pem'}")