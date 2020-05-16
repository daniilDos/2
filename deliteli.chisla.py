number = int(input('Введите число:'))
finish = []
for q in range(number, 0, -1):
    if number % q == 0:
        finish.append(q)
print(f'Делители {number}: {finish}')
