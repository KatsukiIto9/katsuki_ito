current_savings = int(input("現在の貯金額を入力してください: \n"))
saving_goals = int(input("目標貯金額を入力してください: \n"))
monthly_savings = int(input("毎月の貯金額を入力してください: "))

months = 0

while current_savings < saving_goals:
    current_savings += monthly_savings
    months += 1
    print(f"{months} ヶ月目の貯金額: {current_savings} 円")

print("目標額に達しました！")