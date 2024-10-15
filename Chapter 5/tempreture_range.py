temp = float(input("今日は何度ですか？(度)\n"))

if temp < 36.5:
    result = "低体温"
elif temp <= 37.5:
    result = "平熱"
else:
    result = "発熱"

print(f"合計は{result}")