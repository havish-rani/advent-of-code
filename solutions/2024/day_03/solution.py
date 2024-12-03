# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2024
    _day = 3

    @answer(162813399)
    def part_1(self) -> int:
        mul_sum = 0
        for line in self.input: 
            matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
            for match in matches: 
                # print(match)
                nums = re.findall(r'\d+', match)
                nums = [int(num) for num in nums]
                # print("Nums: ", nums)
                mul_sum += (nums[0]*nums[1])
                # print(mul_sum)
            # print(matches)
        return mul_sum

    @answer(53783319)
    def part_2(self) -> int:
        mul_sum = 0
        print(self.input)  
        do_flag = True
        for line in self.input:   
            matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
            print("matches: ", matches)
            for match in matches: 
                if match == 'do()': 
                    do_flag = True
                elif match == "don't()":
                    do_flag = False
                else: 
                    if do_flag: 
                        nums = re.findall(r'\d+', match)
                        nums = [int(num) for num in nums]
                        print("Nums: ", nums)
                        mul_sum += (nums[0]*nums[1])
                print(match)

        return mul_sum

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
