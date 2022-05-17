import unittest
from unittest.mock import patch
from deleteDuplicateFiles import *


@patch('deleteDuplicateFiles.deleteDuplicates')
class testDeleteDuplicate(unittest.TestCase):
    def testNothingDeleted(self, mock_deleteDuplicates):
        mock_deleteDuplicates.return_value = []
        self.assertEqual(deleteDuplicates(), [])


if __name__ == "__main__":
    unittest.main()
