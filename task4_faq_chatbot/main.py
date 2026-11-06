
import re


# Predefined questions and answers
FAQS = {
    "internship": {
        "keywords": ["internship", "intern", "training"],
        "answer": (
            "An internship provides practical experience in a "
            "professional field and helps develop useful skills."
        ),
    },
    "python": {
        "keywords": ["python", "programming language"],
        "answer": (
            "Python is a high-level programming language known "
            "for its readable syntax and wide range of applications."
        ),
    },
    "eligibility": {
        "keywords": ["eligibility", "eligible", "qualification"],
        "answer": (
            "Eligibility requirements depend on the specific "
            "internship or program. Check its official guidelines."
        ),
    },
    "duration": {
        "keywords": ["duration", "how long", "weeks", "months"],
        "answer": (
            "The duration depends on the program. Check the "
            "official internship details for the exact timeline."
        ),
    },
    "certificate": {
        "keywords": ["certificate", "certification"],
        "answer": (
            "Certificate policies vary by program. Contact the "
            "organizer to confirm its requirements."
        ),
    },
    "contact": {
        "keywords": ["contact", "email", "support", "help"],
        "answer": (
            "For specific assistance, contact the relevant "
            "organization through its official support channel."
        ),
    },
    "projects": {
        "keywords": ["project", "projects", "assignment", "task"],
        "answer": (
            "Projects help you apply what you learn. Read the "
            "requirements carefully, implement the solution, "
            "test it, and document your work."
        ),
    },
    "cybersecurity": {
        "keywords": ["cybersecurity", "cyber security", "hacking"],
        "answer": (
            "Cybersecurity focuses on protecting systems, networks, "
            "and data. Beginners can start with networking, Linux, "
            "Python, and web security fundamentals."
        ),
    },
}


GREETINGS = {
    "hi": "Hi! Ask me a question about internships, Python, or projects.",
    "hii": "Hi! Ask me a question about internships, Python, or projects.",
    "hiii": "Hi! Ask me a question about internships, Python, or projects.",
    "hello": "Hello! How can I help you?",
    "hey": "Hey! What would you like to know?",
}

EXIT_COMMANDS = {"exit", "quit", "bye"}


def normalize_text(text):
    """Convert text to lowercase and remove extra punctuation and spaces."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def contains_keyword(text, keyword):
    """Match a keyword as a complete phrase, not a partial word."""
    pattern = r"\b" + re.escape(keyword) + r"\b"
    return re.search(pattern, text) is not None


def get_response(user_input):
    """Return a response based on greetings, FAQs, or exit commands."""
    normalized_input = normalize_text(user_input)

    if not normalized_input:
        return "Please enter a question or message."

    if normalized_input in EXIT_COMMANDS:
        return "Goodbye! Thank you for using the FAQ chatbot."

    # Check greetings as complete words or phrases.
    for greeting, response in GREETINGS.items():
        if normalized_input == greeting:
            return response

    # Find matching FAQ keywords.
        # Find matching FAQ keywords.
    matches = []

    for topic, details in FAQS.items():
        matched_keywords = [
            keyword
            for keyword in details["keywords"]
            if contains_keyword(normalized_input, keyword)
        ]

        if matched_keywords:
            # Prefer the most specific matching keyword.
            longest_keyword = max(
                len(keyword) for keyword in matched_keywords
            )
            matches.append(
                (longest_keyword, len(matched_keywords), topic,
                 details["answer"])
            )

    if matches:
        matches.sort(
            key=lambda item: (item[0], item[1]),
            reverse=True
        )
        return matches[0][3]

    return (
        "Sorry, I don't have an answer for that question. "
        "Please try asking about internships, Python, eligibility, "
        "duration, certificates, projects, or cybersecurity."
    )


def run_chatbot():
    """Start the interactive chatbot session."""
    print("=" * 45)
    print("       RULE-BASED FAQ CHATBOT")
    print("=" * 45)
    print("Ask me about internships, Python, or projects.")
    print("Type 'exit', 'quit', or 'bye' to stop.")

    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)

        if normalize_text(user_input) in EXIT_COMMANDS:
            break


if __name__ == "__main__":
    run_chatbot()
