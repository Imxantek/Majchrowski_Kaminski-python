def forall(pred, iterable):
    return False not in map(pred, iterable)

def exists(pred, iterable):
    return True in map(pred, iterable)

def atleast(n, pred, iterable):
    return sum(map(pred, iterable)) >= n

def atmost(n, pred, iterable):
    return sum(map(pred, iterable)) <= n

if __name__ == '__main__':
    print(forall(lambda x: x % 2 == 0, [2, 4, 6]))
    print(exists(lambda x: x % 2 == 0, [1, 3, 4]))
    print(atleast(2, lambda x: x % 2 == 0, [2, 4, 5]))
    print(atmost(2, lambda x: x % 2 == 0, [2, 4, 1]))