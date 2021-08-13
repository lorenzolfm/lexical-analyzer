from typing import List
import unittest

from utils.model.AbstractSyntaxTree import AbstractSyntaxTree


class AbstractSyntaxTreeTests(unittest.TestCase):
    def test_create_syntax_tree_from_regex(self) -> None:
        tree: AbstractSyntaxTree = AbstractSyntaxTree("(a|b)*abb")
        expected: List = ['a', '|', 'b', '*', '.', 'a', '.', 'b', '.', 'b', '.', '#']
        actual: List = tree.in_order()
        self.assertEqual(actual, expected)

        tree = AbstractSyntaxTree("abc(a|b)?abc(c|d)abc")
        expected = ['a', '.', 'b', '.', 'c', '.', 'a', '|', 'b', '|', '&','.', 'a',
                    '.', 'b', '.', 'c', '.', 'c', '|', 'd', '.', 'a', '.', 'b', '.', 'c', '.', '#']
        actual = tree.in_order()
        self.assertEqual(actual, expected)
        return None
