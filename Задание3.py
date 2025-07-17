# Ввод натуральных чисел a и b 
a = int(input())
b = int(input())

# Нахождение и вывод четных чисел 
numbers = [str(i) for i in range(a, b + 1) if i % 2 == 0]
print(' '.join(numbers))