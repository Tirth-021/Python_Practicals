# Python_Practicals
LMS python assignment with hands on practice with core concepts of python.

### Practical 1

1. Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.

    The program should take input from console or args and should handle unexpected inputs    

    Constraints:

        - For loop is not allowed

        - input should be in words:

            - e.g.: onetwo = 12, sixone = 61

        - words will be within zero to nine

        - Cannot use inbuilt methods like max, min, or any math function    

    Example 1:

        - Input 1: onezero

        - Input 2: twozero

        - Output: onezero

    Example 2:

        - Input 1: twosix

        - Input 2: twofour

        - Output: two
        
> Approach to solve:  

> For changing the words to numbers a function "stringtonum" is made which checks for a specific word and replaces it with the specific number.  
> On changing the words to numbers, that string is converted to integer and passed to GCD function.  
> The GCD of those two numbers are calculated by making use of recursion.  
> On getting the answer it is once again converted to words by using a function "numtostring".  
> Final output is shown.  

![image](https://user-images.githubusercontent.com/125239162/228430765-e0747945-d0c1-4a4e-99a8-43b7eb7cbeb2.png)

### Practical 2  

2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Constraints:

        - 1 <= n <= 8

    Example 1:

        - Input: n = 3

        - Output: ["((()))","(()())","(())()","()(())","()()()"]

        - Example 2:

    Example 2:

        - Input: n = 1

        - Output: ["()"] 

> Approach to solve:  

> A function is created for generating parenthesis.  
> The first for loops iterates for the number of parenthesis.  
> The second for loop produces the left part from center.  
> The third loop produces the right part from center.  


![image](https://user-images.githubusercontent.com/125239162/228431232-637ad833-9847-4ba3-ad6b-c65bb39e060e.png)



### Practical 3  

3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Constraints:

        - 1 <= strs.length <= 104

        - 0 <= strs[i].length <= 100

        - strs[i] consists of lowercase English letters.

    Example 1:

        - Input: strs = ["eat","tea","tan","ate","nat","bat"]

        - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Example 2:

        - Input: strs = [""]

        - Output: [[""]]

    Example 3:

        - Input: strs = ["a"]

        - Output: [["a"]]

> Approach to solve:  

> Default dictionary is first of all imported so that the keys need not to be defined.  
> After that the inputs are appended to a list.  
> The words collected in list is sorted and stored as a key.  
> The values of this dictionary is converted to list.  
> The final list is printed as output.  

![image](https://user-images.githubusercontent.com/125239162/228430813-60592d8a-4238-4973-8f36-1a612b601ab2.png)




