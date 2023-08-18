#Телефонный справочник.

def shou_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по имени или фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Редактировать данные абонента в справочнике\n"
          "6. Удалить абонента из справочника\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input("Ваш выбор: "))
    return choice

def read_csv(filename):
    data = list()
    faelds = ['фамилия', 'имя', 'телефон', 'описание']
    with open(filename, 'r', encoding='utf-8') as guide:
        for line in guide:
            a = dict(zip(faelds, line.strip(' ').split(',')))
            data.append(a)
    return data

def work_with_phonebook():
    choice = shou_menu()
    phone_book = read_csv('phon2.csv')
    while (choice != 8):
        if choice == 1:
            for i in phone_book:
                print(i)
            choice = shou_menu()
        elif choice == 2:
            name = input('Введите имя или фамилию: ')
            for i in phone_book:
                if i['имя'] == name or i['фамилия'] == name:
                    print(i)
            choice = shou_menu()
        elif choice == 3:
            namber = input('Введите номер телефона: ')
            for i in phone_book:
                if i['телефон'] == namber:
                    print(i)
            choice = shou_menu()
        elif choice == 4:
            subscriber = input('Введите: фамилию, имя, телефон, описание абонента.')
            faelds = ['фамилия', 'имя', 'телефон', 'описание']
            dict_1 = dict(zip(faelds, subscriber.strip(' ').split(',')))
            #for i in phone_book:
            if phone_book != dict_1:
                phone_book.append(dict_1)
                for i in phone_book:
                    print(i)
            choice = shou_menu()
        elif choice == 5:
            subscriber_del = input('Укажите какие либо данные удаляемого абонента: ')
            a = subscriber_del
            for i in phone_book:
                if i['фамилия'] == a or i['имя'] == a or i['телефон'] == a or i['описание'] == a:
                    phone_book.remove(i)
                    for i in phone_book:
                        print(i)
            choice = shou_menu()
        elif choice == 6:
            data_del = input('Укажите данные которые необходимо изменить: ')
            data_add = input('Укажите на что нужно изменить данные: ')
            for i in phone_book:
                if i['фамилия'] == data_del:
                    i['фамилия'] = data_add
                elif i['имя'] == data_del:
                    i['имя'] = data_add
                elif i['телефон'] == data_del: 
                    i['телефон'] = data_add
                elif i['описание'] == data_del:
                    i['описание'] = data_add
            for i in phone_book:
                print(i)
            choice = shou_menu()
        elif choice == 7:
            list_1 = list()
            for i in (phone_book):
                for key, value in i.items():
                    list_1.append(value)
            print(list_1)
            with open('csv_save.csv', 'w') as data:
                data.writelines(list_1)
            #data.close
            choice = shou_menu()
    
    if choice == 8:
        print('Завершение работы.')
                
work_with_phonebook()  
                          
                
                
            
                    
            
                

            



