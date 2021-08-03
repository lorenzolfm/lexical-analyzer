from genericType import T


class Node:
    def __init__(self, value: T = None, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def get_value(self) -> T:
        return self._value

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def set_left(self, node) -> None:
        self._left = node

    def set_right(self, node) -> None:
        self._right = node

    def set_value(self, value: T) -> None:
        self._value = value

    def __repr__(self):
        return str(self._value)
