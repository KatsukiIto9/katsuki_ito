# 7回目のループまでを表示します。
for i in range(7):
    print(f"{i + 1} 回目のループ")

print()  # 改行

# 5の段を表示します。
print("5の段を表示します。")
for i in range(1, 10):
    print(5 * i, end="\t")
print()  # 改行

# 50から70までの奇数を表示します。
print("50から70までの奇数を表示します。")
for i in range(51, 71, 2):
    print(i, end="\t")
print()  # 改行

# 10から1までのカウントダウンを表示します。
print("10から1までのカウントダウンを表示します。")
for i in range(10, 0, -1):
    print(i, end="\t")
print()  # 改行

# 15から45までの3の倍数を表示します。
print("15から45までの3の倍数を表示します。")
for i in range(15, 46, 3):
    print(i, end="\t")
print()  # 改行

# -10から-1までの数を表示します。
print("-10から-1までの数を表示します。")
for i in range(-10, 0):
    print(i, end="\t")
print()  # 改行

# 20から2までの偶数を降順で表示します。
print("20から2までの偶数を降順で表示します。")
for i in range(20, 1, -2):
    print(i, end="\t")
print()  # 改行
