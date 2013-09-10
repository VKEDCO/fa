package org.vkedco.toc.nfabitparallel;

public class NFABitParallel {

	static int mStateSet;
	
	static void reset() {
		mStateSet = 1<<0;
	}
	
	static int[][] mDelta = 
	{
		{1 << 0, 1 << 0 | 1 << 1 }, // d(q0,0)={q0}; d(q0,1)={q0, q1}
		{1 << 2, 1 << 2 }, 			// d(q1,0)={q2}; d(q1,1)={q2}
		{0, 0}						// d(q2,0)={}; d(q2,1)={}
	};
	
	static void processInput(String input) {
		for(int i = 0; i < input.length(); i++) {
			final char c = input.charAt(i);
			int nextStateSet = 0;
			for(int s = 0; s <= 2; s++) {
				if ( (mStateSet & (1 << s)) != 0) {
					try {
						nextStateSet |= mDelta[s][c-'0'];
					}
					catch ( ArrayIndexOutOfBoundsException ex) {
					}
				}
			}
			mStateSet = nextStateSet;
		}
	}
	
	static boolean isAccepted() {
		return (mStateSet & (1 << 2)) != 0;
	}
	
	public static void main(String[] args) {
		NFABitParallel.reset();
		NFABitParallel.processInput("00011");
		String inputs[] = { "00011", "11", "00000011111000010", "0", "00", "10000" };
		for(String input: inputs) {
			NFABitParallel.reset();
			NFABitParallel.processInput(input);
			if ( NFABitParallel.isAccepted() ) {
				System.out.println(input + " accepted");
			}
			else {
				System.out.println(input + " rejected");
			}
		}
	}
}
