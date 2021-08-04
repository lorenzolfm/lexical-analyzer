from typing import Dict
from tkinter import Tk

from .Form import Form
from .Container import Container

class View(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Lex")
        self._forms: Dict[str, Form] = {}
        self._create_widgets()
        return None

    def get_form_by_id(self, idd: str) -> Form:
        return self._forms[idd]

    def _create_widgets(self) -> None:
        menu: Container = Container(parent=self, label="Menu")
        self._create_project_form(menu)
        self._create_execution_form(menu)

        view: Container = Container(parent=self, label="View", column=1)
        self._create_regex_output_form(view)
        self._create_symbol_table(view)
        return None

    def _create_project_form(self, parent: Container) -> None:
        idd: str = "regex_input"
        new_form: Form = Form(parent=parent, label="Regex Input")
        new_form.add_entry(idd="regex_entry", label = "New Regex:")
        new_form.add_button(idd="regex_add", label = "Add Regex", row=1, column=1)
        self._forms[idd] = new_form
        return None

    def _create_execution_form(self, parent: Container) -> None:
        idd: str = "source_code_input"
        new_form: Form = Form(parent=parent, label="Source Code Input", row=1)
        new_form.add_text_entry(idd=idd)
        new_form.add_button(idd=idd, label="Enter Source Code", row=1)
        self._forms[idd] = new_form
        return None

    def _create_regex_output_form(self, parent: Container) -> None:
        idd: str = "regex_output"
        new_form: Form = Form(parent=parent, label="Regular Expressions")
        new_form.add_text_entry(idd=idd, height=4, width=50)
        return None

    def _create_symbol_table(self, parent: Container) -> None:
        idd: str = "symbol_table"
        new_form: Form = Form(parent=parent, label="Symbol Table", row=1)
        new_form.add_text_entry(idd=idd, width=50)
        return None
