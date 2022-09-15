# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

some_list = [int(i) for i in input().split(' ')]
new_list = set(some_list)
print(some_list)
print(new_list)
