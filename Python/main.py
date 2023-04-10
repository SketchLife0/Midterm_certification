from datetime import datetime


def Add():
    id = None
    f = open("index.csv", "r+", encoding="utf-8")
    while not id:
        a = input('Введите id заметки: ')
        if a.title() == "Выход":
            break
        if a.isdigit() and int(a) > 0:
            no_repeat = True
            for line in f:
                index = line.find(';')
                line = int(line[:index])
                if int(a) == line:
                    print("ID уже существует")
                    no_repeat = False
                    break
            if no_repeat:
                name = input("Введите заголовок заметки: ").upper()
                text = input("Введите текст заметки: ")
                f.write(f'{int(a)};{name};{text};{datetime.now()}\n')
                f.close()
                print('Запись добавлена')
                id = int(a)
        else:
            print('ID должен состоять из одних цифр и быть больше 0')


def Del():
    id = None
    while not id:
        a = input('Введите id заметки: ')
        if a.title() == "Выход":
            break
        if a.isdigit() and int(a) > 0:
            with open("index.csv", "r", encoding="UTF-8") as f:
                notes = f.readlines()
            object_lost = True
            for line in notes:
                index = line.find(';')
                index_int = int(line[:index])
                if int(a) == index_int:
                    notes.remove(line)
                    with open("index.csv", "w", encoding="UTF-8") as f:
                        f.writelines(notes)
                    print('Заметка удалена')
                    id = int(a)
                    object_lost = False
                    break
            if object_lost:
                print("Заметка отсутсвует")
        else:
            print('ID должен состоять из одних цифр и быть больше 0')


def Edit():
    id = None
    while not id:
        a = input('Введите id заметки: ')
        if a.title() == "Выход":
            break
        if a.isdigit() and int(a) > 0:
            with open("index.csv", "r", encoding="UTF-8") as f:
                notes = f.readlines()
            object_lost = True
            exit_code = False
            for i in range(len(notes)):
                index = notes[i].find(';')
                index_int = int(notes[i][:index])
                if int(a) == index_int:
                    edit_line = notes[i]
                    while True:
                        input_query = input('Хотите исправить заголовок или текст? ').title()
                        t = ['Заголовок', 'Текст']
                        if input_query in t:
                            correct = input('Введите новый заголовок: ' if input_query == t[0] else 'Введите новый текст: ').title()
                            second_index = edit_line.find(';', index + 1)
                            third_index = edit_line.find(';', second_index + 1)
                            index1 = index + 1 if input_query == t[0] else second_index + 1
                            index2 = second_index if input_query == t[0] else third_index
                            edit_line = edit_line.replace(edit_line[index1:index2], correct)
                            last_index = edit_line.rfind(';')
                            edit_line = edit_line.replace(edit_line[last_index + 1:], f"{datetime.now()}\n")
                            notes[i] = edit_line
                            break
                        elif input_query == 'Выход':
                            exit_code = True
                            break
                        else:
                            print('Ошибка: Некорректный ввод')
                    if exit_code:
                        break
                    with open("index.csv", "w", encoding="UTF-8") as f:
                        f.writelines(notes)
                    print('Заметка изменена')
                    id = int(a)
                    object_lost = False
                    break
            if exit_code:
                break
            if object_lost:
                print("Заметка отсутсвует")
        else:
            print('ID должен состоять из одних цифр и быть больше 0')


def Show():
    with open("index.csv", "r", encoding="UTF-8") as f:
        notes = f.readlines()
    type = input("Фильтрация по дате или нет? ").title()
    if type == "Да":
        date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        show_elem = 0
        for line in notes:
            last_index = line.rfind(';') + 1
            if line[last_index:last_index + 10] == date:
                show_elem += 1
                print(line.strip())
        if not show_elem:
            print("Записей нет")
    elif type == "Нет":
        choise = input("Показать все записи? ").title()
        if choise == 'Да':
            for line in notes:
                print(line.strip())
        elif choise == 'Нет':
            id_line = input("Введите id: ")
            if id_line.isdigit() and int(id_line) > 0:
                for line in notes:
                    elem = int(line[:line.find(';')])
                    if int(id_line) == elem:
                        print(line.strip())
                        break
            else:
                print("Записи нет")
        elif choise == 'Выход':
            return
        else:
            print('Ошибка: Некорректный ввод')
    elif type == "Выход":
        return
    else:
        print('Ошибка: Некорректный ввод')


def Help():
    print("""Добавить - Добавить новую заметку
    Удалить - Удалить существующую заметку
    Редактировать - Редактировать существующую заметку
    Показать - Показать список всех заметок
    Выход - Выйти из приложения""")


if __name__ == '__main__':
    action = ('Добавить', 'Удалить', "Редактировать", "Показать", 'Помощь', 'Выход')
    while True:
        query = None
        while query == None:
            job = input('Выберите действие: ').title()
            if job in action:
                query = job
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
            break
