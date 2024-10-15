
total_reps = int(input("エクササイズの回数を入力してください: "))

break_rep = int(input("休憩する回数を入力してください: "))


print("エクササイズを開始します")


for r in range(1, total_reps + 1):
    
    print(f"{r} 回目のエクササイズ")

    if r == break_rep:
        print("休憩します。")
        break
