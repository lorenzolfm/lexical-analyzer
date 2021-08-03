from genericType import T
from Node import Node
from queue import Queue


class BinaryTree:
    def __init__(self, root: Node = None) -> None:
        self._size = 0
        self._root: Node = root
        if root is not None:
            self.insert(root)

    def get_root(self) -> Node:
        return self._root

    def get_size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self._size == 0

    def insert(self, value: T) -> None:
        new_node: Node = Node(value=value)
        if self.empty():
            self._root = new_node
        elif self.contains(value):
            return
        else:
            aux: Node = self._root
            flag: bool = True

            while flag:
                if (value < aux.get_value()):
                    if (aux.get_left() is None):
                        aux.set_left(new_node)
                        flag = False
                    else:
                        aux = aux.get_left()
                else:
                    if (aux.get_right() is None):
                        aux.set_right(new_node)
                        flag = False
                    else:
                        aux = aux.get_right()

        self._size += 1

    def contains(self, value: T) -> bool:
        if self.empty():
            return False
        else:
            aux: Node = self._root

            while (aux is not None):
                if (aux.get_value() == value):
                    return True
                elif (aux.get_value() < value):
                    aux = aux.get_right()
                else:
                    aux = aux.get_left()

            return False

    def remove(self, value: T) -> None:
        if self.empty():
            return
        elif (not self.contains(value)):
            return
        else:
            exclude: Node = self._root

            while (exclude.get_value() != value):
                if (value < exclude.get_value()):
                    exclude = exclude.get_left()
                else:
                    exclude = exclude.get_right()

            son: Node = exclude
            if (exclude.get_left() is not None and exclude.get_right() is not None):
                son = exclude.get_right()

                while (son.get_left() is not None):
                    son = son.get_left()

                exclude.set_value(son.get_value())
                if (son.get_right() is not None):
                    son.set_value(son.get_right().get_value())
                    son.set_right(son.get_right().get_right())

            elif (exclude.get_right() is not None):
                exclude.set_value(exclude.get_right().get_value())
                exclude.set_right(exclude.get_right().get_right())

            elif (exclude.get_left() is not None):
                exclude.set_value(exclude.get_left().get_value())
                exclude.set_left(exclude.get_left().get_left())

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

        # return str(self._root)
