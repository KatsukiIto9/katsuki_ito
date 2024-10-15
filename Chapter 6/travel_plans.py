# 空のリストを角括弧[]で作成
cities = []
print(cities)

# 空のリストをlist()で作成
cities2 = list()
print(cities2)

# 訪れたい都市をリストに追加
cities = ["Tokyo", "Kyoto", "Osaka", "Hiroshima", "Fukuoka"]
print(cities)

# リストの各都市にアクセスして表示
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
print(cities[4])

# リストの範囲外にアクセスしてエラーを確認
print(cities[5])  # ここでエラーが発生します
