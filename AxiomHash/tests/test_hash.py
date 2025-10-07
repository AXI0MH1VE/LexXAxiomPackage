import subprocess
import sys
from pathlib import Path
import pytest
from axiomhash import constant_time_compare, compute_merkle_root, stream_hash

SAMPLE_CONTENT = b"Alexis Adams Primacy Manifested"
EXPECTED_SHA256 = "d229458537b4fb5e2361665a88e93223e3851b39c63673e4b7a4216503c8744c"

 @pytest.fixture
def test_file(tmp_path: Path) -> Path:
    f = tmp_path / "test.txt"
    f.write_bytes(SAMPLE_CONTENT)
    return f

def run_cli(args, input_data=None):
    cmd = [sys.executable, "-m", "axiomhash_cli"] + args
    result = subprocess.run(
        cmd,
        input=input_data,
        capture_output=True,
        text=True,
        check=False,
    )
    return result

def test_sha256_hash_file(test_file: Path):
    result = run_cli([str(test_file)])
    assert result.returncode == 0
    assert f"AxiomHash: {EXPECTED_SHA256}" in result.stdout

def test_sha256_hash_stdin():
    result = run_cli([], input_data=SAMPLE_CONTENT)
    assert result.returncode == 0
    assert f"AxiomHash: {EXPECTED_SHA256}" in result.stdout

def test_compare_success(test_file: Path):
    result = run_cli([str(test_file), "--compare", EXPECTED_SHA256])
    assert result.returncode == 0

def test_compare_failure(test_file: Path):
    result = run_cli([str(test_file), "--compare", "deadbeef" * 8])
    assert result.returncode == 1

def test_merkle_root_multichunk(tmp_path: Path):
    # Force multiple chunks
    content = SAMPLE_CONTENT * 5000
    multi_chunk_file = tmp_path / "multichunk.txt"
    multi_chunk_file.write_bytes(content)
    
    result = run_cli([str(multi_chunk_file), "--merkle", "-v"])
    assert result.returncode == 0
    assert "Merkle-Root:" in result.stdout
    assert "Chunks: 2" in result.stderr

def test_constant_time_compare():
    assert constant_time_compare(EXPECTED_SHA256, EXPECTED_SHA256) is True
    assert constant_time_compare(EXPECTED_SHA256, "a" * 64) is False
    assert constant_time_compare("a" * 64, EXPECTED_SHA256) is False

def test_blake3_support(test_file: Path):
    try:
        import blake3
        result = run_cli([str(test_file), "-a", "blake3"])
        assert result.returncode == 0
        assert "AxiomHash:" in result.stdout
    except ImportError:
        pytest.skip("blake3 not installed, skipping test")
