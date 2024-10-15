movies = ["Inception", "Interstellar", "The Dark Knight", "Memento", "Tenet", "Dunkirk", "The Prestige", "Insomnia"]

print("5番目以降の映画タイトル:", movies[4:])
print("3番目から7番目までの映画タイトル:", movies[2:7])
print("奇数番目の映画タイトル:", movies[0:len(movies):2])
print("リストの逆順:", movies[::-1])
print("元のリスト:", movies)
movies.reverse()
print("逆順に並べ替えたリスト:", movies)
