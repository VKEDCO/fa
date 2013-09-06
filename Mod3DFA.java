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
 * @author Vladimir
 */
public class Mod3DFA {
    
    static final int Q0 = 0;
    static final int Q1 = 1;
    static final int Q2 = 2;
    static final int Q3 = 3;
    
    private static int mCurrState; 
    
    private static int delta(int state, char c) {
        switch ( state ) {
            case Q0: 
                switch ( c ) {
                    case '0': return Q0;
                    case '1': return Q1;
                    default: return Q3;
                }
            case Q1:
                switch ( c ) {
                    case '0': return Q2;
                    case '1': return Q0;
                    default: return Q3;
            }
            case Q2:
                switch ( c ) {
                    case '0': return Q1;
                    case '1': return Q2;
                    default: return Q3;
                }
            default: return Q3;
        }
    }
    
    static void reset() {
        mCurrState = Q0;
    }
    
    static void process(String input) {
        for(int i = 0; i < input.length(); i++) {
            mCurrState = delta(mCurrState, input.charAt(i));
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
        Mod3DFA.mod3StringFilter();
    }
    
}
