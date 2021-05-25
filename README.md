# LFPC
For laboratory work

Lab 1: Regular grammar to finite automata

Takes a word as input and returns "Accepted" or "Rejected", according to the rules. If the word gets rejected, the user is offered the chance to retype a word or quit.

There are 2 functions that help analyze the input: the word_formation function generates the simplest words using the derivation rules. The second function takes the input, then removes duplicate characters when they are next to each other, and returns the simplified word (as in "abbbccaaaa", which turns into "abca").

After this, the third function compares the simplified input with the words in the generated list and decides whether the input word is accepted or not.

Lab 2: NFA to DFA convertor

The program automatically records ''A', 'B' and 'C' to be the states (the analog of 'q0', 'q1' and 'q2') and sets 'A' to be the initial state, 'C' - the final one. You may change this setting by modifying the value of the "initial_state" and "final_states" variables.

The transitions are recorded on the go, which means you may play with different test cases.

For this laboratory, Java seemed to offer more control over the tables used to describe the NFA or the DFA, because it allows us to specify the data type for every single piece of information and the structure that stores it.

Lab 3: Conversion of a Context-Free Grammar to Chomsky's Normal Form
![image](https://user-images.githubusercontent.com/56108881/115160382-887c6f80-a0a0-11eb-9451-4f35066b1ef0.png)
![image](https://user-images.githubusercontent.com/56108881/115160396-9af6a900-a0a0-11eb-9294-129f10478260.png)


Lab 4: Simple precedence parser
Given a grammar, analyze the input using the Simple Precedence Parsing method
First, we construct the first and the last lists of the productions and their rules;
Then, we use these lists to construct the Wirth–Weber precedence relationship table (see the casual example below):

![image](https://user-images.githubusercontent.com/56108881/119568906-bac37000-bdb6-11eb-8100-f2776ce2041d.png)

Finally, we parse the string using a stack and the table above.

Input here: "adabcd"

See what the parser yields at each step, by opening the program written and run with Jupyter Notebook (where the output is displayed at each step).
