def EucAlg(flag = False,x=1,y=1):
    #INPUT
    if flag is False:
        while True:
            try:
                x = int(input("Input X and Y (X >= Y):\nX:\t"))
            except Exception:
                print("Eror input. Try again.")
                continue
            else:
                try:
                    y = int(input("\nY:\t"))
                except Exception:
                    print("Eror input. Try again.")
                    continue
                else:
                    if x < y:
                        print("Eror input. Try again.")
                        continue
                    else:
                        break
    else:
        if x >= y:
            pass
        elif x<y:
            mp = x
            x = y
            y = mp
    # BODY
    A = [0,1]
    B = [1,0]
    while y != 0:
        q = x // y
        r = x - q*y
        a = A[1] - q * A[0]
        b = B[1] - q*B[0]
        x = y
        y = r
        A[1] = A[0]
        A[0] = a
        B[1] = B[0]
        B[0] = b
        nod = x
        a = A[1]
        b = B[1]
    print(f'NOD : {nod} | a : {a} | b : {b}')

    if flag == True:
        return nod,b
    else:
        pass