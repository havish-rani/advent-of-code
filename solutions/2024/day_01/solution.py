# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    def left_right(self) -> tuple[list[int],list[int]]: 
        count = 0
        left = []
        right = []
        for line in self.input: 
            # print(type(line))
            # print("line: ", line)
            line_split = line.split()
            # print(line_split)
            for i in range(len(line_split)): 
                # print("i: ", i)
                if i%2 == 0: 
                    left.append(int(line_split[i]))
                elif i%2 == 1: 
                    right.append(int(line_split[i]))
        left.sort()
        right.sort()
        return (left,right)

    @answer(936063)
    def part_1(self) -> int:
        left,right = self.left_right()
        diff = 0
        for i in range(len(left)): 
            diff += abs(left[i] - right[i])
        return diff


    @answer(23150395)
    def part_2(self) -> int:
        left,right = self.left_right()
        similarity_score = 0
        for i in range(len(left)): 
            freq = right.count(left[i])
            similarity_score += (left[i] * freq)
        return similarity_score

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
