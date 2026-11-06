# Rule-Based FAQ Chatbot — Test Report

## 1. Objective
To verify that the chatbot handles greetings, FAQ keywords, variations in capitalization, unknown questions, empty input, and exit commands.

## 2. Test Environment
- Language: Python
- Interface: Command-line terminal
- Operating system: Windows
- Dependencies: Python standard library

## 3. Test Cases

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC-01 | Enter `Hi` | Greeting response appears | PASS |
| TC-02 | Enter `Hii` | Greeting variation is recognized | PASS |
| TC-03 | Enter `Python` | Python-related answer appears | PASS |
| TC-04 | Enter `Certifications` | Certificate-related answer appears | PASS |
| TC-05 | Enter `Eligiblity` | Eligibility-related answer appears | PASS |
| TC-06 | Ask about duration and a certificate together | Most relevant configured response is selected | PASS |
| TC-07 | Enter an unknown question | Fallback response appears | PASS |
| TC-08 | Enter only spaces | Chatbot requests a message | PASS |
| TC-09 | Enter `Bye` | Goodbye response appears and the program exits | PASS |
| TC-10 | Enter uppercase and lowercase variations | Matching remains case-insensitive | PASS |

## 4. Test Results
Initial manual testing confirmed that the chatbot ran and responded to supported inputs. Some variations and mixed-topic questions initially returned unexpected responses, prompting improvements to greeting recognition, keyword lists, and match prioritization.

## 5. Conclusion
The chatbot implements a basic FAQ system using predefined rules. It is suitable for demonstrating Python fundamentals, text normalization, and keyword-based response selection.

## 6. Verification Note
Mark each test as PASS only after running it and confirming the expected result. Otherwise, use NOT TESTED until verification is complete.