def calculate_salary(base_salary, bonus, trasportation_allowance = 10000):
    return base_salary + bonus + trasportation_allowance

base_salary = int(input("基本給を入力してください: "))

bonus = int(input("ボーナスを入力してください: "))

transportation_allowance = input("交通費を入力してください (省略可能): ")

if transportation_allowance:
    total_salary = calculate_salary(base_salary, bonus, trasportation_allowance=int(transportation_allowance))

else:
    total_salary = calculate_salary(base_salary, bonus)

print("総給与は", total_salary, "円です")