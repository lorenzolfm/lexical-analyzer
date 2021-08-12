from tkinter import ttk

class Logger(ttk.Label):
    def __init__(self, parent: ttk.LabelFrame) -> None:
        self._message: str = ""
        super().__init__(master=parent, text=self._message)
        self.grid(row=2, column=0)
        return None

    def log(self, message) -> None:
        self.config(text=message)
        return None
