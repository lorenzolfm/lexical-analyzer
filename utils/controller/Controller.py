from typing import Dict

from ..view.View import View
from ..view.Form import Form

class Controller:
    def __init__(self) -> None:
        self._view = View()
        self._bind_callbacks()
        return None

    def run(self) -> None:
        self._view.mainloop()

    def _bind_callbacks(self) -> None:
        regex_input: Form = self._view.get_form_by_id("regex_input")
        regex_input.add_btn_callback(btn_id="regex_add", callback=self._handle_add_regex_callback)
        source_code_input: Form = self._view.get_form_by_id("source_code_input")
        source_code_input.add_btn_callback(btn_id="source_code_input", callback=self._handle_source_code_input)
        return None

    def _handle_add_regex_callback(self, response: Dict) -> None:
        try:
            print(response["inputs"]["regex_entry"])
        except:
            pass
        else:
            pass
        return None

    def _handle_source_code_input(self, response: Dict) -> None:
        try:
            print(response["text_entries"]["source_code_input"])
        except:
            pass
        else:
            pass
        return None
