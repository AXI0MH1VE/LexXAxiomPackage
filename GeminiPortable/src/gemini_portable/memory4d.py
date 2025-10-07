import os
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional

class Memory4D:
    """
    A local-first, persistent 4D memory system.
    Stores entries as JSON logs under ~/.axiom/memory/.
    """
    def __init__(self, base_path: Optional[Path] = None) -> None:
        if base_path:
            self.memory_dir = base_path
        else:
            self.memory_dir = Path.home() / ".axiom" / "memory"
        
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.memory_file = self.memory_dir / "4d_log.jsonl"
        self.memory_store: List[Dict[str, Any]] = self._load()

    def _load(self) -> List[Dict[str, Any]]:
        """Loads memories from the persistent JSONL file."""
        if not self.memory_file.exists():
            return []
        
        memories = []
        with self.memory_file.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    memories.append(json.loads(line))
                except json.JSONDecodeError:
                    # Log this in a real system; for now, we skip corrupted lines
                    pass
        return memories

    def _save(self, memory_entry: Dict[str, Any]) -> None:
        """Appends a single memory entry to the persistent JSONL file."""
        with self.memory_file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(memory_entry) + "\n")

    def store(self, content: str, temporal: float, spatial: str, causal: str, counterfactual: str) -> None:
        """Stores a piece of content with associated 4D tags."""
        entry = {
            "content": content,
            "temporal_tag": temporal,
            "spatial_tag": spatial,
            "causal_note": causal,
            "counterfactual_note": counterfactual,
        }
        self.memory_store.append(entry)
        self._save(entry)

    def recall(self, query: str) -> List[Dict[str, Any]]:
        """Recalls relevant memories based on a simple keyword match in the content."""
        query_lower = query.lower()
        return [
            mem for mem in self.memory_store if query_lower in mem["content"].lower()
        ]
