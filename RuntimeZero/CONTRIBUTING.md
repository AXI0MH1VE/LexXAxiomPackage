# Contributing to RuntimeZero

We welcome contributions to RuntimeZero! By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

1.  **Fork the repository:** Start by forking the `LexXAxiomPackage` repository on GitHub.
2.  **Clone your fork:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/LexXAxiomPackage.git
    cd LexXAxiomPackage/RuntimeZero
    ```
3.  **Create a new branch:** Choose a descriptive name for your branch.
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **Make your changes:** Implement your feature or bug fix.
5.  **Write tests:** Ensure your changes are covered by unit tests. (Note: RuntimeZero primarily involves shell scripting and environment setup; testing might involve integration tests or manual verification).
6.  **Run linters and formatters:** Ensure your shell scripts adhere to best practices. (e.g., `shellcheck` for `.sh` files).
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

*   Shell scripts should be POSIX compliant where possible.
*   Use clear variable names and comments.
*   Ensure scripts are idempotent (running them multiple times has the same effect as running once).

## Testing

Due to the nature of environment setup, testing RuntimeZero often involves:

*   **Manual Verification:** Running the `install.sh` script and verifying the environment setup and tool functionality.
*   **Integration Tests:** Automated tests that run the installer and then execute commands from the installed AxiomHive tools to ensure they function correctly.

## Reporting Bugs

If you find a bug, please open an issue on GitHub. Provide a clear description of the bug, steps to reproduce it, and expected behavior.

## Feature Requests

For new features, please open an issue to discuss your idea before implementing it. This helps ensure alignment with the project's vision.
