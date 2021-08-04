from typing import Union
class Node:
    def __init__(self, value: str = "", left_child = None, right_child = None) -> None:
        self._value = value
        self._left_child = left_child
        self._right_child = right_child
        self._firstpos = None
        self._lastpos = None
        self._followpos = None
        return None

    def get_value(self) -> str:
        return self._value

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child

    def set_left_child(self, node) -> None:
        self._left_child = node
        return None

    def set_right_child(self, node) -> None:
        self._right_child = node
        return None
