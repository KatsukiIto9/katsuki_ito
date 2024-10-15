expenses = []


def add_expense(item, amount, date):
    global expenses
    
    expense = {
        "item": item,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)


def display_total_expense():
    global expenses
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"\n支出の合計金額: {total} 円")

item = input("支出項目を入力してください: ")
amount = int(input("金額を入力してください: "))
date = input("日付を入力してください (YYYY-MM-DD): ")

add_expense(item, amount, date)

display_total_expense()