from tkinter import ttk, Tk


class Container(ttk.LabelFrame):
    def __init__(
                self,
                parent: Tk,
                label: str = "",
                row: int = 0,
                column: int = 0,
                rowspan: int = 1
                ) -> None:
        super().__init__(
            master=parent,
            text=label,
            borderwidth=2,
            relief="groove",
            padding=5
        )
        self.grid(row=row, rowspan=rowspan, column=column, sticky="nwse")
        self._make_responsive(parent)

    @staticmethod
    def _make_responsive(parent) -> None:
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
