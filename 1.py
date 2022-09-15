# Вычислить число c заданной точностью d
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal, ROUND_DOWN

number = Decimal(input('Введите число: '))
d = ''.join([str(1.), (((input('Задайте точность округления d: ')[::-1]).replace('.', '')).replace('10', ''))])
print(number.quantize(Decimal(d), ROUND_DOWN))