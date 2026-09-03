# INPUT
number = float(input("Nhập một số: "))

# PROCESS
if number > 0:
    result = "Số dương"
elif number < 0:
    result = "Số âm"
else:
    result = "Bằng 0"

# OUTPUT
print(result)