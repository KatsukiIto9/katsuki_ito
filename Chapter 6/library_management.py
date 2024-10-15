# 複数のリストを作成
titles = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude", "Pride and Prejudice"]
authors = ["George Orwell", "Harper Lee", "F. Scott Fitzgerald", "Gabriel Garcia Marquez", "Jane Austen"]
genres = ["Dystopian", "Historical Fiction", "Classic", "Magical Realism", "Romance"]

# zip関数を使って書籍の情報をタプルに結合
books = tuple(zip(titles, authors, genres))

# 各書籍の詳細を表示
print("書籍の詳細:")
for title, author, genre in books:
    print(f"{title}, {author}: {genre}")

# 特定の書籍の詳細を表示
book_title = input("\n詳細を表示したい書籍のタイトルを入力してください: ")

# 書籍の詳細を探して表示
for title, author, genre in books:
    if title.lower() == book_title.lower():
        print(f"\n{title}の詳細:\\n著者: {author}\\nジャンル: {genre}")
        break
else:
    # ループが完了してもbreakが呼び出されなかった場合に実行
    print(f"\n{book_title}というタイトルの書籍は見つかりませんでした。")

# enumerate関数を使って書籍の情報をインデックスと共に表示
print("\nenumerate関数を使った書籍のタイトル:")
for index, title in enumerate(titles):
    print(f"{index}: {title}")
