list_name = ['инженер конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for first_name in list_name:
    first_name_1 = first_name.split()[-1]
    first_name_1 = first_name_1.capitalize()
    print('Привет,', first_name_1, '! ')