import random

def menu():
    while True:
        choose = input("Выберете тест:\n1\t-\tТест Ферма.\n2\t-\tТест Соловэя-Штрассена.\n3\t-\tВыход.\n - ")
        if choose == "1":
            for i in range(20):
                Ferma()
        elif choose == "2":
            for i in range(20):
                Solovey()
                input("PAUSE - MENU")
        elif choose == "3":
            print("Bye, bro.")
            break
        else:
            print("Error Input. Try again!\t")

def Solovey():
    num2 = input_func()
    lic = [x for x in range(2, num2 - 1)]
    cheker = list()
    out = list()
    for i in range(1000):
        a_num = random.choice(lic)
        #print(random_num)
        #print(num2)
        #power = ((num2 - 1)/2)
        power = int((num2 - 1)/2)
        r = (a_num**power) % num2
        #print(r)
        #input("PAUSE")
        if cheker.count([a_num, r]) < 1:
            cheker.append([a_num, r])

    flag = True
    for i in cheker:
        if i[1] != 1 and i[1] != (num2 - 1):
            flag = False
        else:
            out.append(i)
    if flag is True:
        count = 0
        for i in out:
            if i[1] == jacobi(i[0],num2) % num2:
                count += 1

        if count == len(out):

            print(f"\tЧисло n, вероятно простое. Прошло тест по кол-ву оснований: {len(out)}")
            print(out)
        else:
            print(f"\tЧисло составное. Прошло тест по кол-ву оснований:  {len(out)}")

    else:
        print(f"\tЧисло составное. Прошло тест по кол-ву оснований:  {len(out)}")
        print(out)







def input_func():
    while True:
        try:
            numb = int(input("Нечетное целое число >=5:\t"))
        except Exception:
            print("Error Input. Try again!\t")
            continue
        else:
            if numb >= 5 and numb % 2 == 1:
                return numb
            else:
                print("Error Input. Number < 5 Try again!\t")
                continue
# Тест Ферма
def Ferma():
    num = input_func()
    lic = [x for x in range(2,num-1)]
    cheker = list()
    out = list()
    for i in range(1000):
        random_num = random.choice(lic)
        r = (random_num**(num-1)) % num
        if cheker.count([random_num,r]) < 1:
            cheker.append([random_num,r])
    flag = True
    for i in cheker:
        if i[1] != 1:
            flag = False
        elif i[1] == 1:
            out.append(i)
    if flag is True:

        print(f"\tЧисло n, вероятно простое. Прошло тест по кол-ву оснований: {len(out)}")
        print(out)

    else:
        print(f"\tЧисло составное. Прошло тест по кол-ву оснований:  {len(out)}")

        print(out)
        print(len(cheker))


def jacobi(rnum, num):
    if rnum is None and num is None:
        input("STOPE PACAN")
    lic = [(x*rnum)%num for x in range(1, int((num - 1)/2) + 1)]
    #print(lic)
    count = 0
    for i in lic:
        if i > num/2:
            count+=1
    #print(count)
    return (-1)**count

def jacobi_2(a_num, num, g_in):
    g = g_in
    s = 0
    k = 0
    a1 = 0
    if a_num == 0:
        return 0
    elif a_num == 1:
        return g
    else:
        # Представл в виде a = a1 * 2^k, где а1 - нечет
        count = 0
        mp = a_num
        while True:
            if mp % 2 == 0:
                count += 1
                mp = mp // 2

            elif mp % 2 == 1:
                k = count
                a1 = mp
                break
        print(f"{a1} -- {k}")
        #input()
        if k % 2 == 0:
            s = 1
        elif k % 2 == 1:
            if num % 8 == 1 or num % 8 == 7:
                return 1
            elif num % 8 == 3 or num % 8 == 5:
                return -1
        if a1 == 1:
            return g*s
        if num % 4 == 3 and a1 % 4 == 3:
            return s * -1
        if a_num % a1 == num % a1:
            jacobi_2(a_num,a1, g*s)


def test(a_num):
    count = 0
    mp = a_num
    while True:
        if mp % 2 == 0:
            count += 1
            mp = mp // 2

        elif mp % 2 == 1:
            k = count
            a1 = mp
            print(f"Степень - 2^{k}. a1 - {a1}")
            break




if __name__ == '__main__':
    #menu
    print(jacobi(5,13))
    #print(jacobi_2(5,13,1))
    #test(8)
    #print(jacobi_2(5,13,1))
    #input("PAUSE")
