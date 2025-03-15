# Python Quiz Application

A customizable multiple-choice quiz application that tracks scores and provides explanations for answers.

## Features

- Multiple choice questions with explanations
- Score tracking and percentage calculation
- Randomized question order
- Custom feedback based on performance
- Easy question addition through JSON
- Progress tracking during quiz
- Input validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-quiz
cd python-quiz
```

2. No additional packages required - uses only Python standard library!

## Usage

1. Run the quiz:
```bash
python quiz_app.py
```

2. Follow the prompts to:
   - Start the quiz
   - Answer questions
   - See your results
   - Choose to play again

## Adding Questions

Create or modify `questions.json` with your questions following this format:

```json
[
    {
        "question": "Your question text here?",
        "choices": [
            "First choice",
            "Second choice",
            "Third choice",
            "Fourth choice"
        ],
        "correct_answer": 2,
        "explanation": "Optional explanation of the answer"
    }
]
```

Notes:
- `correct_answer` is the number of the correct choice (1-4)
- `explanation` is optional
- Add as many questions as you like
- Questions will be randomly selected during the quiz

## Question Guidelines

When adding questions:
1. Keep questions clear and concise
2. Ensure all choices are plausible
3. Make sure there's only one correct answer
4. Add helpful explanations
5. Verify the correct_answer number matches the intended choice

## Example Questions

The application comes with sample questions about Python programming. To add your own topics:

1. Create a new JSON file (e.g., `history_questions.json`)
2. Follow the same format as the sample questions
3. Modify the filename in the code or pass it as an argument

## Contributing

1. Fork the repository
2. Create your feature branch
3. Add your questions or features
4. Create a Pull Request

## License

MIT License
