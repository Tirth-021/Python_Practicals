def generate_parenthesis(n):
    """To generate the sequence as mentioned"""
    if n == 0:
        return ['']
    return ['(' + left + ')' + right
            for i in range(n)
            for left in generate_parenthesis(i) #generates the left part of series
            for right in generate_parenthesis(n - i - 1)]  # generates the right part of series.


n = int(input())
result = generate_parenthesis(n)
print(result)
