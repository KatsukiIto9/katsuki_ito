class Recipe:
    def print_name(self):
        print(f"料理名: {self.name}")
        
    def print_main_ingredeint(self):
        print(f"主要材料: {self.main_ingredient}")
        
    def print_cooking_time(self):
        print(f"調理時間: {self.cooking_time}分")

recipes = [Recipe(), Recipe(), Recipe()]

recipes[0].name = input("1つ目の料理の名前を入力してください: ")
recipes[0].main_ingredient = input("1つ目の料理の主要材料を入力してください: ")
recipes[0].cooking_time = int(input("1つ目の料理の調理時間を入力してください: "))

recipes[1].name = input("2つ目の料理の名前を入力してください: ")
recipes[1].main_ingredient = input("2つ目の料理の主要材料を入力してください: ")
recipes[1].cooking_time = int(input("2つ目の料理の調理時間を入力してください: "))

recipes[2].name = input("3つ目の料理の名前を入力してください: ")
recipes[2].main_ingredient = input("3つ目の料理の主要材料を入力してください: ")
recipes[2].cooking_time = int(input("3つ目の料理の調理時間を入力してください: "))

for recipe in recipes:
    recipe.print_name()
    recipe.print_main_ingredient()
    recipe.print_cooking_time()