from typing import Dict, Union, Callable
from tkinter import ttk, Tk, Toplevel, StringVar, BooleanVar, Listbox, SINGLE, END, Text, FIRST, NORMAL, DISABLED

class Form(ttk.LabelFrame):
    def __init__(
        self,
        parent: Union[Tk, Toplevel, ttk.LabelFrame],
        label: str = "",
        row: int = 0,
        column: int = 0
    ) -> None:
        super().__init__(
            master=parent,
            text=label,
            borderwidth=2,
            relief="groove",
            padding=5
        )
        self.grid(row=row, column=column, sticky="nwse")
        self._init_attributes()

    def _init_attributes(self) -> None:
        self._entries: Dict[str, ttk.Entry] = {}
        self._buttons: Dict[str, ttk.Button] = {}
        self._text_entries: Dict[str, Text] = {}
        self._labels: Dict[str, ttk.Label] = {}
        self._checkbuttons: Dict[str, ttk.Checkbutton] = {}
        self._listboxes: Dict[str, Listbox] = {}
        return None

    def add_label(self, idd: str, label: str = "", row: int = 0, column: int = 0) -> None:
        tk_label: ttk.Label = ttk.Label(master=self, text=label)
        tk_label.grid(row=row, column=column)
        self._labels[idd] = tk_label
        return None

    def add_entry(self, idd: str, label: str = "", row: int = 0, column: int = 0) -> None:
        tk_label: ttk.Label = ttk.Label(master=self, text=label)
        tk_label.grid(row=row, column=column)
        tk_entry: ttk.Entry = ttk.Entry(master=self, textvariable=StringVar(), width=10)
        tk_entry.grid(row=row, column=(column+1))
        self._entries[idd] = tk_entry
        return None

    def add_button(self, idd: str, label: str = "", row: int = 0, column: int = 0, rowspan: int = 1, columnspan: int = 1) -> None:
        tk_button: ttk.Button = ttk.Button(master=self, text=label)
        tk_button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        self._buttons[idd] = tk_button
        return None

    def add_text_entry(self, idd: str, height: int = 20, width: int = 20, bg = "#ffffff", row: int = 0, column: int = 0, state=NORMAL) -> None:
        tk_text: Text = Text(master=self, height=height, width=width, bg=bg, state=state)
        tk_text.grid(row=row, column=column)
        self._text_entries[idd] = tk_text
        return None

    def insert_text(self, idd: str, text: str) -> None:
        text_entry = self._text_entries[idd]
        text_entry["state"] = NORMAL
        text_entry.insert('1.0', text+"\n")
        text_entry["state"] = DISABLED
        return None

    def add_checkbutton(self, idd: str, label: str = "", row: int = 0, column: int = 0) -> None:
        self._bool_var: BooleanVar = BooleanVar()
        tk_checkbutton: ttk.Checkbutton = ttk.Checkbutton(master=self, text=label, variable=self._bool_var)
        tk_checkbutton.grid(row=row, column=column)
        self._checkbuttons[idd] = tk_checkbutton
        return None

    def add_listbox(self, idd: str, row: int = 0, column: int = 0) -> None:
        tk_listbox = Listbox(self, listvariable=StringVar(), selectmode=SINGLE)
        tk_listbox.grid(row=row, column=column, columnspan=2)
        self._listboxes[idd] = tk_listbox
        return None

    def add_to_listbox(self, idd: str, name: str) -> None:
        self._listboxes[idd].insert(END, name)
        return None

    def delete_from_listbox(self, idd: str) -> None:
        item = self._get_selected_listbox_item_id(idd)
        self._listboxes[idd].delete(item)
        return

    # O que acontece se nenhum selecionado?
    def _get_selected_listbox_item_id(self, idd: str):
        # Por que o índice 0?
        return self._listboxes[idd].curselection()[0]

    def add_btn_callback(self, btn_id: str, callback: Callable) -> None:
        self._buttons[btn_id]["command"] = lambda: self._post_form(callback)
        return None

    def _post_form(self, callback: Callable) -> Dict:
        res: Dict = {}

        if self._entries:
            res["inputs"] = {}
            for user_input_id, user_input in self._entries.items():
                res["inputs"][user_input_id] = user_input.get()

        if self._checkbuttons:
            res["checkbuttons"] = {}
            for cbtn_id, _ in self._checkbuttons.items():
                res["checkbuttons"][cbtn_id] = self._bool_var.get()

        if self._listboxes:
            res["listbox_selection"] = {}
            for lb_id, _ in self._listboxes.items():
                for obj in self._listboxes[lb_id].curselection():
                    res["listbox_selection"]["obj_name"] = self._listboxes[lb_id].get(obj)

        if self._text_entries:
            res["text_entries"] = {}
            for txt_id, user_input in self._text_entries.items():
                res["text_entries"][txt_id] = user_input.get("1.0", "end")

        callback(res)
        return res
