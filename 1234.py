# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# 1 2 3 4 6 7 8 9



# a = [11, 12, 13, 14, 15, 17, 18, 21]
# res = [a[i]+1 for i in range(len(a)-1) if a[i+1] - 1 != a[i]]
# print(res)





# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
    
#     *Пример:*   
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.  
#  
# 
# a = [1, 5, 2, 3, 4, 6, 1, 7]
# res = [(a[i],a[i+1]) for i in range(len(a)-1) if a[i] < a[i+1]]
# print(res)
# 2-t реш
# a = [1, 5, 2, 3, 4, 6, 1, 7]
# res = [(a[i],a[i+1]) for i in range(len(a)-1) if a[i] < a[i+1]]
# print(res)


# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# абв Ура, пит


# text =  'абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв'
# lst = ' '.join(list(filter(lambda s: s.count('абв') < 1 ,text.split())))
# print(lst)


# s = list(map(int,'11 12 13 15 16 17 18 19 20'.split()))

# a = list(filter(lambda x : x[1]-x[0] == s[0], list(zip(range(len(s)),s))))

# print(a)

