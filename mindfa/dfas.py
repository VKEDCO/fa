## =======================================
## An implementation of the algorithm given in
## Ch. 03 of "Introduction to Automata Theory, Languages,
## and Computation" by J. Hopcroft and J. Ullman.
## The algorithm is based on the Myhill-Nerode Theorem.
##
## Author: Vladimir Kulyukin
## Bugs to vladimir dot kulyukin at gmail dot com
## =======================================
from DFA import DFA

__metaclass__ = type

class MyhillNerodeMinDFA(DFA):
    'Minimization algorithm basd on Myhill-Nerode Theorem'

    def __init__(self):
        super(MyhillNerodeMinDFA, self).__init__()

    def minimize(self):
        self.remove_unreachable_states()
        marked_states = {}
        state_pair_lists = {}
        states, final_states = self.get_states(), self.get_final_states()
        diff_states = states.difference(final_states)
        self.__initialize_marked_states(marked_states)
        for p in final_states:
            for q in diff_states:
                self.__mark_state_pair(p, q, marked_states)
        fin_pairs = set([(x, y)
                           for x in final_states
                           for y in final_states
                           if x != y])
        diff_pairs = set([(x, y)
                             for x in diff_states
                             for y in diff_states
                             if x != y])
        state_pairs = fin_pairs.union(diff_pairs)
        for p, q in state_pairs:
            if self.__is_state_pair_marked_on_some_symbol(p, q, marked_states):
                self.__mark_state_pair(p, q, marked_states)
                self.__mark_listed_state_pairs(p, q, marked_states, state_pair_lists)
            else:
                for symbol in self.get_sigma():
                    pp, qq = self.delta(p, symbol), self.delta(q, symbol)
                    if pp != qq:
                        self.__add_to_state_pair_list_for(pp, qq, p, q, state_pair_lists)
        return self.__construct_min_dfa_from_marked_states(marked_states)

    def __initialize_marked_states(self, marked_states):
        for s1 in self.get_states():
            for s2 in self.get_states():
                if s1 != s2:
                    key01, key02 = (s1, s2), (s2, s1)
                    if not (marked_states.has_key(key01) or marked_states.has_key(key02)):
                        marked_states[key01] = False

    def __mark_state_pair(self, s1, s2, marked_states):
        key01, key02 = (s1, s2), (s2, s1)
        if marked_states.has_key(key01):
            marked_states[key01] = True
        elif marked_states.has_key(key02):
            marked_states[key02] = True
        else:
            raise Exception('Unmarkable state pair: ' + str(key01))

    def __is_state_pair_marked(self, s1, s2, marked_states):
        key01, key02 = (s1, s2), (s2, s1)
        if marked_states.has_key(key01):
            return marked_states[key01]
        elif marked_states.has_key(key02):
            return marked_states[key02]
        else:
            raise Exception('Unknown state pair; ' + str(key01))

    def __is_state_pair_marked_on_some_symbol(self, s1, s2, marked_states):
        for symbol in self.get_sigma():
            p, q = self.delta(s1, symbol), self.delta(s2, symbol)
            if p != q:
                if self.__is_state_pair_marked(p, q, marked_states):
                    return True
        return False

    def __add_to_state_pair_list_for(self, pp, qq, p, q, state_pair_lists):
        key01, key02 = (pp, qq), (qq, pp)
        if state_pair_lists.has_key(key01):
            state_pair_lists[key01].append((p, q))
        elif state_pair_lists.has_key(key02):
            state_pair_lists[key02].append((p, q))
        else:
            state_pair_lists[key01] = [(p, q)]

    def __mark_listed_state_pairs(self, s1, s2, marked_states, state_pair_lists):
        self.__mark_state_pair(s1, s2, marked_states)
        key01, key02 = (s1, s2), (s2, s1)
        state_list_01 = state_pair_lists.get(key01, [])
        state_list_02 = state_pair_lists.get(key02, [])
        for p01, q01 in state_list_01:
            self.__mark_listed_state_pairs(p01, q01, marked_states, state_pair_lists)
        for p02, q02 in state_list_02:
            self.__mark_listed_state_pairs(p02, q02, marked_states, state_pair_lists)

    def __construct_equivalence_class_for_state(self, state, unmarked_states):
        common_state = ()
        shared_unmarked_states = [us for us in unmarked_states if state in us]
        for sus in shared_unmarked_states:
            common_state += sus
        set_common_state = set(common_state)
        common_state = ()
        for x in set_common_state:
            common_state += (x,)
        if len(common_state) == 0:
            common_state = (state,)
        return common_state

    def __find_equivalence_class_for_state(self, state, equiv_classes):
        x = [eqc for eqc in equiv_classes if state in eqc]
        if len(x) == 0:
            return None
        else:
            return x[0]

    ## for debugging only
    def display_unmarked_states(self, marked_states):
        for k, v in marked_states.iteritems():
            if v == False:
                print k

    def __get_unmarked_states(self, marked_states):
        return [k for k, v in marked_states.iteritems() if v == False]

    def __construct_min_dfa_from_marked_states(self, marked_states):
        sigma = self.get_sigma()
        final_states = self.get_final_states()
        unmarked_states = self.__get_unmarked_states(marked_states)
        new_delta_table = {}
        new_states = []
        ##print 'Unmarked state pairs:'
        ##print_unmarked_state_pairs(marked_states)
        for old_state in self.get_states():
            eqc = self.__construct_equivalence_class_for_state(old_state, unmarked_states)
            if len(eqc) > 0 and not eqc in new_states:
                new_states.append(eqc)
        old_start_state = self.get_start_state()
        ##print 'New States: ', str(new_states)
        new_start_state = [s for s in new_states if old_start_state in s][0]
        ##print 'New Start State: ', new_start_state
        ##return None
        q_of_states = [new_start_state]
        explored_states = {}
        while len(q_of_states) != 0:
            ##print q_of_states
            curr_state = q_of_states.pop()
            explored_states[curr_state] = True
            for s in sigma:
                old_state = self.delta(curr_state[0], s)
                new_state = self.__find_equivalence_class_for_state(old_state, new_states)
                if new_state == None:
                    new_state = old_state,
                new_delta_table[(curr_state, s)] = new_state
                if not explored_states.has_key(new_state):
                    q_of_states.append(new_state)
        rslt_dfa = DFA()
        rslt_dfa.set_states(set([x[0] for x in new_delta_table.iterkeys()]))
        rslt_dfa.set_sigma(sigma)
        rslt_dfa.set_start_state(new_start_state)
        rslt_dfa.set_delta_table(new_delta_table)
        rslt_dfa.set_final_states(set([x[0]
                                       for x in new_delta_table.iterkeys()
                                       if len(final_states.intersection(set(x[0]))) > 0]))
        return rslt_dfa
