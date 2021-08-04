import unittest

from utils.model.AbstractSyntaxTree import AbstractSyntaxTree
class AbstractSyntaxTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = AbstractSyntaxTree("ola")
        return None

    def test_needs_concat_symbol(self) -> None:
        self.assertTrue(self.tree._needs_concat_symbol("a", "b"))
        self.assertTrue(self.tree._needs_concat_symbol(")", "b"))
        self.assertTrue(self.tree._needs_concat_symbol("*", "a"))
        self.assertTrue(self.tree._needs_concat_symbol("a", "("))
        return None

    def test_setup_regex(self) -> None:
        expected = "(a|b)*.a.a.#"
        actual = self.tree._setup_regex("(a|b)*aa")
        self.assertEqual(actual, expected)
        return None
