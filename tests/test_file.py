from context import PolyglotPath

import unittest


class TestCases(unittest.TestCase):
    """Advanced test cases."""
    def test_application(self):
        d = PolyglotPath(".")
        d.mkdirs(["dist"])
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()