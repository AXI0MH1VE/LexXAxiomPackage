import json
from pathlib import Path
from unittest.mock import patch

from gemini_portable.memory4d import Memory4D

def test_memory_initialization_and_storage(tmp_path: Path):
    """Test that memory can be initialized, store data, and persist it."""
    mem_system = Memory4D(base_path=tmp_path)
    assert mem_system.memory_dir == tmp_path
    
    # Store an entry
    content = "Test content for recall"
    mem_system.store(
        content=content,
        temporal=123.45,
        spatial="test_env",
        causal="test_case_run",
        counterfactual="n/a"
    )
    
    # Verify it's in the in-memory store
    assert len(mem_system.memory_store) == 1
    assert mem_system.memory_store[0]["content"] == content

    # Verify it was persisted to the file
    log_file = tmp_path / "4d_log.jsonl"
    assert log_file.exists()
    
    with log_file.open("r") as f:
        data = json.loads(f.readline())
        assert data["content"] == content
        assert data["temporal_tag"] == 123.45

def test_memory_recall(tmp_path: Path):
    """Test the recall functionality."""
    mem_system = Memory4D(base_path=tmp_path)
    mem_system.store("First entry about AxiomHive", 1.0, "a", "b", "c")
    mem_system.store("Second entry about Sovereignty", 2.0, "a", "b", "c")
    mem_system.store("Third entry, unrelated", 3.0, "a", "b", "c")

    # Recall a specific term
    recalled = mem_system.recall("Sovereignty")
    assert len(recalled) == 1
    assert recalled[0]["content"] == "Second entry about Sovereignty"

    # Recall a broad term
    recalled_broad = mem_system.recall("entry")
    assert len(recalled_broad) == 3

    # Recall a non-existent term
    recalled_none = mem_system.recall("nonexistent")
    assert len(recalled_none) == 0

def test_memory_loading_from_existing_file(tmp_path: Path):
    """Test that Memory4D loads existing data upon initialization."""
    log_file = tmp_path / "4d_log.jsonl"
    entry1 = {"content": "entry one", "temporal_tag": 1.0, "spatial_tag": "a", "causal_note": "b", "counterfactual_note": "c"}
    entry2 = {"content": "entry two", "temporal_tag": 2.0, "spatial_tag": "a", "causal_note": "b", "counterfactual_note": "c"}

    with log_file.open("w") as f:
        f.write(json.dumps(entry1) + "\n")
        f.write(json.dumps(entry2) + "\n")
        
    # Create a new instance that should load from the file
    mem_system = Memory4D(base_path=tmp_path)
    assert len(mem_system.memory_store) == 2
    assert mem_system.memory_store[1]["content"] == "entry two"
