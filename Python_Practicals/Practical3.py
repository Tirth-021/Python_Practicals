from collections import defaultdict


print("Enter the number of elements")
n = int(input())
strings = []
# getting the elements and storing it in a list
for i in range(0, n):
    elem = input()
    strings.append(elem)


temp = defaultdict(list)
for i in strings:
    temp[str(sorted(i))].append(i) #using the sorted function to be used as a key in default dictionary and append accordingly 
res = list(temp.values())


print("The grouped Anagrams : " + str(res))
