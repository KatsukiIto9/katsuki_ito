def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item}はリストに存在しません。")

shopping_list = input("初期の買い物リストをカンマ区切りで入力してください: ").split(',')

item = input("削除する商品を入力してください: ")

remove_item(shopping_list, item)

print("更新された買い物リスト:", shopping_list)