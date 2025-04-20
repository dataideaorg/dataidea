"""
Tests for the models module
"""
import os
import tempfile
import pytest
import pickle
from dataidea.models import load_model, save_model

class TestModels:
    def test_save_load_model(self):
        """Test saving and loading a model"""
        # Create a simple model (just a dictionary in this case)
        model = {"name": "test_model", "version": 1, "params": {"a": 1, "b": 2}}
        
        # Use a temporary file
        with tempfile.NamedTemporaryFile(suffix='.di') as tmp:
            # Save model
            filepath = save_model(model, tmp.name)
            assert os.path.exists(filepath)
            
            # Load model
            loaded_model = load_model(filepath)
            
            # Check that the loaded model is the same as the original
            assert loaded_model == model
            assert loaded_model["name"] == "test_model"
            assert loaded_model["params"]["a"] == 1 