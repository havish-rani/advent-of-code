# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6
    direction = 'up'

    def turn_90(self): 
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down': 
            self.direction = 'left'
        elif self.direction == 'left': 
            self.direction = 'up'

    def guard_loc(self,padded_mat): 
        for row in range(len(padded_mat)): 
            if '^' in padded_mat[row]: 
                loc = (row,padded_mat[row].index('^'))
        return loc
    
    def move(self, padded_mat,loc): 
        if self.direction == 'up': 
            while padded_mat[loc[0]-1][loc[1]] != '#': 
                padded_mat[loc] = 'X'
                loc = (loc[0]-1,loc[1])
                padded_mat[loc] = '^'
            

    @answer(4752)
    def part_1(self) -> int:
        left_grid = False
        padded_mat = [list(row) for row in self.input]
        row_len = len(padded_mat[0])
        print("row_len: ", row_len)
        loc = self.guard_loc(padded_mat)
        while not left_grid: 
            loc = self.guard_loc(padded_mat)
            # print("loc: ", loc)
            #because of the loc[0] and loc[1] checks in the while, when it is about to leave the grid,
            #it just turns 90 degrees and does an inf loop
            #try putting an if with the loc[0] and loc[1] checks before the while statements in each if
            if self.direction == 'up': 
                while padded_mat[loc[0]-1][loc[1]] != '#' : 
                    padded_mat[loc[0]][loc[1]] = 'X'
                    loc = (loc[0]-1,loc[1])
                    padded_mat[loc[0]][loc[1]] = '^'
                    print("up loc: ", loc)
                    if loc[0] <= 0: 
                        left_grid = True
                        break
                else: 
                    self.turn_90()
            elif self.direction == 'right': 
                while padded_mat[loc[0]][loc[1]+1] != '#': 
                    padded_mat[loc[0]][loc[1]] = 'X'
                    loc = (loc[0],loc[1]+1)
                    padded_mat[loc[0]][loc[1]] = '^'
                    print("right loc: ", loc)
                    if loc[1] >= (row_len-1): 
                        left_grid = True
                        break
                else: 
                    self.turn_90()
            elif self.direction == 'down':
                while padded_mat[loc[0]+1][loc[1]] != '#': 
                    padded_mat[loc[0]][loc[1]] = 'X'
                    loc = (loc[0]+1,loc[1])
                    padded_mat[loc[0]][loc[1]] = '^'
                    print("down loc: ", loc)
                    if loc[0] >= len(padded_mat) - 1: 
                        print("in break")
                        left_grid = True
                        break
                else: 
                    self.turn_90()
            elif self.direction == 'left': 
                while padded_mat[loc[0]][loc[1]-1] != '#': 
                    padded_mat[loc[0]][loc[1]] = 'X'
                    loc = (loc[0],loc[1]-1)
                    padded_mat[loc[0]][loc[1]] = '^'
                    print("left loc: ", loc)
                    if loc[1] <= 0: 
                        left_grid = True
                        break
                else: 
                    self.turn_90()

        print(padded_mat)
        print("dir: ", self.direction)
        distinct_locs = sum(row.count('X') for row in padded_mat)
        # with open("new.txt","w") as file: 
        #     for row in padded_mat: 
        #         file.write(str(row) + '\n')
        return distinct_locs + 1
    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
