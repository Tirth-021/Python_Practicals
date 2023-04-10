def generate_parenthesis(n):
    """To generate the sequence as mentioned"""
    if n == 0:
        return ['']
    return ['(' + left + ')' + right
            for i in range(n)
            for left in generate_parenthesis(i)  # generates the left part of series
            for right in generate_parenthesis(n - i - 1)]  # generates the right part of series.


def main():
    try:
        print("Enter the number n ")
        number = input()
        if number.isdigit():
            num = int(number)
            if num < 0 or num > 8:
                raise ValueError
            else:
                result = generate_parenthesis(int(number))
                print(result)
        else:
            raise TypeError


    except TypeError:
        print("Please enter a number")
    except ValueError:
        print("Please enter a number between 1 to 8")


if __name__ == "__main__":
    main()
