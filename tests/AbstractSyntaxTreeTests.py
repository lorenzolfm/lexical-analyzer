import unittest

from utils.model.AbstractSyntaxTree import AbstractSyntaxTree
class AbstractSyntaxTreeTests(unittest.TestCase):
    def test_create_syntax_tree_from_regex(self) -> None:
        t = AbstractSyntaxTree("ola_mundo")
        return None
