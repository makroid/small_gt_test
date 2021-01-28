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


if __name__ == "__main__":
    to = 130
    test_fib(to)

    d = count_words(txt)

    for dd in d:
        print(dd, "=>", d[dd])