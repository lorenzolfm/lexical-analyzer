import unittest

from utils.model.Parser import Parser
from utils.model.AbstractSyntaxTree import AbstractSyntaxTree
from utils.model.FiniteAutomata import FiniteAutomata
from utils.model.Token import Token
from utils.model.regex_utils import convert_regex_syntax
from utils.algorithm import automata_union


class ParserTests(unittest.TestCase):
    def test_parser(self) -> None:
        symbol_table = {
            "if": Token("if"),
            "else": Token("else"),
            "(": Token("AbreP"),
            ")": Token("FechaP"),
            ":": Token("2pontos"),
            "return": Token("Retorno"),
            "=": Token("Igual"),
            "+": Token("Mais")
        }
        #
        string = """
            if(ifood):
                ifoo = ifod + 10
            else:
                return 666
        """
        # string = "uma frase grande pra ver ab reonhee."

        idd = Token("ID")
        regex_idd = "[a-zA-Z]"
        # c = Token("C")
        # regex = "c"

        regex_idd = convert_regex_syntax(regex_idd)
        regex_idd += "*"

        dig = Token("DIGITO")
        regex_dig = "[0-9]"
        regex_dig = convert_regex_syntax(regex_dig)
        regex_dig += "*"

        input_list = list(string.split())

        tree_idd = AbstractSyntaxTree(regex_idd, idd)
        tree_dig = AbstractSyntaxTree(regex_dig, dig)
        automatas = [
            tree_idd.get_finite_automata(),
            tree_dig.get_finite_automata()
        ]
        fa = automata_union(automatas)
        fa.determinization()
        parser = Parser(fa, symbol_table)

        for string in input_list:
            parser.parse(string)

        for key, value in parser._found_tokens.items():
            print(f"{key} {value}")

        return None
