## ===============================================
## Several examples of applying the Myhill-Nerode
## Theorem to minimize dfas.
## Author: Vladimir Kulyukin
## Bugs to vladimir dot kulyukin at gmail dot com
## ===============================================

from MyhillNerodeMinDFA import MyhillNerodeMinDFA

## ===================================================
## Example from Ch. 03 of "Introduction to Automata Theory,
## Languages, and Computation" by J. Hopcroft and J. Ullman.
## Note that the state 'd' is removed as unreachable and, hence,
## does not figure in the minimized version.

dfa_01 = MyhillNerodeMinDFA()

dfa_01.set_states(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
dfa_01.set_sigma(['0', '1'])
dfa_01.set_start_state('a')
dfa_01.set_final_states(['c'])
## state a
dfa_01.add_transition('a', '0', 'b')
dfa_01.add_transition('a', '1', 'f')
## state b
dfa_01.add_transition('b', '0', 'g')
dfa_01.add_transition('b', '1', 'c')
## state c
dfa_01.add_transition('c', '0', 'a')
dfa_01.add_transition('c', '1', 'c')
## state d
dfa_01.add_transition('d', '0', 'c')
dfa_01.add_transition('d', '1', 'g')
## state e 
dfa_01.add_transition('e', '0', 'h')
dfa_01.add_transition('e', '1', 'f')
## state f 
dfa_01.add_transition('f', '0', 'c')
dfa_01.add_transition('f', '1', 'g')
## state g
dfa_01.add_transition('g', '0', 'g')
dfa_01.add_transition('g', '1', 'e')
## state h
dfa_01.add_transition('h', '0', 'g')
dfa_01.add_transition('h', '1', 'c')

mindfa_01 = dfa_01.minimize()

## ====================================================
## Example 1 from http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/min-fa.html

dfa_02 = MyhillNerodeMinDFA()
dfa_02.set_states(set(['1', '2', '3', '4', '5']))
dfa_02.set_sigma(set(['a', 'b']))
dfa_02.set_final_states(set(['1', '5']))
dfa_02.set_start_state('1')

dfa_02.add_transition('1', 'a', '3')
dfa_02.add_transition('1', 'b', '2')
dfa_02.add_transition('2', 'a', '4')
dfa_02.add_transition('2', 'b', '1')
dfa_02.add_transition('3', 'a', '5')
dfa_02.add_transition('3', 'b', '4')
dfa_02.add_transition('4', 'a', '4')
dfa_02.add_transition('4', 'b', '4')
dfa_02.add_transition('5', 'a', '3')
dfa_02.add_transition('5', 'b', '2')

mindfa_02 = dfa_02.minimize()

## ====================================================
## Example 2 from http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/min-fa.html

dfa_03 = MyhillNerodeMinDFA()

dfa_03.set_states(set(['1', '2', '3', '4', '5', '6']))
dfa_03.set_sigma(set(['a', 'b']))
dfa_03.set_final_states(set(['1', '2', '4', '5', '6']))
dfa_03.set_start_state('1')

dfa_03.add_transition('1', 'a', '2')
dfa_03.add_transition('1', 'b', '3')
dfa_03.add_transition('2', 'a', '2')
dfa_03.add_transition('2', 'b', '4')
dfa_03.add_transition('3', 'a', '3')
dfa_03.add_transition('3', 'b', '3')
dfa_03.add_transition('4', 'a', '6')
dfa_03.add_transition('4', 'b', '3')
dfa_03.add_transition('5', 'a', '5')
dfa_03.add_transition('5', 'b', '3')
dfa_03.add_transition('6', 'a', '5')
dfa_03.add_transition('6', 'b', '4')

mindfa_03 = dfa_03.minimize()

## ==========================================
## example from http://www.eecs.berkeley.edu/~sseshia/172/lectures/Lecture6.pdf

dfa_04 = MyhillNerodeMinDFA()
dfa_04.set_states(set(['a', 'b', 'c', 'd']))
dfa_04.set_sigma(set(['0', '1']))
dfa_04.set_final_states(set(['b', 'c']))
dfa_04.set_start_state('a')
dfa_04.add_transition('a', '0', 'b')
dfa_04.add_transition('a', '1', 'd')
dfa_04.add_transition('b', '0', 'c')
dfa_04.add_transition('b', '1', 'd')
dfa_04.add_transition('c', '0', 'b')
dfa_04.add_transition('c', '1', 'a')
dfa_04.add_transition('d', '0', 'c')
dfa_04.add_transition('d', '1', 'a')

mindfa_04 = dfa_04.minimize()

## ==========================================
## example 1 from https://www.cs.umd.edu/class/fall2009/cmsc330/lectures/discussion2.pdf
## Note that the FA was made complete by adding one state F.

dfa_05 = MyhillNerodeMinDFA()
dfa_05.set_states(set(['A', 'B', 'C', 'D', 'E', 'F']))
dfa_05.set_sigma(set(['0', '1']))
dfa_05.set_final_states(set(['E']))
dfa_05.set_start_state('A')
dfa_05.add_transition('A', '0', 'B')
dfa_05.add_transition('A', '1', 'C')
dfa_05.add_transition('B', '0', 'D')
dfa_05.add_transition('B', '1', 'D')
dfa_05.add_transition('C', '0', 'D')
dfa_05.add_transition('C', '1', 'D')
dfa_05.add_transition('D', '0', 'E')
dfa_05.add_transition('D', '1', 'E')
dfa_05.add_transition('E', '0', 'F')
dfa_05.add_transition('E', '1', 'F')
dfa_05.add_transition('F', '0', 'F')
dfa_05.add_transition('F', '1', 'F')

mindfa_05 = dfa_05.minimize()

## ==========================================
## example 2 from https://www.cs.umd.edu/class/fall2009/cmsc330/lectures/discussion2.pdf
## Note that the FA was made complete by adding one state F.

dfa_06 = MyhillNerodeMinDFA()
dfa_06.set_states(set(['A', 'B', 'C', 'D', 'E', 'F']))
dfa_06.set_sigma(set(['0', '1']))
dfa_06.set_final_states(set(['A', 'C', 'E']))
dfa_06.set_start_state('A')
dfa_06.add_transition('A', '0', 'A')
dfa_06.add_transition('A', '1', 'B')
dfa_06.add_transition('B', '0', 'C')
dfa_06.add_transition('B', '1', 'D')
dfa_06.add_transition('C', '0', 'C')
dfa_06.add_transition('D', '0', 'C')
dfa_06.add_transition('D', '1', 'D')
dfa_06.add_transition('C', '1', 'E')
dfa_06.add_transition('E', '0', 'E')
dfa_06.add_transition('E', '1', 'E')

mindfa_06 = dfa_06.minimize()

## ==========================================
## example 3 from https://www.cs.umd.edu/class/fall2009/cmsc330/lectures/discussion2.pdf
## Note that the FA was made complete by adding one state J.

dfa_07 = MyhillNerodeMinDFA()
dfa_07.set_states(set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']))
dfa_07.set_sigma(set(['1', '2', '3']))
dfa_07.set_start_state('A')
dfa_07.set_final_states(set(['I']))
dfa_07.add_transition('A', '1', 'B')
dfa_07.add_transition('A', '2', 'C')
dfa_07.add_transition('A', '3', 'D')

dfa_07.add_transition('B', '1', 'E')
dfa_07.add_transition('B', '2', 'E')
dfa_07.add_transition('B', '3', 'E')

dfa_07.add_transition('C', '1', 'E')
dfa_07.add_transition('C', '2', 'E')
dfa_07.add_transition('C', '3', 'E')

dfa_07.add_transition('D', '1', 'E')
dfa_07.add_transition('D', '2', 'E')
dfa_07.add_transition('D', '3', 'E')

dfa_07.add_transition('E', '1', 'F')
dfa_07.add_transition('E', '2', 'G')
dfa_07.add_transition('E', '3', 'H')

dfa_07.add_transition('F', '1', 'I')
dfa_07.add_transition('F', '2', 'I')
dfa_07.add_transition('F', '3', 'I')

dfa_07.add_transition('G', '1', 'I')
dfa_07.add_transition('G', '2', 'I')
dfa_07.add_transition('G', '3', 'I')

dfa_07.add_transition('H', '1', 'I')
dfa_07.add_transition('H', '2', 'J')
dfa_07.add_transition('H', '3', 'J')

dfa_07.add_transition('I', '1', 'J')
dfa_07.add_transition('I', '2', 'J')
dfa_07.add_transition('I', '3', 'J')

dfa_07.add_transition('J', '1', 'J')
dfa_07.add_transition('J', '2', 'J')
dfa_07.add_transition('J', '3', 'J')

mindfa_07 = dfa_07.minimize()

## =================================================




                        
