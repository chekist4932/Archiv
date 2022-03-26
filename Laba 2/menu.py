import time
import datetime
import body as b
def menu():
    check = input("1 - Поиск по логину.\n2 - Поиск по времени(получение всех ссесий, проходивших в указанное время).\n3 - Выход.\n>>\t")
    if check == "3":
        print("Работа программы завершена.")
        exit()
    elif check != "2" and check != "1":
        print("Неверный ввод, начнем заного.")
        menu()
    path = input("Введите путь:\n>>\t")
    try:
        file_log = open(path, "r")
    except FileNotFoundError:
        print("Неверный путь, начнем заного.")
        menu()
    else:
        if check == "1":
            log = input("Введите лог:\n>>\t")
            go = input(f"Выполнить поиск по логу: {log}?\n[Y/N]\n>>\t")
            if go.lower() == "y":
                b.body(file_log,log)
            elif go.lower() == "n":
                print("Начнем заного.")
                menu()
            else:
                print("Неверный ввод, начнем заного.")
                menu()
        elif check == "2":
            b.body_2(file_log)
def time_menu():
    try:
        date_s = [int(i) for i in input("Введите дату в формате: DD MM YYYY\n>>\t").split(" ")]
        time_s = [int(i) for i in input("Введите время в формате: HH MM SS\n>>\t").split(" ")]
        unixtime = time.mktime(
            datetime.datetime(date_s[2], date_s[1], date_s[0],time_s[0], time_s[1],
                              time_s[2]).timetuple())
    except Exception:
        print("Неверный ввод. Начнем заного.")
        time_menu()
    else:
        return unixtime
