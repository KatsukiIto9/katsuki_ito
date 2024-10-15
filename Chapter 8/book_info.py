class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def print_title(self):
        print(f"タイトル：{self.title}")
    
    def print_author(self):
        print(f"著者: {self.author}")

books = []

for i in range(3):
    title = input(f"{i+1}冊目の書籍のタイトルを入力してください: ")
    author = input(f"{i+1}冊目の書籍の著者を入力してください: ")
    
    new_book = Book(title, author)
    books.append(new_book)

for book in books:
    book.print_title()
    book.print_author()
