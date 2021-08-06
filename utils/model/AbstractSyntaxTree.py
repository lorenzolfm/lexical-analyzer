from typing import List, Optional

from .regex_utils import setup_regex, operators, _infix_to_postfix
from .newTypes import closure
from .Node import Node


class AbstractSyntaxTree:
    def __init__(self, regex: str) -> None:
        self._size: int = len(regex)
        self._root: Optional[Node] = None
        self._create_syntax_tree_from_regex(regex)

    def _create_syntax_tree_from_regex(self, regex: str) -> None:
        postfix_regex = setup_regex(regex)
        print(postfix_regex)
        print(_infix_to_postfix("(a|b)*.a.b.b"))
        stack: List = []
        for char in postfix_regex:
            if char not in operators:
                tree = Node(char)
                stack.append(tree)
            elif char != closure:
                tree = Node(char)
                op_1 = stack.pop()
                op_2 = stack.pop()
                tree._left_child = op_2
                tree._right_child = op_1
                stack.append(tree)
            else:
                tree = Node(char)
                op = stack.pop()
                tree._left_child = op
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

    def insert(self, value) -> None:
        new_node = Node(value=value)
        if self.empty():
            self._root = new_node
        elif self.contains(value):
            return
        else:
            aux = self._root
            flag: bool = True

            while flag:
                if (value < aux.get_value()):
                    if (aux.get_left_child() is None):
                        aux.set_left_child(new_node)
                        flag = False
                    else:
                        aux = aux.get_left_child()
                else:
                    if (aux.get_right_child() is None):
                        aux.set_right_child(new_node)
                        flag = False
                    else:
                        aux = aux.get_right_child()

        self._size += 1

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

    def remove(self, value) -> None:
        if self.empty():
            return
        elif (not self.contains(value)):
            return
        else:
            exclude: Node = self._root

            while (exclude.get_value() != value):
                if (value < exclude.get_value()):
                    exclude = exclude.get_left_child()
                else:
                    exclude = exclude.get_right_child()

            son: Node = exclude
            if (exclude.get_left_child() is not None and exclude.get_right_child() is not None):
                son = exclude.get_right_child()

                while (son.get_left_child() is not None):
                    son = son.get_left_child()

                exclude.set_value(son.get_value())
                if (son.get_right_child() is not None):
                    son.set_value(son.get_right_child().get_value())
                    son.set_right_child(son.get_right_child().get_right())

            elif (exclude.get_right_child() is not None):
                exclude.set_value(exclude.get_right_child().get_value())
                exclude.set_right_child(exclude.get_right_child().get_right())

            elif (exclude.get_left_child() is not None):
                exclude.set_value(exclude.get_left_child().get_value())
                exclude.set_left_child(exclude.get_left_child().get_left())

            else:
                del exclude

        self._size -= 1
