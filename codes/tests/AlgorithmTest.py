import unittest

from ..utils.model.FiniteAutomata import FiniteAutomata
from ..utils.model.Transition import Transition
from ..utils.model.State import State

from ..utils.algorithm import automata_union

class AlgorithmTest(unittest.TestCase):
    def test_automata_union(self) -> None:
        a = State("A")
        b = State("B")
        c = State("C")

        symbols = {'0', '1', '&'}
        transitions = {
            Transition(a, '0', b),
            Transition(a, '0', c),
            Transition(a, '1', a),
            Transition(a, '&', b),
            Transition(b, '&', c),
            Transition(b, '1', b),
            Transition(c, '0', c),
            Transition(c, '1', c)
        }

        initial_state = a
        final_states = {c}

        fa_0 = FiniteAutomata(
            states = {a,b,c},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )

        print(fa_0)


        # actual = fa_0.determinization()

        # p = State("p")
        # q = State("q")
        # r = State("r")

        # symbols = {'a', 'b', 'c', '&'}
        # transitions = {
            # Transition(p, '&', p),
            # Transition(p, '&', q),
            # Transition(p, 'b', q),
            # Transition(p, 'c', r),
            # Transition(q, 'a', p),
            # Transition(q, 'b', r),
            # Transition(q, 'c', p),
            # Transition(q, 'c', q),
        # }

        # initial_state = p
        # final_states= {r}

        # fa_1 = FiniteAutomata(
            # states = {p,q,r},
            # symbols = symbols,
            # transitions = transitions,
            # initial_state = initial_state,
            # final_states = final_states
        # )

        # actual = automata_union(fa_0, fa_1)
        # print(actual)
        return None
