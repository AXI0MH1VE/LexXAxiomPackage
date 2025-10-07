import argparse
import sys
from typing import NoReturn
from axiomhash import (
    stream_hash,
    compute_merkle_root,
    constant_time_compare,
    SUPPORTED_ALGORITHMS,
    blake3,
)

def die(message: str, exit_code: int = 1) -> NoReturn:
    """Prints an error message to stderr and exits."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(exit_code)

def main() -> None:
    parser = argparse.ArgumentParser(description="AxiomHash: A deterministic streaming file hasher.")
    parser.add_argument("file", nargs="?", type=argparse.FileType("rb"), default=sys.stdin.buffer, help="File to hash. Reads from stdin if not provided.")
    parser.add_argument("-a", "--algorithm", choices=SUPPORTED_ALGORITHMS, default="sha256", help="Hashing algorithm to use.")
    parser.add_argument("-c", "--compare", metavar="HEX_DIGEST", help="Compare the final hash against this value in constant time.")
    parser.add_argument("-m", "--merkle", action="store_true", help="Compute and print the Merkle root of the file chunks.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    if args.algorithm == "blake3" and blake3 is None:
        die("blake3 algorithm selected but library not installed.\nInstall with: pip install 'axiomhash-cli[fast]'", 2)

    try:
        with args.file as f:
            digest, chunk_hashes = stream_hash(f, args.algorithm)

        if args.verbose:
            source = 'stdin' if args.file == sys.stdin.buffer else args.file.name
            print(f"Algorithm: {args.algorithm}", file=sys.stderr)
            print(f"Source: {source}", file=sys.stderr)
            print(f"Chunks: {len(chunk_hashes)}", file=sys.stderr)

        if args.merkle:
            merkle_root = compute_merkle_root(chunk_hashes, args.algorithm)
            print(f"Merkle-Root: {merkle_root}")

        print(f"AxiomHash: {digest}")

        if args.compare:
            if constant_time_compare(digest, args.compare):
                if args.verbose:
                    print("Integrity check: PASSED", file=sys.stderr)
                sys.exit(0)
            else:
                if args.verbose:
                    print("Integrity check: FAILED", file=sys.stderr)
                sys.exit(1)

    except (IOError, ValueError) as e:
        die(str(e), 2)

if __name__ == "__main__":
    main()
