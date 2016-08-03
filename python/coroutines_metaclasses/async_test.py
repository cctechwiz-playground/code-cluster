# Task wrapper for generator
def tasker(tsk):
    def inner(*args, **kwargs):
        t = tsk(*args, **kwargs)
        t.step()
        return t
    return inner

@tasker
class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                # .send(None) same is calling next() to prime the generator
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup) # register callback for fut
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        try:
            result = fut.result() # block for result, in callback, so done
            self.step(result, None) # send result to gen, tiggers yield
        except Exception as exc: # catch erros in async call
            self.step(None, exc)

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
# async test
import time
from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor(max_workers=8)
pool_m = ThreadPoolExecutor(max_workers=16)

# TODO: Get this working, then I don't need to know how many workers I will use
# Currently throws "RuntimeError('cannot join current thread',)"
# https://pythonhosted.org/futures/
"""
with ThreadPoolExecutor(max_workers=1) as e:
    e.submit(func, **kwargs)
"""

def func(x, y):
    time.sleep(1)
    return x + y

def func1(x, y):
    time.sleep(2)
    return x + y

def func2(x, y):
    time.sleep(1)
    return x + y

def func3(x, y):
    # print('f3')
    time.sleep(3)
    return x + y

def do_func(f, x, y):
    # print('called:\nf:{}\nx:{}\ny:{}\npool:{}'.format(f, x, y, pool))
    try:
        result = yield pool.submit(f, x, y) # add to thread pool, yield result
        print('Got:', result)
    except Exception as e:
        print('Failed:', repr(e))

def do_many(n):
    try:
        while n > 0:
            result = yield pool_m.submit(func, n, n)
            print('Got(m):', result)
            n -= 1
    except Exception as e:
        print('Failed:', repr(e))

def after(delay, gen):
    yield pool.submit(time.sleep, delay)
    # print('got here 1')
    yield from gen
    # print('got here 2')

Task(do_func(func1, 0, 1))
# no need to step because of @tasker now
# t1.step() # step with None primes the generator

Task(do_func(func2, 0, 2))
# t2.step()

Task(do_func(func3, 0, 3))
# t3.step()

# For some reason this one needs its own pool with 16 workers
Task(do_many(10))
# t4.step()

# It DOES work if I comment out the previous Tasks, I must not fully
# understand how the pools work.
# Task(after(10, do_func(func3, 0, 4)))
