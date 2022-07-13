import unittest
from unittest import TestCase


class CmsBlogs(unittest.TestCase):
    def test_published_bogs(self):
        f = open("data/published_blogs.csv", "r")
        lines = len(f.readlines()[1:])
        self.assertEqual(int(lines), 1, "Record count should be 1")
        f.close()

    def test_draft_blogs(self):
        f = open("data/draft_blogs.csv", "r")
        x = len(f.readlines()[1:])
        self.assertEqual(int(x), 2, "Record count should be 2")
        f.close()


if __name__ == '__main__':
    unittest.main()
