# Создать контакт
def add_contact():
    book = open("phone_book.txt", "a+", encoding="utf-8")
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    note = input("Введите заметку: ")
    book.write(f"{name},{number},{note}\n")
    book.close()
    print(f"{name}, {number}, {note} добавлен в список контактов")


# Показать все контакты
def all_contacts():
    with open("phone_book.txt", "r+", encoding="utf-8") as book:
        return book.readlines()


# Проверить контакты на наличие 
def not_contact():
    print("Контакт не существует. Желаете его создать?")
    add = input("Введите 1 если Да, 2 - если Нет ->  ").lower()
    if add == "1":
        add_contact()


# Сортировать контакты в алфавитном порядке
def sort_book():
    contact_list = [contact for contact in all_contacts()]
    contact_list.sort()
    file = open("phone_book.txt", "w", encoding="utf-8")
    for contacts in contact_list:
        file.write(str(contacts))
    file.close()


# Поиск контактов
def find_contact():
    book = all_contacts()
    flag = False
    if ( what := input("Начнём поиск?\nУкажите номер из списка: 1-ФИО, 2-Номер телефона, 3-Заметка -> ")) == "1":
        name = input("Введите имя: ")
        for line, contact in enumerate(book):
            if name in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    elif what == "2":
        number = input("Введите номер телефона: ")
        for line, contact in enumerate(book):
            if number in contact.lower().split(",")[1]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    elif what == "3":
        note = input("Введите заметку: ")
        for line, contact in enumerate(book):
            if note in contact.lower().split(",")[2]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if not flag:
            not_contact()
    else:
        print("Выберите 1, 2 или 3")
        find_contact()


# Редактирование контакта
def change_name():
    book = all_contacts()
    flag = False
    if (
        what := input(
            "Что будем менять?\nУкажите номер из списка: 1-фио, 2-номер, 3-комментарий? → "
        )
    ) == "1":
        name = input("Кого будем менять: ").lower()
        for line, contact in enumerate(book):
            if name in contact.lower().split(",")[0]:
                print("id =", line, *contact.split(","), end="")

                flag = True
        if flag:
            name_id = int(input("Введите № id редактируемого контакта: "))
            new_name = input("Введите новое имя контакта: ")
            change_contact = book[name_id]
            book[
                name_id
            ] = f'{new_name},{change_contact.split(",")[1]},{change_contact.split(",")[2]}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()

    elif what == "2":
        number = input("Введите номер: ").lower()
        for line, contact in enumerate(book):
            if number in contact.lower().split(",")[1]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("Введите № id редактируемого контакта: "))
            number = input("Введите новый номер телефона: ")
            change_contact = book[name_id]
            book[
                name_id
            ] = f'{change_contact.split(",")[0]},{number},{change_contact.split(",")[2]}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()

    elif what == "3":
        note = input("Введите комментарий: ").lower()
        for line, contact in enumerate(book):
            if note in contact.lower().split(",")[2]:
                print("id =", line, *contact.split(","), end="")
                flag = True
        if flag:
            name_id = int(input("Введите № id редактируемого контакта: "))
            note = input("Введите новую заметку для контакта: ")
            change_contact = book[name_id]
            book[
                name_id
            ] = f'{change_contact.split(",")[0]},{change_contact.split(",")[2]},{note}'
            file = open("phone_book.txt", "w", encoding="utf-8")
            for contacts in book:
                file.write(str(contacts))
            file.close()
        else:
            not_contact()
    else:
        print("Нужно выбрать 1, 2 или 3")
        change_name()
    content()


# Удалить контакт
def delete_contact():
    book = all_contacts()
    flag = False
    name = input("Выберите контакт для удаления: ").lower()
    for line, contact in enumerate(book):
        if name in contact.lower().split(",")[0]:
            print("id =", line, *contact.split(","), end="")
            flag = True
    if flag:
        name_id = int(input("Введите № id удаляемого контакта: → "))
        print(f"{book.pop(name_id)} удален.")
        file = open("phone_book.txt", "w", encoding="utf-8")
        for contacts in book:
            file.write(str(contacts))
        file.close()
    else:
        not_contact()


# Открыть Избранное
def open_favorite_contacts():
    with open("favorite_contacts.txt", "r+", encoding="utf-8") as book:
        return book.readlines()


# Добавить в Избранное
def add_favorite_contact():
    book = all_contacts()
    if not book:
        print('Список Избранного пуст.')
    else:
        print("\nСписок всех контактов:")
        for line, contact in enumerate(book):
            print("id =", line, *contact.split(","), end="")

        point = int(input("\nВведите id контакта → "))

        selected_contact = book[point]        
        favorite_file = open("favorite_contacts.txt", "a+", encoding="utf-8")
        favorite_file.write(f"{selected_contact}\n")
        favorite_file.close()
        print(f"Контакт добавлен в избранное")

# Работа справочника
def content():
    with open("phone_book.txt", "a+", encoding="utf-8") as f:
        while True:
            menu = {
                1: "1 → Показать все контакты",
                2: "2 → Создать новый контакт",
                3: "3 → Поиск контакта",
                4: "4 → Редактировать контакт",
                5: "5 → Удалить контакт",
                6: "6 → Добавить в Избранное",
                7: "7 → Открыть Избранное",
                0: "0 → Выйти из программы",
                99: ("*" * 26),
                    }
            print("\n", "*" * 7, "Содержание", "*" * 7)
            print(*menu.values(), sep="\n")
            point = input("\nВведите № пункта → ")
            if point == "1":  # Показать все контакты
                book = all_contacts()
                if not book:
                    print('Список пуст.')
                else:
                    print("\nСписок всех контактов:")
                    print(*book, sep="")  # Вывод списка контактов по алфавиту

            elif point == "2":  # Создание нового контакта
                add_contact()

            elif point == "3":  # Поиск контакта
                find_contact()
                
            elif point == "4":  # Редактирование контакта
                change_name()
                
            elif point == "5":  # Удаление контакта
                delete_contact()
            
            elif point == "6": # Добавить в избранное
                add_favorite_contact()

            elif point == "7": # Открыть Избранное
                favorite_book = open_favorite_contacts()
                if not favorite_book:
                    print('Избранных контактов нет.')
                else:
                    print("\nСписок Избранных контактов:")
                    print(*favorite_book, sep="")  # Вывод списка Избранного по алфавиту

            elif point == "0":  # Выход из программы
                sort_book()  # Сортировка контактов перед выходом
                break
            else:
                print("Ошибка ввода. Выберите один из пунктов")


# Запуск программы
if __name__ == "__main__":
    content()