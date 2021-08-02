class FiniteAutomata:
    def __init__(self, states, symbols, transitions, initial_state, final_states):
        self._states = states
        self._symbols = symbols
        self._transitions = transitions
        self._initial_state = initial_state
        self._final_states = final_states
