wind_speed = float(input("風速を入力してくださいー＞(m/s)"))

if wind_speed <= 1.5:
    print("微風")
elif 1.6 <= wind_speed <= 4.0:
    print("弱風")
elif 4.1 <= wind_speed <= 8.0:
    print("中風")
else:
    print("強風")