# Day 1 (2023)

`TITLE` ([prompt](https://adventofcode.com/2023/day/1))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1
regex very helpful, in python there are 6 main functions to use with the regex module re 
1. re.search(pattern, string)
Searches for the first occurrence of the pattern in the string.  
Returns a match object if found, else None.  
```python
match = re.search(r'\d+', 'Order 1234')  
print(match.group())  # Output: 1234
```
2. re.match(pattern, string)
Checks if the pattern matches at the beginning of the string.  
Returns a match object if found, else None.  
```python
match = re.match(r'Order', 'Order 1234')  
print(match.group())  # Output: Order
```
3. re.findall(pattern, string)
Finds all occurrences of the pattern in the string.  
Returns a list of matches.  
```python
matches = re.findall(r'\d+', 'Order 1234, Order 5678')  
print(matches)  # Output: ['1234', '5678']
```
4. re.sub(pattern, replacement, string)
Replaces all occurrences of the pattern with the replacement.  
```python  
result = re.sub(r'\d+', '####', 'Order 1234')  
print(result)  # Output: Order ####
```
5. re.split(pattern, string)
Splits the string at occurrences of the pattern.  
```python
parts = re.split(r'\s+', 'Split this sentence into words')  
print(parts)  # Output: ['Split', 'this', 'sentence', 'into', 'words']  
```
6. re.compile(pattern)
Compiles a regular expression into a regex object for repeated use.
Improves performance when using the same pattern multiple times.  
```python
pattern = re.compile(r'\d+')  
print(pattern.findall('Order 1234, Order 5678'))  # Output: ['1234', '5678']
```
## Part 2
Be careful when replacing things in a string.  
Using this number_dict  
```python
number_dict = {
        "one": '1', "two": '2', "three": '3', "four": '4', 
        "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'
}  
```
versus this number dict  
```python
number_dict = {"one": 'one1one', "two": 'two2two', "three": 'three3three', "four": 'four4four', "five": 'five5five', 
                    "six": 'six6six', "seven": 'seven7seven', "eight": 'eight8eight', "nine": 'nine9nine'} 
``` 
impacted the answer, b/c with the first one if there is a string like twone, then that would become tw1 bc 1 is the first key in the dictionary and the two is lost which changes the answer. However, with the second one, that would become twone1one, which preseves the two in the string. This results in the final string becoming two2twone1one. This dictionary allows the written numbers to be properly transformed without losing any numbers. 


