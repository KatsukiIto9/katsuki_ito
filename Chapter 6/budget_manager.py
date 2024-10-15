# 予算管理アプリケーション
expenses = {"rent": 70000, "groceries": 30000, "utilities": 10000, "entertainment": 15000}

# 支出項目の追加
new_item = input("追加する支出項目: ")
new_amount = int(input(f"{new_item}の金額: "))
expenses[new_item] = new_amount

# 支出項目の削除
remove_item = input("削除する支出項目: ")
if remove_item in expenses:
    del expenses[remove_item]
    print(f"{remove_item}を削除しました。")
else:
    print(f"{remove_item}は見つかりませんでした。")

# 支出項目の更新
update_item = input("更新する支出項目: ")
if update_item in expenses:
    new_amount = int(input(f"{update_item}の新しい金額: "))
    expenses[update_item] = new_amount
    print(f"{update_item}の金額を更新しました。")
else:
    print(f"{update_item}は見つかりませんでした。")

# 支出項目の検索
search_item = input("検索する支出項目: ")
if search_item in expenses:
    print(f"{search_item}の金額は{expenses[search_item]:,}円です。")
else:
    print(f"{search_item}は見つかりませんでした。")

# 全支出項目と金額の表示
print("\n全支出項目と金額:")
for item, amount in expenses.items():
    print(f"{item}: {amount:,}円")

# 総支出金額の計算
total_expense = sum(expenses.values())
print(f"\n総支出金額: {total_expense:,}円")
