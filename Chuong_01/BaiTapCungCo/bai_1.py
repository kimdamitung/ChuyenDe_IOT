print("Cách 1: không dùng hàm con")
a = int(input("Nhập hệ số thứ nhất: "))
b = int(input("Nhập hệ số thứ hai : "))
print(f"Tổng của {a} + {b} = {a + b}")
print("Cách 2: sử dụng hàm con")
def sum(a, b):
	return a + b
x = int(input("Nhập hệ số thứ nhất: "))
y = int(input("Nhập hệ số thứ hai : "))
print(f"Tổng của {x} + {y} = {sum(x, y)}")
# f"" là kiểu formatted string line: nhúng biểu thức trực tiếp bên trong chuỗi thông qua {}