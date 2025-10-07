import click
import sys
from typing import IO
from . import keystore, crypto

 @click.group()
def main() -> None:
    """AxiomSSI: Sovereign Self-Identity Management Tool."""
    pass

 @main.group()
def id() -> None:
    """Manage local identities."""
    pass

 @id.command("create")
 @click.option("--handle", required=True, help="A unique handle for the new identity (e.g., @AppData\Roaming\Microsoft\Windows\Recent\Alexis Adams Lab.lnk).")
def id_create(handle: str) -> None:
    """Create a new local identity."""
    try:
        did = keystore.create_identity(handle)
        click.echo(f"Successfully created identity '{handle}' with ID: {did}")
    except (ValueError, keystore.KeystoreError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

 @id.command("list")
def id_list() -> None:
    """List all local identities."""
    try:
        identities = keystore.list_identities()
        if not identities:
            click.echo("No identities found.")
            return
        for ident in identities:
            click.echo(f"- {ident['handle']} ({ident['id']})")
    except keystore.KeystoreError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

 @main.command("sign")
 @click.option("--handle", required=True, help="The handle of the identity to sign with.")
 @click.option("--in", "in_file", type=click.File("rb"), required=True, help="Input file to sign.")
 @click.option("--out", "out_file", type=click.File("wb"), required=True, help="Output file for the signature.")
def sign(handle: str, in_file: IO[bytes], out_file: IO[bytes]) -> None:
    """Sign a file with an identity's private key."""
    try:
        identity = keystore.get_identity(handle)
        if not identity:
            click.echo(f"Error: Identity '{handle}' not found.", err=True)
            sys.exit(1)
        
        private_key = crypto.deserialize_private_key(identity["privateKeyPem"])
        message = in_file.read()
        signature = crypto.sign_message(private_key, message)
        out_file.write(signature)
        click.echo(f"File signed successfully. Signature written to {getattr(out_file, 'name', 'output')}")
    except Exception as e:
        click.echo(f"Error during signing: {e}", err=True)
        sys.exit(1)

 @main.command("verify")
 @click.option("--handle", required=True, help="The handle of the identity to verify with.")
 @click.option("--in", "in_file", type=click.File("rb"), required=True, help="The original input file.")
 @click.option("--sig", "sig_file", type=click.File("rb"), required=True, help="The signature file.")
def verify(handle: str, in_file: IO[bytes], sig_file: IO[bytes]) -> None:
    """Verify a file's signature."""
    try:
        identity = keystore.get_identity(handle)
        if not identity:
            click.echo(f"Error: Identity '{handle}' not found.", err=True)
            sys.exit(1)
            
        public_key = crypto.deserialize_public_key(identity["publicKeyPem"])
        message = in_file.read()
        signature = sig_file.read()
        
        if crypto.verify_signature(public_key, signature, message):
            click.echo("Verification successful: Signature is valid.")
            sys.exit(0)
        else:
            click.echo("Verification FAILED: Signature is invalid.", err=True)
            sys.exit(1)
            
    except Exception as e:
        click.echo(f"Error during verification: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
