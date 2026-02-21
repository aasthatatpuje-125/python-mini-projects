# Questions and answers
questions = [
    {
        "question": "What can travel around the world while staying in the same corner?",
        "options": ["1. An aeroplane", "2. A stamp", "3. A satellite", "4. A shadow"],
        "answer": 2
    },
    {
        "question": "What has a face and two hands but no arms or legs?",
        "options": ["1. A Clock", "2. A Robot", "3. A Painting", "4. A Watch"],
        "answer": 1
    },
    {
        "question": "What has keys but can’t open locks?",
        "options": ["1. A Piano", "2. A Keyboard", "3. A Map", "4. A Treasure Chest"],
        "answer": 1
    },
    {
        "question": "The more you take, the more you leave behind. What are they?",
        "options": ["1. Footsteps", "2. Memories", "3. Secrets", "4. Shadows"],
        "answer": 1
    },
    {
        "question": "If there are three apples and you take away two, how many do you have?",
        "options": ["1. One", "2. Two", "3. Three", "4. None"],
        "answer": 2
    },
    {
        "question": "Some months have 31 days, others have 30 days. How many have 28 days?",
        "options": ["1. 1", "2. 12", "3. 6", "4. 9"],
        "answer": 2
    },
    {
        "question": "A farmer has 17 sheep, and all but 9 run away. How many sheep are left?",
        "options": ["1. 0", "2. 9", "3. 8", "4. 17"],
        "answer": 2
    },
    {
        "question": "If you’re in a dark room with a candle, a wood stove, and a gas lamp, you only have one match. What do you light first?",
        "options": ["1. The Candle", "2. The Wood Stove", "3. The Gas Lamp", "4. The Match"],
        "answer": 4
    },
    {
        "question": "A father is 40 years old, and his son is 10. How many years ago was the father three times the son’s age?",
        "options": ["1. 10 years ago", "2. 15 years ago", "3. 5 years ago", "4. 20 years ago"],
        "answer": 3
    },
    {
        "question": "Which is heavier: a pound of feathers or a pound of bricks?",
        "options": ["1. Feathers", "2. Bricks", "3. Both are equal", "4. Neither"],
        "answer": 3
    },
    {
        "question": "If a farmer has 3 baskets with 10 eggs in each, and breaks all but 3, how many eggs does he have left?",
        "options": ["1. 3", "2. 10", "3. 30", "4. 0"],
        "answer": 1
    },
    {
        "question": "I am an odd number. Take away one letter, and I become even. What number am I?",
        "options": ["1. Seven", "2. Eleven", "3. Nine", "4. Three"],
        "answer": 1
    }
]

# Function to run the quiz
def run_quiz():
    score = 0
    print("Welcome to the Quiz!\n")

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        
        for option in q['options']:
            print(option)
        
        try:
            user_answer = int(input("Enter the number of your answer: "))
            
            if user_answer == q['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['options'][q['answer'] - 1]}\n")
        
        except ValueError:
            print("Invalid input! Please enter a number.\n")

    print(f"Quiz Over! Your final score is {score}/{len(questions)}.")

# Run the quiz
if __name__ == "__main__":
    run_quiz()