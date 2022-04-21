
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

 DD
