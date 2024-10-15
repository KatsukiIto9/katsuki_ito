participants = (
    ("Alice", 28),
    ("Bob", 34),
    ("Charlie", 22),
    ("Diana", 31),
    ("Edward", 45),
    ("Fiona", 29),
    ("George", 37),
    ("Hannah", 26)
)

print("各参加者の名前と年齢:")
for name, age in participants:
    print(f"{name}: {age}歳")

total_age = 0
for _, age in participants:
    total_age += age
average = total_age / len(participants)
print(f"\\n全参加者の平均年齢: {average:.2f}歳")