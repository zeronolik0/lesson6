# Ввод кол-ва чисел
n = int(input())
count = 0

# Подсчет и вывод кол-ва чисел = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        count += 1
print(count)