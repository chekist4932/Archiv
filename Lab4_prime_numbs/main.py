import multiprocessing as mp
import sys
import tqdm
import time
import math
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def per(size, num,lit_con,result,que):
    try:
        decimal = 10

        mp_lic = [x for x in range(lit_con[lit_con.index(num) - 1] + 1, num + 1)]
        sss = len(mp_lic)

        one_perc = (sss // 100)
        for k,j in enumerate(range(lit_con[lit_con.index(num) - 1] + 1, num + 1)):
            flag = True
            for i in range(2, int(math.sqrt(size)) + 1):
                if j % i == 0 and j != i:
                    flag = False
            if flag:
                result.append(j)
            if k == one_perc * decimal:
                decimal += 10
                try:
                    que.put(f"Процесс - {mp.current_process().name} находится на {j}-ой итерации.")
                    #print(f"Процесс - {mp.current_process().name} находится на {j}-ой итерации.")
                    #print(f"{mp.current_process().name} +")
                except Exception:
                    pass
        que.put("CLOSED!")
        return result
    except KeyboardInterrupt:
        print(f"Презждевременное завершение процесса - {mp.current_process().name}")
        que.put("CLOSED!")
        return result
    except Exception as er:
        print(f"Презждевременное завершение процесса - {mp.current_process().name} | Ошибка завершения - {str(er)} ")
        que.put("CLOSED!")


def call_back(result):
    with open("Prime_numbers.txt","a") as file:
        print("Начата записать.")
        output = sum(result, [])
        output.sort()
        file.write(f"\t\tNew session at - {time.ctime(time.time())}\n")
        for i in tqdm.tqdm(output):
            file.write(str(i) + "\n")
        print("Запись заверешена.")


def menu(size, count_proc):
    mp_val = (size // count_proc) + size - ((size // count_proc) * count_proc)
    lit_con = [1]

    for i in range(count_proc):
        lit_con.append(mp_val)
        mp_val += size//count_proc
    result = []
    my_pool = mp.Pool(processes=count_proc)
    mng = mp.Manager()
    que = mng.Queue()
    async_res = my_pool.starmap_async(
        per,
        iterable=[[size,x,lit_con,result, que] for x in lit_con[1:]],
        callback=call_back
    )
    closed_count = 0
    while True:
        try:
            if not que.empty():
                perc = que.get(block=False)
                if perc != "CLOSED!":
                    print(perc)
                elif perc == "CLOSED!":
                    closed_count += 1
                if closed_count == count_proc:
                    print('END')
                    break
            else:
                continue
        except Exception as ex:
            print(ex)

    async_res.wait()
    print("Перебор окончен.")




if __name__ == "__main__":
    if len(sys.argv) > 3 or len(sys.argv) < 3:
        exit("Необходимо указать 2 параметра : [верхняя граница] [Кол-во процессов]")
    elif len(sys.argv) == 3:
        try:
            size = int(sys.argv[1])
            if size > 10000000:
                exit("Слишком большое число")
            count_proc = int(sys.argv[2])
            if count_proc > mp.cpu_count():
                exit("Для данного устройства нецелесообразно использовать больше процессов.")
            menu(size, count_proc)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as err:
            print(f"Презждевременное завершение  программы.")
            sys.exit()
