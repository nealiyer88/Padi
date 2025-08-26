"""Main CLI entry point for PADI PDF processor."""
import click
from pathlib import Path
from typing import Optional

# Use absolute imports
from padi.utils.config_manager import ConfigManager
from padi.utils.platform_utils import get_platform_info


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """PADI - PDF Digitization Agent for Large Textbooks."""
    pass


@cli.command()
@click.argument('pdf_path', type=click.Path(exists=True, path_type=Path))
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), 
              help='Output directory for digitized content')
@click.option('--batch-size', '-b', type=int, default=30,
              help='Number of pages per batch (default: 30)')
@click.option('--merge-strategy', '-m', type=click.Choice(['fixed', 'chapter']), 
              default='fixed', help='Strategy for merging pages into batches')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
def process(pdf_path: Path, output_dir: Optional[Path], batch_size: int, 
           merge_strategy: str, verbose: bool):
    """Process a PDF file and convert it to digitized format."""
    click.echo(f"🚀 Starting PDF processing for: {pdf_path}")
    
    # Load configuration
    config = ConfigManager()
    click.echo(f"📋 Loaded configuration from: {config.config_dir}")
    
    # Show platform info
    platform_info = get_platform_info()
    click.echo(f"💻 Platform: {platform_info['system']} {platform_info['release']}")
    
    # Set output directory
    if output_dir:
        final_output_dir = output_dir
    else:
        final_output_dir = config.get_output_directory()
    
    click.echo(f"📁 Output directory: {final_output_dir}")
    click.echo(f"📦 Batch size: {batch_size}")
    click.echo(f"🔗 Merge strategy: {merge_strategy}")
    
    # TODO: Implement actual PDF processing
    click.echo("⚠️  PDF processing not yet implemented - this is a placeholder")
    click.echo("✅ Project structure created successfully!")


@cli.command()
def info():
    """Show system information and configuration."""
    click.echo("🔍 PADI System Information")
    click.echo("=" * 40)
    
    # Platform info
    platform_info = get_platform_info()
    click.echo(f"Platform: {platform_info['system']} {platform_info['release']}")
    click.echo(f"Machine: {platform_info['machine']}")
    click.echo(f"Python: {platform_info['python_version']}")
    
    # Configuration info
    config = ConfigManager()
    click.echo(f"Config directory: {config.config_dir}")
    click.echo(f"Default batch size: {config.get_batch_size()}")
    click.echo(f"Default merge strategy: {config.get_merge_strategy()}")


if __name__ == '__main__':
    cli()
