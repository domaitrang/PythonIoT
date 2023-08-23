a = [1, 2, 3, 4, 5]
b = a
# b = [1, 2, 3, 4, 5]
# print(a is b)

#  b thay đổi, a có thay đổi không?
b[0] = 8
print("a = ", a)
print("b = ", b)