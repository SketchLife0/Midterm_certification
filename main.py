def Add():
    id = None
    f = open("index.txt", "r+", encoding="UTF-8")
    while id == None:
        a = input('Введите id заметки: ')
        if a.isdigit():
            no_repeat = True
            for line in f:
                if a == line.strip():
                    print("ID уже существует")
                    no_repeat = False
                    break
            if no_repeat:
                f.writelines(a)
                f.close()
                id = a
        else:
            print('ID должен состоять из одних цифр')


def Del():
    pass


def Edit():
    pass


def Show():
    pass


def Help():
    print("""Добавить - Добавить новую заметку
    Удалить - Удалить существующую заметку
    Редактировать - Редактировать существующую заметку
    Показать - Показать список всех заметок
    Выход - Выйти из приложения""")


cont = True
action = ('Добавить', 'Удалить', "Редактировать", "Показать", 'Помощь', 'Выход')
while cont:
    query = None
    while query == None:
        a = input('Выберите действие: ').title()
        if a in action:
            query = a
        else:
            print("Действие некорректно")
    if query == action[0]:
        Add()
    elif query == action[1]:
        Del()
    elif query == action[2]:
        Edit()
    elif query == action[3]:
        Show()
    elif query == action[4]:
        Help()
    else:
        cont = False

# if __name__ == '__main__':
#     print_hi('PyCharm')
