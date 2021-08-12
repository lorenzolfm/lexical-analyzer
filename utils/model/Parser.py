from typing import Dict

from .Token import Token
from .FiniteAutomata import FiniteAutomata


class Parser:
    def __init__(self, automata: FiniteAutomata, symbol_table: Dict[str, Token]) -> None:
        self._automata = automata
        self._symbol_table = symbol_table

    # ID [a-zA-Z]*

    # if(🌎);

    # if -> Palavra reservada
    # ( -> Palavra reservada
    # ifood -> ID
    # ) -> Palavra reservada

    # 1ª Palavra reconhecida -> if
    # (food) -> maior palavra reconhecida = (
    # food) -> maior palavra reconhecida = food

    def parse(self, string: str) -> None:
        begin_ptr: int = 0
        end_lexeme: int = 0

        size: int = len(string)
        i = 0
        last_size = 0
        while (i < size):
            lexeme: str = string[begin_ptr:end_lexeme]

            if lexeme not in self._symbol_table.keys():
                token = self._automata.eval_lexeme(lexeme)
                if token:
                    size_of_last_accepted_lexeme = len(lexeme)
                    last_recognized_token = token

                    if size_of_last_accepted_lexeme > last_size:
                        last_size = size_of_last_accepted_lexeme

            i += 1

        # Vou adicionar o maior lexema que foi aceito pelo automato (se houver), caso ele ainda não esteja na TS.
        return None

    def new_parser(self, string: str) -> None:
        begin_ptr: int = 0
        end_lexeme: int = 1

        size_of_string: int = len(string)
        greater_size: int = 0

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
                    begin_ptr = end_lexeme
                    last_token = None
                    last_lexeme = ""

            end_lexeme += 1

            if end_lexeme >= size_of_string and last_token:
                self._symbol_table[last_lexeme] = last_token
                begin_ptr = end_lexeme
                last_token = None
                last_lexeme = ""

        print(self._symbol_table)

        return None
