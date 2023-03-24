from collections import defaultdict


print("Enter the number of elements")
n = int(input())
strings = []

for i in range(0, n):
    elem = input()
    strings.append(elem)


temp = defaultdict(list)
for i in strings:
    temp[str(sorted(i))].append(i)
res = list(temp.values())


print("The grouped Anagrams : " + str(res))
