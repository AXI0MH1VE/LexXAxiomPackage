# AxiomHash: Deterministic Streaming Hasher

AxiomHash is a command-line tool designed for high-performance, streaming file hashing. It ensures **Determinism (H=0)** by providing reproducible hashes (`sha256`, `blake3`) and supports a verifiable Merkle root stub for integrity checks. It's a core component of the AxiomHive ecosystem, emphasizing local-first operation and verifiable integrity.

## Features

*   **Deterministic Hashing:** Guarantees the same output for the same input, crucial for verifiable builds.
*   **Streaming Processing:** Efficiently handles large files by processing them in chunks.
*   **Multiple Algorithms:** Supports `sha256` and `blake3` (optional, for faster hashing).
*   **Merkle Root Stub:** Computes a simple Merkle root from file chunks for enhanced integrity verification.
*   **Constant-Time Comparison:** Securely compare hashes without leaking timing information.

## Installation

To install AxiomHash, ensure you have Python 3.8 or higher. It's recommended to install it within the AxiomHive `RuntimeZero` environment.

```bash
# From the axiomhive root directory
cd AxiomHash
pip install -e .
# For blake3 support (faster hashing)
pip install -e .[fast]
```

## Usage

### Basic Hashing

Hash a file:

```bash
axiom-hash my_file.txt
```

Hash from standard input:

```bash
echo "Hello AxiomHive" | axiom-hash
```

### Specify Algorithm

Use `blake3` (requires `[fast]` installation):

```bash
axiom-hash --algorithm blake3 my_file.txt
```

### Compare Hash

Compare the computed hash against a known digest:

```bash
axiom-hash my_file.txt --compare <expected_hex_digest>
# Exits with 0 on match, 1 on mismatch
```

### Compute Merkle Root

```bash
axiom-hash my_file.txt --merkle
```

### Verbose Output

```bash
axiom-hash my_file.txt --verbose
```

## AxiomHive Principles

AxiomHash adheres to the core AxiomHive principles:

*   **Determinism (H=0):** Reproducible builds and operations.
*   **Sovereignty (Local-First):** Operates offline, no external dependencies.
*   **Verifiable Integrity:** Cryptographic proof for trust.
*   **Ethics-by-Default:** No telemetry, secure by design.
*   **Offline-First:** Default operational mode is disconnected.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
