from itertools import combinations


def itertools_():
    from itertools import combinations_with_replacement
    string, n = input().split()
    aux = "".join(sorted(string))
    y = list(combinations_with_replacement(aux, int(n)))

    for item in sorted(y):
        print(*item, sep="")


def groupby_():
    from itertools import groupby

    x = groupby(input())
    aux = []
    for key, iter_item, in x:

        count = 0
        for _ in iter_item:
            count +=1
        aux.append((count, int(key)))
    print(*aux)

def itertools_en():

    n = int(input())
    ls = input().split()
    k = int(input())
    com = list(combinations(ls, k))
    tol = [i for i in com if "a" in i]
    print(tol)
    print(f'{(len(tol) / len(com)):.12f}')

def company_Logo():
    from collections import Counter
    s = input()
    s = sorted(s)

    fre = Counter(list(s))

    for k, v in fre.most_common(3):
        print(k, v)



if __name__ == '__main__':
    company_Logo()
