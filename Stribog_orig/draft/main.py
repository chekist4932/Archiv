# Хеш-функция ГОСТ Р 34.11-2012 "Стрибог"
import math
import LPS


def stribog():
    while True:
        choose = input("1.\t512 bit\n2.\t256 bit\n-\t")
        if choose == "1":
            Layout = 512
            break
        elif choose == "2":
            Layout = 256
            break
        else:
            print("Input error. Try again.")
            continue

    while True:
        choose = input("Iput:\n1.\tFile\n2.\tKeyboard\n-\t")
        if choose == "1":
            while True:
                print("\nInput mess in mes.txt")
                mp_choose = input("1.\tGo\n-\t")
                if mp_choose == "1":
                    try:
                        file = open("mes.txt", encoding="utf-8")
                        mes = file.read()
                        file.close()
                        Msg = bin(int.from_bytes(mes.encode("utf-8"), "little"))[2:].zfill(
                            (len(mes.encode("utf-8").hex()) // 2) * 8)
                    except Exception as err:
                        print(err)
                        continue
                    else:
                        break
                else:
                    print("Input error. Try again.")
                    continue
            break
        elif choose == "2":
            mes = input("\nInput your message:\n-\t")
            Msg = bin(int.from_bytes(mes.encode("utf-8"), "little"))[2:].zfill(
                (len(mes.encode("utf-8").hex()) // 2) * 8)
            break
        else:
            print("Input error. Try again.")
            continue

    if Layout == 512:
        hash_ = "0" * 512

    elif Layout == 256:
        hash_ = "00000001" * 64

    N_vector = "0" * 512
    E_vector = "0" * 512

    # print(Msg)

    while True:
        if len(Msg) < 512:
            Len_Msg = len(Msg)
            Msg = ("0" * (511 - Len_Msg)) + '1' + Msg

            # print(LPS.bin_to_hex(Msg))

            hash_ = LPS.g_N(hash_, Msg, N_vector)

            # print(LPS.bin_to_hex(hash_))

            N_vector = bin((int(N_vector, 2) + Len_Msg) % 2 ** 512)[2:].zfill(512)
            E_vector = bin((int(E_vector, 2) + int(Msg, 2)) % 2 ** 512)[2:].zfill(512)

            # print(f"N - {N_vector}")
            # print(f"E - {E_vector}")
            # input("wait...")

            Zero_vector = "0" * 512
            # print(f"First hash - {LPS.bin_to_hex(hash_)}")
            hash_ = LPS.g_N(hash_, N_vector, Zero_vector)
            # print(f"Second hash - {LPS.bin_to_hex(hash_)}")


            if Layout == 512:
                hash_ = LPS.g_N(hash_, E_vector, Zero_vector)
            elif Layout == 256:
                hash_ = LPS.g_N(hash_, E_vector, Zero_vector)[:256]

            num = int(hash_, 2)
            hash_ = num.to_bytes(math.ceil(math.log2(num) / 8), 'little').hex()
            print(hash_)
            break
        else:
            Mp_Msg = Msg
            mod_pr = len(Msg)
            Msg = Mp_Msg[mod_pr - 512:]
            hash_ = LPS.g_N(hash_, Msg, N_vector)
            N_vector = bin((int(N_vector, 2) + 512) % 2 ** 512)[2:].zfill(512)
            E_vector = bin((int(E_vector, 2) + int(Msg, 2)) % 2 ** 512)[2:].zfill(512)
            Msg = Mp_Msg[:mod_pr - 512]


stribog()
