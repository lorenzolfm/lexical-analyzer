from typing import List

from .regex_utils import setup_regex, operators
from .newTypes import closure, optional
from .Node import Node

class AbstractSyntaxTree:
    def __init__(self, regex: str) -> None:
        self._size: int = len(regex)
        self._create_syntax_tree_from_regex(regex)

    def _create_syntax_tree_from_regex(self, regex: str) -> None:
        postfix_regex = setup_regex(regex)
        stack: List = []
        for char in postfix_regex:
            if char not in operators:
                tree = Node(char)
                stack.append(tree)
            elif (char != closure) and (char != optional):
                tree = Node(char)
                op_1, op_2 = stack.pop(), stack.pop()
                tree.set_left_child(op_2)
                tree.set_right_child(op_1)
                stack.append(tree)
            else:
                tree = Node(char)
                op = stack.pop()
                tree.set_left_child(op)
                stack.append(tree)

        self._root: Node = stack.pop()
        return None

    def get_root(self):
        return self._root

    def in_order(self):
        array: List[Node] = []
        if not self.empty():
            self._root.in_order(array)

        return array

    def get_size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self._size == 0

    def contains(self, value) -> bool:
        if self.empty():
            return False
        else:
            aux: Node = self._root

            while (aux is not None):
                if (aux.get_value() == value):
                    return True
                elif (aux.get_value() < value):
                    aux = aux.get_right_child()
                else:
                    aux = aux.get_left_child()

            return False
