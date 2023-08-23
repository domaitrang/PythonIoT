# ôn lại kiến thức buổi trước:
# hàm input() cho kết quả là 1 chuỗi, hay string
# hàm print()
a = int(input("nhập vào một số: "))
print("Số bạn vừa nhập là: ", a)

# format một số
a = int(input("nhập số quả táo: "))

# if(a == 1):
#      print("there is", a, 'apple')
# else:
#     print("there are", a, 'apples')

a = int(input("nhập số quả táo: "))
s = ""
if a > 1:
    s = "s"
# print("there are {} apple{}".format(a,s))
print(f"There are {a} apple{s}")


# Bài tập 2
""" tien_USD=float(input("Nhập vào số tiền đô bạn đang có : "))
ty_gia=float(input("Tỷ giá quy đổi hiện tại : "))
tien_VND=tien_USD*ty_gia
print("số tiền đô la của bạn là :",tien_USD," được quy đổi sang tiền việt là :",tien_VND , "với tỉ giá là : ",ty_gia) """

USD = float(input("Số tiền bạn muốn đổi: "))
rate = float(input("tỉ giá hiện tại: "))
VND = USD * rate
print(f"{USD} $ = {VND} VNĐ")

# Hiển thị có định dạng, ví dụ 362,064.00 đồng
USD = float(input("Số tiền bạn muốn đổi: "))
rate = float(input("tỉ giá hiện tại: "))
VND = USD * rate
print(f"{USD} $ =", "{:,.2f}".format(VND), "VNĐ")

# Toán tử trong python:

# Toán tử số: + , -, x, : (toán học) --> python: +, -, * , /
a = 12
b = 5
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a x b = ", a * b)
print("a : b = ", a / b)

# Phép chiaw lấy nguyên (//) và phép chia lấy dư (%)
a = 11
b = 2
print("Phần nguyên của phép chia a/b là: ", a // b) # 11 = 2 * 5 + 1
print("Phần dư của phép chia a/b là: ", a % b)

# Toán tử hàm mũ: a^b trong python dùng **
print("3 luỹ thừa 2 bằng: ", 3 ** 2)

# Toán tử so sánh: >, <, >=, <=, == != kết quả của phép so sánh là True hoặc False
a = 11
b = 2
print(a > 5) # True
print(a < 7) # False
print(a == b) # False

#  Toán tử gán VT = VP --> gán giá trị VP cho biến ở vế trái
x = 2
y = x

#  Gán cùng lúc nhiều giá trị:
a, b = 5, 6
print("a = ", a)
print("b = ", b)
#  Phep giao hoán:
a, b = b, a

print("a = ", a)
print("b = ", b)

# Toán tử logic: and, or, not
a = 6
# A and B : Chỉ đúng khi cả hai cùng đúng
print((a > 10) and (a < 4))

# A or B : Chỉ sai khi cả 2 cùng sai
a = 6
print((a==2) or (a==3))
# A not B
a = 6
print(not (a == 9)) # True

# Toán tử thao tác với bit (ít dùng): AND (&), OR (|), XOR (^), NOT ( ), LEFT_SHIFT (<<), RIGHT_SHIFT
a = 10
b = 12
print(a, bin(a))
print(b, bin(b))
c =a & b
print(c, bin(c))

# Toán tử thành viên (membership): in và not in
arr = [1, 2, 3, 4, 54, 7, 8, 9]
print(54 in arr)
print(0 in arr)

# Toán tử định danh: is và not is
x = 5
y = 5
print(y is x)
y = x
z = y
print(z is x)

# Nếu z thay đổi thì x có thay đổi không?
z = 4
print("x = ", x)
print("y = ", y)
print("z = ", z)


a = [1, 2, 3, 4, 5]
b = a
# b = [1, 2, 3, 4, 5]
# print(a is b)

#  b thay đổi, a có thay đổi không?
b[0] = 8
print("a = ", a)
print("b = ", b)