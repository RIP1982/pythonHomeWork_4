# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите значение степени k: '))
coefficients = []

for i in range(0, k+1):
    coefficients.append(random.randint(0, 100))

if coefficients[-1] == 0:
    coefficients[-1] = random.randint(1, 100)
print(coefficients)

polynomial = ''
for i in range(len(coefficients)):
    if i == 0:
        if coefficients[i] != 0:
            polynomial = ' + ' + str(coefficients[i])
        else:
            polynomial = polynomial
    elif i ==1:
        if coefficients[i] != 0:
            polynomial = ' + ' + str(coefficients[i]) + '*x' + polynomial
        else:
            polynomial = polynomial
    elif 1 < i < k:
        if coefficients[i] != 0:
            polynomial = ' + ' + str(coefficients[i]) + '*x^'+str(i) + polynomial
        else:
            polynomial = polynomial
    else:
        polynomial = str(coefficients[i]) + '*x^' + str(i) + polynomial
print(f'{polynomial} = 0')