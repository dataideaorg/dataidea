"""
Tests for the utils module
"""
import time
import pytest
from unittest.mock import patch, MagicMock
from dataidea.utils import timer

class TestUtils:
    def test_timer(self):
        """Test the timer decorator"""
        # Create a function that takes a specific amount of time
        @timer
        def slow_function():
            time.sleep(0.1)
            return "done"
        
        # Call the function and capture its output
        with patch('builtins.print') as mock_print:
            result = slow_function()
            
            # Check the function return value
            assert result == "done"
            
            # Check that print was called with something containing the function name
            mock_print.assert_called_once()
            args, _ = mock_print.call_args
            assert "slow_function" in args[0]
            assert "seconds" in args[0] 