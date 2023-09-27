def x_frequency(file_directory, found_letter, spis_sl, arr_range):

    sum = 0
    if spis_sl == 2:
        for letter in file_directory:
            for smth in letter:
                if found_letter in smth:
                    sum = sum + 1
        print(sum)
    else:
        letter_dictionary = dict.fromkeys(found_letter, 0)
        for letter in file_directory:
            for i in range(arr_range):
                letter_inspis = found_letter[i]
                for smth in letter:


                        if letter_inspis in smth:
                            letter_dictionary[letter_inspis] += 1
        print(letter_dictionary)
    return sum

path_to_file = open('test.txt')
y = int(input("Список или строка? 1/2: "))
if y == 1:
    n = int(input("Введите размер массива: "))
    x = []
    for i in range (n):
        i = input("Введите искомую букву: ")
        x.append(i)


else:
    x = input("Введите искомую букву: ")
    n = 0

x_frequency(path_to_file, x, y, n)