from collections import defaultdict
from itertools import chain


def acronym(lst):
    result= "".join(map(lambda x: x[0], lst))
    return result

def median(lst):
    lst = sorted(lst)
    n=len(lst)
    return lst[n//2] if n%2==1 else (lst[n//2]+lst[(n//2)-1])/2

def sqrt(x, epsilon, y=1.0):
    return y if abs(y**2-x)<epsilon else sqrt(x, epsilon, (y+x/y)/2)

def make_alpha_dict(text):
    split=text.split()
    chars=sorted(list(set("".join(split))))
    return{
        # char: ... for char in chars tworzy nam slownik
        # [word for word in split if char in word] tworzy liste dla kazdego klucza
        char: [word for word in split if char in word]
        for char in chars
    }

def flatten(lst):
    # isinstance sprawdza czy jest lista lub krotka
    res = [flatten(x) if isinstance(x, (list, tuple)) else [x] for x in lst]
    # sum(...,[]) spłaszcza liste o jeden poziom
    return sum(res, [])

def group_anagrams(lst):
    keys = set(map(lambda x: "".join(sorted(x)), lst))
    return{
        k: [word for word in lst if "".join(sorted(word))==k]
        for k in keys
    }
if __name__=="__main__":
    print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1, 1]))
    # 1 1 1 1 2 3 4 4 5 19
    print(sqrt(3, 0.1))
    print(make_alpha_dict("ona i on"))
    print(flatten([1, [2, 3], [[4, 5], 6]]))
    print(group_anagrams(["kot", "tok", "pies", "kep", "pek"]))