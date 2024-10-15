class Product:
    
    def print_name(self):
        print(f"製品名: {self.name}")
        
    def print_price(self):
        print(f"価格: {self.price}円")
        
    def print_stock(self):
        print(f"在庫数: {self.stock}個")

p = Product()
p.name = input("製品の名前を入力してください: ")
p.price = int(input("製品の価格を入力してください: "))
p.stock = int(input("製品の在庫数を入力してください: "))

p.print_name()
p.print_price()
p.print_stock()