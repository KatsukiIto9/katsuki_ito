schedule = ["Breakfast", "Work", "Lunch", "Meeting", "Gym", "Dinner", "Sleep"]

print("===FOR===")

for activity in schedule:
    print(activity)
    
print("===WHILE===")
i = 0
while i < len(schedule):
    print(schedule[i])
    i += 1