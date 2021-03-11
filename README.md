# LFPC
For laboratory work

Lab 1: Regular grammar to finite automata
Takes a word as input and returns "Accepted" or "Rejected", according to the rules. If the word gets rejected, the user is offered the chance to retype a word or quit.

There are 2 functions that help analyze the input: the word_formation function generates the simplest words using the derivation rules. The second function takes the input, then removes duplicate characters when they are next to each other, and returns the simplified word (as in "abbbccaaaa", which turns into "abca").

After this, the third function compares the simplified input with the words in the generated list and decides whether the input word is accepted or not.

Lab 2: NFA to DFA convertor
The program automatically records ''A', 'B' and 'C' to be the states (the analog of 'q0', 'q1' and 'q2') and sets 'A' to be the initial state, 'C' - the final one. You may change this setting by modifying the value of the "initial_state" and "final_states" variables.

The transitions are recorded on the go, which means you may play with different test cases.

For this laboratory, Java seemed to offer more control over the tables used to describe the NFA or the DFA, because it allows us to specify the data type for every single piece of information and the structure that stores it. A Python version might be on its way soon.
