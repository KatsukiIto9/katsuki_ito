class Vehicle:
    def print_model(self):
        print(f"モデル名:{self.model}")
        
    def print_year(self):
        print(f"製造年:{self.year}")
        
    def print_price(self):
        print(f"価格: {self.price}円")

vehicles = [Vehicle(), Vehicle(), Vehicle()]

vehicles[0].model = input("1台目の車両のモデル名を入力してください: ")
vehicles[0].year = input("1台目の車両の製造年を入力してください: ")
vehicles[0].price = int(input("1台目の車両の価格を入力してください: "))

vehicles[1].model = input("2台目の車両のモデル名を入力してください: ")
vehicles[1].year = input("2台目の車両の製造年を入力してください: ")
vehicles[1].price = int(input("2台目の車両の価格を入力してください: "))

vehicles[2].model = input("3台目の車両のモデル名を入力してください: ")
vehicles[2].year = input("3台目の車両の製造年を入力してください: ")
vehicles[2].price = int(input("3台目の車両の価格を入力してください: "))

for vehicle in vehicles:
    vehicle.print_model()
    vehicle.print_year()
    vehicle.print_price()