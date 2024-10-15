books = ["1984", "Mockingbird", "Gatsby", "Solitude", "Pride", "War", "Catcher", "Hobbit"]


print("5番目以降の本のタイトル:", books[4:])

print("3番目から7番目までの本のタイトル:", books[2:7])

print("奇数番目の本のタイトル:", books[0:len(books):2])


print("リストの逆順:", books[::-1])
print("元のリスト:", books)
books.reverse()
print("逆順に並べ替えたリスト:", books)
