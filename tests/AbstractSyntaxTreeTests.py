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
        self.assertTrue(self.tree._needs_concat_symbol("c", "d"))
        return None

    def test_setup_regex(self) -> None:
        expected = "(a|b)*.a.a.#"
        actual = self.tree._setup_regex("(a|b)*aa")
        self.assertEqual(actual, expected)

        expected = "a.b.c.d.#"
        actual = self.tree._setup_regex("abcd")
        self.assertEqual(actual, expected)

        expected = "a.b.c.d.(a|d)?.a.d.#"
        actual = self.tree._setup_regex("abcd(a|d)?ad")
        self.assertEqual(actual, expected)
        return None

    def test_get_substr(self) -> None:
        string = "(abcde)"
        expected = "abcde"
        actual = self.tree._get_substr(string, 1)
        self.assertEqual(actual, expected)

        string = "(ab(abc)ab)"
        expected = "ab(abc)ab"
        actual = self.tree._get_substr(string, 1)
        self.assertEqual(actual, expected)

        string = "asdf(ab(abc)ab)"
        expected = "ab(abc)ab"
        actual = self.tree._get_substr(string, 5)
        self.assertEqual(actual, expected)

        string = "#.*(b|a).a"
        expected = "b|a"
        actual = self.tree._get_substr(string, 4)
        self.assertEqual(actual, expected)
        return None

    def test_revert(self) -> None:
        expected = "#.*(b|a).a"
        actual = self.tree._reverse_regex("a.(a|b)*.#")
        self.assertEqual(actual, expected)
        return None

    def test_outro_parsing(self) -> None:
        expected = "a.*b"
        actual = self.tree._outro_parsing("a*.b")
        self.assertEqual(actual, expected)
        return None

    def test_reorg(self) -> None:
        expected = "|ba"
        actual = self.tree._reorg("b|a")
        self.assertEqual(expected, actual)

        expected = ".#.*aa"
        actual = self.tree._reorg("#.*a.a")
        self.assertEqual(actual, expected)

        expected = ".#.*(|ba)a"
        actual = self.tree._reorg("#.*(b|a).a")
        self.assertEqual(actual, expected)

        expected = ".#.a(|ba)"
        actual = self.tree._reorg("#.a.(b|a)")
        self.assertEqual(actual, expected)

        expected = ".#.*(.*(|ba)a)a"
        actual = self.tree._reorg("#.*(*(b|a).a).a")
        self.assertEqual(actual, expected)
        return None

