import unittest
# import Python_Practicals
from Python_Practicals import practical_1


class SimpleTest(unittest.TestCase):

    def test1(self):
        num = "onezero"
        num2 = "twozero"
        self.assertEqual(practical_1.Prac1.string_to_num(num), '10')
        self.assertEqual(practical_1.Prac1.string_to_num(num2), '20')

    def test2(self):
        num = "10"
        num2 = "20"
        self.assertEqual(practical_1.Prac1.num_to_string(num), 'onezero')
        self.assertEqual(practical_1.Prac1.num_to_string(num2), 'twozero')

    def test3(self):
        num = 10
        num2 = 20
        self.assertEqual(practical_1.Prac1.Gcd(num, num2), 10)


if __name__ == '__main__':
    unittest.main()
