# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
from itertools import cycle

class Solution(StrSplitSolution):
    _year = 2024
    _day = 6
    direction = 'up'

    GridPoint = tuple[int, int]
    Grid = dict[GridPoint, str]
    # visited_locs = set()

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
    
    def guard_loc_grid(self,grid): 
        for k,v in grid.items(): 
            if v == '^': 
                return k
            
    def parse_grid(self,raw_grid: list[str]):
        """
        returns 2-tuples of (row, col) with their value
        """
        result = {}

        for row, line in enumerate(raw_grid):
            for col, c in enumerate(line):
                result[row, col] = c

        return result
    
    # def move_grid(self,grid): 
    #     grid = self.parse_grid(self.input)
    #     guard_loc = self.guard_loc_grid(grid)
    #     self.visited_locs.add((guard_loc,self.direction))
    #     while True: 
    @answer(4752)
    def part_1(self) -> int:
        #first way
        # left_grid = False
        # padded_mat = [list(row) for row in self.input]
        # row_len = len(padded_mat[0])
        # loc = self.guard_loc(padded_mat)
        
        #grid way
        grid = self.parse_grid(self.input)
        guard_loc = self.guard_loc_grid(grid)
        visited_locs = set()
        visited_locs.add(guard_loc)
        print("guard loc: ", guard_loc)
        # print("row_len: ", row_len)
        while True: 
            # loc = self.guard_loc(padded_mat)
            # print("loc: ", loc)
            #because of the loc[0] and loc[1] checks in the while, when it is about to leave the grid,
            #it just turns 90 degrees and does an inf loop
            #try putting an if with the loc[0] and loc[1] checks before the while statements in each if
            if self.direction == 'up': 
                next_loc = (guard_loc[0] - 1, guard_loc[1]) 
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                else: 
                    guard_loc = next_loc
                    visited_locs.add(guard_loc)
                # while padded_mat[loc[0]-1][loc[1]] != '#' : 
                #     padded_mat[loc[0]][loc[1]] = 'X'
                #     loc = (loc[0]-1,loc[1])
                #     padded_mat[loc[0]][loc[1]] = '^'
                #     print("up loc: ", loc)
                #     if loc[0] <= 0: 
                #         left_grid = True
                #         break
                # else: 
                #     self.turn_90()
            elif self.direction == 'right': 
                next_loc = (guard_loc[0], guard_loc[1]+1) 
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                else: 
                    guard_loc = next_loc
                    visited_locs.add(guard_loc)
                # while padded_mat[loc[0]][loc[1]+1] != '#': 
                #     padded_mat[loc[0]][loc[1]] = 'X'
                #     loc = (loc[0],loc[1]+1)
                #     padded_mat[loc[0]][loc[1]] = '^'
                #     print("right loc: ", loc)
                #     if loc[1] >= (row_len-1): 
                #         left_grid = True
                #         break
                # else: 
                #     self.turn_90()
            elif self.direction == 'down':
                next_loc = (guard_loc[0]+1, guard_loc[1]) 
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                else: 
                    guard_loc = next_loc
                    visited_locs.add(guard_loc)
                # while padded_mat[loc[0]+1][loc[1]] != '#': 
                #     padded_mat[loc[0]][loc[1]] = 'X'
                #     loc = (loc[0]+1,loc[1])
                #     padded_mat[loc[0]][loc[1]] = '^'
                #     print("down loc: ", loc)
                #     if loc[0] >= len(padded_mat) - 1: 
                #         print("in break")
                #         left_grid = True
                #         break
                # else: 
                #     self.turn_90()
            elif self.direction == 'left': 
                next_loc = (guard_loc[0], guard_loc[1]-1)
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                else: 
                    guard_loc = next_loc
                    visited_locs.add(guard_loc)
                # while padded_mat[loc[0]][loc[1]-1] != '#': 
                #     padded_mat[loc[0]][loc[1]] = 'X'
                #     loc = (loc[0],loc[1]-1)
                #     padded_mat[loc[0]][loc[1]] = '^'
                #     print("left loc: ", loc)
                #     if loc[1] <= 0: 
                #         left_grid = True
                #         break
                # else: 
                #     self.turn_90()

        # print(padded_mat)
        # print("dir: ", self.direction)
        # distinct_locs = sum(row.count('X') for row in padded_mat)
        # with open("new.txt","w") as file: 
        #     for row in padded_mat: 
        #         file.write(str(row) + '\n')
        # print("visited locs: ", visited_locs)
        return len(visited_locs)


    def part_2_help(self, grid): 
        OFFSETS = cycle(['up', 'right', 'down', 'left'])
        offset = next(OFFSETS)
        guard_loc = next(k for k, v in grid.items() if v == "^")
        visited_locs = set()
        visited_locs.add((guard_loc,offset))
        while True: 
            # print("visited locs: ", visited_locs)
            if offset == 'up': 
                next_loc = guard_loc[0] - 1, guard_loc[1]
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                    offset = next(OFFSETS)
                    visited_locs.add((guard_loc,offset))
                else: 
                    to_add = next_loc,offset
                    # print("to add: ", to_add)
                    if to_add in visited_locs: 
                        return False
                    visited_locs.add(to_add)
                    guard_loc = next_loc
            elif offset == 'right': 
                next_loc = guard_loc[0], guard_loc[1]+1
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                    offset = next(OFFSETS)
                    visited_locs.add((guard_loc,offset))
                else:  
                    to_add = next_loc,offset
                    # print("to add: ", to_add)
                    if to_add in visited_locs: 
                        return False
                    visited_locs.add(to_add)
                    guard_loc = next_loc
            elif offset == 'down': 
                next_loc = guard_loc[0]+1, guard_loc[1]
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                    offset = next(OFFSETS)
                    visited_locs.add((guard_loc,offset))
                else: 
                    to_add = next_loc,offset
                    # print("to add: ", to_add)
                    if to_add in visited_locs: 
                        return False
                    visited_locs.add(to_add)
                    guard_loc = next_loc
            elif offset == 'left': 
                next_loc = guard_loc[0], guard_loc[1]-1
                if next_loc not in grid: 
                    break
                if grid[next_loc] == '#': 
                    self.turn_90()
                    offset = next(OFFSETS)
                    # print("dir: ", self.direction)
                    visited_locs.add((guard_loc,offset))
                else: 
                    to_add = next_loc,offset
                    # print("to add: ", to_add)
                    if to_add in visited_locs: 
                        return False
                    visited_locs.add(to_add)
                    guard_loc = next_loc    
        return True
    
    

    # @answer(1234)
    def part_2(self) -> int:
        grid = self.parse_grid(self.input)
        possible_loops = 0     
        for loc in grid:
            if grid[loc] != ".": 
                continue 
            grid[loc] = "#"
            val = self.part_2_help(grid)
            if not val: 
                possible_loops += 1
            grid[loc] = "."
        return possible_loops

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
