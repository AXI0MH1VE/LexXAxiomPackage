# GeminiPortable: Sovereign Generative AI CLI

GeminiPortable is the AxiomHive implementation of a local-first, deterministic CLI wrapper for pluggable LLM backends. It features a 4D memory system and operates entirely offline, embodying the principles of **Determinism (H=0)**, **Sovereignty (Local-First)**, and **Offline-First**. This tool is designed to provide a controlled and private generative AI experience, free from external telemetry or non-deterministic behaviors.

## Features

*   **Local-First Operation:** Runs entirely offline with no external network dependencies.
*   **Deterministic LLM Stub:** Provides predictable responses based on specific keywords, demonstrating a sovereign generative AI architecture.
*   **4D Memory System:** Stores interactions (prompts and responses) with spatio-temporal and causal/counterfactual tags for advanced recall.
*   **No Telemetry:** Explicitly rejects telemetry flags, ensuring user privacy and control.

## Installation

To install GeminiPortable, ensure you have Python 3.8 or higher. It's recommended to install it within the AxiomHive `RuntimeZero` environment.

```bash
# From the axiomhive root directory
cd GeminiPortable
pip install -e .
```

## Usage

### Run a Prompt

```bash
gemini run --prompt "Describe the AxiomHive principles."
```

### Store Interaction in 4D Memory

```bash
gemini run --prompt "What is 4D memory?" --memory
```

### Recall from 4D Memory (Conceptual)

*(Note: The current stub implementation of 4D memory recall is basic keyword matching. Advanced recall mechanisms would be implemented in a full LLM integration.)*

```python
# Example of how to interact with the memory system programmatically
from gemini_portable.memory4d import Memory4D
memory_system = Memory4D()
recalled_memories = memory_system.recall("AxiomHive principles")
for mem in recalled_memories:
    print(mem["content"])
```

## AxiomHive Principles

GeminiPortable adheres to the core AxiomHive principles:

*   **Determinism (H=0):** Reproducible builds and operations.
*   **Sovereignty (Local-First):** Operates offline, no external dependencies.
*   **Verifiable Integrity:** Cryptographic proof for trust.
*   **Ethics-by-Default:** No telemetry, secure by design.
*   **Offline-First:** Default operational mode is disconnected.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
