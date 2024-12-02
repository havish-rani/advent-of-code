# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2
    unsafe_reports = []
    part_1_ans = 0

    def increasing(self,report): 
        return all((report[i] > report[i+1]) & (abs(report[i] - report[i+1]) <= 3) for i in range(len(report)-1))
    
    def decreasing(self,report): 
        return all((report[i] < report[i+1]) & (abs(report[i] - report[i+1]) <= 3) for i in range(len(report)-1))

    @answer(463)
    def part_1(self) -> int:
        safe_count = 0 
        for line in self.input: 
            report = line.split()
            safe_dec = False
            safe_inc = False
            report = list(map(int,report))
            if self.increasing(report):
                safe_dec = True
                # print("increasing list")
            elif self.decreasing(report):
                safe_inc = True
                # print("decreasing list")
            else: 
                self.unsafe_reports.append(report)
            if safe_dec or safe_inc: safe_count += 1
        self.part_1_ans = safe_count
        return safe_count
    
    @answer(514)
    def part_2(self) -> int:
        dampened_count = 0
        for report in self.unsafe_reports: 
            dampened = False
            for i in range(len(report)): 
                copy = report.copy()
                copy.pop(i)
                if (self.increasing(copy) or self.decreasing(copy)): 
                    dampened = True
                    # self.debug(copy)
            # print(report)
            if dampened: dampened_count += 1
        return dampened_count + self.part_1_ans



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
