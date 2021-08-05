from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self,
                 value: str = "",
                 left_child: Optional[Node] = None,
                 right_child: Optional[Node] = None
                 ) -> None:
        self._value = value
        self._left_child: Optional[Node] = left_child
        self._right_child: Optional[Node] = right_child
        self._position: int = 0
        self._nullable: bool = False
        self._firstpos: set = set()
        self._lastpos: set = set()
        self._followpos: set = set()

    def get_position(self) -> int:
        return self._position

    def get_nullable(self) -> bool:
        return self._nullable

    def get_firstpos(self) -> set:
        return self._firstpos

    def get_lastpos(self) -> set:
        return self._lastpos

    def get_followpos(self) -> set:
        return self._followpos

    def set_position(self, pos: int) -> None:
        self._position = pos
        return None

    def set_firstpos(self, firstpos: set) -> None:
        self._firstpos = firstpos
        return None

    def set_lastpos(self, lastpos: set) -> None:
        self._lastpos = lastpos
        return None

    def set_followpos(self, followpos: set) -> None:
        self._followpos = followpos
        return None

    def get_value(self) -> str:
        return self._value

    def get_left_child(self) -> Optional[Node]:
        return self._left_child

    def get_right_child(self) -> Optional[Node]:
        return self._right_child

    def set_value(self, value: str) -> None:
        self._value = value

    def set_left_child(self, node: Node) -> None:
        self._left_child = node
        return None

    def set_right_child(self, node: Node) -> None:
        self._right_child = node
        return None

    def in_order(self, array: List) -> None:
        if self._left_child is not None:
            self._left_child.in_order(array)

        array.append(self._value)

        if self._right_child is not None:
            self._right_child.in_order(array)

        return None

    def __repr__(self) -> str:
        return self.get_value()
