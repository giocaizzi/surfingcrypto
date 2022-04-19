""" timer """
import datetime
import time


def timeit(method, is_classmethod=True):
    def timed(*args, **kw):
        ts = datetime.datetime.now()
        result = method(*args, **kw)
        te = datetime.datetime.now()
        if is_classmethod:
            args = args[1:]
        print(
            " #  {} \n"
            "    - args: {} \n"
            "    - kwargs: {} \n"
            "    ----------------\n"
            "    {} sec".format(method.__name__, args, kw, str(te - ts))
        )
        print(" - ")
        return result

    return timed


class Foo(object):
    @timeit
    def __init__(self, a=2, b=3):
        time.sleep(0.2)
        self.a = a
        self.b = b

    @timeit
    def f1(self):
        time.sleep(0.5)
        # print(f"f1, a={self.a},b={self.b}")

    @timeit
    def f2(self, c):
        time.sleep(1)
        # print(f"f2=,c={c}")

    @timeit
    def f3(self, *args, **kw):
        time.sleep(1.5)
        # print(f"f3, args:{args}, kw: {kw}")

    def __repr__(self) -> str:
        return f"Foo({self.a},{self.b})"

    def __str__(self) -> str:
        return f"Foo({self.a},{self.b})"


@timeit
def external():
    time.sleep(1.5)


f = Foo(a=5)
f.f2(4)
f.f3()

external()
