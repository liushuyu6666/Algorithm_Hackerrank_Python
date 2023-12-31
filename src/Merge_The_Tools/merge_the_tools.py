def merge_the_tools(string, k):
    length = len(string)
    seg = length // k  # [0, k), [k, 2k)

    for i in range(seg):
        print(rearrangement(string[i * k: (i + 1) * k]))

def rearrangement(string: str):
    char_set = set()

    target_str: str = ""
    for l in string:
        if l not in char_set:
            char_set.add(l)
            target_str += l

    return target_str
