
import random
def even_count(a):

    print(a)
    arr = []
    even = 0
    for i in range(a):
        i = random.randint(1, 99)
        arr.append(i)
        if i % 2 == 0:
            even += 1

    print(arr)
    print("Кол-во четных чисел в списке = ", even)
    return even

n = int(input("Введите размер массива: "))
even_count(n)