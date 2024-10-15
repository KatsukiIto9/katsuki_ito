temp = float(input("摂氏温度を入力してください:\n"))

result = "適温" if 0 <= temp < 100 else "不適温"

print(f"入力された温度は{result}です。")