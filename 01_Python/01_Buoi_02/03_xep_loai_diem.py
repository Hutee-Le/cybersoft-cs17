# INPUT
score = float(input("Nhập điểm: "))

# PROCESS
if score < 0 or score > 10:
    result = "Điểm không hợp lệ"
elif score >= 9:
    result = "Xuất sắc"
elif score >= 8:
    result = "Giỏi"
elif score >= 6.5:
    result = "Khá"
elif score >= 5:
    result = "Trung bình"
else:
    result = "Yếu"

# OUTPUT
print(result)