# Day 3 (2024)

`TITLE` ([prompt](https://adventofcode.com/2024/day/3))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1
started using some simple list comprehension 
```python
nums = [int(num) for num in nums]
```   
once again used regex, was very easy for part one
## Part 2
was confused how to make a regex for part two  
turned out easiest was was keeping the same one as part one, and adding do() and don't() as alternative cases  
this allowed to iterate through all the matches from the regex, and when hitting a don't() match, set a boolean to false and set a boolean to true when hitting a do() match to know when to increment the count. 

