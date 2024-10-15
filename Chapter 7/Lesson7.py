# def function1():
#     print("function1")

# def function2():
#     print("fucntion2")
#     return function1()

# def function3(arg1, arg2):
#     print("function3: 引数１ = " + arg1 + ", 引数2 = " + arg2)

# def function4(num1, num2):
#     result = num1 ** num2
#     print(f"function4 : {num1}の{num2}値は{result}")
#     return result

# function1()

# result2 = function2()
# print(f"Main : {result2}")

# function3("sunday", "monday")

# result4 = function4(6,7)
# print(f"{result4}")

# def func(kuku2):
#     kuku2[0] *= 100

# kuku2 = [i * 2 for i in range(1,10)]
# print(f"Before:{kuku2}")
# func(kuku2)
# print(f"After: {kuku2}")

def func():
    return 1,2,3

w = func()
print(w)

x, y, z = func()
# x, y = func()
print(x, y ,z)

a, *b = func()
print(a, b)