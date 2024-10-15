num = int(input("進数を入力してください。:\n"))
if num >= 6:
    print("numを７倍します。")
    num *= 7
    if num == 0:
        print("numを５足します。")
        if num == 0:
            num += 5
print("numの値は",num)