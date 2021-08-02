import unittest

from utils.model.State import State
from utils.model.Transition import Transition
from utils.model.FiniteAutomata import FiniteAutomata

class FiniteAutomataTests(unittest.TestCase):
    def test_determinization(self) -> None:
        a = State("A")
        b = State("B")
        c = State("C")

        symbols = ['0', '1', '&']
        transitions = [
            Transition(a, '0', b),
            Transition(a, '0', c),
            Transition(a, '1', a),
            Transition(a, '&', a),
            Transition(b, '&', c),
            Transition(b, '1', b),
            Transition(c, '0', c),
            Transition(c, '1', c)
        ]

        initial_state = a
        final_states= [c]

        fa = FiniteAutomata(
            states = [a,b,c],
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )

        fa.determinization()
        return None
