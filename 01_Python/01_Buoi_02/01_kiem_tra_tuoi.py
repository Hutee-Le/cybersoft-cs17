# INPUT
age = int(input("Nhập tuổi: "))

# PROCESS
if age < 0:
    result = "Dữ liệu không hợp lệ"
elif age < 18:
    result = "Chưa đủ tuổi"
else:
    result = "Đủ tuổi"

# OUTPUT
print(result)