"""PADI - PDF Digitization Agent for Large Textbooks."""

from .cli.main import cli

def main() -> None:
    """Main entry point for PADI."""
    cli()

if __name__ == "__main__":
    main()
