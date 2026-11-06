# Task 4: Rule-Based FAQ Chatbot

## Overview
The Rule-Based FAQ Chatbot is a command-line application developed using Python. It answers predefined questions by matching user input with configured keywords and topics.

## Features
- Responds to common greetings.
- Answers frequently asked questions using predefined responses.
- Supports case-insensitive input.
- Normalizes text by removing extra spaces and punctuation.
- Matches keywords and prioritizes longer, more specific matches.
- Handles unknown questions with a fallback response.
- Supports exit commands such as `exit`, `quit`, and `bye`.
- Handles empty input.
- Supports common variations of greetings and FAQ keywords.

## Technologies Used
- Python
- `re` — text normalization and keyword matching

## Requirements
- Python 3.10 or later
- A terminal or command prompt

No external packages are required.

## Project Structure

```text
task4_faq_chatbot/
├── main.py
├── README.md
└── TEST_REPORT.md
```

## How to Run

1. Open the project folder in VS Code.
2. Open a terminal in `task4_faq_chatbot`.
3. Run:

```bash
python main.py
```

4. Type a question and read the chatbot's response.
5. Type `exit`, `quit`, or `bye` to end the session.

## Example

```text
You: Python
Bot: Python is a high-level programming language known
for its readable syntax and wide range of applications.

You: Bye
Bot: Goodbye! Thank you for using the FAQ chatbot.
```

## Concepts Used
- Functions and dictionaries
- Lists and loops
- Conditional statements
- String manipulation
- Regular expressions
- Keyword matching
- Exception handling
- Interactive command-line input

## Limitations
This is a rule-based chatbot. It relies on predefined keywords and responses and does not use machine learning or natural language processing models. Questions outside its configured rules may not receive the intended answer.

## Internship
Developed as part of the Datheon Python Programming Internship.