# AxiomSSI: Sovereign Self-Identity

AxiomSSI is a local-first, sovereign self-identity tool designed for managing cryptographic keypairs and digital signatures. It empowers users with absolute control over their digital identities, operating entirely offline and without reliance on external authorities. AxiomSSI is a foundational component of the AxiomHive ecosystem, embodying the principles of **Sovereignty (Local-First)** and **Verifiable Integrity**.

## Features

*   **Local Key Management:** Generates and securely stores `ed25519` private/public key pairs locally.
*   **Offline Operation:** All identity and signing operations are performed entirely offline.
*   **Digital Signing:** Sign any file with your managed identity.
*   **Signature Verification:** Verify the authenticity and integrity of signed files.
*   **DID (Decentralized Identifier) Support:** Generates `did:axiom:local:` DIDs for managed identities.

## Installation

To install AxiomSSI, ensure you have Python 3.8 or higher. It's recommended to install it within the AxiomHive `RuntimeZero` environment.

```bash
# From the axiomhive root directory
cd AxiomSSI
pip install -e .
```

## Usage

### Create an Identity

```bash
axiom id create --handle "@your_handle"
```

### List Identities

```bash
axiom id list
```

### Sign a File

```bash
axiom sign --handle "@your_handle" --in my_document.txt --out my_document.sig
```

### Verify a Signature

```bash
axiom verify --handle "@your_handle" --in my_document.txt --sig my_document.sig
# Exits with 0 on success, 1 on failure
```

## AxiomHive Principles

AxiomSSI adheres to the core AxiomHive principles:

*   **Determinism (H=0):** Reproducible builds and operations.
*   **Sovereignty (Local-First):** Operates offline, no external dependencies.
*   **Verifiable Integrity:** Cryptographic proof for trust.
*   **Ethics-by-Default:** No telemetry, secure by design.
*   **Offline-First:** Default operational mode is disconnected.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
