# INPUT
numbers = input("Nhập các số nguyên: ")

# PROCESS
numbers = numbers.split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

# OUTPUT
print("Số lớn thứ hai là:", second_largest)