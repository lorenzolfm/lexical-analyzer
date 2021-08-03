import unittest

from ..utils.algorithm import automata_union
from ..utils.model.State import State
from ..utils.model.Transition import Transition
from ..utils.model.FiniteAutomata import FiniteAutomata

class FiniteAutomataTests(unittest.TestCase):
    def test_e_closure(self) -> None:
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

        fa = FiniteAutomata(
            states = {a,b,c},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )


        actual = fa._get_e_closure()
        self.assertEqual(actual[a], {a, b, c})
        self.assertEqual(actual[b], {b, c})
        self.assertEqual(actual[c], {c})

        p = State("p")
        q = State("q")
        r = State("r")

        symbols = {'a', 'b', 'c', '&'}
        transitions = {
            Transition(p, '&', p),
            Transition(p, '&', q),
            Transition(p, 'b', q),
            Transition(p, 'c', r),
            Transition(q, 'a', p),
            Transition(q, 'b', r),
            Transition(q, 'c', p),
            Transition(q, 'c', q),
        }

        initial_state = p
        final_states= {r}

        fa = FiniteAutomata(
            states = {p,q,r},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )
        actual = fa._get_e_closure()
        self.assertEqual(actual[p], {p,q})
        self.assertEqual(actual[q], {q})
        self.assertEqual(actual[r], {r})

        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2")
        q3 = State("q3")

        symbols = {'a', 'b', '&'}
        transitions = {
            Transition(q0, 'a', q1), Transition(q0, '&', q1), Transition(q1, 'a', q2), Transition(q1, 'b', q2), Transition(q1, '&', q2),
            Transition(q2, 'b', q3),
            Transition(q3, 'a', q1),
            Transition(q3, 'b', q0),
        }

        initial_state = q0
        final_states= {q2}

        fa = FiniteAutomata(
            states = {q0,q1,q2,q3},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )
        actual = fa._get_e_closure()
        self.assertEqual(actual[q0], {q0,q1,q2})
        self.assertEqual(actual[q1], {q1,q2})
        self.assertEqual(actual[q2], {q2})
        self.assertEqual(actual[q3], {q3})
        return None

    def test_get_new_transitions(self) -> None:
        q0, q1, q2, q3 = State("q0"), State("q1"), State("q2"), State("q3")
        symbols = {'a', 'b', '&'}
        transitions = {
            Transition(q0, 'a', q1),
            Transition(q0, '&', q1),
            Transition(q1, 'a', q2),
            Transition(q1, 'b', q2),
            Transition(q1, '&', q2),
            Transition(q2, 'b', q3),
            Transition(q3, 'a', q1),
            Transition(q3, 'b', q0),
        }
        initial_state = q0
        final_states= {q2}
        fa = FiniteAutomata(
            states = {q0,q1,q2,q3},
            symbols = symbols,
            transitions = transitions,
            initial_state = initial_state,
            final_states = final_states
        )
        e_closure = fa._get_e_closure()
        new_states = list(e_closure.values())
        fa._symbols.remove("&")
        new_transitions = fa._get_new_transitions(new_states, e_closure)
        # Era pra ser isso mesmo?
        print(new_transitions)
        return None
