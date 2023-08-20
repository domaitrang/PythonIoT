# Các kiểu dữ liệu trong python:
# số, chuỗi, tuble, list, dictionary, set...

# Kiểu số: số nguyên, số thập phân, số phức
# số nguyên: là số không có phần thập phân
a = 5
print(a, type(a))

b = "Chào bạn!"
print(b, type(b))
# Số thập phân: là số có phần thập phân

c = 2.5
print(c, type(c))

# Số phúc: x^2 = -1---> x = sqrt(-1) goi nó là  x == j
# dạng số phức: z = a + bj
z1 = 1 + 2j
z2 = 3 - 4j
print(z1 + z2)

# Vậy nhập và xuất dữ liệu như thế nào?
# Sử dụng hàm input() để nhận dữ liệu từ bàn phím; xuất ra màn hình bằng lệnh print()
# Hàm input() mặc định cho ra kết quả dạng chuỗi (string)

s = input("Nhập tên của bạn: ") # nhập biến s từ bàn phím
print("Chào ", s) # xuất biến s ra màn hình để đọc

a = int(input("a = ")) # a = 2; ép kiểu thành số nguyên dùng int
b = int(input("b = ")) # b = 3
print(a + b)

a = 2
b = float(input("b = ")) # b = 4
print(a + b)

# z1 = complex(input("nhập số phức z1: ")) # ép kiểu thành số phức
# z2 = complex(input("nhập số phức z2: ")) # ép kiểu thành số phức
z1 = 2                 + 3j
z2 = 1 - 2j
print(z1 + z2)


