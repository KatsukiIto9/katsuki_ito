score = int(input("試験の点数を入力してくださいー＞"))

if 100 >= score >= 90:
    print("優秀")
elif 89 >= score >= 70:
    print("良好") 
elif 69 >= score >= 50:
    print("合格")
elif score <= 49:
    print("不合格")