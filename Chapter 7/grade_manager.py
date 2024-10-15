def calculate_grades(scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)
    highest_score = max(scores)
    return total_score, average_score, highest_score

print("\n成績管理アプリケーション")

scores = list(map(float, input("各科目の得点をカンマ区切りで入力してください: ").split(",")))

total_score, average_score, highest_score = calculate_grades(scores)

print(f"\n総得点: {total_score}")
print(f"平均点: {average_score}")
print(f"最高得点: {highest_score}")