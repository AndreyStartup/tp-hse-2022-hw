class Contact:
    def __init__(self, last_name, first_name, middle_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.number = number
        self.email = email


    def get_info(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} {self.number} {self.email}'

def find_contact(data):
    for i in range(len(array)):
        count = 0
        global id
        search_array = data.split()
        for x in search_array:
            if len(search_array) == 1:
                if x in array[i].get_info().split():
                    print(array[i].get_info())
                    id = i
            if len(search_array) == 2:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 2:
                        print(array[i].get_info())
                        id = i
            if len(search_array) == 3:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 3:
                        print(array[i].get_info())
                        id = i
            if len(search_array) == 4:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 4:
                        print(array[i].get_info())
                        id = i
            if len(search_array) == 5:
                if x in array[i].get_info().split():
                    count +=1
                    if count == 5:
                        print(array[i].get_info())
                        id = i


array = []


while True:
    Option = int(input('Варианты опций:\n 1-Файл \n 2-Поиск \n 3-Изменить \n 4-Выход \n '))

    if Option == 1:
        Filename = input('Название файла: ')
        with open(Filename, encoding='utf-8') as file:
            for line in file:
                str_line = str(line)
                commas = str_line.replace(',', "")
                full_contact_data = commas.split()
                print(full_contact_data)
                count = 0
                first_name = '-'
                middle_name = '-'
                number = '-'
                email = '-'
                for i in full_contact_data:
                    if count == 4:
                        email = full_contact_data[4]
                    elif count == 3:
                        if '+' in i:
                            number = full_contact_data[3]
                        elif '@' in i:
                            email = full_contact_data[3]
                    elif count == 2:
                        if '+' in i:
                            number = full_contact_data[2]
                        elif '@' in i:
                            email = full_contact_data[2]
                        else:
                            middle_name = full_contact_data[2]
                    elif count == 1:
                        if '+' in i:
                            number = full_contact_data[1]
                        elif '@' in i:
                            email = full_contact_data[1]
                        else:
                            first_name = full_contact_data[1]
                    else:
                        last_name = full_contact_data[0]
                    count += 1
                contact = Contact(last_name, first_name, middle_name, number, email)
                array.append(contact)
        print('Файл загружен')
        continue
    elif Option == 2 or Option == 3:
        search = input('Введите данные в поисковик (Если нужны контакты, в которых не хватает данных введите "-"): \n')
        find_contact(search)
        if Option == 3:
            Variants = int(input('Что хотите изменить:\n 1-Фамилию\n 2-Имя\n 3-Отчество\n 4-Номер\n 5-Почту\n 6-Отмена\n '))
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
            elif Variants == 6:
                continue


    elif Option == 4:
        break

