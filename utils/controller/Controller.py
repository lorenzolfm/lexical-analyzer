from typing import Dict
from copy import copy

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
        self._keywords: Dict[str, Token] = {}
        self._symbol_table: Dict[str, Token] = {}

    def run(self) -> None:
        self._view.mainloop()

    def _bind_callbacks(self) -> None:
        regex_input: Form = self._view.get_form_by_id("regular_definition_input")
        regex_input.add_btn_callback(btn_id="rd_add", callback=self._handle_add_regular_definition_callback)
        regex_input.add_btn_callback(btn_id="rd_done", callback=self._handle_done_reg_def_input_callback)

        source_code_input: Form = self._view.get_form_by_id("source_code_input")
        source_code_input.add_btn_callback(btn_id="source_code_input", callback=self._handle_source_code_input)

        keywords_input: Form = self._view.get_form_by_id("keywords")
        keywords_input.add_btn_callback(btn_id="keywords", callback=self._handle_keyword_input_callback)

        tokens_found: Form = self._view.get_form_by_id("tokens_found")
        tokens_found.add_btn_callback(btn_id="tokens_found", callback=self._handle_export_tokens_found_callback)

        return None

    def _handle_add_regular_definition_callback(self, response: Dict) -> None:
        try:
            regular_definition = list(response["inputs"]["rd_entry"].split())
            name: str = regular_definition[0]
            regex: str = regular_definition[-1]
            if regex[0] == "[":
                string = "["
                i = 1
                while (string[-1] != "]"):
                    string += regex[i]
                    i += 1
                regex = convert_regex_syntax(string) + regex[i:]
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
            # self._view.clear_text(idd="symbol_table")
            if len(automatas) > 1:  # FIXME: precisa mesmo?
                self._automata: FiniteAutomata = automata_union(automatas)
                self._automata.determinization()
                self._log("Árvores e autômatos gerados com sucesso.")
        return None

    def _handle_source_code_input(self, response: Dict) -> None:
        try:
            source_code = list(response["text_entries"]["source_code_input"].split())
        except:
            self._log("Algo deu errado ao processar o código fonte")
        else:
            self._view.clear_text(idd="symbol_table")
            self._view.clear_text(idd="tokens_found")
            self._reset_symbol_table()

            parser = Parser(self._automata, self._symbol_table)
            for string in source_code:
                parser.parse(string)

            symbol_table = parser.get_symbol_table()
            for lexeme, token in symbol_table.items():
                self._view.insert_text(idd="symbol_table", text=f"{lexeme}, {token}")

            for lexeme, token in parser.get_found_tokens().items():
                self._view.insert_text(idd="tokens_found", text=f"{lexeme}, {token}")
        return None

    def _handle_keyword_input_callback(self, response: Dict) -> None:
        try:
            keywords = list(response["text_entries"]["keywords"].split())
        except:
            self._log("Algo deu errado ao processar as palavras-chave.")
        else:
            for word in keywords:
                self._keywords[word] = Token(name=word)

            self._reset_symbol_table()
            self._view.clear_text(idd="symbol_table")
            self._view.clear_text(idd="tokens_found")

            for lexeme, token in self._symbol_table.items():
                self._view.insert_text(idd="symbol_table", text=f"{lexeme}, {token}")

        return None

    def _handle_export_tokens_found_callback(self, response: Dict) -> None:
        try:
            tokens = response["text_entries"]["tokens_found"]
        except:
            self._log("Algo deu errado ao exportar.")
        else:
            file = open("docs/tokens.txt", "w")
            file.write(tokens)
            self._log("Exportado com sucesso. Verifique o diretório docs.")
            return None

    def _log(self, msg: str) -> None:
        self._view.log_msg(msg)
        return None

    def _reset_symbol_table(self) -> None:
        self._symbol_table = copy(self._keywords)
        return None
