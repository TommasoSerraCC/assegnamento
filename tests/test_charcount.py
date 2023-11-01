import unittest
from unittest.mock import patch
import os
import sys
import io

# Import the function 'process' from my module
from assignments.charcount import process

class TestProcess(unittest.TestCase):
    def test_test(self):
        self.assertEqual(2,2)

if __name__=='__main__':
    unittest.main()
