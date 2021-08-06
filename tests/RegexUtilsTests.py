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
        expected: str = "abc#."
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

    def test_insert_concats(self) -> None:
        regex: str = "(a|b)?abcd(a|b)*abcd"
        expected: str = "(a|b)?.a.b.c.d.(a|b)*.a.b.c.d"
        actual: str = insert_concats(regex)
        self.assertEqual(actual, expected)
        return None

    def test_infix_to_postfix(self) -> None:
        regex: str = "(a|b)*.a.b.b"
        expected: str = "ab|*a.b.b."
        actual = infix_to_postfix(regex)
        self.assertEqual(actual, expected)

        regex = "a.b.c.(a|b)?.a.b.c"
        expected = "ab.c.ab|?.a.b.c."
        actual = infix_to_postfix(regex)
        self.assertEqual(actual, expected)
        return None

    def test_setup_regex(self) -> None:
        return None
