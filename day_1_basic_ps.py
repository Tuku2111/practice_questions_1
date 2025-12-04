# Find the maximum of two numbers
#
# Estimated time: 2 minutes
# Check if a number is even or odd
#
# Estimated time: 2 minutes
# Calculate the sum of all numbers in a list
#
# Estimated time: 3 minutes
# Reverse a string
#
# Estimated time: 2 minutes
# Count the number of vowels in a string
#
# Estimated time: 3 minutes
# Create a list of squares of numbers from 1 to 10
#
# Estimated time: 3 minutes
# Check if a string is a palindrome
#
# Estimated time: 4 minutes
# Convert Celsius to Fahrenheit
#
# Estimated time: 2 minutes
# Print all even numbers from 1 to 20
#
# Estimated time: 2 minutes
from functools import reduce

lst = [3,0,9,1,2,2]
st  = 'sushmita'
print(max(lst))

print(['even'  if num%2==0 else "odd" for num in lst])

print(sum(lst))

print(st[::-1])

print(reduce(lambda count, ch: count + (1 if ch in ['a','e','i','o','u'] else 0),st,0))

print(list(map(lambda x:x*x,[i for i in range(1,11)])))

print('pal' if st[::-1]==st else 'not pal')

print((lambda cel:cel*(9/5)+32)(25))

print([i  for i in range(1,21) if i%2==0])

# Your solutions are **clean, concise, and Pythonic**—great job! You're using the right tools like list comprehensions, lambda functions, `reduce`, `map`, slicing, and built-in functions like `sum` and `max`. Here’s a quick breakdown of how your approach scores in terms of **performance and memory**:
#
# ---
#
# ### 🔍 Feedback & Improvements
#
# 1. **Even/Odd Check**:
#    ✅ List comprehension is efficient for small lists.
#    🧠 If the list is huge, consider using a generator to reduce memory usage:
#
#    ```python
#    gen = ("even" if num % 2 == 0 else "odd" for num in lst)
#    ```
#
# 2. **Reverse String & Palindrome**:
#    ✅ `st[::-1]` is the fastest and cleanest way.
#    🧠 For large strings, slicing uses more memory than iterative comparison:
#
#    ```python
#    def is_palindrome(s):
#        return all(s[i] == s[~i] for i in range(len(s)//2))
#    ```
#
# 3. **List of Squares**:
#    ✅ `map` and list comprehension are both good.
#    🧠 If you're not storing, use a generator:
#
#    ```python
#    squares = (x*x for x in range(1, 11))
#    ```
#
# 4. **Reduce for Vowel Count**:
#    ✅ Nice use of `reduce`.
#    🧠 Slightly more efficient with `set` for faster membership testing:
#
#    ```python
#    vowels = set('aeiou')
#    ```
#
# 5. **Lambda for Conversion**:
#    ✅ Elegant and functional style.
#    🔁 Consider naming the function for clarity in larger codebases.
#
# ---
#
# ### 🧠 Slightly Tougher Practice Questions (Intermediate)
#
# 1. **Find the second largest number in a list**
# 2. **Remove duplicates from a list without using `set()`**
# 3. **Count the frequency of each character in a string**
# 4. **Flatten a nested list (1 level deep)**
# 5. **Find the factorial of a number using `reduce()`**
# 6. **Merge two dictionaries and sum values of common keys**
# 7. **Check if two strings are anagrams**
# 8. **Write a function to return Fibonacci numbers up to `n`**
# 9. **Sort a list of tuples by the second element**
# 10. **Check if a number is prime**
#
# Would you like to solve these one by one or get hints/solutions too?

for i in range(len(st)//2):
    t = (st[i] == st[~i])


print(sorted(lst)[1])

print(list(dict.fromkeys(lst)))

print({ i : lst.count(i) for i in list(dict.fromkeys(lst))})

main_lst = [1,4,[5,9,6,3],2]
def fltn(lst):
    temp_lst = []
    for i in lst:
        if isinstance(i,list):
            temp_lst.extend(fltn(i))
        else:
            temp_lst.append(i)
    return temp_lst

print(fltn(main_lst))

print(reduce(lambda x,y:x*y ,[i for i in range(1,6)]))

d1 ={1:4,7:9,0:1}
d2 = {1:6,9:3,0:8}

merged = {}
for key in set(d1.keys()).union(d2.keys()):
    merged[key]=d1.get(key,0)+d2.get(key,0)

print(merged)

from collections import Counter

print(Counter(d1)+Counter(d2))

st1 = 'listen'
st2 = 'silent'

if Counter(st1)==Counter(st2):  # sorted
    print('its anagram')
else:
    print('not anagram')

def get_fib(n):
    fib_sq = []
    a, b = 0,1
    while a <=n:
        fib_sq.append(a)
        a,b = b , a+b
    return fib_sq

print(get_fib(20))

data = [(1, 3), (2, 1), (4, 2)]


print(sorted(data,key=lambda x:x[1]))


def is_p(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(is_p(12))

# Next Set of Python Coding Questions
# Rotate a list to the right by k positions
# Example: [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]
#
# Find the longest word in a sentence
# Input: "The quick brown fox jumps" → Output: "jumps"
#
# Group words that are anagrams
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#
# Find common elements in three sorted lists
# Without using sets
#
# Check if a string is a valid palindrome ignoring non-alphanumeric characters
# Input: "A man, a plan, a canal: Panama" → Output: True
#
# *Implement a basic calculator supporting +, -, , /
# Input: 3 + 5 * 2 → Output: 13
# (Assume space-separated input string)
#
# Get the top k most frequent elements in a list
# Input: [1,1,1,2,2,3], k = 2 → Output: [1,2]
#
# Generate Pascal's Triangle up to n rows
#
# Check if a number can be expressed as a sum of two squares
# Example: 5 → 1² + 2², 3 → can't
#
# Find all pairs in a list that sum up to a target value
# Input: lst = [2, 4, 3, 5, 7], target = 7 → Output: [(2, 5), (3, 4)]

k = 2
l = [1,2,3,4,5]
print(l[-k:]+l[:-k])


s = "The quick brown fox jumps"

print(max(s.split(" "),key=len))


from collections import defaultdict
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

ana = defaultdict(list)

for i in a:
    ana[''.join(sorted(i))].append(i)

print(ana.values())

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}

for word in a:
    key = ''.join(sorted(word))
    anagrams.setdefault(key, []).append(word)

print(list(anagrams.values()))

from collections import defaultdict

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)

list(map(lambda word: anagrams[''.join(sorted(word))].append(word), a))
print((anagrams))





