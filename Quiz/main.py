import random
from data import questions_dict

def quiz():
    
    score = 0
    total_questions = 25
    
    selected_questions = random.sample(questions_dict, total_questions)

    for question in selected_questions:
        print(question["question"])
        
        # Combine correct and incorrect answers
        answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(answers)  # Shuffle answers
        
        # Display answers
        for i, answer in enumerate(answers):
            print(f"{i + 1}. {answer}")
        
        # Get user input
        user_answer = input("あなたの答えを入力してください (1-4): ")

        # Check if answer is correct
        correct_answer = question["correct_answer"]
        if answers[int(user_answer) - 1] == correct_answer:
            print("正解です！\n")
            score += 1
        else:
            print(f"残念！正解は {correct_answer} です。\n")

    # Display final score
    print(f"クイズ終了！あなたのスコアは {score}/{total_questions} です。")

quiz()
