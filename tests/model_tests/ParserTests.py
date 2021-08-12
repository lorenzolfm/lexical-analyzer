import unittest

from utils.model.Parser import Parser
from utils.model.AbstractSyntaxTree import AbstractSyntaxTree
from utils.model.FiniteAutomata import FiniteAutomata
from utils.model.Token import Token


class ParserTests(unittest.TestCase):
    def test_parser(self) -> None:
        string = "ifood"
        tk: Token = Token("ifood")
        tree = AbstractSyntaxTree("ifood", tk)
        fa = tree.get_finite_automata()
        parser: Parser = Parser(fa, {})
        parser.new_parser(string)

