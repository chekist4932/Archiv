

def FP_Bin():
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


def FP_Mod():
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


def inFunc(mode):
    # INPUT
    while True:
        try:
            a = int(input("Введите основание (a):\n-\t"))
        except Exception:
            print("Invalid input. Try again!")
        else:
            while True:
                try:
                    n = int(input("Введите натуральный показатель (n):\n-\t"))
                except Exception:
                    print("Invalid input. Try again!")
                else:
                    if n < 0:
                        print("Invalid input. Try again!")
                        continue
                    else:
                        if mode == 1:
                            while True:
                                try:
                                    m = int(input("Введите значение модуля (m):\n-\t"))
                                except Exception:
                                    print("Invalid input. Try again!")
                                else:
                                    if m <= 0:
                                        print("Invalid input. Try again!")
                                        continue
                                    else:
                                        return a, n, m

                        else:
                            return a,n