import time
import random

print("Timer Based Quiz Application")

score = 0
# seconds per question
time_limit = 30   

questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["a) Chittagong", "b) Dhaka", "c) Khulna", "d) Rajshahi"],
        "answer": "b"
    },
    {
        "question": "Which language is mainly used for web pages?",
        "options": ["a) Python", "b) C++", "c) HTML", "d) Java"],
        "answer": "c"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Process Unit", "b) Central Processing Unit",
                    "c) Computer Power Unit", "d) Control Process Unit"],
        "answer": "b"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["a) //", "b) <!-- -->", "c) #", "d) /* */"],
        "answer": "c"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["a) int", "b) float", "c) bool", "d) string"],
        "answer": "c"
    }
]

# Randomize question order
random.shuffle(questions)

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for opt in q["options"]:
        print(opt)

    start_time = time.time()
    user_ans = input(f"Enter answer (a/b/c/d) within {time_limit} seconds: ").strip().lower()
    end_time = time.time()

    time_taken = end_time - start_time

    if time_taken > time_limit:
        print("Time's up! No point awarded.")
    elif user_ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Finished")
print(f"Your Score: {score} out of {len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage}%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F")
