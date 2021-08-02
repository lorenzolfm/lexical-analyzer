class State:
    def __init__(self, name: str, label: str):
        self._name = name
        self._label = label

    def get_name(self) -> str:
        return self._name

    def get_label(self) -> str:
        return self._label
