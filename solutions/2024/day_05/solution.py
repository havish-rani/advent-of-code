# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import StrSplitSolution, answer
from collections import defaultdict
import math

class Solution(StrSplitSolution):
    _year = 2024
    _day = 5
    invalid = []
    def parsing(self): 
        rules_before = defaultdict(list)
        rules_after = defaultdict(list)
        outputs = []
        for line in self.input: 
            if '|' in line: 
                x,y = line.split('|')
                rules_before[int(x)].append(int(y))
                rules_after[int(y)].append(int(x))
            elif len(line) != 0: 
                nums = line.split(',')
                nums = [int(n) for n in nums]
                outputs.append(nums)
        return rules_before, rules_after,outputs
    
    @answer(5329)
    def part_1(self) -> int:
        rules_before, rules_after, outputs = self.parsing()
        print("rules before: ", rules_before) 
        print("rules after: ", rules_after)
        print("outputs: ", outputs)
        middle_num_sum = 0
        for output in outputs: 
            flag = True
            for i in range(len(output)): 
                # if any([a not in rules_before[output[i]] for a in output[i+1:]]) or any([b not in rules_after[output[i]] for b in output[:i]]):
                for j in range(i+1,len(output)): 
                    if (output[j] not in rules_before[output[i]]):
                        flag = False
                
                #For part one I parsed the rules into a dictionary of pageNo : [pagesThatMustComeAfter], 
                # and just went through the numbers in the line, checking if any of the previously seen 
                # pages should've come afterwards
                # before = output[:i]
                # if any(b not in rules_after[output[i]] for b in before): 
                #     flag = False
                    
            if flag: 
                mid_index = len(output) // 2
                middle_num_sum += output[mid_index]

            else: 
                self.invalid.append(output)
        return middle_num_sum

    @answer(5833)
    def part_2(self) -> int:
        rules_before, _, _ = self.parsing()
        sum = 0
        for inv in self.invalid: 
            for i in range(len(inv)): 
                for j in range(i+1,len(inv)): 
                    if (inv[j] not in rules_before[inv[i]]):
                        a, b = inv[i], inv[j]
                        inv[j], inv[i] = a,b
                print("inv: ", inv)
        for inv in self.invalid: 
            sum += inv[len(inv) // 2]                 
        return sum   

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
