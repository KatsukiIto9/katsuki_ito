# 旅行先リストを作成
original_destinations = ["Paris", "Tokyo", "New York", "Sydney"]

# リストの値をコピー
copied_destinations = original_destinations.copy()

# リストの参照をコピー
reference_destinations = original_destinations

# 値比較を行い結果を表示
print("値比較 (original_destinations と copied_destinations):", original_destinations == copied_destinations)
print("値比較 (original_destinations と reference_destinations):", original_destinations == reference_destinations)

# メモリアドレスを表示
print("メモリアドレス (original_destinations):", id(original_destinations))
print("メモリアドレス (copied_destinations):", id(copied_destinations))
print("メモリアドレス (reference_destinations):", id(reference_destinations))

# アドレス比較を行い結果を表示
print("アドレス比較 (original_destinations と copied_destinations):", original_destinations is copied_destinations)
print("アドレス比較 (original_destinations と reference_destinations):", original_destinations is reference_destinations)

# リストの変更前を表示
print("変更前のリスト:")
print("original_destinations:", original_destinations)
print("copied_destinations:", copied_destinations)
print("reference_destinations:", reference_destinations)

# original_destinationsの3番目の要素を変更
original_destinations[2] = "Barcelona"

# 変更後の各リストを表示
print("変更後のリスト:")
print("original_destinations:", original_destinations)
print("copied_destinations:", copied_destinations)
print("reference_destinations:", reference_destinations)
