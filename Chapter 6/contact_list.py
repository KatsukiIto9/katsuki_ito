# コンタクトリストを作成
contacts = {"Alice": "090-1234-5678", "Bob": "080-2345-6789", "Charlie": "070-3456-7890"}

# 新しいコンタクトを追加
contacts["David"] = "060-4567-8901"
print("コンタクトを追加後:")
print(contacts)

# 既存のコンタクトを更新
contacts["Alice"] = "090-9876-5432"
print("コンタクトを更新後:")
print(contacts)

# コンタクトを削除
del contacts["Bob"]
print("コンタクトを削除後:")
print(contacts)

# 特定のコンタクトを検索
print("Charlie が存在するか確認:", "Charlie" in contacts)
print("Eve の電話番号:", contacts.get("Eve", "not found"))
