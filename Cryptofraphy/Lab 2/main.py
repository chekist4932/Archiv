from PrimeNum import test_miller, Ferma, Solovey, jacobi
import EucAlg
from FastPower import FP_Bin, FP_Mod
import random
#dfdfd
'''
def func():
    print("ZeroFuck")


l = [func]

l[0]()

def FastPowerBin():
    a,n = inFunc(0)
    x = 1
    print(f"a - {a} || n - {n}")
    binar = []
    while n != 0:
        binar.append(n%2)
        n = n // 2
    binar.reverse()
    print(binar)

    for ind,i in enumerate(binar):
        x = x * (a ** (i * 2**(len(binar)-ind-1)))
    print(x)


def FastPowerMod():
    a, n, mod = inFunc(1)
    print(f"Osn - {a}, Power - {n}, Mod - {mod}")
    binar = []
    while n != 0:
        binar.append(n % 2)
        n = n // 2
    binar.reverse()
    print(binar)

    x = a**binar[0]

    for i in binar:
        y = (a ** 2) % mod
        if i == 1:
            x = (x*y) % mod
    print(x)
'''



def Modulo_comparison():
    while True:
        try:
            a = int(input("Input 'a' (ax==b(mod(m))):\na:\t"))
        except Exception:
            print("Eror input. Try again.")
            continue
        else:
            try:
                b = int(input("Input 'b' (ax==b(mod(m))):\nb:\t"))
            except Exception:
                print("Eror input. Try again.")
                continue
            else:
                while True:
                    try:
                        m = int(input("Input 'm' (ax==b(mod(m))):\nm:\t"))
                    except Exception:
                        print("Eror input. Try again.")
                        continue
                    else:
                        break
                break
        break
    nod,a_obr = EucAlg.EucAlg(True,m,a)
    out_list = []
    if b % nod != 0:
        print("Решений нет.")
    else:
        if nod != 1:
            a = a/nod
            b = b/nod
            m1 = m/nod
            pusto,a_obr = EucAlg.EucAlg(True,m1,a)
            out = b * a_obr % m
            out_list = [out+(x*m1) for x in range(nod)]
            #print(f"First X: {out}")
            print(f"All X: {out_list}")
        else:
            out = b*a_obr%m
            print(f"First X: {out}")







def NULL():
    print("NULL\n")

def PrimeNum():
    def check(prime, p):
        for i in range(t):
            if test_miller([p, random.randint(2, p - 2)]) is True:
                if i == t - 1:
                    return p
                else:
                    continue
            else:
                return False
    while True:
        try:
            k = int(input("Введите разрядность k искомого простого числа: "))
        except Exception:
            print("Error Input. Try again!\t")
            continue
        else:
            while True:
                try:
                    t = int(input("Введите параметр t>=1: "))
                except Exception:
                    print("Error Input (Isn't number). Try again!\t")
                    continue
                else:
                    if t<1:
                        print("Error Input (t < 1). Try again!\t")
                        continue
                    elif t >=1:
                        break
            break

    while True:
        p = 0
        prime = []
        for i in range(k):
            prime.append(round(random.random()))
        prime[0] = 1
        prime[-1] = 1
        for ind, i in enumerate(prime):
            p += i * (2 ** (len(prime) - ind - 1))
        # print(prime)
        #print(f"{p}\n")

        if check(prime,p) is False:
            continue
        else:
            break
    print(f"Prime number:\t\033[36m{p}\033[0m")


def menu():
    funcs = [EucAlg.EucAlg, [FP_Bin, FP_Mod], jacobi, [Ferma,Solovey], test_miller, PrimeNum, Modulo_comparison, NULL, NULL, NULL]
    while True:
        choose = input("Выберете алгоритм:"
                       "\n1\t-\tОбобщенный (расширенный) алгоритм Евклида."
                       "\n2\t-\tАлгоритм быстрого возведения в степень."
                       "\n3\t-\tВычисление символа Якоби."
                       "\n4\t-\tАлгоритмы проверки чисел на простоту."
                       "\n5\t-\tТест Миллера-Рабина."
                       "\n6\t-\tГенерация простого числа заданной размерности."
                       "\n7\t-\tРешение сравнения первой степени."
                       "\n8\t-\tРешение сравнения второй степени."
                       "\n9\t-\tРешение системы сравнений."
                       "\n10\t-\tПостроение конечного поля и реализация операций над данным полем."
                       "\n11\t-\tВыход.\n - ")
        try:
            int(choose)
        except Exception:
            print("Error Input. Try again!\t")
        else:
            if choose == "2":
                while True:
                    wh = input("1\t-\tЧерез двоичное представление числа."
                               "\n2\t-\tАлгоритм быстрого возведения в степень по модулю\n - ")

                    if wh == "1" or wh == "2":
                        funcs[int(choose)-1][int(wh)-1]()
                        break
                    else:
                        print("Error Input. Try again!\n")
                        continue
            elif choose == '3':
                pass
            elif choose == "4":
                pass
            elif choose == "5":
                funcs[int(choose)-1]([False])
            elif int(choose) <= 10 and int(choose) >= 0:
                funcs[int(choose)-1]()
            elif choose == "11":
                print("Bye, bro.")
                break
            else:
                print("Error Input. Try again!\n")



        """if choose == "1":
            EucAlg()
        elif choose == "2":
            wh = input("1\t-\tЧерез двоичное представление числа."
                       "\n2\t-\tАлгоритм быстрого возведения в степень по модулю\n - ")
            if wh == "1":
                FastPowerBin()
            elif wh == "2":
                FastPowerMod()
            else:
                print("Error Input. Try again!\t")
        #elif choose == "":
        #    pass
        #elif choose == "3":
        #    pass
        #elif choose == "4":
        #    pass
        #elif choose == "5":
        #    pass
        #elif choose == "6":
        #    pass
        #elif choose == "7":
        #    pass"""





menu()


