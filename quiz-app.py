from typing import List, Dict
import json
import random
from pathlib import Path
import time

class Question:
    def __init__(self, text: str, choices: List[str], correct_answer: int, explanation: str = ""):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer
        self.explanation = explanation

class Quiz:
    def __init__(self):
        self.questions: List[Question] = []
        self.score = 0
        self.total_questions = 0
        
    def load_questions(self, filename: str = "questions.json"):
        """Load questions from a JSON file"""
        try:
            with open(filename, 'r') as f:
                questions_data = json.load(f)
                
            for q_data in questions_data:
                question = Question(
                    text=q_data['question'],
                    choices=q_data['choices'],
                    correct_answer=q_data['correct_answer'],
                    explanation=q_data.get('explanation', '')
                )
                self.questions.append(question)
                
            self.total_questions = len(self.questions)
            print(f"Loaded {self.total_questions} questions successfully!")
            
        except FileNotFoundError:
            print(f"Could not find {filename}. Please ensure it exists in the current directory.")
            raise
        except json.JSONDecodeError:
            print(f"Error parsing {filename}. Please ensure it's properly formatted JSON.")
            raise
            
    def shuffle_questions(self):
        """Randomize question order"""
        random.shuffle(self.questions)
        
    def display_question(self, question: Question, number: int):
        """Display a single question with its choices"""
        print(f"\nQuestion {number} of {self.total_questions}")
        print("=" * 40)
        print(f"\n{question.text}\n")
        
        for i, choice in enumerate(question.choices, 1):
            print(f"{i}. {choice}")
            
    def get_answer(self) -> int:
        """Get and validate user's answer"""
        while True:
            try:
                answer = input("\nEnter your answer (number): ")
                answer_num = int(answer)
                if 1 <= answer_num <= 4:
                    return answer_num
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
                
    def run(self):
        """Run the quiz"""
        if not self.questions:
            print("No questions loaded!")
            return
            
        print("\nWelcome to the Quiz!")
        print("=" * 20)
        input("Press Enter to start...")
        
        self.shuffle_questions()
        self.score = 0
        
        for i, question in enumerate(self.questions, 1):
            self.display_question(question, i)
            user_answer = self.get_answer()
            
            if user_answer == question.correct_answer:
                print("\n✅ Correct!")
                self.score += 1
            else:
                print("\n❌ Incorrect!")
                print(f"The correct answer was: {question.choices[question.correct_answer - 1]}")
            
            if question.explanation:
                print(f"\nExplanation: {question.explanation}")
            
            time.sleep(1)
            
        self.display_results()
        
    def display_results(self):
        """Show final results"""
        percentage = (self.score / self.total_questions) * 100
        
        print("\nQuiz Complete!")
        print("=" * 20)
        print(f"Your score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        # Give feedback based on score
        if percentage >= 90:
            print("Outstanding! 🌟")
        elif percentage >= 70:
            print("Good job! 👍")
        elif percentage >= 50:
            print("Not bad! Keep practicing! 📚")
        else:
            print("You might want to study more! 💪")

def main():
    # Create sample questions if they don't exist
    sample_questions = [
        {
            "question": "What is Python's primary use?",
            "choices": [
                "Web development",
                "General-purpose programming",
                "Data analysis",
                "Game development"
            ],
            "correct_answer": 2,
            "explanation": "Python is a versatile language used for many purposes, but it's primarily a general-purpose programming language."
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "choices": [
                "Integer",
                "String",
                "Varchar",
                "Float"
            ],
            "correct_answer": 3,
            "explanation": "Varchar is a SQL data type, not a Python data type."
        },
        {
            "question": "What does PEP 8 define?",
            "choices": [
                "Python's style guide",
                "Python's package manager",
                "Python's debug tool",
                "Python's test framework"
            ],
            "correct_answer": 1,
            "explanation": "PEP 8 is Python's style guide for code formatting."
        }
    ]
    
    if not Path("questions.json").exists():
        with open("questions.json", "w") as f:
            json.dump(sample_questions, f, indent=4)
    
    try:
        quiz = Quiz()
        quiz.load_questions()
        quiz.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    while True:
        again = input("\nWould you like to take the quiz again? (y/n): ").lower()
        if again == 'y':
            quiz.run()
        else:
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
