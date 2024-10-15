def calculate_average(name, grades):
    average = sum(grades) / len(grades)
    return average

grades = [85, 90, 78]
name = "John Doe"
average_grade = calculate_average(name, grades)
print(f"{name} の平均点は {average_grade : .2f} 点です")