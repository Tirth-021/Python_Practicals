import unittest
import Python_Practicals
from Python_Practicals import Practical3


class SimpleTest(unittest.TestCase):

    def test1(self):
        lst = ("eat", "tea", "tan", "ate", "nat", "bat")
        self.assertEqual(Practical3.group_anagrams(lst), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])


if __name__ == '__main__':
    unittest.main()
