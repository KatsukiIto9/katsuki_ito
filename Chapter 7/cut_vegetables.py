def cut_vegetable(vegetable):
    print(f"{vegetable}の皮をむいて切ります")
    return f"{vegetable}の皮をむいて切りました"

result_carrot = cut_vegetable("ニンジン")
print(result_carrot)

result_onion = cut_vegetable("玉ねぎ")
print(result_onion)

result_potato = cut_vegetable("じゃがいも")
print(result_potato)