import multiprocessing as mp
import threading
from typing import Callable, Any
import time




def func(lic, **kwargs):
    for i in range(10):
        time.sleep(1)
    print(f"{mp.current_process().name} - Finished | List - {lic}")

