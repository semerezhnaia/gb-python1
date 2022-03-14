list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list_1):
    cnt = list_1[i]
    if cnt[-1].isdigit():
        if cnt.startswith(('+')):
            len_str = 3
        else:
            len_str = 2
        if len(cnt) < len_str:
            cnt = cnt.zfill(len_str)
            list_1[i] = cnt
    i += 1
print(" ".join(list_1))