
num1 = 10_000_000
num2 = 5
num3 = 3.14
num4 = 1 + 2j

addition = num1 + num2
print(f"{num1} と {num2} の加算は {addition}\n")

subtraction = num1 - num2
print(f"{num2} から {num1} を減算すると {subtraction}\n")

multiplication = num2 * num3
print(f"{num2} と {num3} の乗算は {multiplication}\n")

division = num1 / num2
print(f"{num1} を {num2} で割ると {division}\n")

quotient = num1 // num2
print(f"{num1} を {num2} で割った商 (切り捨て) は: {quotient}\n")

remainder = num1 % num2
print(f"{num1} を {num2} で割ったときの剰余は: {remainder}\n")

absolute_value = abs(num4)
print(f"{num4} の絶対値は: {absolute_value}\n")

power = num2 ** num3
print(f"{num2} を {num3} で累乗すると: {power}\n")
