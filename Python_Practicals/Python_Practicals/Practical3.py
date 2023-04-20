"""Practical 3"""


class LengthError(Exception):
    """Raised Number of strings is more than expected. """
    pass


class MoreLetters(Exception):
    """Raised length of string is more than expected. """
    pass


def group_anagrams(words):
    """Function to group anagrams by sorting
       Input: list of words
       Output: list of words with sorted anagrams"""
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())


elem = eval(input())

try:
    for i in elem:
        if isinstance(i, int):
            raise TypeError
        if len(i) > 100 or len(i) < 0:
            raise MoreLetters
        for j in i:
            if j.isupper():
                raise ValueError
    if len(elem) > 104 or len(elem) < 1:
        raise LengthError

except TypeError:
    print("Please enter only string")
except ValueError:
    print("Please don't enter capital strings")
except LengthError:
    print("More or Less arguments than expected. ")
except MoreLetters:
    print("Length os string is more. ")

else:
    group_anagrams(elem)

    print(group_anagrams(elem))
