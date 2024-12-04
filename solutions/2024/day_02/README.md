# Day 2 (2024)

`TITLE` ([prompt](https://adventofcode.com/2024/day/2))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1
used the all() function in python for the first time with some list comprehension  
can use this function to iterate over a list and check a condition, and it has to be true for all elements for all()  to return true, otherwise it returns false.  
There is another function called any() that works in the same way as all() except it returns true when the condition is matched just once. 
```python
all((report[i] > report[i+1]) & (abs(report[i] - report[i+1]) <= 3) for i in range(len(report)-1))
``` 
## Part 2

