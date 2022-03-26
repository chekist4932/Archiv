import body as b
def menu():
    check = input("1 - Поиск по никнейму\n2 - Выход\n")
    if check == "1":
        nickname = input("Введите никнейм\n")
        a = input(f"Выполнить поиск по никнейму: {nickname}?\n[Y/N]\n")
        if a.lower() == "y":
            data_dict, now_time = b.body(nickname)
            b.input_dict(data_dict, now_time)
        elif a.lower() == "n":
            menu()
        else:
            print("Неверный ввод, попробуй еще!")
            menu()
    elif check == "2":
        print("Программа завершена.")
    else:
        print("Неверный ввод, попробуй еще!")
        menu()
