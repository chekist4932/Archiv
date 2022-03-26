
import menu
menu.menu()
"""
import os
from time import time
now = time()
nickname = " "
fls = list(os.listdir(path="C:/Users/georg/Desktop/Laba1"))
file_name = ""
for i in fls:
    if str(i).find("telegram_clear_data.txt") != -1:
        file_name = str(i)
file_data = open(f"{file_name}","r", encoding="windows-1251")
data_base_name = {}
count_proc = 1
count_perc = 20
count_res = 1
line = file_data.readline()
print("Выполняется поиск...")
for i in file_data:
    print(i)
    if count_proc == 9:
        break
print(f"Поиск завершен! Найдено соппадений: {len(data_base_name.keys())}")
file_data.close()
print("-"*40)
for i in data_base_name.keys():
    print(f"\033[1mСовпадение: {i}")
    print(
        f"\033[1mName: {data_base_name[i][1]}\nFname: {data_base_name[i][2]}\nPhoneNumber: {data_base_name[i][3]}\nId: {data_base_name[i][4]}\nNickname: {data_base_name[i][5]}\nServId: {data_base_name[i][6]}")
    print("-" * 40)
print(f"Программа завершается. Время работы программы: {round(time() - now,1)} сек")

file_name = "telegram_clear_data.txt"
file_data = open(f"{file_name}","r", encoding="windows-1251")
c = 0
for i in file_data:
    print(i)
    c += 1
    if c == 20:
        break
"""
