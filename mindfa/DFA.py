## ================================================
## Deterministic Finite State Automaton
## Author: Vladimir Kulyukin
## Bugs to vladimir dot kulyukin at gmail dot com
## ================================================

__metaclass__ = type

class DFA:
    'Deterministic Finite State Automaton'
    def __init__(self):
        self.__states = set()
        self.__sigma = set()
        self.__start_state = None
        self.__final_states = set()
        self.__delta_table = {}
    
    def set_states(self, iterable):
        self.__states = set(iterable)

    def get_states(self):
        return self.__states

    def set_start_state(self, start_state):
        self.__start_state = start_state

    def get_start_state(self):
        return self.__start_state

    def set_sigma(self, iterable):
        self.__sigma = set(iterable)

    def get_sigma(self):
        return self.__sigma

    def set_final_states(self, iterable):
        self.__final_states = set(iterable)

    def get_final_states(self):
        return self.__final_states

    def set_delta_table(self, delta_table):
        self.__delta_table = delta_table

    def get_delta_table(self):
        return self.__delta_table

    def add_transition(self, from_state, symbol, end_state):
        self.__delta_table[(from_state, symbol)] = end_state

    def del_transition(self, from_state, symbol, end_state):
        key = (from_state, symbol)
        if self.__delta_table.has_key(key):
            del self.__delta_table[key]

    def delta(self, state, symbol):
        key = (state, symbol)
        if self.__delta_table.has_key(key):
            return self.__delta_table[key]
        else:
            raise Exception('No transition available on ' + str(key))

    def process_input_from_state(self, state, input):
        curr_state = state
        for symbol in input:
            try:
                curr_state = self.delta(curr_state, symbol)
            except Exception:
                return None
        return curr_state

    def process_input(self, input):
        return self.process_input_from_state(self.__start_state,
                                             input)

    def is_input_accepted(self, input):
        return self.process_input(input) in self.__final_states

    ## self is a DFA if either it has no states or no input alphabet
    ## or the transition function, delta, is defined for every
    ## symbol in the alphabet and every state in the state set.
    def is_dfa(self):
        if len(self.__states) == 0 or len(self.__sigma) == 0:
            return True
        else:
            for state in self.__states:
                for symbol in self.__sigma:
                    try:
                        self.delta(state, symbol)
                    except Exception:
                        return False
            return True

    def remove_unreachable_states(self):
        reachable_states = {}
        reachable_states[self.__start_state] = True
        expected_states = {}
        q = [self.__start_state]
        while len(q) > 0:
            curr_state = q.pop()
            for s in self.__sigma:
                end_state = self.delta(curr_state, s)
                if not reachable_states.has_key(end_state):
                    reachable_states[end_state] = True
                if not expected_states.has_key(end_state):
                    q.append(end_state)
            expected_states[curr_state] = True
        new_states = set([state
                          for state in self.__states
                          if reachable_states.get(state, False) == True])
        new_delta_table = {}
        for k, v in self.__delta_table.iteritems():
            if reachable_states.get(k[0], False) and reachable_states.get(v, False):
                new_delta_table[k] = v
        self.set_states(new_states)
        self.set_delta_table(new_delta_table)

    ## for debugging only
    def get_delta_transitions(self, state):
        return [(k, '->', v) for (k, v) in self.__delta_table.iteritems() if k[0] == state]
