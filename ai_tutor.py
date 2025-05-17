"""Command-line AI tutor application."""

from __future__ import annotations

import argparse
import random
from typing import Dict, List

# Dataset of questions by category
QUESTIONS = {
    "math": [
        {
            "question": "What is 2 + 2?",
            "answer": "4",
            "explanation": "Adding two plus two equals four."
        },
        {
            "question": "What is the square root of 16?",
            "answer": "4",
            "explanation": "Four times four equals sixteen."
        },
        {
            "question": "Solve for x: 2x = 10",
            "answer": "5",
            "explanation": "Divide both sides by 2 to get x = 5."
        },
    ],
    "science": [
        {
            "question": "What gas do plants breathe in that humans and animals breathe out?",
            "answer": "carbon dioxide",
            "explanation": "Plants take in carbon dioxide for photosynthesis."
        },
        {
            "question": "How many planets are in our solar system?",
            "answer": "8",
            "explanation": "There are eight recognized planets orbiting the Sun."
        },
    ],
    "history": [
        {
            "question": "Who was the first president of the United States?",
            "answer": "George Washington",
            "explanation": "George Washington served as president from 1789 to 1797."
        },
        {
            "question": "In what year did World War II end?",
            "answer": "1945",
            "explanation": "The war ended in 1945 with the surrender of Japan."
        },
    ],
}


class Tutor:
    """Simple tutor that asks questions and tracks correct answers."""

    def __init__(self, category: str, questions: Dict[str, List[dict]] = QUESTIONS):
        if category not in questions:
            raise ValueError(f"Unknown category: {category}")
        # shuffle questions for randomness
        self.questions = list(questions[category])
        random.shuffle(self.questions)
        self.correct = 0
        self.total = len(self.questions)

    def ask(self, input_fn=input, print_fn=print) -> int:
        """Ask all questions using provided input and print functions."""
        for q in self.questions:
            print_fn("\n" + q["question"])
            user_answer = input_fn("Your answer: ").strip().lower()
            if user_answer == q["answer"].lower():
                print_fn("Correct!")
                self.correct += 1
            else:
                print_fn(f"Incorrect. The correct answer is: {q['answer']}")
                print_fn("Explanation:", q["explanation"])

        print_fn(f"\nYour score: {self.correct}/{self.total}")
        return self.correct


def list_categories() -> List[str]:
    """Return the list of available categories."""
    return list(QUESTIONS.keys())


def main(argv: List[str] | None = None) -> int:
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Simple AI Tutor")
    parser.add_argument("category", nargs="?", help="Question category")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available categories and exit",
    )
    args = parser.parse_args(argv)

    if args.list:
        print("Available categories:", ", ".join(list_categories()))
        return 0

    if not args.category:
        parser.print_help()
        return 1

    try:
        tutor = Tutor(args.category)
    except ValueError as exc:
        print(exc)
        return 1

    tutor.ask()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

