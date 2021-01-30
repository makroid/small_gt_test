import os

def test_fib(to=10):
    f0 = 0
    f1 = 1
    f2 = f1
    while f2 < to:
        f2 = f1 + f0
        print("f2={}".format(f2))
        f0 = f1
        f1 = f2

    print("in test fib")


def count_words(s):
    toks = s.split()
    d = {}
    for t in toks:
        if t not in d:
            d[t] = 1
        else:
            d[t] += 1
    return d


txt = """this is a random test text, quite random"""

def new_feature_in_master(m):
    n = 0
    while i<m:
        n += i
    return n

def first_func_in_feature_a(a, n):
    b = 1
    for i in range(n)
        b *= a
    return b


if __name__ == "__main__":
    to = 330

    print("fib:")
    test_fib(to)

    print("adding feature a")

    d = count_words(txt)

    for dd in d:
        print(dd, "=>", d[dd])