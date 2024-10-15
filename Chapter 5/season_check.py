month = int(input("今何月ですか？１～１２入力してください\n"))

if month <= 3:
    print("冬です。")
elif month >= 4 and month <= 6:
    print("春です。")
elif month >= 7 and month <= 9:
    print("夏です。")
elif month >= 10 and month <= 12:
    print("秋です。")
else:
    print("無効な月です。1～12の範囲で入力してください。")