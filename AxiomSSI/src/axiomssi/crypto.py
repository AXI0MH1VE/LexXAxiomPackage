from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

def generate_keypair() -> tuple[ed25519.Ed25519PrivateKey, ed25519.Ed25519PublicKey]:
    """Generates an Ed25519 private/public key pair."""
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key: ed25519.Ed25519PrivateKey, message: bytes) -> bytes:
    """Signs a message with a private key."""
    return private_key.sign(message)

def verify_signature(public_key: ed25519.Ed25519PublicKey, signature: bytes, message: bytes) -> bool:
    """Verifies a signature with a public key."""
    try:
        public_key.verify(signature, message)
        return True
    except InvalidSignature:
        return False

def serialize_private_key(private_key: ed25519.Ed25519PrivateKey) -> str:
    """Serializes a private key to a PEM string."""
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem.decode('ascii')

def serialize_public_key(public_key: ed25519.Ed25519PublicKey) -> str:
    """Serializes a public key to a PEM string."""
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem.decode('ascii')

def deserialize_private_key(pem_data: str) -> ed25519.Ed25519PrivateKey:
    """Deserializes a private key from a PEM string."""
    key = serialization.load_pem_private_key(pem_data.encode('ascii'), password=None)
    assert isinstance(key, ed25519.Ed25519PrivateKey)
    return key

def deserialize_public_key(pem_data: str) -> ed25519.Ed25519PublicKey:
    """Deserializes a public key from a PEM string."""
    key = serialization.load_pem_public_key(pem_data.encode('ascii'))
    assert isinstance(key, ed25519.Ed25519PublicKey)
    return key
