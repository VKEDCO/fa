package org.vkedco.toc.nfabitparallel;

/*
 *==============================================================================
 * An implementation of a simple NFA as a parallel bit search.
 * Inspired by the book A. Brooks-Weber "Formal Language: A Practical Approach"
 *==============================================================================
 */

public class NFAParallelBitSearch {

	// this is the set of states representend as binary number.
	// the rightmost bit denotes q0; the middle bit denotes q1,
	// the leftmost bit denotes q2. if a bit is set to 1, the
	// nfa is in that state.
	static int mStateSet;
	
	// set the state set to '001'
	static void reset() { mStateSet = 1<<0; }
	
	// mDeltaTable[state][symbol] = binary string
	static int[][] mDeltaTable = 
	{
		{1 << 0, 1 << 0 | 1 << 1}, // transitions from q0: d(0,0)={0}; d(0,1)={0,1}
		{1 << 2, 1 << 2}, 	   // transitions from q1: d(1,0)={2}; d(1,1)={2}
		{0, 0}			   // transitions from q2: d(2,0)={};  d(2,1)={}
	};
	
	static void processInput(String input) {
		for(int i = 0; i < input.length(); i++) {
			final char c = input.charAt(i);
			int nextStateSet = 0;
			for(int s = 0; s <= 2; s++) {
				if ( (mStateSet & (1 << s)) != 0) {
					try {
						nextStateSet |= mDeltaTable[s][c-'0'];
					}
					catch ( ArrayIndexOutOfBoundsException ex) {
					}
				}
			}
			mStateSet = nextStateSet;
		}
	}
	
	// accept iff mStateState & '100' is not a zero, i.e., the lefmost bit
	// of mStateState is 1.
	static boolean isAccepted() {
		return (mStateSet & (1 << 2)) != 0;
	}
	
	static void bitFiddlingExamples() {
		System.out.println("1 << 0 == " + Integer.toString(1<<0));
		System.out.println("1 << 1 == " + Integer.toString(1<<1));
		System.out.println("1 << 2 == " + Integer.toString(1<<2));
		System.out.println("1 << 1 | 1 << 2 == " + Integer.toString(1 << 1 | 1 << 2));
		System.out.println("1 << 2 | 1 << 0 == " + Integer.toString(1 << 2 | 1 << 0));
		System.out.println("1 << 1 & 1 << 2 == " + Integer.toString(1 << 1 & 1 << 2));
		System.out.println("(1 << 2 | 1 << 0) & (1 << 2) == " + Integer.toString((1 << 2 | 1 << 0) & (1 << 2)));
	}
	
	// display the bits of mStateSet
	static void displayStateSet() {
        	int q0_is_set = 1 << 0;
        	int q1_is_set = 1 << 1;
        	int q2_is_set = 1 << 2;
        	System.out.print("State Set: ");
        	if ( (mStateSet & q2_is_set) != 0 )
            		System.out.print('1');
        	else
            		System.out.print('0');
        
        	if ( (mStateSet & q1_is_set) != 0 )
            		System.out.print('1');
        	else
            		System.out.print('0');
        
        	if ( (mStateSet & q0_is_set) != 0 )
            		System.out.print('1');
        	else
            	System.out.print('0');
        	System.out.println();
    	}
	
	public static void main(String[] args) {
		NFAParallelBitSearch.reset();
		NFAParallelBitSearch.processInput("00011");
		String inputs[] = { "00011", "11", "00000011111000010", "0", "00", "10000" };
		for(String input: inputs) {
			NFAParallelBitSearch.reset();
			NFAParallelBitSearch.processInput(input);
			if ( NFAParallelBitSearch.isAccepted() ) {
				System.out.println(input + " accepted");
			}
			else {
				System.out.println(input + " rejected");
			}
		}
	}
}

