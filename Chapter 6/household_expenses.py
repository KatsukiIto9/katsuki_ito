expenses = (
    ("Groceries", 20000),
    ("Utilities", 15000),
    ("Rent", 80000),
    ("Transportation", 10000),
    ("Entertainment", 5000),
    ("Miscellaneous", 3000)
    )
print("各カテゴリの支出:")
for category, amount in expenses:
    print(f"{category}: ¥{amount:,}")

total_expense = 0
for _, amount in expenses:
    total_expense += amount
print(f"\n全支出の合計: ¥{total_expense:,}")