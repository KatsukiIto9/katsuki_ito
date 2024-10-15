def sum_all(*args):
    total = sum(args)
    return total

numbers = list(map(int,input("数値をカンマ区切りで入力してください: ").split(',')))

total_sum = sum_all(*numbers)

print(f"合計：{total_sum}")
