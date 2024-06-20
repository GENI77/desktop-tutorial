first = input('введите число')
second = input('введите число')
third = input('введите число')
print(first)
print(second)
print(third)
if first == second == third:
    print('3')
if first == second != third or first != second == third or first == second != third:
    print('2')
if first != second != third:
    print('0')


