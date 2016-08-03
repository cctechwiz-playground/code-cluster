def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr) # Python2 => cr.next() Python3 => next(cr)
        return cr
    return start


# Sink
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


@coroutine
def filter_evens(target):
    while True:
        item = (yield)
        if item % 2 == 0:
            target.send(item)


@coroutine
def filter_odds(target):
    while True:
        item = (yield)
        if item % 2 != 0:
            target.send(item)


@coroutine
def add_one(target):
    while True:
        item = (yield)
        target.send(item + 1)


# generator
def gen_list(n):
    i = 0
    while i < n:
        yield i
        i += 1


# Source
list = gen_list(8)
# fe = filter_evens(add_one(printer()))
# fo = filter_odds(add_one(printer()))
fe = filter_evens(printer())
fo = filter_odds(printer())
print("Filtering Evens:")
for i in list:
    fe.send(i)

list = gen_list(8)
print("Filtering Odds:")
for i in list:
    fo.send(i)
