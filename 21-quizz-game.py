questions = (
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "Who wrote 'Hamlet'?",
    "What is the square root of 64?"
)

options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Rome"),          # options for question 1
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),          # options for question 2
    ("A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"),    # options for question 3
    ("A. Shakespeare", "B. Dickens", "C. Hemingway", "D. Tolkien"), # options for question 4
    ("A. 6", "B. 7", "C. 8", "D. 9")                            # options for question 5
)

answers = (
    "A",    # correct answer for question 1
    "B",    # correct answer for question 2
    "C",    # correct answer for question 3
    "A",    # correct answer for question 4
    "C"     # correct answer for question 5
)

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    
    # Printing options for the current question
    for option in options[question_num]:
        print(option)
    
    # Get user's guess
    guess = input("Enter your answer (A, B, C, D): ").upper()
    
    # Store the guess
    guesses.append(guess)
    
    # Check if the answer is correct
    if guess == answers[question_num]:
        score += 1
    
    question_num += 1

# Final score
print(f"\nYour final score is: {score}/{len(questions)}")
