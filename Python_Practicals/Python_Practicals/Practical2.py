def generate_parenthesis(n):
    """To generate the sequence as mentioned"""
    if n == 0:
        return ['']
    return ['(' + left + ')' + right
            for i in range(n)
            for left in generate_parenthesis(i)  # generates the left part of series
            for right in generate_parenthesis(n - i - 1)]  # generates the right part of series.


try:
    print("Enter the number n ")
    n = int(input())
    if n < 0 or n > 8:
        raise ValueError
    if isinstance(n, str):
        raise TypeError
except ValueError:
    print("Please enter a number between 1 to 8")
except TypeError:
    print("Please enter a number")

else:
    result = generate_parenthesis(n)
    print(result)
