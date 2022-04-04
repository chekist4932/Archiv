import random

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




def test_miller(flag:list):
    # INPUT
    if flag[0] is False:
        n = input_func()
        a = random.randint(2, n - 2)
    else:
        #("GEN PRIME")
        n = flag[0]
        a = flag[1]
    # BODY
    exp = n - 1

    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        if flag[0] is False:
            print("Число вероятно простое.")
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            if flag[0] is False:
             print("Число вероятно простое.")
            return True
        exp <<= 1
    if flag[0] is False:
     print("Число вероятно составное.")
    return False


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
    lic = [(x*rnum)%num for x in range(1, int((num - 1)/2) + 1)]
    #print(lic)
    count = 0
    for i in lic:
        if i > num/2:
            count+=1
    #print(count)
    return (-1)**count




