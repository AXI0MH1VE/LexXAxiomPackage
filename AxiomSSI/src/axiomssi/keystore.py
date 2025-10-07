import os
import json
from pathlib import Path
from typing import Dict, Any, Optional, List

from . import crypto

KEYSTORE_DIR = Path(os.path.expanduser("~/.axiom"))
KEYSTORE_FILE = KEYSTORE_DIR / "keys.json"
REQUIRED_PERMS = 0o600

class KeystoreError(Exception):
    pass

def _ensure_keystore() -> None:
    """Ensures the keystore directory and file exist with correct permissions."""
    try:
        KEYSTORE_DIR.mkdir(mode=0o700, exist_ok=True)
        if not KEYSTORE_FILE.exists():
            KEYSTORE_FILE.touch(mode=REQUIRED_PERMS)
            KEYSTORE_FILE.write_text("{}", encoding='utf-8')
        
        current_perms = KEYSTORE_FILE.stat().st_mode & 0o777
        if current_perms != REQUIRED_PERMS:
            os.chmod(KEYSTORE_FILE, REQUIRED_PERMS)
            current_perms = KEYSTORE_FILE.stat().st_mode & 0o777
            if current_perms != REQUIRED_PERMS:
                 raise KeystoreError(
                    f"Failed to set keystore permissions. Please run: chmod 600 {KEYSTORE_FILE}"
                )
    except OSError as e:
        raise KeystoreError(f"Could not initialize keystore at {KEYSTORE_DIR}: {e}")

def load_keystore() -> Dict[str, Any]:
    _ensure_keystore()
    try:
        return json.loads(KEYSTORE_FILE.read_text(encoding='utf-8'))
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise KeystoreError(f"Keystore file is corrupted or missing: {e}")

def save_keystore(data: Dict[str, Any]) -> None:
    _ensure_keystore()
    KEYSTORE_FILE.write_text(json.dumps(data, indent=2), encoding='utf-8')

def create_identity(handle: str) -> str:
    """Creates a new identity and saves it to the keystore."""
    if not handle.startswith(' @'):
        raise ValueError("Handle must start with ' @'.")
    
    keystore = load_keystore()
    if handle in keystore:
        raise ValueError(f"Handle '{handle}' already exists.")

    priv, pub = crypto.generate_keypair()
    
    did = f"did:axiom:local:{handle[1:]}"
    keystore[handle] = {
        "id": did,
        "privateKeyPem": crypto.serialize_private_key(priv),
        "publicKeyPem": crypto.serialize_public_key(pub),
    }
    save_keystore(keystore)
    return did

def get_identity(handle: str) -> Optional[Dict[str, Any]]:
    keystore = load_keystore()
    return keystore.get(handle)

def list_identities() -> List[Dict[str, str]]:
    keystore = load_keystore()
    return [{"handle": h, "id": d["id"]} for h, d in keystore.items()]
