# ショッピングカートを作成
cart = {"apple": 100, "banana": 150, "orange": 200}

# 新しい商品を追加
cart["grape"] = 250
print("商品を追加後:")
print(cart)

# 既存の商品を更新
cart["banana"] = 180
print("商品を更新後:")
print(cart)

# 商品を削除
del cart["apple"]
print("商品を削除後:")
print(cart)

# カート内の商品を表示し、合計金額を計算
total_price = 0
for item, price in cart.items():
    print(f"{item}: ¥{price}")
    total_price += price
print(f"合計金額: ¥{total_price}")
