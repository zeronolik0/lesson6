# Ввод натурального числа x
x = int(input())
count = 0

# Подсчет и вывод кол-ва делителей x
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        count += 2 if i != x // i else 1

print("Количество натуральных делителей:", count)