import csv
import menu
from tqdm import tqdm
import time
import threading

class thread:
    def __init__(self, count):
        self.counter = [x+1 for x in range(count)]
        self.t1 = threading.Thread(target= load, args=[self.counter])

def load(counter):
    for i in tqdm(counter):
        time.sleep(0.1)

def body_2(file_log):
    time_dict = {}
    count = 0
    unixtime = menu.time_menu()
    point = thread(10)
    point.t1.start()
    next(csv.reader(file_log))
    for line in csv.reader(file_log):
        if int(unixtime) >= int(line[0]) and int(unixtime) <= int(line[1]):
            time_dict[count] = line
        count += 1
    point.t1.join()
    file_log.close()
    print("Поиск завершен.")
    if len(time_dict) != 0:
        print(f"Совпадений по указанному времени: {len(time_dict)}")
        save_res(time_dict)
    else:
        print("Совпадения по узащанному времени отсутствуют.")
        menu.menu()

def body(file_log,log):
    log_dict = {}
    count = 0
    list_black = ["2", "r", "f"]
    point = thread(10)
    point.t1.start()
    flag = True
    next(csv.reader(file_log))
    for line in csv.reader(file_log):
        if str(line[3]).find(log) != -1:
            for i in list_black:
                if str(line[3]).find(i) != -1:
                    flag = False
                    break
            if flag == True:
                log_dict[count] = line
        count += 1
    point.t1.join()
    file_log.close()
    print("Поиск завершен.")
    if len(log_dict) != 0:
        print(f"Совпадений по указаннмоу логу: {len(log_dict)}")
        save_res(log_dict)
    else:
        print("По указаному логу не найдено совпадений.")
        menu.menu()

def save_res(container):
    choice = input("Желаете сохраннить результаты поиска?(Сохранение проиходит в формате csv)\n[Y/N]\n>>\t")
    if choice.lower() == "y":
        file_name = input("Введите под каким именем необходимо создать файл(Допускаются только буквы и цифры):\n>>\t")
        if file_name.isalnum():
            try:
                file_save = open(f"{file_name}.csv", "x", newline="")
            except FileExistsError:
                print("Файл с таким названием уже существует. Начнем заного.")
                save_res(container)
            else:
                point2 = thread(5)
                writter = csv.writer(file_save)
                point2.t1.start()
                for line in container.values():
                    writter.writerow(line)
                point2.t1.join()
            print(f"Файл <{file_name}> создан, данные сохранены.")
            menu.menu()
        else:
            print("Неверный  ввод, начнем заного.")
            save_res(container)
    elif choice.lower() == "n":
        print("Начнем заного.")
        menu.menu()
    else:
        print("Неверный ввод, начнем заного.")
        save_res(container)