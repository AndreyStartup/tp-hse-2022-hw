import Functions


array=[]
while True:
    Option = int(input('Выберите опцию:\n1-Файл\n2-Минимум\n3-Максимум\n4-Сумма\n5-Произведение\n6-Выход\n'))
    if Option == 1:
        Filename = input('Введите название файла: ')
        with open(Filename, 'r') as file:
            for line in file:
                array1 = line.split()
                for i in array1:
                    array.append(int(i))
    elif Option == 2:
        print("Минимальное: " + str(Functions._min(array)))
    elif Option == 3:
        print("Максимальное: " + str(Functions._max(array)))
    elif Option == 4:
        print("Сумма: " + str(Functions._sum(array)))
    elif Option == 5:
        print("Произведение: " + str(Functions._mult(array)))
    elif Option == 6:
        break
