from typing import List, Dict, Set

from .newTypes import closure, optional, operators, epsilon, end_of_sentence
from .FiniteAutomata import FiniteAutomata
from ..algorithm import get_key_by_value
from .regex_utils import setup_regex
from .Token import Token
from .Transition import Transition
from .State import State
from .Node import Node

state_id: int = 65

class AbstractSyntaxTree:
    def __init__(self, regex: str, token: Token) -> None:
        self._create_syntax_tree_from_regex(regex)
        self._set_token_for_final_states(regex)

    def _create_syntax_tree_from_regex(self, regex: str) -> None:
        postfix_regex = setup_regex(regex)
        symbols: Set[str] = set()
        leaf_nodes: Dict[int, Node] = {}
        position: int = 1
        stack: List = []
        for char in postfix_regex:
            if char not in operators:
                tree: Node = Node(value=char, leaf_nodes=leaf_nodes, position=position)
                stack.append(tree)
                leaf_nodes[position] = tree
                position += 1
                symbols |= {char}
            elif (char != closure) and (char != optional):
                op_1, op_2 = stack.pop(), stack.pop()
                tree: Node = Node(value=char, leaf_nodes=leaf_nodes, left_child=op_2, right_child=op_1)
                stack.append(tree)
            else:
                op = stack.pop()
                tree: Node = Node(value=char, leaf_nodes=leaf_nodes, left_child=op)
                stack.append(tree)

        self._root: Node = stack.pop()
        self._size: int = len(postfix_regex)
        self._create_finite_automata(leaf_nodes, symbols - {end_of_sentence, epsilon})

        return None

    def _create_finite_automata(self, leaf_nodes: Dict[int, Node], symbols: Set[str]) -> None:
        # Method setup
        global state_id
        final_state_flag: int = max(list(leaf_nodes.keys()))
        # state_id: int = 65
        first_set: Set[int] = self._root.get_firstpos()
        stack: List[Set[int]] = [first_set]
        marked_states: List[Set[int]] = []

        # DFA setup
        initial_state: State = State(name=chr(state_id), label=str(first_set))
        state_id += 1
        states: Set[State] = {initial_state}
        final_states: Set[State] = {initial_state} if final_state_flag in first_set else set()
        transitions: Set[Transition] = set()

        # Conversion setup
        convert_state_to_set: Dict[State, Set[int]] = {initial_state: first_set}
        while stack:
            set_of_position_nodes: Set[int] = stack.pop()
            marked_states.append(set_of_position_nodes)
            for symbol in sorted(symbols):
                followpos: Set[int] = set()
                for pos in sorted(set_of_position_nodes):
                    if symbol == leaf_nodes[pos].get_value():
                        followpos |= leaf_nodes[pos].get_followpos()

                if followpos:
                    origin_state = get_key_by_value(convert_state_to_set, set_of_position_nodes)
                    if origin_state is None:
                        origin_state = State(name=chr(state_id), label=str(set_of_position_nodes))
                        state_id += 1
                        convert_state_to_set[origin_state] = set_of_position_nodes
                        states.add(origin_state)
                        if final_state_flag in set_of_position_nodes:
                            final_states.add(origin_state)

                    destiny_state = get_key_by_value(convert_state_to_set, followpos)
                    if destiny_state is None:
                        destiny_state: State = State(name=chr(state_id), label=str(followpos))
                        state_id += 1
                        convert_state_to_set[destiny_state] = followpos
                        states.add(destiny_state)
                        if final_state_flag in followpos:
                            final_states.add(destiny_state)

                    transitions.add(Transition(origin_state, symbol, destiny_state))

                    if (followpos not in marked_states + stack):
                        stack.append(followpos)

        self._finite_automata: FiniteAutomata = FiniteAutomata(states=states,
                                                               initial_state=initial_state,
                                                               final_states=final_states,
                                                               transitions=transitions,
                                                               symbols=symbols)

        return None

    def _set_token_for_final_states(self, token) -> None:
        for state in self._finite_automata.get_final_states():
            state.set_token(token)
        return None

    def get_finite_automata(self) -> FiniteAutomata:
        return self._finite_automata

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

    def __repr__(self) -> str:
        return str(self.in_order())
