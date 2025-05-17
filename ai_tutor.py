# Simple AI Tutor CLI Application

import random

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
    def __init__(self, category: str):
        if category not in QUESTIONS:
            raise ValueError(f"Unknown category: {category}")
        # shuffle questions for randomness
        self.questions = list(QUESTIONS[category])
        random.shuffle(self.questions)
        self.correct = 0
        self.total = len(self.questions)

    def ask(self):
        for q in list(self.questions):
            print("\n" + q["question"])
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == q["answer"].lower():
                print("Correct!")
                self.correct += 1
            else:
                print(f"Incorrect. The correct answer is: {q['answer']}")
                print("Explanation:", q["explanation"])
            
        print(f"\nYour score: {self.correct}/{self.total}")


def main():
    print("Welcome to the AI Tutor!")
    category = input(f"Choose a category {list(QUESTIONS.keys())}: ").strip().lower()
    try:
        tutor = Tutor(category)
    except ValueError as e:
        print(e)
        return
    tutor.ask()


if __name__ == "__main__":
    main()

