count = 0
list_file = []
list_2 = []
list3 = []
with open("telegram_clear_data.txt", "r") as file:
    for i in file:
        list_file = i.split("\n")[0].split("|")
        list_2 = i.lstrip("|").strip().split("|")
        list3 = i.split("|")
        print(list_2)
        print(list_file)
        print(list3)
        print(i)
        count += 1
        if count == 7:
            break