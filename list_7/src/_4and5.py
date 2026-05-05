from functools import cache

@cache # jesli tego tutaj nie dodamy to rekurencyjne wywolania nie beda juz zapamietywane
def fib(n : int):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n-2)

def make_generator(f):

    def generator():

        current = 1

        while True:
            yield f(current)
            current += 1
        
    return generator()

def make_generator_mem(f):

    f_with_cache = cache(f)
    return make_generator(f_with_cache)

if __name__ == '__main__':

    generator_fib = make_generator_mem(fib)

    print("Generator fib: ")
    for i in range (40):
        print(next(generator_fib))

    generator_arytm = make_generator_mem(lambda n: 5 + (n - 1) * 3)

    print("Generator arytm: ")
    for i in range (40):
        print(next(generator_arytm))

    generator_geom = make_generator_mem(lambda n: 2 ** n)

    print("Generator geom: ")
    for i in range (40):
        print(next(generator_geom))