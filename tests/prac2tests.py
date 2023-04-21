import unittest
import Python_Practicals
from Python_Practicals import Practical2


class SimpleTest(unittest.TestCase):

    def test1(self):
        n = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEqual(Practical2.generate_parenthesis(n), ['()()()', '()(())', '(())()', '(()())', '((()))'])

    def test2(self):
        n = 4
        self.assertEqual(Practical2.generate_parenthesis(n),
                         ['()()()()', '()()(())', '()(())()', '()(()())', '()((()))', '(())()()', '(())(())',
                          '(()())()', '((()))()', '(()()())', '(()(()))', '((())())', '((()()))', '(((())))'])


if __name__ == '__main__':
    unittest.main()
