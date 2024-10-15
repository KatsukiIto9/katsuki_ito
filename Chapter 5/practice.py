#Sample p.60
# time = int(input("今何時ですか？０～２３を入力してください：\n"))

# if time <  12:
#     print(f"午前{time}時です。")
# elif time == 12:
#     print("正午です。")
# else:
#     print(f"午後{time-12}時です。")

#Sample p.61

# num = int(input("整数を入力してください\n"))
# if 15 <= num < 30:
#     print("入力した数値は, 15以上30未満です。")
# print("プログラムを終了します")

#Sample p.62

# required_unit = int(input("取得している必修単位数　ー＞"))
# total_unit = int(input("取得している合計位数　ー＞"))

# if required_unit >= 40 and total_unit >= 128:
#     print("無事卒業できます。おめでとうございます！")
# elif required_unit < 40 and total_unit >= 128:
#     print("必修単位　あと%d単位" % (40 - required_unit))
# elif required_unit >= 40:
#     print("合計単位　あと%d単位" % (128 - required_unit))
# else:
#     print("必修単位も合計単位も足りていないです。")

#Sample p.65

# score = int(input("点数を入力してください\n"))

# if score >= 60:
#     result = "合格"
# else:
#     result = "不合格"
# print(f"結果:{result}")

# for i in range(5):
#     print(f"{i+1}回目のループ")

# for i in range(1,10):
#     print(3 * i , end=",")

# for i in range(3,7):
#     for j in range(1,10):
#         print(i * j, end="\t")
#     print()

# i = 0
# while i < 5:
#     print(f"{i + 1}回目のループ")
#     i += 1

# for m in range(1,13):
#     print(f"{m}月")
#     if m == 5:
#         print(f"==={m}月で終了します。")
#         break

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     if i == 4:
#         break
#     print()

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i *j, end="\t")
#         if j == 4:
#             break
#     print()

# i = 1
# while True:
#     print(f"16の{i}乗：{16**i}")
#     if i == 5:
#         break
#     i += 1

# for m in range(1, 13):
#     if m == 7:
#         continue
#     print("%02d月" % (m))

for i in range(5):
    print(f"{i + 1}回目の処理")
    if i + 1 == 3:
        break
    else:
        print("ループを終了します。")