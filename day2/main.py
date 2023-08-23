print(bool(1))
a = 10
b = 12
print(bin(a))
print(bin(b))
c = a & b
print(c, bin(c))

a = 10
b = ~a
print(b, bin(b))

print(a, bin(a))
a = a << 2 # 10 * 2^2 = 40
print(a, bin(a))

x = 1   # 1 là giá trị đơn
y = 1
z = x
# z = 2
print(x is z)

a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
b = a
print(a is b)
b[0] = 10
print(a)
print(b)