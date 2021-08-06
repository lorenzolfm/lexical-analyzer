from __future__ import annotations
from typing import List, Optional, Dict, Set

from .newTypes import concat, closure, union, epsilon


class Node:
    def __init__(self,
                 value: str,
                 leaf_nodes: Dict[int, Node],
                 left_child: Optional[Node] = None,
                 right_child: Optional[Node] = None,
                 position: Optional[int] = None,
                 ) -> None:
        self._value = value
        self._left_child: Optional[Node] = left_child
        self._right_child: Optional[Node] = right_child
        self._position: Optional[int] = position
        self._nullable: bool = self._set_nullable()
        self._firstpos: set = self._set_firstpos()
        self._lastpos: set = self._set_lastpos()
        self._followpos: Optional[set] = self.set_followpos(leaf_nodes)

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

    def _set_nullable(self) -> bool:
        if self.is_leaf():
            if self._value == epsilon:
                return True
            else:
                return False
        elif self._value == union:
            return (self._left_child.get_nullable() or self._right_child.get_nullable())
        elif self._value == concat:
            return (self._left_child.get_nullable() and self._right_child.get_nullable())
        else:
            return True

    def _set_firstpos(self) -> set:
        if self.is_leaf():
            if self._value == epsilon:
                return set()
            else:
                return {self._position}
        elif self._value == union:
            return (self._left_child.get_firstpos() | self._right_child.get_firstpos())
        elif self._value == concat:
            if self._left_child.get_nullable():
                return (self._left_child.get_firstpos() | self._right_child.get_firstpos())
            else:
                return self._left_child.get_firstpos()
        else:
            return self._left_child.get_firstpos()

    def _set_lastpos(self) -> set:
        if self.is_leaf():
            if self._value == epsilon:
                return set()
            else:
                return {self._position}
        elif self._value == union:
            return (self._left_child.get_firstpos() | self._right_child.get_firstpos())
        elif self._value == concat:
            if self._right_child.get_nullable():
                return (self._left_child.get_firstpos() | self._right_child.get_firstpos())
            else:
                return self._right_child.get_firstpos()
        else:
            return self._left_child.get_firstpos()

    def set_followpos(self, node: Dict[int, Node]) -> Optional[set]:
        if not self.is_leaf():
            if self._value == concat:
                for pos in self._left_child.get_lastpos():
                    node[pos].update_followpos(self._left_child.get_firstpos())
            elif self._value == closure:
                for pos in self._lastpos:
                    node[pos].update_followpos(self._firstpos)

            return None

        return set()

    def update_followpos(self, followpos: Set[int]) -> None:
        self._followpos |= followpos
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

    def is_leaf(self) -> bool:
        if (self._left_child and self._right_child):
            return True

        return False

    def __repr__(self) -> str:
        return self.get_value()
