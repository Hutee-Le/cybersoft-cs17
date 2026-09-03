# INPUT
numbers = input("Nhập các số nguyên: ")
threshold = int(input("Nhập ngưỡng: "))

# PROCESS
numbers = numbers.split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

result = []

for number in numbers:
    if number >= threshold:
        result.append(number)

# OUTPUT
print("Các số lớn hơn hoặc bằng ngưỡng:", result)