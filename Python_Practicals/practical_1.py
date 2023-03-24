"""Practical1"""


class Prac1:
    """Class for containing all methods as required"""   

    def get_values():
        """ For getting the initial values"""
        print("Enter first number")
        num = input()  # converting the returned string to integer
        try:
            number1 = int(Prac1.string_to_num(num))
        except ValueError:
            print("Please enter correct format") 
            exit()

        print("Enter second number")
        num2 = input()
        try:
            number2 = int(Prac1.string_to_num(num2))
        except ValueError:
            print("Please enter correct format") 
            exit()
        
        TEMP = str(Prac1.Gcd(number1, number2))  # converting the returned GCD to string
        RESULT = Prac1.num_to_string(TEMP)
        print(f"Result is {RESULT}")

    def string_to_num(num):

        """conditions used to replace a word to following number.
         It would still be a string only"""
        
        if ('zero' in num):
            num = num.replace("zero", "0")
        if ('one' in num):
            num = num.replace("one", "1")
        if ('two' in num):
            num = num.replace("two", "2")
        if ('three' in num):
            num = num.replace("three", "3")
        if ('four' in num):
            num = num.replace("four", "4")
        if ('five' in num):
            num = num.replace("five", "5")
        if ('six' in num):
            num = num.replace("six", "6")
        if ('seven' in num):
            num = num.replace("seven", "7")
        if ('eight' in num):
            num = num.replace("eight", "8")
        if ('nine' in num):
            num = num.replace("nine", "9")
        return num
    
    def num_to_string(num):

        """function used to convert numbers to word"""

        if ('0' in num):
            num = num.replace("0", "zero")
        if ('1' in num):
            num = num.replace("1", "one")
        if ('2' in num):
            num = num.replace("2", "two")
        if ('3' in num):
            num = num.replace("3", "three")
        if ('4' in num):
            num = num.replace("4", "four")
        if ('5' in num):
            num = num.replace("5", "five")
        if ('6' in num):
            num = num.replace("6", "six")
        if ('7' in num):
            num = num.replace("7", "seven")
        if ('8' in num):
            num = num.replace("8", "eight")
        if ('9' in num):
            num = num.replace("9", "nine")

        return num

    def Gcd(x, y):
        """ For calculating the GCD"""
        if (y == 0):
            return x
        else:
            return Prac1.Gcd(y, x % y)


Prac1.get_values()
