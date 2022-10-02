class Contact:
    def __init__(self, last_name, first_name, middle_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.number = number
        self.email = email


    def get_info(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} {self.number} {self.email}'

def find(*data):
    for i in range(len(array)):
        count = 0
        global id
        for x in data:
            if len(data) == 1:
                if x in array[i].get_info().split():
                    print(array[i].get_info())
                    id = i
            if len(data) == 2:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 2:
                        print(array[i].get_info())
                        id = i
            if len(data) == 3:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 3:
                        print(array[i].get_info())
                        id = i
            if len(data) == 4:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 4:
                        print(array[i].get_info())
                        id = i
            if len(data) == 5:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 5:
                        print(array[i].get_info())
                        id = i


array = []


while True:
    Option = int(input('Варианты опций:\n 1-Файл \n 2-Поиск \n 3-Изменить \n 4-Выход \n '))

    if Option == 1:
        file = input('Название файла: ')
        with open(file, encoding='utf-8') as f:
            for line in f:
                p = str(line)
                t = p.replace(',', "")
                r = t.split()
                print(r)
                count = 0
                fn = '-'
                mn = '-'
                nb = '-'
                em = '-'
                for i in r:
                    if count == 4:
                        em = r[4]
                    elif count == 3:
                        if '+' in i:
                            nb = r[3]
                        elif '@' in i:
                            em = r[3]
                    elif count == 2:
                        if '+' in i:
                            nb = r[2]
                        elif '@' in i:
                            em = r[2]
                        else:
                            mn = r[2]
                    elif count == 1:
                        if '+' in i:
                            nb = r[1]
                        elif '@' in i:
                            em = r[1]
                        else:
                            fn = r[1]
                    else:
                        ln = r[0]
                    count += 1
                contact = Contact(ln, fn, mn, nb, em)
                array.append(contact)
        print('Файл загружен')
        continue
    elif Option == 2 or Option == 3:
        search = input('Введите данные в поисковик (Если нужны контакты, в которых не хватает данных введите "-"): \n')
        search_result = search.split()
        if len(search_result) == 1:
            result = find(search_result[0])
        if len(search_result) == 2:
            result = find(search_result[0], search_result[1])
        if len(search_result) == 3:
            result = find(search_result[0], search_result[1], search_result[2])
        if len(search_result) == 4:
            result = find(search_result[0], search_result[1], search_result[2],search_result[3])
        if len(search_result) == 5:
            result =  find(search_result[0], search_result[1], search_result[2], search_result[3], search_result[4])
        if Option == 3:
            Variants = int(input('Что хотите изменить:\n 1-Фамилию\n 2-Имя\n 3-Отчество\n 4-Номер\n 5-Почту\n '))
            if Variants == 1:
                array[id].last_name = input('Введите фамилию: ')
            elif Variants == 2:
                array[id].first_name = input("Введите имя: ")
            elif Variants == 3:
                array[id].middle_name = input("Введите отчество: ")
            elif Variants == 4:
                array[id].number = input("Введите номер: ")
            elif Variants == 5:
                array[id].email = input("Введите почту: ")


    elif Option == 4:
        break

