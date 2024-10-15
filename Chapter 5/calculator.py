import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def calculator():
    while True:
        clear()

        try:
            
            num1 = int(input("最初の変数を入力してください:\n"))
            num2 = int(input("次の変数を入力してください:\n"))
        except ValueError:
            print("数値を入力してください。")
            continue

        
        operation = input("どのような操作を使用したいか(+ , - , * , /)\n")

        
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("ゼロで割ることはできません。")
                continue
        else:
            print("無効な操作です。")
            continue

        
        repeat = input("もう一度計算を行いますか？(yes/no): ")
        if repeat.lower() != 'yes':
            print("電卓を使用していただきありがとうございます！")
            break

# Run the calculator
calculator()
