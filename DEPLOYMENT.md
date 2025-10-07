# AxiomHive: Deployment and Validation

This guide provides the exact commands to install, test, and validate the AxiomHive starter stack.

## 1. Installation

From the `axiomhive` root directory, run the `RuntimeZero` installer. This will create a local, sandboxed environment in `_runtime/` and install all AxiomHive tools.

```bash
bash RuntimeZero/install.sh
```

After installation, add the launcher to your shell's PATH as instructed by the script:

```bash
# Add this to your ~/.bashrc or ~/.zshrc for persistent access
export PATH="/path/to/your/axiomhive/_runtime/bin:$PATH"

# Or, for the current session:
source /path/to/your/axiomhive/_runtime/bin/activate
```

## 2. Running Core Tools

Once the environment is active, you can use the installed tools directly.

```bash
# Verify AxiomHash
echo "test" | axiom-hash

# Verify AxiomSSI
axiom id list

# Verify GeminiPortable
gemini run --prompt "Describe the AxiomHive principles."
```

## 3. Running All Tests

To validate the integrity and correctness of the entire stack, you can run all tests from the root of the monorepo.

```bash
# Install development dependencies for all projects
pip install -e AxiomHash/[dev] -e AxiomSSI/[dev] -e GeminiPortable/[dev] -e Athena/[dev] -e Tesseract/[dev]

# Run all tests
pytest AxiomHash/ AxiomSSI/ GeminiPortable/ Athena/ Tesseract/
```

## 4. Producing Integrity Attestation

To verify the integrity of the project's foundational documents, run the attestation tool from the `axiomhive` root directory:

```bash
python3 Shared/tools/integrity_attest.py
```

This will generate `VALIDATION/integrity_attestation.txt`. The hash in this file should match the hash from the latest trusted CI run.
