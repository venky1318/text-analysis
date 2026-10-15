# Text Analysis — Test Cases

## Testing Objective

To verify that the program accurately counts words, characters, vowels, unique words, and repeated words.

## Test Cases

| Test ID | Input | Expected Result |
|---|---|---|
| TC01 | `Python is useful` | 3 words |
| TC02 | `Hello hello` | 2 words; `hello` repeated twice |
| TC03 | `AEIOU` | 5 vowels |
| TC04 | `Hi, world!` | 2 words; 10 characters |
| TC05 | Empty string | 0 words, 0 characters, 0 vowels |
| TC06 | `cat cat dog` | 3 words; `cat` occurs twice |
| TC07 | `123 456` | 2 tokens, 0 vowels |
| TC08 | `Sky` | 1 word, 0 vowels |
| TC09 | Text with multiple spaces | Word count ignores extra whitespace |
| TC10 | Text with punctuation | Punctuation does not create additional words |

## Test Execution Record

Run the tests using the `analyze_text()` function. Record actual results and mark each test as Pass or Fail.

| Test ID | Actual Result | Status |
|---|---|---|
| TC01–TC10 | Record after execution | Pending |

## Testing Notes

Character count includes every character in the input, including spaces and punctuation. Word counting ignores case and extracts words using a regular expression. Vowel counting includes only a, e, i, o, and u.

The expected results should be compared with the actual program output before marking tests as passed.
