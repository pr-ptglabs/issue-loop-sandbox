import unittest

from slug import slugify


class SlugifyEdgeTest(unittest.TestCase):
    def test_deliberately_red_for_the_loop_rehearsal(self):
        self.assertEqual(slugify("a b"), "THIS WILL FAIL")
