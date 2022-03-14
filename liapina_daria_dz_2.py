list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов.']
s = 0
while s < len(list_1):
    count = list_1[s]
    if count[-1].isdigit():
        if count.startswith(('+')):
            len_str = 3
        else:
            len_str = 2
        if len(count) < len_str:
            count = count.zfill(len_str)
            list_1[s] = count
    s += 1
print(" ".join(list_1))