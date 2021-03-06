import unittest

from utils.model.AbstractSyntaxTree import AbstractSyntaxTree
from utils.model.FiniteAutomata import FiniteAutomata
from utils.algorithm import automata_union
from utils.model.Token import Token


class IntegrationTests(unittest.TestCase):
    def test_token_recognization(self) -> None:
        id_ = Token("<ID>")
        relop = Token("<RELOP>")
        tree_0 = AbstractSyntaxTree("(a|b|c|d|e|f)*", id_)
        tree_1 = AbstractSyntaxTree(">=|<=|==|!=|>|<", relop)

        auto_list = [tree_0.get_finite_automata(), tree_1.get_finite_automata()]
        fa: FiniteAutomata = automata_union(auto_list)
        fa.determinization()

        expected = id_
        actual = fa.eval_lexeme("acbde")
        self.assertEqual(expected, actual)
        actual = fa.eval_lexeme("abc")
        self.assertEqual(expected, actual)

        expected = relop
        actual = fa.eval_lexeme(">")
        self.assertEqual(expected, actual)

        return None
