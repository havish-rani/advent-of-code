# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2331)
    def part_1(self) -> int:
        count = 0
        sum = 0
        for index, game_info in enumerate(self.input,start=1): 
            flag = True
            # index, game_info = line.split(":")
            print("Index: ", index) 
            _, game_info = game_info.split(":")
            print("Game Info: ", game_info)
            color_dict = {"red": 12, "green": 13, "blue": 14}
            color_list = ['red', 'blue', 'green']
            for color in color_list: 
                color_nums = re.findall(rf'\d+ {color}',game_info)
                print("color_nums: ", color_nums)
                nums = re.findall(r'\d+',str(color_nums))
                print("nums: ", nums)
                for num in nums: 
                    if int(num) > color_dict[color]: 
                        flag = False
            # for num, color in color_nums: 
            #     print("sum: ", sum)
            #     if int(num) > color_dict[color]: 
            #         print("num: ", num)
            #         print("color: ", color)
            #         flag = False 
            if flag: sum += index
            # count += 1
            # if count == 5: break
        return sum

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
