def add_book(book_list, new_book):
    if new_book not in book_list:
        book_list.append(new_book)

book_list = input("初期のお気に入りの本リストをカンマ区切りで入力してください: ").split(",")
new_book = input("追加する本のタイトルを入力してください: ")

add_book(book_list, new_book)

print("更新されたお気に入りの本リスト:", book_list)