import random
import string


class password_generator:
    def __init__(self, length, count, charset=string.ascii_letters + string.digits):
        self.length = length
        self.charset = charset
        self.count = count
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        else:
            self.index += 1
            password=""
            for i in range(self.length):
                password+=random.choice(self.charset)
            return password

if __name__ == '__main__':
    generator = password_generator(length=8, count=5)

    print("Test 1: Jawne wywołanie wbudowanej funkcji next()")
    print(next(generator))
    print(next(generator))

    print("\nTest 2: Wywołanie w ramach pętli for (dla pozostałych haseł)")
    for pwd in generator:
        print(pwd)