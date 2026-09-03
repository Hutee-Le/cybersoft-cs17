# INPUT
salary = 15_000_000
sale = float(input("Nhập doanh thu: "))

# PROCESS
if sale > 100_000_000:
    salary = salary * 1.1
    result = salary
elif sale >= 80_000_000 and sale <= 100_000_000:
    result = salary
elif sale >= 10_000_000 and sale < 80_000_000:
    salary = salary * 0.9
    result = salary
else:
    result = "Cần xử lý theo quy định doanh nghiệp"

# OUTPUT
print(result)