# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer(1086)
    def part_1(self) -> int:
        current_val = 50
        zero_count = 0
        for line in self.input: 
            dir = line[0:1]
            amount = line[1:]

            if dir == 'L':
                int_amt = int(amount) % 100
                print("int_amt: ", int_amt)
                if current_val - int_amt >= 0: 
                    current_val -= int_amt

                else: 
                    new_amt = 100 - int_amt
                    current_val += new_amt
                # print(dir)
                # print(amount)
                print("current_val: ", current_val)
            elif dir == 'R':
                int_amt = int(amount) % 100
                if current_val + int_amt <= 99: 
                    current_val += int_amt
                else: 
                    new_amt = 100 - int_amt
                    current_val -= new_amt
                # print(dir)
                # print(amount)
                print("current_val: ", current_val)
            if current_val == 0: 
                zero_count += 1
        return zero_count

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
