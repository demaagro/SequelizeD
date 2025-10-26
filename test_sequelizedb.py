# test_sequelizedb.py
"""
Tests for SequelizeDB module.
"""

import unittest
from sequelizedb import SequelizeDB

class TestSequelizeDB(unittest.TestCase):
    """Test cases for SequelizeDB class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SequelizeDB()
        self.assertIsInstance(instance, SequelizeDB)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SequelizeDB()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
