#!/usr/bin/env python3
"""Launcher script for PADI - adds src to Python path and runs CLI."""
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run CLI
from padi.cli.main import cli

if __name__ == "__main__":
    cli()
