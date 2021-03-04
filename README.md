# LFPC
For laboratory work

Lab 1: Regular grammar to finite automata
Takes a word as input and returns "Accepted" or "Rejected", according to the rules. If the word gets rejected, the user is offered the chance to retype a word or quit.

There are 2 functions that help analyze the input: the word_formation function generates the simplest words using the derivation rules. The second function takes the input, then removes duplicate characters when they are next to each other, and returns the simplified word (as in "abbbccaaaa", which turns into "abca").

After this, the third function compares the simplified input with the words in the generated list and decides whether the input word is accepted or not.
