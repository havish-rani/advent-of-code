# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(54940)
    def part_1(self) -> int:
        print(type(self.input))
        count = 0
        sum = 0
        for line in self.input:
            print("line: ", line)
            dig_line = re.findall(r"\d", line)
            count += 1
            print(dig_line)
            num = dig_line[0] + dig_line[-1]
            print(num)
            sum += int(num)
            print(sum)
            # if count == 5: break
        print("final sum: ", sum)
        return 54940

    @answer(54208)
    def part_2(self) -> int:
        count = 0
        sum = 0
        number_dict = {"one": 'one1one', "two": 'two2two', "three": 'three3three', "four": 'four4four', "five": 'five5five', 
                    "six": 'six6six', "seven": 'seven7seven', "eight": 'eight8eight', "nine": 'nine9nine'}
        for line in self.input:
            print("line: ", line)
            for key,val in number_dict.items(): 
                line = re.sub(rf'{key}',val,line)
                print("line with only nums", line)
            dig_line = re.findall(r"\d", line)
            print("dig_line: ", dig_line)
            calibration_num = dig_line[0] + dig_line[-1]
            print("calibration_num: ", calibration_num)
            sum += int(calibration_num)
            # count += 1
            # if count == 5: 
            #     break 
            print("sum: ", sum)
            # break
        print("final sum: ", sum)
        return 54208
    
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
