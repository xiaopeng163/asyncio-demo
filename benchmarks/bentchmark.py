import time
from datetime import datetime
from multiprocessing.pool import ThreadPool

from step1 import search

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.5f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


N = 100
COUNT = 10000

@timeit
def synchronous():
    for i in range(COUNT):
        search(N)

@timeit
def multi_process():
    pool = ThreadPool(10)
    result = pool.map(search, [N]*COUNT)
    pool.close()
    pool.join()



if __name__ == "__main__":
    synchronous()
    multi_process()