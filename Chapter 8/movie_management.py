class Movie:
    counter = 0
    
    def __init__(self, title, director):
        self.title = title
        self.director = director
        Movie.counter += 1
    
    def print_title(self):
        print(f"タイトル:{self.title}")
        
    def print_director(self):
        print(f"監督：{self.director}")
        
    def check_num(cls):
        print(f"現在の映画の本数: {cls.counter}本")

movies = []

for i in range(3):
    title = input(f"{i+1}本目の映画のタイトルを入力してください: ")
    director = input(f"{i+1}本目の映画の監督を入力してください: ")
    new_movie = Movie(title, director)
    movies.append(new_movie)

for movie in movies:
    movie.print_title()
    movie.print_director()

Movie.check_num()