# INPUT
username = input("Nhập username: ")
password = input("Nhập password: ")

# PROCESS
if username == "admin" and password == "123456":
    result = "Đăng nhập thành công"
else:
    result = "Đăng nhập thất bại"

# OUTPUT
print(result)