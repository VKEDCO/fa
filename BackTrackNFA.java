package org.vkedco.toc.nfa;

public class BackTrackNFA {
	
	static short[][][] mDelta = {
		{{0}, 	{0, 1}},	// mDelta[q0, 0], mDelta[q0, 1]
		{{2}, 	{2}},		// mDelta[q1, 0], mDelta[q1, 1]
		{{}, 	{}}		// mDelta[q2, 0], mDelta[q2, 1]
	};
	
	static boolean process_aux(short st, String input, int char_pos) {
		if ( char_pos == input.length() ) return st == 2;
		
		char c = input.charAt(char_pos);
		short[] next_states;
		try {
			next_states = mDelta[st][c - '0'];
		}
		catch ( ArrayIndexOutOfBoundsException ex ) {
			return false;
		}
		
		for(int i=0; i < next_states.length; i++) {
			if ( process_aux(next_states[i], input, char_pos+1) )
				return true;
		}
		
		return false;
	}
	
	public static boolean process(String input) {
		return process_aux((short)0, input, 0);
	}
	
	public static void main(String[] args) {
		System.out.println(process("00010010001000100010000000011111000100100110"));
	}

}
