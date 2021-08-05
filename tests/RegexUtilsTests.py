import unittest

from utils.model.regex_utils import *

class RegexUtilsTests(unittest.TestCase):
    def test_remove_whitespaces(self) -> None:
        regex: str = "a b c d "
        expected: str = "abcd"
        actual: str = remove_white_spaces(regex)
        self.assertEqual(actual, expected)
        return None

    def test_add_ending(self) -> None:
        regex: str = "abc"
        expected: str = "abc.#"
        actual: str = add_ending(regex)
        self.assertEqual(actual, expected)
        return None

    def test_needs_concat_symbol(self) -> None:
        self.assertTrue(needs_concat_symbol("a", "b"))
        self.assertTrue(needs_concat_symbol(")", "b"))
        self.assertTrue(needs_concat_symbol("*", "a"))
        self.assertTrue(needs_concat_symbol("a", "("))
        self.assertFalse(needs_concat_symbol("|", "a"))
        self.assertFalse(needs_concat_symbol(" ", "a"))
        self.assertFalse(needs_concat_symbol("a", "|"))
        self.assertFalse(needs_concat_symbol(")", "*"))
        return None

    def test_add_concat_symbol_at_index(self) -> None:
        regex: str = "(a|b)?abcd(a|b)*abcd"
        expected: str = "(a|b)?.abcd(a|b)*abcd"
        actual: str = add_concat_symbol_at_index(regex, 6 + 0)
        self.assertEqual(actual, expected)

        regex = actual
        expected = "(a|b)?.a.bcd(a|b)*abcd"
        actual: str = add_concat_symbol_at_index(regex, 7 + 1)
        self.assertEqual(actual, expected)
        return None

    def test_reverse_regex(self) -> None:
        regex: str = "ab(c(oi)d)ef(gh)ij"
        expected: str = "ji(hg)fe(d(io)c)ba"
        actual: str = reverse_regex(regex)
        self.assertEqual(actual, expected)
        return None

    def test_insert_concats(self) -> None:
        regex: str = "(a|b)?abcd(a|b)*abcd"
        expected: str = "(a|b)?.a.b.c.d.(a|b)*.a.b.c.d"
        actual: str = insert_concats(regex)
        self.assertEqual(actual, expected)
        return None

    def test_reorg(self) -> None:
        expected = "|ba"
        actual = reorg_regex("b|a")
        self.assertEqual(expected, actual)

        expected = ".#.*aa"
        actual = reorg_regex("#.*a.a")
        self.assertEqual(actual, expected)

        expected = ".#.*(|ba)a"
        actual = reorg_regex("#.*(b|a).a")
        self.assertEqual(actual, expected)

        expected = ".#.a(|ba)"
        actual = reorg_regex("#.a.(b|a)")
        self.assertEqual(actual, expected)

        expected = ".#.*(.*(|ba)a)a"
        actual = reorg_regex("#.*(*(b|a).a).a")
        self.assertEqual(actual, expected)
        return None

    def test_setup_regex(self) -> None:
        regex: str = "a(a(a|b)*)*"
        expected = ".#.*(.*(|ba)a)a"
        actual = setup_regex(regex)
        self.assertEqual(actual, expected)
        return None
