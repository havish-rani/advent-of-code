# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer
import re
from collections import defaultdict


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4
    X_list = []

    def padded_input(self):
        width = len(self.input[0])
        # ensure every line is the same length; we'll mess up lines if it's not
        assert all(len(l) == width for l in self.input)

        padded_list =  [
            "." * (width + 8),
            "." * (width + 8),
            "." * (width + 8),
            "." * (width + 8),
            *[f"....{l}...." for l in self.input],
            "." * (width + 8),
            "." * (width + 8),
            "." * (width + 8),
            "." * (width + 8),
        ]

        padded_mat = [list(row) for row in padded_list]
        print(type(padded_mat))
        return padded_mat


    def ne_diag_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            # print("x: ", x)
            # print("y: ", y)
            if padded[x+1][y-1] == 'M' and padded[x+2][y-2] == 'A' and padded[x+3][y-3] == 'S': 
                count += 1
        return count
    def se_diag_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            if padded[x+1][y+1] == 'M' and padded[x+2][y+2] == 'A' and padded[x+3][y+3] == 'S': 
                count += 1
        return count
    def sw_diag_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            if padded[x-1][y+1] == 'M' and padded[x-2][y+2] == 'A' and padded[x-3][y+3] == 'S': 
                count += 1
        return count
    def nw_diag_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            if padded[x-1][y-1] == 'M' and padded[x-2][y-2] == 'A' and padded[x-3][y-3] == 'S': 
                count += 1
        return count
    def right_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            if padded[x][y+1] == 'M' and padded[x][y+2] == 'A' and padded[x][y+3] == 'S': 
                count += 1
        return count
    def left_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            if padded[x][y-1] == 'M' and padded[x][y-2] == 'A' and padded[x][y-3] == 'S': 
                count += 1
        return count
    def up_check(self,padded):
        count = 0 
        for (x,y) in self.X_list: 
            if padded[x-1][y] == 'M' and padded[x-2][y] == 'A' and padded[x-3][y] == 'S': 
                count += 1
        return count
    def down_check(self,padded): 
        count = 0
        for (x,y) in self.X_list: 
            if padded[x+1][y] == 'M' and padded[x+2][y] == 'A' and padded[x+3][y] == 'S': 
                count += 1
        return count

    
    @answer(2401)
    def part_1(self) -> int:
        padded = self.padded_input()
        for row in range(len(padded)): 
            for col,val in enumerate(padded[row]): 
                if val == 'X': 
                    self.X_list.append((row,col))
        print("x list: ", self.X_list)
        count = (self.ne_diag_check(padded) + self.se_diag_check(padded) + self.sw_diag_check(padded) 
                + self.nw_diag_check(padded) + self.right_check(padded) + self.left_check(padded) + self.up_check(padded)
                + self.down_check(padded))
        return count
            

    @answer(1822)
    def part_2(self) -> int:
        width = len(self.input[0])
        padded_list =  [
            "." * (width + 2),
            *[f".{l}." for l in self.input],
            "." * (width + 2),
        ]

        padded_mat = [list(row) for row in padded_list]
        a_list = []
        for row in range(len(padded_mat)): 
            for col,val in enumerate(padded_mat[row]): 
                if val == 'A': 
                    a_list.append((row,col))
        count = 0
        for (x,y) in a_list: 
            diag_one = str(padded_mat[x-1][y-1] + padded_mat[x][y] + padded_mat[x+1][y+1])
            diag_two = str(padded_mat[x+1][y-1] + padded_mat[x][y] + padded_mat[x-1][y+1])
            if ((diag_one == "MAS" or diag_one == "SAM") and (diag_two == "MAS" or diag_two == "SAM")): 
                count += 1
        return count


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
