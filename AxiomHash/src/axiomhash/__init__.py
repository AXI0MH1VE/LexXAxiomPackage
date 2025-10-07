# AxiomHash: Deterministic Streaming Hasher. H=0 Primacy.
import hashlib
import sys
from typing import IO, List, Optional, Tuple, Any

try:
    from blake3 import blake3
except ImportError:
    blake3 = None

CHUNK_SIZE = 65536  # 64KB
SUPPORTED_ALGORITHMS = ["sha256", "blake3"]

def get_hasher(algorithm: str = "sha256") -> Any:
    """Returns a hasher instance for the given algorithm."""
    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}. Supported: {SUPPORTED_ALGORITHMS}")
    if algorithm == "blake3":
        if blake3 is None:
            raise ImportError("blake3 is not installed. Use 'pip install axiomhash-cli[fast]'")
        return blake3()
    return hashlib.sha256()

def stream_hash(
    stream: IO[bytes], algorithm: str = "sha256"
) -> Tuple[str, List[str]]:
    """Hashes a stream of bytes, returning the final digest and a list of chunk hashes."""
    hasher = get_hasher(algorithm)
    chunk_hashes = []
    while chunk := stream.read(CHUNK_SIZE):
        chunk_hasher = get_hasher(algorithm)
        chunk_hasher.update(chunk)
        chunk_hashes.append(chunk_hasher.hexdigest())
        hasher.update(chunk)
    return hasher.hexdigest(), chunk_hashes

def compute_merkle_root(chunk_hashes: List[str], algorithm: str = "sha256") -> str:
    """
    Computes a simple Merkle root from a list of chunk hashes.
    v2.0 Stub: Simple concatenation and hash of all chunk hashes.
    """
    if not chunk_hashes:
        return get_hasher(algorithm).hexdigest()
    merkle_base = "".join(chunk_hashes).encode("utf-8")
    root_hasher = get_hasher(algorithm)
    root_hasher.update(merkle_base)
    return root_hasher.hexdigest()

def constant_time_compare(a: str, b: str) -> bool:
    """Performs a constant-time comparison of two hex digests."""
    return hashlib.compare_digest(a, b)
