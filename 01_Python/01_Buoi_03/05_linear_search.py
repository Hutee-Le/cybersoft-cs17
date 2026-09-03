# INPUT
numbers = input("Nhập các số nguyên: ")
target = int(input("Nhập số cần tìm: "))

# PROCESS
numbers = numbers.split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

positions = []

for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i)

# OUTPUT
if len(positions) > 0:
    print("Các vị trí tìm thấy:", positions)
else:
    print("Không tìm thấy số", target)