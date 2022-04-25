
print(2+2)

# string
print('C:\some\\test')
print(r'C:\some\test')

print('py' 'thon')

x = 'abc'
print('C:\\some\\name\\' + x)
print(f'C:\\some\\name\\{x}')
print("C:\\some\\name\\{}".format(x))
print("C:\\some\\name\\{}\\{}".format(x, 123))
print("C:\\some\\name\\{x}\\{y}".format(x=x, y=123))


# List  [1,2,3]

squares = [1,2,3]
print(squares[0])

# 切片
print(squares[0:2])
print(squares[-1])
print(squares[-1:])

squares.append("4")

squares.append(5)

print(squares)

list = [x*10 for x in range(10)]
print(list)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


# 集合，sets，无排序
# 元组，tuples，不可修改
# 列表，list，可修改
# 词典，dict，关系数据

# （1）集合
# 并集、交集
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)
# {'apple', 'pear', 'banana', 'orange'}

basket.add('a')
print(basket)
# {'a', 'pear', 'apple', 'orange', 'banana'}

basket.add('a')
print(basket)
# {'a', 'pear', 'apple', 'orange', 'banana'}

basket2 = {'apple','orange','apple','pear','orange','banana','b'}
print(basket2)
# {'orange', 'apple', 'b', 'banana', 'pear'}

print(basket.union(basket2))
# 并集
# {'a', 'b', 'pear', 'apple', 'orange', 'banana'}
print(basket.intersection(basket2))
# 交集
# {'pear', 'banana', 'orange', 'apple'}
print(basket.difference(basket2))
# 不同
# {'a'}

# （2）元组
掩饰