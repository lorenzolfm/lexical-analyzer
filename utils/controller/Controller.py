from typing import Dict

from ..view.View import View
from ..view.Form import Form
from ..model.AbstractSyntaxTree import AbstractSyntaxTree
from ..algorithm import automata_union

class Controller:
    def __init__(self) -> None:
        self._view = View()
        self._bind_callbacks()
        self._regexs = []
        return None

    def run(self) -> None:
        self._view.mainloop()

    def _bind_callbacks(self) -> None:
        regex_input: Form = self._view.get_form_by_id("regular_definition_input")
        regex_input.add_btn_callback(btn_id="rd_add", callback=self._handle_add_regex_callback)
        regex_input.add_btn_callback(btn_id="rd_done", callback=self._handle_done_regex_input_callback)

        source_code_input: Form = self._view.get_form_by_id("source_code_input")
        source_code_input.add_btn_callback(btn_id="source_code_input", callback=self._handle_source_code_input)
        return None

    def _handle_add_regex_callback(self, response: Dict) -> None:
        try:
            regular_definition = list(response["inputs"]["rd_entry"].split())
            if regular_definition:
                regex = regular_definition[-1]
                print(regex)
                self._regexs.append(regex)
        except:
            print("Algo deu errado")
        else:
            pass
        return None

    def _handle_done_regex_input_callback(self, response: Dict) -> None:
        try:
            automatas = []
            for regex in self._regexs:
                tree = AbstractSyntaxTree(regex)
                automatas.append(tree.get_finite_automata())
            automata = automata_union(automatas)
            automata.determinization()
            self._automata = automata
            print(self._automata)
        except:
            print("Algo deu errado")
        else:
            pass
        return None

    def _handle_source_code_input(self, response: Dict) -> None:
        try:
            source_code = list(response["text_entries"]["source_code_input"].split())
        except:
            print("Algo deu errado")
        else:
            for lexeme in source_code:
                print(f"Lexema: {lexeme}, Accept: {self._automata.eval_lexeme(lexeme)}")
        return None
