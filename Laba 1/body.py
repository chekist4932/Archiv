import os
from time import time
def body(nickname: str):
    now = time()
    fls = list(os.listdir(path="C:/Users/georg/Desktop/Laba1"))
    file_name = ""
    for i in fls:
        if str(i).find("telegram_clear_data.txt") != -1:
            file_name = str(i)
    file_data = open(f"{file_name}", "r", encoding="windows-1251")
    data_base_name = {}
    count_proc = 1
    count_perc = 20
    count_res = 1
    print("Выполняется поиск...")
    try:
        for i in file_data:
            if count_proc % 8200000 == 0:
                print(f"Поиск выполнен на {count_perc} %")
                count_perc += 20
                count_proc = 1
            if i.find(nickname) != -1:
                if i.count("|") == 7 and len(nickname) == len(i.split("|")[6]):
                    data_base_name[count_res] = i.lstrip("|").strip().split("|")
                    b = choice_pp(count_res)
                    count_res += 1
                    if b == -1:
                        break
                    else:
                        pass
                count_proc += 1

            else:
                count_proc += 1
            if len(data_base_name) == 1000:
                break
    except MemoryError:
        print("На вашем устройстве недостаточно памяти. Вывожу результаты поиска.")
    file_data.close()
    print(f"Поиск завершен! Найдено соппадений: {len(data_base_name.keys())}")
    return data_base_name, now

def input_dict(data: dict, now):
    print("-" * 40)
    for i in data.keys():
        print(f"\033[1mСовпадение: {i}")
        print(
            f"\033[1mName: {data[i][1]}\nFname: {data[i][2]}\nPhoneNumber: {data[i][3]}\nId: {data[i][4]}\nNickname: {data[i][5]}\nServId: {data[i][6]}")
        print("-" * 40)
    print(f"Программа завершается. Время работы программы: {round(time() - now, 1)} сек")

def choice_pp(count_res):
    choice = input(f"Надено {count_res} совпадение, желаете продолжить? [Y/N]")
    if choice.lower() == "y":
        pass
    elif choice.lower() == 'n':
        return -1
    else:
        print("Неверный ввод")
        choice_pp(count_res)