# 行と列を表示する表を作成します
print("行と列を表示する表を作成します")
for row in range(1, 4):  # 1から3までの行をループ
    for col in range(1, 4):  # 1から3までの列をループ
        print(f"({row}, {col})", end="\t")  # 行と列の組み合わせを表示、タブ区切り
    print()  # 改行

print()  # 改行

# 直角三角形の星印を表示します
print("直角三角形の星印を表示します")
for i in range(1, 6):  # 1から5までの行をループ
    for j in range(i):  # 現在の行数分の星を表示
        print("*", end="")  # 星を表示
    print()  # 改行
