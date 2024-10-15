# 趣味リストを作成
original_hobbies = ["Reading", "Traveling", "Gardening", "Cooking"]

# リストの値をコピー
copied_hobbies = original_hobbies.copy()

# リストの参照をコピー
reference_hobbies = original_hobbies

# 値比較を行い結果を表示
print("値比較 (original_hobbies と copied_hobbies):", original_hobbies == copied_hobbies)
print("値比較 (original_hobbies と reference_hobbies):", original_hobbies == reference_hobbies)

# メモリアドレスを表示
print("メモリアドレス (original_hobbies):", id(original_hobbies))
print("メモリアドレス (copied_hobbies):", id(copied_hobbies))
print("メモリアドレス (reference_hobbies):", id(reference_hobbies))

# アドレス比較を行い結果を表示
print("アドレス比較 (original_hobbies と copied_hobbies):", original_hobbies is copied_hobbies)
print("アドレス比較 (original_hobbies と reference_hobbies):", original_hobbies is reference_hobbies)

# リストの変更前を表示
print("変更前のリスト:")
print("original_hobbies:", original_hobbies)
print("copied_hobbies:", copied_hobbies)
print("reference_hobbies:", reference_hobbies)

# original_hobbiesの3番目の要素を変更
original_hobbies[2] = "Hiking"

# 変更後の各リストを表示
print("変更後のリスト:")
print("original_hobbies:", original_hobbies)
print("copied_hobbies:", copied_hobbies)
print("reference_hobbies:", reference_hobbies)
