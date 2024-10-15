def calculate_budget(incomes, expenses):
    total_income = sum(incomes)
    total_expense = sum(expenses)
    balance = total_income - total_expense
    return total_income, total_expense, balance

print("\n個人予算管理アプリケーション")
# 収入を入力し、リストに変換
incomes = list(map(float, input("収入をカンマ区切りで入力してください: ").split(",")))
# 支出を入力し、リストに変換
expenses = list(map(float, input("支出をカンマ区切りで入力してください: ").split(",")))
# 予算を計算
total_income, total_expense, balance = calculate_budget(incomes, expenses)
# 結果を表示
print(f"\n総収入: {total_income}")
print(f"総支出: {total_expense}")
print(f"残高: {balance}")
