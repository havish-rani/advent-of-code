# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        safe_count = 0 
        for line in self.input: 
            report = line.split()
            safe_dec = False
            safe_inc = False
            report = list(map(int,report))
            if all((report[i] > report[i+1]) & (abs(report[i] - report[i+1]) <= 3) for i in range(len(report)-1)):
                safe_dec = True
                print("increasing list")
            if all((report[i] < report[i+1]) & (abs(report[i] - report[i+1]) <= 3) for i in range(len(report)-1)):
                safe_inc = True
                print("decreasing list")

            # for i in range(len(report)-1): 
            #     if (abs(report[i] - report[i+1]) > 3): 
            #         safe = False
            #     # if (report[i])
            #     # print(i)
            if safe_dec or safe_inc: safe_count += 1
        return safe_count
            # print(report)
            
        

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
