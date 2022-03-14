list_1 = [57.8, 46.51, 97, 52.67, 40.6, 71.06, 12.3, 65, 57.64, 57.21, 67]
print('Список цен: ')
for price in list_1:
    print(int(price), 'руб.', int(price * 100 % 100), 'коп.', end = ', ')
# не получается добавить нули в копейки...
print('\n\nОтсортированный список по возрастанию: ')
list_1.sort()
print(list_1)
print('\n\nОтсортированный список по убыванию: ')
list_2 = sorted(list_1, reverse = True)
print(list_2)
print('\n\nСписок 5-ти самых дорогих товаров: ')
print(list_1[-5:])
