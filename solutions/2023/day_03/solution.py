# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import StrSplitSolution, answer
import re
from collections import defaultdict
from operator import mul 

class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    def padded_input(self) -> list[str]:
        width = len(self.input[0])
        # ensure every line is the same length; we'll mess up lines if it's not
        assert all(len(l) == width for l in self.input)

        return [
            "." * (width + 2),
            *[f".{l}." for l in self.input],
            "." * (width + 2),
        ]

    @answer(521515)
    def part_1(self) -> int:
        sum = 0
        # print(type(self.input))
        # print(len(self.input[0]))
        list_len = len(self.input)
        # matches = re.finditer(r'\d+', str(self.input))
        # print("len str: ", len(str(self.input)))
        symbols = re.compile(r'[^\w.]')
        # count = 0
        for line_num, line in enumerate(self.input): 
            # print("lineA: ", line)
            matches = re.finditer(r'\d+', line)
            for match in matches:
                # above check 
                symbol_flag = False
                if line_num != 0: 
                    line_to_search = self.input[line_num - 1]
                    # print("Line2: ", line_to_search)
                    if match.start() == 0: 
                        if symbols.search(line_to_search[match.start():match.end()+1]) != None: 
                            # print("line above: ", line_to_search[match.start():match.end()+1])
                            symbol_flag = True
                    elif match.end() == len(line)-1: 
                       if symbols.search(line_to_search[match.start()-1:match.end()]) != None: 
                            # print("line above: ", line_to_search[match.start()-1:match.end()])
                            symbol_flag = True
                    else: 
                        if symbols.search(line_to_search[match.start()-1:match.end()+1]) != None: 
                            # print("line above: ", line_to_search[match.start()-1:match.end()+1])
                            symbol_flag = True 
                # below check 
                if line_num != list_len - 1: 
                    line_to_search = self.input[line_num + 1]
                    # print("Line2: ", line_to_search)
                    if match.start() == 0: 
                        if symbols.search(line_to_search[match.start():match.end()+1]) != None: 
                            # print("line below: ", line_to_search[match.start():match.end()+1])
                            symbol_flag = True
                    elif match.end() == len(line)-1: 
                       if symbols.search(line_to_search[match.start()-1:match.end()]) != None: 
                            # print("line below: ", line_to_search[match.start()-1:match.end()])
                            symbol_flag = True
                    else: 
                        if symbols.search(line_to_search[match.start()-1:match.end()+1]) != None: 
                            # print("line below: ", line_to_search[match.start()-1:match.end()+1])
                            symbol_flag = True 
                # left check 
                if (match.start() > 0): 
                    # print("line left: ", line[match.start()-1])
                    if symbols.search(line[match.start()-1]) != None: 
                        symbol_flag = True
                # right check 
                if (match.end () < len(line)-1): 
                    # print("line right: ", line[match.end()])
                    if symbols.search(line[match.end()]) != None: 
                        symbol_flag = True
                if symbol_flag: 
                    sum += int(match.group())
                    # print("Parts Num: ", match.group())
            # count += 1
            # if count == 20: break
        return sum
        

    @answer(69527306)
    def part_2(self) -> int:
        # sum = 0
        # print(type(self.input))
        # print(len(self.input[0]))
        list_len = len(self.input)
        # matches = re.finditer(r'\d+', str(self.input))
        # print("len str: ", len(str(self.input)))
        symbols = re.compile(r'\*')
        # count = 0
        gear_dict = defaultdict(list)
        for line_num, line in enumerate(self.input): 
            print("lineA: ", line)
            numbers = re.finditer(r'\d+', line)
            for number in numbers:
                # above check 
                if line_num != 0: 
                    line_to_search = self.input[line_num - 1]
                    # print("Line2: ", line_to_search)
                    if number.start() == 0: 
                        if symbols.search(line_to_search[number.start():number.end()+1]) != None:
                            key = str(line_num-1) + str(number.start() + line_to_search[number.start():number.end()+1].find('*'))
                            gear_dict[key].append(int(number.group()))
                    elif number.end() == len(line)-1: 
                       if symbols.search(line_to_search[number.start()-1:number.end()]) != None: 
                            key = str(line_num-1) + str(number.start() - 1 + line_to_search[number.start()-1:number.end()].find('*'))
                            gear_dict[key].append(int(number.group()))
                    else: 
                        if symbols.search(line_to_search[number.start()-1:number.end()+1]) != None: 
                            key = str(line_num-1) + str(number.start() -1 + line_to_search[number.start()-1:number.end()+1].find('*'))
                            gear_dict[key].append(int(number.group()))
                # below check 
                if line_num != list_len - 1: 
                    line_to_search = self.input[line_num + 1]
                    if number.start() == 0: 
                        if symbols.search(line_to_search[number.start():number.end()+1]) != None: 
                            key = str(line_num+1) + str(number.start() + line_to_search[number.start():number.end()+1].find('*'))
                            gear_dict[key].append(int(number.group()))
                            print("key: ", key)
                    elif number.end() == len(line)-1: 
                       if symbols.search(line_to_search[number.start()-1:number.end()]) != None: 
                            key = str(line_num+1) + str(number.start() - 1 + line_to_search[number.start()-1:number.end()].find('*'))
                            gear_dict[key].append(int(number.group()))
                            print("key: ", key)
                    else: 
                        if symbols.search(line_to_search[number.start()-1:number.end()+1]) != None: 
                            key = str(line_num+1) + str(number.start() -1 + line_to_search[number.start()-1:number.end()+1].find('*'))
                            gear_dict[key].append(int(number.group()))
                            print("key: ", key)
                # left check 
                if (number.start() > 0): 
                    if symbols.search(line[number.start()-1]) != None: 
                        key = str(line_num) + str(number.start() - 1)
                        gear_dict[key].append(int(number.group()))
                # right check 
                if (number.end () < len(line)-1): 
                    # print("line right: ", line[number.end()])
                    if symbols.search(line[number.end()]) != None:
                        key = str(line_num) + str(number.end()) 
                        gear_dict[key].append(int(number.group()))
        # gears: dict[tuple[int, int], list[int]] = defaultdict(list)
        # grid = self.padded_input()

        # for line_num, line in enumerate(grid):
        #     for number in re.finditer(r"\d+", line):
        #         # A
        #         if "*" in (
        #             l := grid[line_num - 1][number.start() - 1 : number.end() + 1]
        #         ):
        #             assert l.count("*") == 1
        #             gears[(line_num - 1, number.start() - 1 + l.index("*"))].append(
        #                 int(number.group())
        #             )

        #         # B
        #         if line[number.start() - 1] == "*":
        #             gears[(line_num, number.start() - 1)].append(int(number.group()))

        #         # C
        #         if line[number.end()] == "*":
        #             gears[(line_num, number.end())].append(int(number.group()))

        #         # D
        #         if "*" in (
        #             l := grid[line_num + 1][number.start() - 1 : number.end() + 1]
        #         ):
        #             assert l.count("*") == 1
        #             gears[(line_num + 1, number.start() - 1 + l.index("*"))].append(
        #                 int(number.group())
        #             )
        return sum([mul(*nums) for nums in gear_dict.values() if len(nums) == 2])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
10252318
9500176
69527306