#!/bin/bash
set -e

echo "--- AxiomHive RuntimeZero Installer ---"
# ... (initial checks and variable setup remain the same) ...

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
INSTALL_DIR="$SCRIPT_DIR/../_runtime"
VENV_DIR="$INSTALL_DIR/.venv"
BIN_DIR="$INSTALL_DIR/bin"
PROJECT_ROOT="$SCRIPT_DIR/.."

echo "Installing to: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Create virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate venv for this script
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

echo "Installing AxiomHive components..."
# Install all sovereign tools from the local monorepo source
pip install --editable "$PROJECT_ROOT/AxiomHash"
pip install --editable "$PROJECT_ROOT/AxiomSSI"
pip install --editable "$PROJECT_ROOT/GeminiPortable"
# Stubs for Athena and Tesseract are also installed
pip install --editable "$PROJECT_ROOT/Athena"
pip install --editable "$PROJECT_ROOT/Tesseract"


echo "Creating unified launcher 'axiom-run' and activation script..."
# ... (launcher creation remains the same) ...

LAUNCHER_PATH="$BIN_DIR/axiom-run"
cat > "$LAUNCHER_PATH" << EOF
#!/bin/bash
# AxiomHive Launcher v1.0
export AXIOM_OFFLINE=1
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"
exec "\$@"
EOF
chmod +x "$LAUNCHER_PATH"

# Create an activation script for convenience
ACTIVATOR_PATH="$BIN_DIR/activate"
cat > "$ACTIVATOR_PATH" << EOF
#!/bin/bash
# AxiomHive Environment Activator
export AXIOM_OFFLINE=1
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"
echo "AxiomHive environment activated. Tools (axiom, axiom-hash, gemini) are on your PATH."
EOF



echo ""
echo "--- Installation Complete ---"
echo "To activate the AxiomHive environment, run:"

echo ""

echo "  source \"$ACTIVATOR_PATH\""

echo ""

"This will add the correct, sovereign tools to your PATH."
echo "Then you can run 'gemini run --prompt "..."' as intended."
