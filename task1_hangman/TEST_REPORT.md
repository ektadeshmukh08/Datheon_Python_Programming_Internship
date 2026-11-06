# Hangman Game — Test Report

## 1. Objective
To verify that the Hangman game correctly handles valid guesses, invalid inputs, repeated guesses, winning, and losing.

## 2. Test Cases

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC-01 | Start the game | Welcome message and hidden word displayed | PASS |
| TC-02 | Enter a correct letter | Matching letters are revealed | PASS |
| TC-03 | Enter an incorrect letter | Remaining attempts decrease by one | PASS |
| TC-04 | Enter a number | Input is rejected without losing an attempt | PASS |
| TC-05 | Enter multiple characters | Input is rejected without losing an attempt | PASS |
| TC-06 | Enter special characters | Input is rejected without losing an attempt | PASS |
| TC-07 | Repeat a previously guessed letter | Duplicate warning appears; no extra attempt is lost | PASS |
| TC-08 | Guess all letters correctly | Win message is displayed | PASS |
| TC-09 | Reach six incorrect guesses | Loss message and correct word are displayed | PASS |

## 3. Test Results
Manual testing was performed through the terminal. The winning condition, input validation, incorrect-guess handling, and duplicate-guess handling were observed during testing.

## 4. Conclusion
The Hangman game behaved as expected in the manually tested scenarios.

Note: The test statuses above should be marked PASS only after each corresponding scenario has been executed and verified.