
def search(nickname, phone, check):
    with open ('telegram_clear_data.txt') as file:
        nickname_list = []
        a = 0
        proc = 10
        kolvo = 0
        print("Поиск начат...")
        if check == "phone":
            for line in file:
                line = line.lstrip('|').rstrip('|\n').split("|")
                if line[5] == nickname:
                    nickname_list.append(line)
                kolvo += 1

                if kolvo == 4500000:
                    print(f"Поиск выполнен на {proc}%...")
                    kolvo = 0
                    proc += 10
        elif check == "nick":
            for line in file:
                line = line.lstrip('|').rstrip('|\n').split("|")
                if line[5] == nickname:
                    nickname_list.append(line)
                kolvo += 1

                if kolvo == 4500000:
                    print(f"Поиск выполнен на {proc}%...")
                    kolvo = 0
                    proc += 10
        print ("Поиск завершен.\n")

    for i in nickname_list:
        print (f'Имя- {i[1]}\nФамилия- {i[2]}\nТелефон- {i[3]}\nID- {i[4]}\nНик- {i[5]}\n')
    print (f'Найдено совпадений - {len(nickname_list)}\n')

def mn():
    start = input(f"Начать поиск - 1\nВыйти - 2\n")
    if start == "1":
        n = input('Введите ник: ')
        search(n)
    if start == "2":
        exit()
    if start != "1" and start != "2":
        print('ОШИБКА! Неверный выбор.\nПопробуйте снова.\n')
        mn()

mn()





'''c = int(input((f"Поиск по нику - 1\nВыйти - 2"))
def mn(v):
    if v == 1:
        nick = input("Введите ник:")
        search(nick)
    elif v == 2:
        exit()
    elif v != 1 and v != 2:
        print("Неверный ввод, попробуйте снова.")
        mn(с)

mn(c)
'''