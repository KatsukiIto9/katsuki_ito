balance = int(input("電子マネー残高を入力してください -> "))
charge_amount = int(input("希望するチャージ額を入力してください -> "))

if balance < charge_amount:
    balance += charge_amount
    print(f"自動で {charge_amount:,} 円チャージしました。")

print(f"電子マネー残高：{balance:,}円")
