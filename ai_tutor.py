"""Command line AI Tutor application."""

from __future__ import annotations

import argparse
import random
from typing import Callable, Iterable

# Dataset of questions by category
QUESTIONS: dict[str, list[dict[str, str]]] = {
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
    """Tutor asks questions from a category and tracks the user's score."""

    def __init__(self, category: str) -> None:
        """Initialize the Tutor with a question category."""
        if category not in QUESTIONS:
            raise ValueError(f"Unknown category: {category}")
        self.questions = list(QUESTIONS[category])
        random.shuffle(self.questions)
        self.correct = 0
        self.total = len(self.questions)

    def ask(
        self,
        input_fn: Callable[[str], str] = input,
        output_fn: Callable[[str], None] = print,
    ) -> None:
        """Iteratively ask questions using provided input/output functions."""
        for q in list(self.questions):
            output_fn("\n" + q["question"])
            user_answer = input_fn("Your answer: ").strip().lower()
            if user_answer == q["answer"].lower():
                output_fn("Correct!")
                self.correct += 1
            else:
                output_fn(f"Incorrect. The correct answer is: {q['answer']}")
                output_fn("Explanation: " + q["explanation"])
            
        print(f"\nYour score: {self.correct}/{self.total}")


def parse_args(args: Iterable[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="AI Tutor")
    parser.add_argument(
        "category",
        nargs="?",
        help="question category",
        choices=list(QUESTIONS.keys()),
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="list available categories and exit",
    )
    return parser.parse_args(args)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    if args.list:
        print("Available categories:")
        for cat in QUESTIONS:
            print(f"- {cat}")
        return

    category = args.category
    if category is None:
        category = input(f"Choose a category {list(QUESTIONS.keys())}: ").strip().lower()

    try:
        tutor = Tutor(category)
    except ValueError as e:
        print(e)
        return
    tutor.ask()


if __name__ == "__main__":
    main()

