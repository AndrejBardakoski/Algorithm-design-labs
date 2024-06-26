# task 3

A bracket sequence is called regular if it is possible to obtain correct arithmetic expression by inserting characters
`«+»` and `«1»` into this sequence. For example, sequences `«(())()»`, `«()»` and `«(()(()))»` are regular, while `«)(»`
, `«(()»` and
`«(()))(»` are not.

One day Johnny got bracket sequence. He decided to remove some of the brackets from it in order to obtain a regular
bracket sequence. What is the maximum length of a regular bracket sequence which can be obtained?

### Input

Input consists of a single line with non-empty string of `«(»` and `«)»` characters. Its length does not exceed `10^6`.

### Output

Output the maximum possible length of a regular bracket sequence.

### Sample 1

| input   | result |
|---------|--------|
| (()))(  | 4      |

### Sample 2

| input   | result  |
|---------|---------|
| ((()()) | 6       |