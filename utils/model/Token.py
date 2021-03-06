from typing import Optional


class Token:
    def __init__(self, name: str, attribute: Optional[str] = None) -> None:
        self._name: str = name
        self._attribute: Optional[str] = attribute

    def get_name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"<{self._name}>"
