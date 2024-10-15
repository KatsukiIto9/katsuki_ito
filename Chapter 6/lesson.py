# fruits = ["grape", "peach", "banana", "apple"]
# print("== for ==")

# for s in fruits:
#     print(s)

# print("== while ==r")
# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# list1 = [1,2,3,4]
# list2 = [1,2.3,4]

# print(id(list1))
# print(id(list2))
# print(list1 is list2)

# list1 = [1,2,3,4]
# list2 = list1.copy()
# print(list1 == list2)
# print(id(list1))
# print(id(list2))
# print(list1 is list2)

# list1 = [1,2,3,4]
# list2 = list1
# print(list1 == list2)
# print(id(list1))
# print(id(list2))
# print(list1 is list2)

# score1 = [11,12,13,14]
# score2 = score1.copy()
# score3 = score1
# print("before:", score1)
# score1[2] = 21
# print("score1:", score1)
# print("score2:", score2)
# print("score3:", score3)

# a = [11,12,13,14,15,16,17,18,19,20]
# print(a[4:])
# print(a[2:6])
# print(a[1:10:2])
# print(a[::-1])
# print(a)

# c = [1,2,3]
# print("iter")
# cit = iter(c)
# print(next(cit))
# print(next(cit))
# print(next(cit))

# print("reverse")
# crv = reversed(c)
# print(next(crv))
# print(next(crv))
# print(next(crv))
# print(next(crv))

# scores = [
#     [56, 78, 91],
#     [22, 45, 61],
# ]

# print("== scores == ")
# print(scores)

# print("== for:scores == ")
# for score in scores:
#     print(score)

# print("== for nest: s ==")
# for score in scores:
#     for s in score:
#         print(s, end="\t")
#     print()

# tuple1 = ()
# print(tuple1)

# tuple2 = tuple()
# print(tuple2)

# tuple3 = (1,2,3,4,5)
# print(tuple3)
# print(tuple3[1])

# tuple_ng = (1)
# print(tuple_ng)

# tuple4 = (1,)
# print(tuple4)

# tuple5 = 1,2,3,4,5
# print(tuple5)

# fruits = ("grape", "peach", "banana", "apple")
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])

# tuple1 = tuple(["apple", "grape", "banana","peach"])
# tuple2 = tuple(range(1,10))
# print(tuple1)
# print(tuple2)

# temp_list = [
#     ["Tokyo", 25, 32],
#     ["Nagoya", 21, 28],
#     ["Osaka", 20, 27],
#     ["Kyoto", 19, 26],
#     ["Fukuoka", 22, 27]
# ]

# temp_list = [
#     ("Tokyo", 25, 32),
#     ("Nagoya", 21, 28),
#     ("Osaka", 20, 27),
#     ("Kyoto", 19, 26),
#     ("Fukuoka", 22, 27)
# ]

# set1 = {"tiger", "horse", "lion", "pig"}
# for s in set1:
#     print(s)

# fruits = {"apple", "grape", "banana", "peach"}
# print(fruits)
# fruits.add("strawberry")
# print(fruits)
# fruits.add("banana")
# print(fruits)

# multi2 = set(range(3,21,2))
# multi3 = set(range(3,21,3))
# print(multi2)
# print(multi3)
# print(multi2.union(multi3))
# multi2 | multi3
# print(multi3)

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})
f = dict({'one':1, 'three':3}, two=2)
print(a == b == c == d == e == f)
print(a)