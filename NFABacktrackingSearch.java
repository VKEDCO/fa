package org.vkedco.toc.nfa;

/*
 *==============================================================================
 * An implementation of a simple NFA as a backtracking search.
 * Inspired by the book A. Brooks-Weber "Formal Language: A Practical Approach"
 *==============================================================================
 */

public class NFABacktrackingSearch {
	
	static short[][][] mDeltaTable = {
		{{0}, 	{0, 1}}, // mDelta[0, 0], mDelta[0, 1]
		{{2}, 	{2}},	 // mDelta[1, 0], mDelta[1, 1]
		{{}, 	{}}		 // mDelta[2, 0], mDelta[2, 1]
	};
	
	static boolean process_backtrack(short st, String input, int char_pos) {
		if ( char_pos == input.length() ) return st == 2;
		
		char c = input.charAt(char_pos);
		short[] next_states;
		try {
			next_states = mDeltaTable[st][c-'0'];
		}
		catch ( ArrayIndexOutOfBoundsException ex ) {
			return false;
		}
		
		// call process_backtrack recursively and backtrack to
		// this point if it returns false.
		for(int i=0; i < next_states.length; i++) {
			if ( process_backtrack(next_states[i], input, char_pos+1) )
				return true;
		}
		
		return false;
	}
	
	public static boolean process(String input) {
		return process_backtrack((short)0, input, 0);
	}
	
	public static void main(String[] args) {
		System.out.println(process("00010010001000100010000000011111000100100110"));
	}

}

