"""grid.py
Grid and map parsing utilities.
"""
from typing import List, Tuple, Dict, Optional
import math

class Grid:
    def __init__(self, rows:int, cols:int, cells:List[List[int]]):
        self.rows = rows
        self.cols = cols
        self.cells = cells  # integer movement cost >=0; 1 or 0 treated as cost 1; 1 obstacle indicated by large sentinel

    def in_bounds(self, r:int, c:int)->bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def passable(self, r:int, c:int)->bool:
        return self.cells[r][c] != 1  # here 1 is obstacle in maps; adjust if you want explicit sentinel

    def cost(self, r:int, c:int)->int:
        v = self.cells[r][c]
        if v == 0:
            return 1
        return v

    def neighbors(self, r:int, c:int, diagonals:bool=False):
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        if diagonals:
            dirs += [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if self.in_bounds(nr,nc) and self.passable(nr,nc):
                yield nr,nc

def load_map_simple(path:str)->Grid:
    with open(path,'r') as f:
        tokens = []
        for line in f:
            line=line.strip()
            if not line or line.startswith('#'):
                continue
            tokens.extend(line.split())
    rows = int(tokens[0]); cols = int(tokens[1])
    vals = list(map(int, tokens[2:2+rows*cols]))
    cells = [vals[i*cols:(i+1)*cols] for i in range(rows)]
    return Grid(rows,cols,cells)
