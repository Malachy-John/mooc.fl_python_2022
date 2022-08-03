# Write your solution here

def histogram(word: str):
    groups = {}

    for letter in word:
        if letter not in groups:
            groups[letter] = 0
        groups[letter]+=1

    for letter,values in groups.items():
        print(f"{letter}", end ="")
        print(f" {'*' * values}")


if __name__ == "__main__":
    histogram("abba")