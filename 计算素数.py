def _not_divisible(n):
    return lambda x: x % n > 0


def _add_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def primes():
    yield 2
    it = _add_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# primes是一个生成器函数，被for in遍历
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
