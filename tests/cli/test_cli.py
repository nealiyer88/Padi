"""Tests for CLI functionality."""
import pytest
from pathlib import Path
import sys
from click.testing import CliRunner

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from padi.cli.main import cli


class TestCLI:
    """Test cases for CLI functionality."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.runner = CliRunner()
        # Create a temporary PDF file for testing
        self.test_pdf = Path("test_sample.pdf")
        self.test_pdf.write_text("Fake PDF content for testing")
    
    def teardown_method(self):
        """Cleanup test fixtures."""
        if self.test_pdf.exists():
            self.test_pdf.unlink()
    
    def test_process_default_values(self):
        """Test that default values are used when no options provided."""
        result = self.runner.invoke(cli, ['process', str(self.test_pdf)])
        
        assert result.exit_code == 0
        assert "Batch Size: 30" in result.output
        assert "Merge Strategy: fixed" in result.output
        assert "Output Directory: outputs" in result.output
        assert "Verbose: False" in result.output
    
    def test_process_custom_values(self):
        """Test that custom values override defaults."""
        result = self.runner.invoke(cli, [
            'process', 
            str(self.test_pdf),
            '--batch-size', '40',
            '--merge-strategy', 'chapter',
            '--output-dir', 'my_output',
            '--verbose'
        ])
        
        assert result.exit_code == 0
        assert "Batch Size: 40" in result.output
        assert "Merge Strategy: chapter" in result.output
        assert "Output Directory: my_output" in result.output
        assert "Verbose: True" in result.output
    
    def test_process_short_options(self):
        """Test that short options work correctly."""
        result = self.runner.invoke(cli, [
            'process', 
            str(self.test_pdf),
            '-b', '25',
            '-m', 'fixed',
            '-o', 'short_output',
            '-v'
        ])
        
        assert result.exit_code == 0
        assert "Batch Size: 25" in result.output
        assert "Merge Strategy: fixed" in result.output
        assert "Output Directory: short_output" in result.output
        assert "Verbose: True" in result.output
    
    def test_process_invalid_batch_size(self):
        """Test that invalid batch size is handled gracefully."""
        result = self.runner.invoke(cli, [
            'process', 
            str(self.test_pdf),
            '--batch-size', 'invalid'
        ])
        
        assert result.exit_code != 0  # Should fail with invalid input
    
    def test_process_invalid_merge_strategy(self):
        """Test that invalid merge strategy is handled gracefully."""
        result = self.runner.invoke(cli, [
            'process', 
            str(self.test_pdf),
            '--merge-strategy', 'invalid'
        ])
        
        assert result.exit_code != 0  # Should fail with invalid input
    
    def test_info_command(self):
        """Test that info command works correctly."""
        result = self.runner.invoke(cli, ['info'])
        
        assert result.exit_code == 0
        assert "PADI System Information" in result.output
        assert "Config directory: config" in result.output
        assert "Default batch size:" in result.output
        assert "Default merge strategy:" in result.output
        assert "Default output directory:" in result.output
    
    def test_help_command(self):
        """Test that help command works correctly."""
        result = self.runner.invoke(cli, ['--help'])
        
        assert result.exit_code == 0
        assert "PADI - PDF Digitization Agent for Large Textbooks" in result.output
        assert "process" in result.output
        assert "info" in result.output
    
    def test_process_help(self):
        """Test that process command help works correctly."""
        result = self.runner.invoke(cli, ['process', '--help'])
        
        assert result.exit_code == 0
        assert "Process a PDF file and convert it to digitized format" in result.output
        assert "--batch-size" in result.output
        assert "--merge-strategy" in result.output
        assert "--output-dir" in result.output
        assert "--verbose" in result.output
