# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(936063)
    def part_1(self) -> int:
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
            # count += 1 
            # if count == 5: break
        print("left: ", left)
        print("right: ", right)
        left.sort()
        right.sort()
        print("left sort: ", left)
        print("right sort: ", right)
        diff = 0
        for i in range(len(left)): 
            diff += abs(left[i] - right[i])
        return diff


    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
