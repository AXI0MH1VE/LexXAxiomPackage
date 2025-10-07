import click
import time
import sys
from typing import Optional

from .memory4d import Memory4D
from .backends.local_stub import get_response

# Global instance for the application lifecycle
memory_system = Memory4D()

@click.group()
def main() -> None:
    """
    GeminiPortable: Sovereign Generative AI CLI.

    This is the AxiomHive implementation. It is local-first,
    deterministic, and contains no telemetry.
    """
    pass

@main.command("run")
@click.option("--prompt", required=True, help="The prompt for the generative AI.")
@click.option("--memory", "use_memory", is_flag=True, help="Store the prompt and response in 4D memory.")
def run(prompt: str, use_memory: bool) -> None:
    """Run a prompt through the local, deterministic AI backend."""
    # This is the sovereign tool; it does not have external telemetry flags.
    # We explicitly check for and reject them to avoid confusion.
    if any(arg.startswith('--telemetry') for arg in sys.argv):
        click.echo("Error: Telemetry flags are not supported by AxiomHive's GeminiPortable.", err=True)
        click.echo("Ensure you are using the tool installed by 'RuntimeZero/install.sh'.", err=True)
        sys.exit(1)

    response = get_response(prompt)
    click.echo(response)

    if use_memory:
        timestamp = time.time()
        content_to_store = f"PROMPT: {prompt}\nRESPONSE: {response}"
        memory_system.store(
            content=content_to_store,
            temporal=timestamp,
            spatial="local_cli",
            causal="User initiated prompt.",
            counterfactual="What if the prompt was different?"
        )
        click.echo("\n[INFO] Interaction stored in 4D memory.")

if __name__ == "__main__":
    main()
