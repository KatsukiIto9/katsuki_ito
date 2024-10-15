# ユーザーに現在の貯金額を入力してもらう
current_savings = int(input("現在の貯金額を入力してください: "))

# ユーザーに目標貯金額を入力してもらう
savings_goal = int(input("目標貯金額を入力してください: "))

# ユーザーに毎月の貯金額を入力してもらう
monthly_saving = int(input("毎月の貯金額を入力してください: "))

# 月数カウンタを0で初期化
months = 0

# 現在の貯金額が目標貯金額未満の間、ループを実行
while current_savings < savings_goal:
    # 現在の貯金額に毎月の貯金額を加算
    current_savings += monthly_saving

    # 月数カウンタを1増やす
    months += 1

    # 貯金の進捗を表示
    print(f"{months} ヶ月目の貯金額: {current_savings} 円")

# 目標額に達したらメッセージを表示
print("目標額に達しました！")
