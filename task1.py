# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 10, 3, 4, 5]

sum_numbers = 0

for i in range(len(my_list)):
    if i % 2 != 0:
        sum_numbers += my_list[i]
print(f'Сумма элементов на нечетных позициях равнa {sum_numbers}')
