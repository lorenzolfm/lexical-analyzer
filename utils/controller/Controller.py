from typing import Dict, List

from ..view.View import View
from ..view.Form import Form
from ..model.AbstractSyntaxTree import AbstractSyntaxTree
from ..algorithm import automata_union
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
            print("try")
        except:
            self._log("Algo deu errado ao adicionar a definição regular")
        else:
            print("finally")
        # try:
            # regular_definition = list(response["inputs"]["rd_entry"].split())
            # name = regular_definition[0]
            # regex = regular_definition[-1]
        # except:
            # print("Algo deu errado")
        # else:
            # self._regular_definitions[name] = regex
        return None

    def _handle_done_reg_def_input_callback(self, response: Dict) -> None:
        try:
            print("try")
        except:
            self._log("Algo deu errado ao processar as definições regulares")
        else:
            print("finally")
        return None

    def _handle_source_code_input(self, response: Dict) -> None:
        try:
            print("try")
        except:
            self._log("Algo deu errado ao processar o código fonte")
        else:
            print("finally")
        return None

    def _log(self, msg: str) -> None:
        self._view.log_msg(msg)
        return None
