# class MyClass:
    
#     def func1(self):
#         print("func1:")
        
#     def func2(self, text):
#         print(f"func2:{text}")
        
#     def func3(self):
#         print("func3:", self.num)
        

# obj = MyClass()

# obj.func1()
# obj.func2("power")
# obj.num = 12345
# obj.func3()
# print(MyClass.__doc__)

class Test:
    pass

t = Test()
t.a = 1
t.b = 2.5
t.c = "hoge"
t.d = True
t.e = [1,2,3]
t.f = (4,5)
t.g = {"six": 6, "seven": 7}
del t.d

def func(self):
    print(f"self.cの値：{self.c}")

Test.h = func
t.h()