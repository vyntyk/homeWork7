from imp import impo
from exp import expp
from logger import log_info

def find():
    second_name = input('1. Введите фамилию человека: ')
    return second_name

def inpp():
    str_person = input('4. Введите данные нового сотрудника: ')
    return str_person

def start():
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    menu_number = int(input("Введите номер необходимого действия: "))
    while (menu_number  != 9):
        if menu_number  == 1:
            info = find()
            expp(info)
            log_info(info)
        elif menu_number  == 4:
            info = inpp()
            impo(info)
            log_info(info)
        print("\n" + "=" * 20)
        print("Выберите необходимое действие")
        print("1. Найти сотрудника")
        print("2. Сделать выборку сотрудников по должности")
        print("3. Сделать выборку сотрудников по зарплате")
        print("4. Добавить сотрудника")
        print("5. Удалить сотрудника")
        print("6. Обновить данные сотрудника")
        print("7. Экспортировать данные в формате json")
        print("8. Экспортировать данные в формате cmv")
        print("9. Закончить работу")
        menu_number = int(input("Введите номер необходимого действия: "))
