# 図書館の書籍管理
books = {
    "Harry Potter and the Philosopher's Stone": "J.K. Rowling",
    "The Hobbit": "J.R.R. Tolkien",
    "The Chronicles of Narnia": "C.S. Lewis",
    "Percy Jackson & the Olympians": "Rick Riordan"
}

# 書籍の追加
new_title = input("追加する書籍のタイトル: ")
new_author = input(f"{new_title}の著者: ")
books[new_title] = new_author

# 書籍の削除
remove_title = input("削除する書籍のタイトル: ")
if remove_title in books:
    del books[remove_title]
    print(f"{remove_title}を削除しました。")
else:
    print(f"{remove_title}は見つかりませんでした。")

# 書籍の更新
update_title = input("更新する書籍のタイトル: ")
if update_title in books:
    new_author = input(f"{update_title}の新しい著者: ")
    books[update_title] = new_author
    print(f"{update_title}の著者を更新しました。")
else:
    print(f"{update_title}は見つかりませんでした。")

# 書籍の検索
search_title = input("検索する書籍のタイトル: ")
if search_title in books:
    print(f"{search_title}の著者は{books[search_title]}です。")
else:
    print(f"{search_title}は見つかりませんでした。")

# 全書籍の表示
print("\\n全書籍のタイトルと著者:")
for title, author in books.items():
    print(f"{title}: {author}")
