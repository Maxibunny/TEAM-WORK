print('Введи 2 числа')

x = int(input('x = '))
y = int(input('y = '))

if x == y:
    print('Нет Min и Max >>>', x,'=',y)
else:
    if x > y:
        Max = x
        Min = y
    else:
        Max = y
        Min = x

    print('Max -->', Max)
    print('Min -->', Min)
