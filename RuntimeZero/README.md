# RuntimeZero: AxiomHive Local Installer

RuntimeZero is the foundational installer for the AxiomHive ecosystem. It sets up a sandboxed, local-first environment, ensuring that all AxiomHive tools operate with pinned dependencies and isolated execution. This guarantees **Determinism (H=0)** and **Sovereignty (Local-First)** by preventing external interference and ensuring reproducible builds.

## Features

*   **Sandboxed Environment:** Creates a dedicated Python virtual environment (`_runtime/`) for all AxiomHive tools.
*   **Pinned Dependencies:** Installs all tool dependencies with exact version pinning for deterministic builds.
*   **Local-First Installation:** All components are installed from local source, eliminating external network dependencies during setup.
*   **Unified Launcher:** Provides an `axiom-run` script to easily execute AxiomHive tools within the sandboxed environment.
*   **Environment Activation:** Offers a convenient `activate` script to set up the shell environment for AxiomHive tools.

## Installation

To install the AxiomHive stack using RuntimeZero, navigate to the `axiomhive` root directory and run the `install.sh` script:

```bash
bash RuntimeZero/install.sh
```

This script will:

1.  Create the `_runtime/` directory.
2.  Set up a Python virtual environment within `_runtime/`.
3.  Install all AxiomHive components (AxiomHash, AxiomSSI, GeminiPortable, Athena, Tesseract) in editable mode from their local source directories.
4.  Create the `axiom-run` unified launcher and an environment `activate` script.

## Usage

### Activating the AxiomHive Environment

After installation, you can activate the AxiomHive environment in your current shell session:

```bash
source /path/to/your/axiomhive/_runtime/bin/activate
```

This will add the AxiomHive tools (e.g., `axiom-hash`, `axiom`, `gemini`) to your PATH.

### Using the Unified Launcher

Alternatively, you can use the `axiom-run` launcher to execute any AxiomHive command without explicitly activating the environment:

```bash
/path/to/your/axiomhive/_runtime/bin/axiom-run axiom-hash my_file.txt
```

## AxiomHive Principles

RuntimeZero adheres to the core AxiomHive principles:

*   **Determinism (H=0):** Reproducible builds and operations.
*   **Sovereignty (Local-First):** Operates offline, no external dependencies.
*   **Verifiable Integrity:** Cryptographic proof for trust.
*   **Ethics-by-Default:** No telemetry, secure by design.
*   **Offline-First:** Default operational mode is disconnected.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
