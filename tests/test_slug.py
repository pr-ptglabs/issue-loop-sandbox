import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_lowercases_and_dashes(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_collapses_and_trims_separators(self):
        self.assertEqual(slugify("  Hello,   World!  "), "hello-world")
