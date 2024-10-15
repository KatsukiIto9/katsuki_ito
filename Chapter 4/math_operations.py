import math 

radius = 2
pi = math.pi
area = math.pi * radius ** 2
print(f"半径 {radius} の円の面積: {area}")

round_up = math.ceil(6.2)
print(f"6.2 を切り上げます: {round_up}")

round_down = math.floor(6.2)
print(f"6.2 を切り下げます: {round_down}")

round_value = round(pi)
print(f"3.14159 を切り下げます: {round_value}")

round_two_decimals = round(pi, 2)
print(f"3.14159 を小数点以下 2 桁に丸める: {round_two_decimals}")

print(f"円周率の値: {pi}")