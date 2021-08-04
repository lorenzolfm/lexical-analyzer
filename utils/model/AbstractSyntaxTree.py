from queue import Queue
from .Node import Node

class AbstractSyntaxTree:
    def __init__(self, regex: str) -> None:
        regex = regex.replace(" ", "")
        self._create_syntax_tree_from_regex(regex)

        self._size: int = 0
        self._root = Node()
        return None

    def _create_syntax_tree_from_regex(self, regex: str) -> None:
        regex = self._setup_regex(regex)
        regex = self._reorg(regex)
        return None

    def _setup_regex(self, regex: str) -> str:
        regex_size: int = len(regex)
        previous: str = " "
        n_concat: int = 0

        new_regex: str = regex
        for i in range(regex_size):
            current = regex[i]
            if self._needs_concat_symbol(previous, current):
                new_regex = new_regex[:i+n_concat] + "." + new_regex[i+n_concat:]
                n_concat += 1
            previous = current

        return new_regex + ".#"

    def _needs_concat_symbol(self, previous: str, current: str) -> bool:
        return (previous.isalnum() or previous in "*?)") and (current.isalnum() or current == "(")

    def _reorg(self, regex: str) -> str:
        reorg = ""
        regex = self._reverse_regex(regex)
        operators = "|?*."
        i = 0
        while (i < len(regex) - 1):
            actual = regex[i]
            next_ = regex[i+1]

            if actual == "(":
                string = self._get_substr(regex, i + 1)
                subregex: str = self._reorg(string)
                i += len(subregex)
                reorg += subregex
            elif (actual not in operators) and (next_ in operators):
                reorg += next_ + actual
                i += 2
            else:
                reorg += actual + next_
                i += 1

        return reorg

    def _reverse_regex(self, regex: str) -> str:
        output: str = ""
        for i in reversed(regex):
            if i == "(":
                output += ")"
            elif i == ")":
                output += "("
            else:
                output += i
        return output

    def _get_substr(self, string: str, index: int) -> str:
        substring = ""
        stack = ['(']
        while (stack):
            if string[index] == ")":
                stack.pop()
                if stack:
                    substring += string[index]
            elif string[index] == "(":
                stack.append("(")
                substring += string[index]
            else:
                substring += string[index]
            index += 1

        return substring

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
