# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int (input('Введите количество монет: '))
count = 0
for i in range (n):
    m = int (input('Введите расположение монет (0 или 1): '))
    if m > 0:
        i+=1
    else:
        count+=1    
       
print ('Минимальное количество монет, которые нужно перевернуть: ', count)
