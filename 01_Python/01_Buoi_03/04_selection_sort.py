# INPUT
numbers = input("Nhập các số nguyên: ")

# PROCESS
numbers = numbers.split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    temp = numbers[i]
    numbers[i] = numbers[min_index]
    numbers[min_index] = temp

# OUTPUT
print("Danh sách sau khi sắp xếp:", numbers)