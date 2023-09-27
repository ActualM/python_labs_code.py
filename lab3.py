
import random
def new_generation(a, spis):
    generated_arr = []


    print(spis)
    generated_arr = [val for val in spis if pow(val, 2) < 30]
    print(generated_arr)


    return generated_arr

n = int(input("Введите размер массива: "))
arr = []
for i in range(n):
    i = random.randint(1, 10)
    arr.append(i)
new_generation(n, arr)