from typing import Dict

from .Token import Token
from .FiniteAutomata import FiniteAutomata


class Parser:
    def __init__(self, automata: FiniteAutomata, symbol_table: Dict[str, Token]) -> None:
        self._automata = automata
        self._symbol_table = symbol_table

    def get_symbol_table(self) -> Dict:
        return self._symbol_table

    def parse(self, string: str) -> None:
        begin_ptr: int = 0
        end_lexeme: int = 1

        size_of_string: int = len(string)

        last_lexeme = ""
        last_token = None
        while (begin_ptr < size_of_string):
            lexeme: str = string[begin_ptr:end_lexeme]

            if lexeme not in self._symbol_table.keys():
                token = self._automata.eval_lexeme(lexeme)
                if token:
                    last_lexeme = lexeme
                    last_token = token
                elif last_token:
                    self._symbol_table[last_lexeme] = last_token
                    begin_ptr = end_lexeme - 1
                    end_lexeme -= 1
                    last_token = None
                    last_lexeme = ""
                else:
                    begin_ptr = end_lexeme
            else:
                last_lexeme = lexeme
                last_token = self._symbol_table[lexeme]

            end_lexeme += 1

            if end_lexeme > size_of_string and last_token:
                self._symbol_table[last_lexeme] = last_token
                begin_ptr = end_lexeme
                last_token = None
                last_lexeme = ""

        return None
