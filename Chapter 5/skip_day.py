
skip_day = int(input("スキップする日を入力してください (1-7): "))

print("1週間の健康習慣を記録します")


for day in range(1, 8):
    
    if day == skip_day:
        continue

    print(f"今日は {day} 日目。水を飲みました！")
