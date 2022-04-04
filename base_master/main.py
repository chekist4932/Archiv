from datetime import datetime

base_32 = [['00000', 'A'], ['00001', 'B'], ['00010', 'C'], ['00011', 'D'], ['00100', 'E'], ['00101', 'F'],
           ['00110', 'G'], ['00111', 'H'], ['01000', 'I'], ['01001', 'J'], ['01010', 'K'], ['01011', 'L'],
           ['01100', 'M'], ['01101', 'N'], ['01110', 'O'], ['01111', 'P'], ['10000', 'Q'], ['10001', 'R'],
           ['10010', 'S'], ['10011', 'T'], ['10100', 'U'], ['10101', 'V'], ['10110', 'W'], ['10111', 'X'],
           ['11000', 'Y'], ['11001', 'Z'], ['11010', '2'], ['11011', '3'], ['11100', '4'], ['11101', '5'],
           ['11110', '6'], ['11111', '7']]

base_64 = [['000000', 'A'], ['000001', 'B'], ['000010', 'C'], ['000011', 'D'], ['000100', 'E'], ['000101', 'F'],
           ['000110', 'G'], ['000111', 'H'], ['001000', 'I'], ['001001', 'J'], ['001010', 'K'], ['001011', 'L'],
           ['001100', 'M'], ['001101', 'N'], ['001110', 'O'], ['001111', 'P'], ['010000', 'Q'], ['010001', 'R'],
           ['010010', 'S'], ['010011', 'T'], ['010100', 'U'], ['010101', 'V'], ['010110', 'W'], ['010111', 'X'],
           ['011000', 'Y'], ['011001', 'Z'], ['011010', 'a'], ['011011', 'b'], ['011100', 'c'], ['011101', 'd'],
           ['011110', 'e'], ['011111', 'f'], ['100000', 'g'], ['100001', 'h'], ['100010', 'i'], ['100011', 'j'],
           ['100100', 'k'], ['100101', 'l'], ['100110', 'm'], ['100111', 'n'], ['101000', 'o'], ['101001', 'p'],
           ['101010', 'q'], ['101011', 'r'], ['101100', 's'], ['101101', 't'], ['101110', 'u'], ['101111', 'v'],
           ['110000', 'w'], ['110001', 'x'], ['110010', 'y'], ['110011', 'z'], ['110100', '0'], ['110101', '1'],
           ['110110', '2'], ['110111', '3'], ['111000', '4'], ['111001', '5'], ['111010', '6'], ['111011', '7'],
           ['111100', '8'], ['111101', '9'], ['111110', '+'], ['111111', '/']]


def HexToBinary(hex_: str):
    binary = ""
    for i in range(0, len(hex_), 2):  # разбиваем строку по 2 символа (1 байт) - 1 число в 16-рич
        char = hex_[i:i + 2]  # на каждой итерации следующая двойка из stt - строка байт
        binary += bin(int(char, 16))[2:].zfill(8)  # 1 байт - 8 бит
    return binary


def BinToHex(binary):
    hex_ = ""
    mp = [binary[x:x + 8] for x in range(0, len(binary), 8)]
    for i in mp:
        hex_ += hex(int(i, 2))[2:].zfill(2)
    return hex_


def SaveToFile(text: str, mode: str):
    date = str(datetime.now())[:-9].replace(":", "--")
    with open(f"{mode}-{date}.txt", "w", encoding="utf-8") as file:
        file.write(f"{text}")


def EncodeBase64(msg: str):  # сообщение в виде строки
    msg = msg.encode("ascii")  # переводим в байты по кодировке ascii
    msg = msg.hex()  # байты переводим в хекс (16-ричная система)
    binary_message = HexToBinary(msg)  # хекс переводим в биты (16рич - 2ич)
    count = 0
    if len(binary_message) % 24 != 0:
        while len(binary_message) % 24 != 0:
            binary_message += '0'
            count += 1
    six_bit_msg_blocks = [binary_message[i:i + 6] for i in
                          range(0, len(binary_message), 6)]  # делим двоичное сообщение по 6 бит
    new_mes = ""
    for char in six_bit_msg_blocks:
        for const in base_64:
            if char == const[0]:
                new_mes += const[1]
    if count == 8:
        result = new_mes[:-1] + "="
    elif count == 16:
        result = new_mes[:-2] + "=="
    else:
        result = new_mes
    SaveToFile(result, "en64")
    print(result, "\n")


