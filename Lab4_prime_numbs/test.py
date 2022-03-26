import multiprocessing as mp
import sys
import time
import threading
import tqdm
import math

def per(i,j,lic):
    if j % i == 0:
        del lic[lic.index(j)]



def body(lic):

    for i in lic:

        for j in lic[lic.index(i)+1:]:
            if j % i == 0:
                del lic[lic.index(j)]


def wait(lis):
    global flag
    flag = True
    while flag:
        for i in range(100):
            lis.append(i)
        print("Wait few seconds")
        time.sleep(5)
        print(lis)
        return 0



def while_body(lic:list):
    for i in lic:
        if i != lic[-1]:
            count = lic.index(i) + 1
        else:
            break
        while count <= lic.index(lic[-1]):
            if lic[count] % i  == 0:
                del lic[lic.index(lic[count])]
            count += 1

class Test:
    def __init__(self, lis):
        self.lis = lis
        self.flag = True
        th = threading.Thread(target=self.wait)
        th.start()
        time.sleep(2)
        self.flag = False
    def wait(self):
        while self.flag:
            for i in range(100):
                self.lis.append(i)
            print("Wait few seconds")
            time.sleep(5)
            print(self.lis)
            return 0

if __name__ == '__main__':
    """lit = []
    li = [x for x in range(100)]
    for i in tqdm.tqdm(li):
        lit.append(i*i)
        pass
    print(lit)
"""

    size = 10000
    count_proc = 3
    mp_val = (size // count_proc) + size - ((size // count_proc) * count_proc)
    lit_con = [1]
    for i in range(count_proc):
        lit_con.append(mp_val)
        mp_val += size // count_proc
    res = []
    mp_list = [[size,x,lit_con,res] for x in lit_con[1:]]
    for num in lit_con[1:]:
        for j in tqdm.trange(lit_con[lit_con.index(num) - 1] + 1, num + 1):
            flag = True
            for i in range(2, int(math.sqrt(size)) + 1):
                if j % i == 0 and j != i:
                    flag = False
            if flag:
                res.append(j)



    """size =  1000 #int(sys.argv[1])
    count = 3
    mp = (size//count)+size - (size//count*count)
    print(mp)
    input()
    lit_con = [1]
    for i in range(count):
        lit_con.append(mp)
        mp += size//count
    print(lit_con)
    res = []
    val = []
    now = time.time()
    print(lit_con[1:])
    for num in lit_con[1:]:
        for j in range(lit_con[lit_con.index(num)-1]+1, num+1):
            flag = True
            val.append(j)
            for i in range(2, int(math.sqrt(size)) + 1):
                if j % i == 0 and j !=i:
                    flag = False
            if flag:
                res.append(j)
                pass
            # print(j)
    print(f"Time gone - {time.time() - now}")
    #res.sort()
    #print(res)
    #print(val)
    for i in val:
        if val.count(i) != 1:
            print(i)
"""

    """mng = mp.Manager()
    lic = mng.list(range(2, size + 1))
    lit = [x for x in range(2, size + 1)]"""
    #print(lit)
    """with mp.Pool(processes=2) as my_pool:
        print(mp.active_children())
        for i in range(10):
            res = my_pool.apply_async(wait, args=(lic,))"""
    """for i in lic:
        if i % 2 == 0:
            del lic[lic.index(i)]
    print(lic)"""








    """val = mp.Value('i', 10)
    vval = mp.Value('i', 10)
    print(val.value > 0)
    print(vval)"""