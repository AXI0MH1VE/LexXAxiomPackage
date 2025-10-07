import pytest
from click.testing import CliRunner
from pathlib import Path
from unittest.mock import patch
import os
import stat
from axiomssi.cli import main
from axiomssi.keystore import KEYSTORE_FILE, REQUIRED_PERMS

 @pytest.fixture
def runner(tmp_path: Path):
    """Fixture to mock the home directory and provide a CliRunner."""
    with patch('axiomssi.keystore.KEYSTORE_DIR', tmp_path):
        # Ensure the patched KEYSTORE_FILE is updated as well
        with patch('axiomssi.keystore.KEYSTORE_FILE', tmp_path / "keys.json"):
            yield CliRunner()

def test_id_create_and_list(runner: CliRunner):
    result_create = runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    assert result_create.exit_code == 0
    assert "Successfully created identity" in result_create.output
    assert " @testuser" in result_create.output

    result_list = runner.invoke(main, ['id', 'list'])
    assert result_list.exit_code == 0
    assert " @testuser" in result_list.output
    assert "did:axiom:local:testuser" in result_list.output

def test_id_create_duplicate_handle(runner: CliRunner):
    runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    result = runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    assert result.exit_code == 1
    assert "Error: Handle ' @testuser' already exists." in result.output

def test_keystore_permissions(runner: CliRunner, tmp_path: Path):
    keystore_file = tmp_path / "keys.json"
    runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    
    assert keystore_file.exists()
    perms = stat.S_IMODE(keystore_file.stat().st_mode)
    assert perms == REQUIRED_PERMS

def test_keystore_permissions_correction(runner: CliRunner, tmp_path: Path):
    keystore_file = tmp_path / "keys.json"
    # Pre-create the file with wrong permissions
    keystore_file.touch()
    os.chmod(keystore_file, 0o777)
    
    # The first command should fix it
    result = runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    assert result.exit_code == 0
    
    perms = stat.S_IMODE(keystore_file.stat().st_mode)
    assert perms == REQUIRED_PERMS
