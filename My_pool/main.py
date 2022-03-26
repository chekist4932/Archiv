import multiprocessing as mp
import threading
from typing import Callable, Any
import time
from func import func


class TaskStatus:
    def __init__(self, pid: Any, is_alive=False):
        self.pid = pid
        self.is_running = is_alive


class MyPool:

    def __init__(self, max_size: int):
        self._max_size = max_size

        self._tas = []
        self._flag = True
        self._procs = []


        self._th = threading.Thread(target=self._run, args=(self._tas, ))
        self._check = threading.Thread(target=self._checker)
        self._th.start()
        self._check.start()


    def add_task(self, task_name: str, task: Callable, *args: list[Any], **kwargs: dict[Any, Any]):
        self._tas.append([task, task_name, *args, *kwargs])


    def delety(self):
        #print(threading.active_count())
        while True:
            if len(self._tas) == 0 and len(self._procs) == 0:
                self._flag = False
                break
            else:
                continue



    def _checker(self):
        while self._flag:
            for i in self._procs:
                #print("+")
                if not i[1].is_alive():
                    del self._procs[self._procs.index(i)]



    def _run(self, tas):
        #print(threading.current_thread())
        while self._flag:
            if len(tas) > 0:
                #print(self._procs)
                if len(self._procs) < self._max_size:
                    proc = mp.Process(target=tas[0][0], name=tas[0][1], args=(tas[0][2], ),
                                      kwargs=self._tas[0][3])

                    proc.start()

                    self._procs.append([tas[0][1], proc])
                    #print(self._procs)

                    del tas[0]
                    #print(self._tas)
            else:

                continue

    """def _run(self):

        # TODO: реализовать метод.
        #  Цикл предназначен для получения ожидающих задач из tasks и запуска процессов по мере их завершения
        while True:
            if len(self._tas) > 0:

                if len(self._procs) < self._max_size:
                    proc = mp.Process(target=self._tas[0][0], name=self._tas[0][1], args=self._tas[0][2],
                                      kwargs=self._tas[0][3])

                    for j in self._procs:
                        if not j[1].is_alive():
                            del self._procs[0]
                    self._procs.append([self._tas[0][1], proc])
                    proc.start()
                    print(self._tas)
                    del self._tas[0]

                else:
                    continue"""

    def remove_task(self, task_name: str) -> bool:
        flag = 0
        for i in self._procs:
            if i[1].name == task_name:
                i[1].terminate()
                while i[1].is_alive():
                    pass
                flag = 1

        if flag == 0:
            for i in self._tas:
                if i[1] == task_name:
                    del self._tas[self._tas.index(i)]
                    flag = 2
        if flag == 0:
            raise Exception("Задача не была найдена.")
        else:
            return True

    def get_task_info(self, task_name: str) -> TaskStatus:
        """возвращает информацию о процессе выполнения задачи

        :param task_name: имя задачи
        :return: объект TaskStatus, хранящий в себе параметры задачи, а именно:
            статус задачи - is_running: True - если задача выполняется, иначе False.
            идентификатор выполяющего процесса - pid: числовой идентификатор процесса - если задача выполняется,
                иначе None
        """
        # TODO: реализовать метод

        for i in self._procs:
            if i[1].name == task_name:
                if i[1].is_alive():
                    info = TaskStatus(i[1].pid, True)
                    return info
        info = TaskStatus(None)
        return info

    def wait_all(self):
        while True:
            if len(self._tas) == 0 and len(self._procs) == 0:
                break
            else:
                continue


    def wait_task(self, task_name: str):
        # Ожидает завершения первой попавшейся задачи под именем task_name.

        flag_len = 0
        while True:
            flag_1 = 0
            proc = None

            for i in self._procs:
                if i[1].name == task_name:
                    flag_1 += 1
                    proc = i[1]

            if flag_1 == 1:

                if proc.is_alive():
                    while proc.is_alive():
                        pass
                    break
                elif not proc.is_alive(): #Спорно
                    break
            elif flag_1 > 1:
                raise Exception("Запущены две задачи с одинаковым именем.")
            if len(self._tas) == 0:
                if flag_len == 0:
                    flag_len = 1
                    continue
                elif flag_len == 1:
                    if flag_1 == 0:
                        raise Exception("Задача не была найдена.")



        """while True:
            flag = 0
            obj = None
            for i in self._procs:
                if i[1].name == task_name:
                    obj = i[1]
                    flag += 1
            if flag == 1:
                obj.join()
                break
            elif flag > 1:
                raise Exception("Запущено две задачи с одинаковым именем")
            elif flag == 0:
                count = 0
                for i in self._tas:
                    if i[1] == task_name:
                        count += 1
                if count == 1:
                    continue
                elif count == 0:
                    raise Exception("Задача не была найдена в исполнении/очереди на исполнение")
                elif count > 1:
                    raise Exception("Существует две задачи с одинаковым именем")"""






if __name__ == '__main__':

    pool = MyPool(5)
    #time.sleep(2)
    pool.add_task("proc0", func, [1, 2, 3], {"1": "kek"})
    pool.add_task("proc1", func, [1, 2, 3], {"1": "kek"})
    pool.add_task("proc2", func, [1, 2, 3], {"1": "kek"})
    name = "proc4"
    # pool.remove_task(name)
    # print(f"pid: {pool.get_task_info(name).pid} -- is_run : {pool.get_task_info(name).is_running}")

    # print(f"pid: {pool.get_task_info(name).pid} -- is_run : {pool.get_task_info(name).is_running}")
    # pool.wait_task(name)
    # print(f"pid: {pool.get_task_info(name).pid} -- is_run : {pool.get_task_info(name).is_running}")
    #pool.wait_all()
    pool.add_task("proc3", func, [1, 2, 3], {"1": "kek"})
    pool.add_task("proc4", func, [1, 2, 3], {"1": "kek"})

    """print(mp.active_children())
    print(pool.get_task_info("proc3").pid)
    print(mp.active_children())
    print(pool.get_task_info("proc3").is_running)
    print(mp.active_children())
    """
    #pool.remove_task(name)
    pool.add_task("proc3", func, [1, 2, 3], {"1": "kek"})

    pool.add_task("proc4", func, [1, 2, 3], {"1": "kek"})

    pool.add_task("proc6", func, [1, 2, 3], {"1": "kek"})
    pool.add_task("proc7", func, [1, 2, 3], {"1": "kek"})
    pool.delety()



