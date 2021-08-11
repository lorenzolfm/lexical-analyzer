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
        self.assertTrue(needs_concat_symbol("?", "a"))

        self.assertFalse(needs_concat_symbol("|", "a"))
        self.assertFalse(needs_concat_symbol(" ", "a"))
        self.assertFalse(needs_concat_symbol("a", "|"))
        self.assertFalse(needs_concat_symbol(")", "*"))
        self.assertFalse(needs_concat_symbol(")", "?"))
        self.assertFalse(needs_concat_symbol("b", ")"))
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
        regex: str = "(a|b)*abb"
        expected: str = "ab|*a.b.b.#."
        actual: str = setup_regex(regex)
        self.assertEqual(actual, expected)

        regex = "abc(a|b)?abc"
        expected = "ab.c.ab|?.a.b.c.#."
        actual = setup_regex(regex)
        self.assertEqual(actual, expected)

        regex = "abc(a|b)?abc(c|d)abc"
        expected = "ab.c.ab|?.a.b.c.cd|.a.b.c.#."
        actual = setup_regex(regex)
        self.assertEqual(actual, expected)
        return None

    def test_replace_optional(self) -> None:
        regex: str = "a?"
        expected: str = "(a|&)"
        actual: str = replace_optional(regex)
        self.assertEqual(actual, expected)

        regex = "(a(a|b))?"
        expected = "((a(a|b))|&)"
        actual = replace_optional(regex)
        self.assertEqual(actual, expected)

        regex = "(a|b)?(a|b)*aa"
        expected = "((a|b)|&)(a|b)*aa"
        actual = replace_optional(regex)
        self.assertEqual(actual, expected)

        regex = "(a|b)?abb"
        expected = "((a|b)|&)abb"
        actual = replace_optional(regex)
        self.assertEqual(actual, expected)

        return None

    def test_convert_regex_syntax(self) -> None:
        regex: str = "[a-g]"
        expected: str = "(a|b|c|d|e|f|g)*"
        actual = convert_regex_syntax(regex)
        self.assertEqual(actual, expected)

        regex = "[0-9]"
        expected = "(0|1|2|3|4|5|6|7|8|9)*"
        actual = convert_regex_syntax(regex)
        self.assertEqual(actual, expected)

        regex = "[a-dB-E]"
        expected = "(a|b|c|d|B|C|D|E)*"
        actual = convert_regex_syntax(regex)
        self.assertEqual(actual, expected)
        return None
