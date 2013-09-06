/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package org.vkedco.toc.dfa;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author Vladimir Kulyukin
 */
public class Mod3DFATable {

    static final int Q0 = 0;
    static final int Q1 = 1;
    static final int Q2 = 2;
    static final int Q3 = 3;
    
    private static int mCurrState;
    
    static int[][] deltaTable = 
    {
        {Q0, Q1}, // state Q0: delta('0', Q0) = Q0; delta('1', Q1)
        {Q2, Q0}, // state Q1: delta('0', Q1) = Q2; detal('1', Q0)  
        {Q1, Q2}, // state Q2: delta('0', Q2) = Q1; delta('1', Q2)
        {Q3, Q3}  // state Q3: delta('0', Q3) = Q3; delta('1', Q3)
    };
    
    static void reset() {
        mCurrState = Q0;
    }
    
    static void process(String input) {
        for(int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            try {
                // This is based on the following Java trick:
                // System.out.println('1'-'0'); // this outputs 1
                // System.out.println('1'-'1'); // this outputs 0
                mCurrState = deltaTable[mCurrState][c-'0'];
            }
            catch ( ArrayIndexOutOfBoundsException ex ) {
                mCurrState = Q3;
            } 
        }
    }
    
    
    
    static boolean isAccepted() {
        return mCurrState == Q0;
    }
    
    static void mod3StringFilter() {
        try {
            BufferedReader input = 
                    new BufferedReader(new InputStreamReader(System.in));
            String inputStr = input.readLine();
            while ( inputStr != null ) {
                Mod3DFA.reset();
                Mod3DFA.process(inputStr);
                if ( Mod3DFA.isAccepted() ) 
                    System.out.println("YES");
                else
                    System.out.println("NO");
                inputStr = input.readLine();
            }
        }
        catch ( IOException ex ) {
            System.err.println(ex.toString());
        }
    }
    
    public static void main(String[] argv) {
        Mod3DFATable.mod3StringFilter();
    }
}
