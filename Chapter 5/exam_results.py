score = int(input("試験の点数を入力してください（0～100）-> "))

if score >= 80:
    print(f"あなたの点数は {score} 点です。合格です！")
else:
    print(f"あなたの点数は {score} 点です。不合格です！")