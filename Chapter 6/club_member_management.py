# クラブメンバーのセットを作成
members = {"John", "Alice", "Bob", "Diana"}

# 新しいメンバーを追加
members.add("Eve")
print("メンバー追加後:")
print(members)

# メンバーを削除
members.remove("Alice")
print("メンバー削除後:")
print(members)

# 新しいセットを作成
new_members = {"Frank", "Diana", "Grace"}

# 和集合を計算して表示
all_members = members.union(new_members)
print("和集合:")
print(all_members)

# 積集合を計算して表示
common_members = members.intersection(new_members)
print("積集合:")
print(common_members)

# 差集合を計算して表示
exclusive_members = members.difference(new_members)
print("差集合:")
print(exclusive_members)

# 対称差を計算して表示
symmetric_difference_members = members.symmetric_difference(new_members)
print("対称差:")
print(symmetric_difference_members)