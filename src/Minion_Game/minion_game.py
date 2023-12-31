def minion_game(string: str):
    # your code goes here
    length = len(string)
    kevin_scores = 0  # vowels
    stuart_scores = 0  # consonants
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(length):
        if string[i].lower() in vowels:
            kevin_scores += length - i
        else:
            stuart_scores += length - i

    if stuart_scores > kevin_scores:
        print(f"Stuart {stuart_scores}")
    elif kevin_scores > stuart_scores:
        print(f"Kevin {kevin_scores}")
    else:
        print("Draw")
