
import random
def step_generation(a, spis):
    generated_arr = []


    print(spis)
    for i in range(n):
        for q in range(i+1):
            generated_arr.append(spis[q])
        print(generated_arr)
        generated_arr.clear()


    return generated_arr

n = int(input("Введите размер массива: "))
arr = []
for i in range(n):
    i = random.randint(1, 99)
    arr.append(i)
step_generation(n, arr)