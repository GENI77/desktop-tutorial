pole1 = int(input('введите число от 3 до 20  '))
pole2 = []
for i in range(1, 21):
    for j in range(1, 21):
        if pole1 % (i + j) == 0 and i != j and i <= j:
            pole2.append(i)
            pole2.append(j)
print('resuit', pole2)
