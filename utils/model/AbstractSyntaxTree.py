from queue import Queue
from .Node import Node

class AbstractSyntaxTree:
    def __init__(self, regex: str) -> None:
        self._size: int = 0
        self._root = Node()
        self._create_syntax_tree_from_regex(regex)
        return None

    def _create_syntax_tree_from_regex(self, regex: str) -> None:
        regex+= "#"
        print(regex)
        return None

    def get_root(self):
        return self._root

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

    def __repr__(self):
        aux = self._root
        fila = Queue()
        fila.put(aux)
        saida = ""
        separator = ""
        while not fila.empty():
            fila_aux = Queue()
            while not fila.empty():
                node = fila.get()
                saida += f" {node} {separator}"
                if (node is not None and (node.get_left() is not None or node.get_right() is not None)):
                    fila_aux.put(node.get_left())
                    fila_aux.put(node.get_right())

                if separator == "X":
                    separator = "|"
                else:
                    separator = "X"

            fila = fila_aux
            saida += "\n"

        return saida
