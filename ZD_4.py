# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('text.txt', 'w', encoding='utf-8') as data:
    tx = input('Введите строку: ')
    data.write(tx)


new_list = []
r = None
for d in tx:
    if d != r:
        new_list.append(d)
        new_list.append(str(1))
        r = d
    else:
        new_list[-1] = str(int(new_list[-1]) + 1)
print("".join(new_list))

with open('text2.txt', 'w', encoding='utf-8') as data:
    data.write("".join(new_list))
