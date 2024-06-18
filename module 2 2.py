first = 125
second = 65
third = 25
print(first)
print(second)
print(third)
if first == second == third:
    print('3')
if first == second != third or first != second == third or first == second != third:
    print('2')
else:
    print('0')

