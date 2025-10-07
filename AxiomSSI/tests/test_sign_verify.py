import pytest
from click.testing import CliRunner
from pathlib import Path
from unittest.mock import patch
from axiomssi.cli import main

 @pytest.fixture
def runner(tmp_path: Path):
    """Fixture to mock the home directory and provide a CliRunner."""
    with patch('axiomssi.keystore.KEYSTORE_DIR', tmp_path):
        yield CliRunner()

def test_sign_verify_roundtrip(runner: CliRunner, tmp_path: Path):
    # 1. Create an identity
    result = runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    assert result.exit_code == 0

    # 2. Create a file to sign
    message_file = tmp_path / "message.txt"
    message_file.write_text("verifiable integrity")
    sig_file = tmp_path / "message.sig"

    # 3. Sign the file
    result = runner.invoke(main, ['sign', '--handle', ' @testuser', '--in', str(message_file), '--out', str(sig_file)])
    assert result.exit_code == 0
    assert sig_file.exists() and sig_file.read_bytes()

    # 4. Verify the signature
    result = runner.invoke(main, ['verify', '--handle', ' @testuser', '--in', str(message_file), '--sig', str(sig_file)])
    assert result.exit_code == 0
    assert "Verification successful" in result.output

def test_verify_failure_wrong_message(runner: CliRunner, tmp_path: Path):
    runner.invoke(main, ['id', 'create', '--handle', ' @testuser'])
    
    message_file = tmp_path / "message.txt"
    message_file.write_text("original message")
    sig_file = tmp_path / "message.sig"
    
    runner.invoke(main, ['sign', '--handle', ' @testuser', '--in', str(message_file), '--out', str(sig_file)])

    tampered_file = tmp_path / "tampered.txt"
    tampered_file.write_text("tampered message")

    result = runner.invoke(main, ['verify', '--handle', ' @testuser', '--in', str(tampered_file), '--sig', str(sig_file)])
    assert result.exit_code == 1
    assert "Verification FAILED" in result.output

def test_verify_failure_wrong_key(runner: CliRunner, tmp_path: Path):
    runner.invoke(main, ['id', 'create', '--handle', ' @user1'])
    runner.invoke(main, ['id', 'create', '--handle', ' @user2'])
    
    message_file = tmp_path / "message.txt"
    message_file.write_text("message from user1")
    sig_file = tmp_path / "message.sig"
    
    # Sign as user1
    runner.invoke(main, ['sign', '--handle', ' @user1', '--in', str(message_file), '--out', str(sig_file)])

    # Verify as user2
    result = runner.invoke(main, ['verify', '--handle', ' @user2', '--in', str(message_file), '--sig', str(sig_file)])
    assert result.exit_code == 1
    assert "Verification FAILED" in result.output

def test_sign_nonexistent_handle(runner: CliRunner, tmp_path: Path):
    message_file = tmp_path / "message.txt"
    message_file.write_text("some data")
    sig_file = tmp_path / "message.sig"

    result = runner.invoke(main, ['sign', '--handle', ' @ghost', '--in', str(message_file), '--out', str(sig_file)])
    assert result.exit_code == 1
    assert "Error: Identity ' @ghost' not found." in result.output
