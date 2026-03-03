# test_pooledge.py
"""
Tests for PoolEdge module.
"""

import unittest
from pooledge import PoolEdge

class TestPoolEdge(unittest.TestCase):
    """Test cases for PoolEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PoolEdge()
        self.assertIsInstance(instance, PoolEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PoolEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
