# 趣味のセットを作成
my_hobbies = {"Reading", "Cycling", "Gardening", "Cooking"}

# 新しい趣味を追加
my_hobbies.add("Photography")
print("趣味追加後:")
print(my_hobbies)

# 趣味を削除
my_hobbies.remove("Gardening")
print("趣味削除後:")
print(my_hobbies)

# 友人の趣味のセットを作成
friend_hobbies = {"Cooking", "Traveling", "Photography", "Painting"}

# 和集合を計算して表示
all_hobbies = my_hobbies.union(friend_hobbies)
print("和集合:")
print(all_hobbies)

# 積集合を計算して表示
common_hobbies = my_hobbies.intersection(friend_hobbies)
print("積集合:")
print(common_hobbies)

# 差集合を計算して表示
exclusive_hobbies = my_hobbies.difference(friend_hobbies)
print("差集合:")
print(exclusive_hobbies)

# 対称差を計算して表示
symmetric_difference_hobbies = my_hobbies.symmetric_difference(friend_hobbies)
print("対称差:")
print(symmetric_difference_hobbies)

