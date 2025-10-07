# Contributing to AxiomHash

We welcome contributions to AxiomHash! By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

1.  **Fork the repository:** Start by forking the `LexXAxiomPackage` repository on GitHub.
2.  **Clone your fork:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/LexXAxiomPackage.git
    cd LexXAxiomPackage/AxiomHash
    ```
3.  **Create a new branch:** Choose a descriptive name for your branch.
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **Make your changes:** Implement your feature or bug fix.
5.  **Write tests:** Ensure your changes are covered by unit tests. Run tests with `pytest`.
6.  **Run linters and formatters:** We use `ruff` for linting and formatting. Ensure your code adheres to the project's style.
    ```bash
    ruff check . --fix
    ruff format .
    ```
7.  **Commit your changes:** Write clear and concise commit messages.
    ```bash
    git commit -m "feat: Add new feature" # or "fix: Fix bug in X"
    ```
8.  **Push to your fork:**
    ```bash
    git push origin feature/your-feature-name
    ```
9.  **Open a Pull Request:** Go to the original `LexXAxiomPackage` repository on GitHub and open a pull request from your branch.

## Code Style

*   Follow PEP 8 guidelines.
*   Use type hints for all functions and variables.
*   Write clear and concise comments where necessary.

## Testing

All new features and bug fixes must be accompanied by appropriate unit tests. To run the tests:

```bash
pytest
```

## Reporting Bugs

If you find a bug, please open an issue on GitHub. Provide a clear description of the bug, steps to reproduce it, and expected behavior.

## Feature Requests

For new features, please open an issue to discuss your idea before implementing it. This helps ensure alignment with the project's vision.