def DecodeBase64(coded_mes: str):
    bin_mes = ""
    for char in coded_mes:
        for i in base_64:
            if char == i[1]:
                bin_mes += i[0]
                break
    if coded_mes.count("=") == 1:
        bin_mes = bin_mes[:-2]
    elif coded_mes.count("=") == 2:
        bin_mes = bin_mes[:-4]
    eight_bit_blocks = [bin_mes[i:i + 8] for i in range(0, len(bin_mes), 8)]
    result = BinToHex("".join(eight_bit_blocks))
    result = bytes.fromhex(result).decode("ascii")
    SaveToFile(result, "de64")
    print(result, "\n")


# BASE32
def EncodeBase32(msg: str):
    msg = msg.encode("ascii").hex()
    binary_msg = HexToBinary(msg)
    count = 0
    if len(binary_msg) % 40 != 0:
        while len(binary_msg) % 5 != 0:
            binary_msg += '0'
            count += 1
    five_bit_blocks = [binary_msg[i:i + 5] for i in range(0, len(binary_msg), 5)]
    result = ""
    for num, char in enumerate(five_bit_blocks):
        for const in base_32:
            if char == const[0]:
                result += const[1]
    if (len(binary_msg) - count) % 5 == 3:
        result += "======"
    elif (len(binary_msg) - count) % 5 == 1:
        result += "===="
    elif (len(binary_msg) - count) % 5 == 4:
        result += "==="
    elif (len(binary_msg) - count) % 5 == 2:
        result += "="
    SaveToFile(result, "en32")
    print(result, "\n")


def DecodeBase32(coded_mes: str):
    binary_msg = ""
    for char in coded_mes:
        for i in base_32:
            if char == i[1]:
                binary_msg += i[0]
    if coded_mes.count("=") == 6:
        binary_msg = binary_msg[:-2]
    elif coded_mes.count("=") == 4:
        binary_msg = binary_msg[:-4]
    elif coded_mes.count("=") == 3:
        binary_msg = binary_msg[:-1]
    elif coded_mes.count("=") == 1:
        binary_msg = binary_msg[:-3]
    eight_bit_blocks = [binary_msg[i:i + 8] for i in range(0, len(binary_msg), 8)]
    result = BinToHex("".join(eight_bit_blocks))
    result = bytes.fromhex(result).decode("ascii")
    SaveToFile(result, "de32")
    print(result, "\n")


def GettingMsg():
    while True:
        try:
            choice = input("1.\tKeyboard\n2.\tFile\n-\t")
        except Exception:
            print("\nAgain\n")
            continue
        else:
            if choice == "1":
                try:
                    mes = input("Input msg:\n-\t")
                except Exception:
                    print("\nAgain\n")
                    continue
                else:
                    break
            elif choice == "2":
                try:
                    path = input("Path to file:\n-\t")
                    with open(path, encoding="ascii") as file:
                        mes = file.read()
                except Exception:
                    print(f"\nAgain\n")
                    continue
                else:
                    break
            else:
                print("\nAgain\n")
                continue
    return mes


def laba2():
    while True:
        flag = input("1.\tBASE64\n2.\tBASE32\n\t")
        flag_1 = input("1.\tEncode\t2.Decode\n\t")
        if flag == "1":
            if flag_1 == "1":
                EncodeBase64(GettingMsg())
                pass
            elif flag_1 == "2":
                DecodeBase64(GettingMsg())
            else:
                print("Again.")
                continue
        elif flag == "2":
            if flag_1 == "1":
                EncodeBase32(GettingMsg())
            elif flag_1 == "2":
                DecodeBase32(GettingMsg())
            else:
                print("Again.")
                continue
        else:
            print("Again.")
            continue


laba2()
