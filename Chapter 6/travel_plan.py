# 複数のリストを作成
cities = ["Tokyo", "Paris", "New York", "London", "Sydney"]
countries = ["Japan", "France", "USA", "UK", "Australia"]
attractions = ["Tokyo Tower", "Eiffel Tower", "Statue of Liberty", "London Eye", "Sydney Opera House"]

# zip関数を使って旅行計画をタプルに結合
travel_plans = tuple(zip(cities, countries, attractions))

# 各旅行計画の詳細を表示
print("旅行計画の詳細:")
for city, country, attraction in travel_plans:
    print(f"{city}, {country}: {attraction}")

# 特定の都市の詳細を表示
city_name = input("\n詳細を表示したい都市の名前を入力してください: ")

# 都市の詳細を探して表示
for city, country, attraction in travel_plans:
    if city.lower() == city_name.lower():
        print(f"\n{city}の詳細:\n国: {country}\n観光名所: {attraction}")
        break
else:
    # ループが完了してもbreakが呼び出されなかった場合に実行
    print(f"\n{city_name}という都市は見つかりませんでした。")

# enumerate関数を使って都市の情報をインデックスと共に表示
print("\nenumerate関数を使った都市の名前:")
for index, city in enumerate(cities):
    print(f"{index}: {city}")
