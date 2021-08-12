from typing import Dict, List

from ..view.View import View
from ..view.Form import Form
from ..model.AbstractSyntaxTree import AbstractSyntaxTree
from ..model.FiniteAutomata import FiniteAutomata
from ..model.regex_utils import convert_regex_syntax
from ..algorithm import automata_union
from ..model.Token import Token
from ..model.Parser import Parser

class Controller:
    def __init__(self) -> None:
        self._view = View()
        self._bind_callbacks()
        self._regular_definitions = {}
        return None

    def run(self) -> None:
        self._view.mainloop()

    def _bind_callbacks(self) -> None:
        regex_input: Form = self._view.get_form_by_id("regular_definition_input")
        regex_input.add_btn_callback(btn_id="rd_add", callback=self._handle_add_regular_definition_callback)
        regex_input.add_btn_callback(btn_id="rd_done", callback=self._handle_done_reg_def_input_callback)

        source_code_input: Form = self._view.get_form_by_id("source_code_input")
        source_code_input.add_btn_callback(btn_id="source_code_input", callback=self._handle_source_code_input)
        return None

    def _handle_add_regular_definition_callback(self, response: Dict) -> None:
        try:
            regular_definition = list(response["inputs"]["rd_entry"].split())
            name: str = regular_definition[0]
            regex: str = regular_definition[-1]
            if regex[0] == "[":
                regex = convert_regex_syntax(regex)
        except:
            self._log("Algo deu errado ao adicionar a definição regular")
        else:
            self._regular_definitions[name] = regex
            self._view.insert_text(idd="regular_definition_output", text="".join(regular_definition))
        return None

    def _handle_done_reg_def_input_callback(self, response: Dict) -> None:
        try:
            automatas = []
            for name, regex in self._regular_definitions.items():
                token = Token(name)
                tree = AbstractSyntaxTree(regex, token)
                automatas.append(tree.get_finite_automata())
        except:
            self._log("Algo deu errado ao processar as definições regulares")
        else:
            self._view.clear_text(idd="symbol_table")
            if len(automatas) > 1:
                self._automata: FiniteAutomata = automata_union(automatas)
                self._automata.determinization()
        return None

    def _handle_source_code_input(self, response: Dict) -> None:
        try:
            source_code = list(response["text_entries"]["source_code_input"].split())
        except:
            self._log("Algo deu errado ao processar o código fonte")
        else:
            self._view.clear_text(idd="symbol_table")

            symbol_table = {}
            parser = Parser(self._automata, symbol_table)
            for string in source_code:
                parser.parse(string)

            symbol_table = parser.get_symbol_table()
            for lexeme, token in symbol_table.items():
                self._view.insert_text(idd="symbol_table", text=f"{lexeme}, {token}")
        return None

    def _log(self, msg: str) -> None:
        self._view.log_msg(msg)
        return None
