import unittest
import server
import requests


class UnitTest(unittest.TestCase):

    def test_wrong(self):
        self.assertEqual(10, server.multiply(10, 3))

    def test_right(self):
        self.assertEqual(18, server.multiply(3, 6))


if __name__ == '__main__':
    unittest.main()
    