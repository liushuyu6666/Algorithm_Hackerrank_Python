from typing import List
from itertools import product


def maximize_it():
    # line 1
    k, m = map(int, input().split())

    # following lines
    set_list: List[set] = []
    for _ in range(k):
        squared = [x ** 2 for x in map(int, input().split())]
        squared_len = squared.pop(0)
        if squared_len > 0:
            set_list.append(set(squared))

    all_s = [sum(cartesian) % m for cartesian in product(*set_list)]

    print(max(all_s))


if __name__ == '__main__':
    maximize_it()