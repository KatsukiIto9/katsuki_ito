# Create a multidimensional list
grades = [
    [85, 90, 92],  # Grades for Student 1
    [78, 88, 85],  # Grades for Student 2
    [91, 94, 89],  # Grades for Student 3
    [70, 76, 72],  # Grades for Student 4
    [88, 84, 90]   # Grades for Student 5
]

# Display the grades for each student
print("Grades for each student:")
student_number = 1  # Variable to track student number
for student_grades in grades:
    print(f"Student {student_number}: {student_grades}")
    student_number += 1

# Calculate and display the average grade for each student
print("\nAverage grades for each student:")
student_number = 1  # Variable to track student number
for student_grades in grades:
    average = sum(student_grades) / len(student_grades)
    print(f"Average for Student {student_number}: {average:.2f}")
    student_number += 1

# Calculate and display the overall average grade for the class
total_sum = 0
total_count = 0
for student_grades in grades:
    total_sum += sum(student_grades)
    total_count += len(student_grades)
class_average = total_sum / total_count
print(f"\nOverall average grade for the class: {class_average:.2f}")
