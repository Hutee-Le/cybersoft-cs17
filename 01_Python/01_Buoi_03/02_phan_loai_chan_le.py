# INPUT
numbers = input("Nhập các số nguyên: ")

# PROCESS
numbers = numbers.split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# OUTPUT
print("Các số chẵn:", even_numbers)
print("Các số lẻ:", odd_numbers)