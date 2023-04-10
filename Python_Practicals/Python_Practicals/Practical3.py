"""Practical 3"""


class LengthError(Exception):
    "Raised Number of strings is more than expected. "
    pass


class MoreLetters(Exception):
    "Raised length of string is more than expected. "
    pass


def group_anagrams(words):
    """Function to group anagrams by sorting"""
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())


elem = eval(input())


def main():
    try:
        for i in elem:
            if len(i) > 100:
                raise moreletters
            for j in i:
                if j.isupper():
                    raise ValueError
        if len(elem) > 104:
            raise lengtherror

    except ValueError:
        print("Please don't enter capital strings")
    except lengtherror:
        print("More arguments than expected. ")
    except moreletters:
        print("Length os string is more. ")

    else:
        group_anagrams(elem)

        print(group_anagrams(elem))


if __name__ == "__main__":
    main()
