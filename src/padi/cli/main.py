"""Main CLI entry point for PADI PDF processor."""
import click
from pathlib import Path
from typing import Optional

# Use absolute imports
from padi.utils.config import ConfigManager


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """PADI - PDF Digitization Agent for Large Textbooks."""
    pass


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True, path_type=Path))
@click.option('--batch-size', '-b', type=int, default=30,
              help='Number of pages per batch (default: 30)')
@click.option('--merge-strategy', '-m', type=click.Choice(['fixed', 'chapter']), 
              default='fixed', help='Strategy for merging pages into batches')
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), 
              default='outputs', help='Output directory for digitized content')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
def process(pdf_path: Path, batch_size: int, merge_strategy: str, 
           output_dir: Path, verbose: bool):
    """Process a PDF file and convert it to digitized format."""
    click.echo(f"🚀 Starting PDF processing for: {pdf_path}")
    
    # Load configuration
    config = ConfigManager()
    click.echo(f"📋 Loaded configuration from: {config.config_dir}")
    
    # Print parsed arguments for confirmation
    click.echo("📋 Parsed CLI Arguments:")
    click.echo(f"   PDF Path: {pdf_path}")
    click.echo(f"   Batch Size: {batch_size}")
    click.echo(f"   Merge Strategy: {merge_strategy}")
    click.echo(f"   Output Directory: {output_dir}")
    click.echo(f"   Verbose: {verbose}")
    
    # Call the stub process_pdf function
    process_pdf(pdf_path, batch_size, merge_strategy, output_dir, verbose)


def process_pdf(pdf_path: Path, batch_size: int, merge_strategy: str, 
                output_dir: Path, verbose: bool) -> None:
    """Stub function for PDF processing - Phase 1.1 implementation will go here."""
    click.echo("\n🔧 PDF Processing Pipeline:")
    click.echo(f"   1. Loading PDF: {pdf_path}")
    click.echo(f"   2. Batch size: {batch_size} pages")
    click.echo(f"   3. Merge strategy: {merge_strategy}")
    click.echo(f"   4. Output directory: {output_dir}")
    click.echo(f"   5. Verbose mode: {verbose}")
    
    # TODO: Implement actual PDF processing logic
    click.echo("\n⚠️  PDF processing not yet implemented - this is a placeholder")
    click.echo("✅ CLI argument parsing confirmed - ready for Phase 1.1 implementation!")


@cli.command()
def info():
    """Show system information and configuration."""
    click.echo("🔍 PADI System Information")
    click.echo("=" * 40)
    
    # Configuration info
    config = ConfigManager()
    click.echo(f"Config directory: {config.config_dir}")
    click.echo(f"Default batch size: {config.get_batch_size()}")
    click.echo(f"Default merge strategy: {config.get_merge_strategy()}")
    click.echo(f"Default output directory: {config.get_output_directory()}")


if __name__ == '__main__':
    cli()
