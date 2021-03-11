package com.labs.oop;
import java.util.*;

public class Main {

    public static void main(String[] args){
        //This convertor is designed for a specific NFA, in which "A" is the initial state and "C" is the finals state
        //The transitions, however, can be changed on the go, through input
        int num_of_states = 3;
        char states_ar[] = {'A', 'B', 'C'}; // new char[nos];
        //We'll be using a dictionary to keep track of the position of the state
        HashMap<Character, Integer> states = new HashMap<Character, Integer>();
        states.put('A', 0);
        states.put('B', 1);
        states.put('C', 2);

        //We set the initial state:
        char initial_state = 'A';
        HashMap<Character, Integer> final_states = new HashMap<Character, Integer>();
        final_states.put('C' ,1);

        int num_of_symbols = 2;
        char alphabet[] = {'a', 'b'};

        Queue<String> q = new LinkedList<>();
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        q.add(initial_state+"");
        map.put(initial_state+"", 1);

        System.out.println("Enter where each state transitions to for each path in the NFA.\nMultiple destination states don't need to be separated by anything)");
        System.out.println("Enter '-' if there's no transition for a path: ");
        String NFA_table[][] = new String[num_of_states][num_of_symbols];

        System.out.print("\n\t");
        for(int al=0;al<num_of_symbols;al++)
            System.out.print(alphabet[al]+"\t");
        System.out.println();

        Scanner sc = new Scanner(System.in); //We'll use the scanner to input transitions
        for(int i=0;i<num_of_states;i++){
            System.out.print(states_ar[i]+"|\t");
            for(int j=0;j<num_of_symbols;j++){
                //It's easier to input the transitions right as we go
                NFA_table[i][j] = sc.next();
            }
        }
        //This is where the conversion takes place:
        System.out.println("\nEquivalent DFA Table: ");
        String DFA_table[][] = new String[1000][num_of_symbols];
        String final_states_DFA[] = new String[1000];
        int nfa_final_states = 0;
        HashMap<Character, Integer> new_states;
        for(int i=0;q.size() > 0;i++){
            String current_state = q.remove();
            System.out.print(current_state+"|\t");
            for(int j=0;j<num_of_symbols;j++){
                DFA_table[i][j] = "";
                if(current_state.length() == 1 && !states.containsKey(current_state.charAt(0))){
                    DFA_table[i][j] = current_state;
                    if(!map.containsKey(DFA_table[i][j])){
                        q.add(DFA_table[i][j]);
                        map.put(DFA_table[i][j], 1);
                    }
                    if(final_states.containsKey((DFA_table[i][j].charAt(0))))
                        final_states_DFA[nfa_final_states++] = DFA_table[i][j];
                    System.out.print(DFA_table[i][j]+"\t");
                    continue;
                }
                int new_final_state = 0;
                new_states = new HashMap<Character, Integer>();
                for(int k=0;k<current_state.length();k++){
                    if(!states.containsKey(current_state.charAt(k)))
                        continue;
                    if(final_states.containsKey(current_state.charAt(k)))
                        new_final_state = 1;
                    for(int ch=0;ch<NFA_table[states.get(current_state.charAt(k))][j].length();ch++){
                        if(!new_states.containsKey(NFA_table[states.get(current_state.charAt(k))][j].charAt(ch)) && states.containsKey(NFA_table[states.get(current_state.charAt(k))][j].charAt(ch))){
                            DFA_table[i][j] += NFA_table[states.get(current_state.charAt(k))][j].charAt(ch);//null state is appearing i.e AC
                            new_states.put(NFA_table[states.get(current_state.charAt(k))][j].charAt(ch), 1);
                        }
                    }
                }

                if(!map.containsKey(DFA_table[i][j])){
                    q.add(DFA_table[i][j]);
                    map.put(DFA_table[i][j], 1);
                }
                if(new_final_state == 1)
                    final_states_DFA[nfa_final_states++] = DFA_table[i][j];
                System.out.print(DFA_table[i][j]+"\t");
            }
        }

    }

}
