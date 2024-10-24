def reverse_number(n):
    reversed_num = 0
    while n > 0:
        last_digit = n % 10  # Извлекаем последнюю цифру
        reversed_num = reversed_num * 10 + last_digit  # Добавляем её в результат
        n = n // 10  # Убираем последнюю цифру из исходного числа
    return reversed_num

try:
    number = int(input("Введите число: "))
except ValueError:
    print("Введено некорректное значение!")
    exit()

print(reverse_number(number))