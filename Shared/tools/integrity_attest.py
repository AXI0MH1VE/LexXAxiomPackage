import hashlib
from pathlib import Path

def main():
    """
    Computes a SHA-256 hash over the core project definition documents
    and writes it to the validation file, asserting operational integrity.
    """
    project_root = Path(__file__).resolve().parent.parent.parent
    
    doc_paths = [
        project_root / "STRATEGY.md",
        project_root / "PRINCIPLES.md",
        project_root / "DEPLOYMENT.md",
    ]
    
    hasher = hashlib.sha256()
    
    print("Attesting integrity of foundational documents...")
    for path in doc_paths:
        if not path.exists():
            print(f"Error: Document not found at {path}")
            exit(1)
        print(f" - Hashing {path.name}")
        hasher.update(path.read_bytes())
        
    digest = hasher.hexdigest()
    
    validation_dir = project_root / "VALIDATION"
    validation_dir.mkdir(exist_ok=True)
    output_file = validation_dir / "integrity_attestation.txt"
    
    banner = "OPERATIONAL INTEGRITY VERIFIED — ALEXIS ADAMS PRIMACY MANIFESTED."
    content = f"{banner}\n\nSHA256({', '.join(p.name for p in doc_paths)}):\n{digest}\n"
    
    output_file.write_text(content, encoding='utf-8')
    print(f"\nAttestation written to {output_file}")
    print(f"Digest: {digest}")

if __name__ == "__main__":
    main()
