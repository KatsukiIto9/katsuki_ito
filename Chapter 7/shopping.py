def go_shopping(money, shopping_list):
    total_cost = 100 * len(shopping_list)
    
    change = money - total_cost
    return change

shopping_list = ["apple", "banana", "carrot"]
change = go_shopping(1000, shopping_list)
print(f"おつり: {change}")