"""search.py
Contains BFS, UCS, A* implementations. Returns path, cost, nodes_expanded, time.
"""
import time
from collections import deque
import heapq
from typing import Tuple, List, Dict

def reconstruct_path(came_from, start, goal):
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from[cur]
    path.append(start)
    path.reverse()
    return path

def bfs(grid, start, goal):
    t0 = time.time()
    frontier = deque([start])
    came_from = {start: None}
    nodes = 0
    while frontier:
        cur = frontier.popleft()
        nodes += 1
        if cur == goal:            path = reconstruct_path(came_from,start,goal)            return path, len(path)-1, nodes, time.time()-t0
        for nbr in grid.neighbors(*cur):
            if nbr not in came_from:
                came_from[nbr]=cur
                frontier.append(nbr)
    return None, float('inf'), nodes, time.time()-t0

def ucs(grid, start, goal):
    t0 = time.time()
    pq = []
    heapq.heappush(pq, (0, start))
    cost_so_far = {start:0}
    came_from = {}
    nodes=0
    while pq:
        c, cur = heapq.heappop(pq)
        nodes+=1
        if cur==goal:
            path = reconstruct_path(came_from, start, goal)
            return path, c, nodes, time.time()-t0
        for nbr in grid.neighbors(*cur):
            new_cost = c + grid.cost(*nbr)
            if nbr not in cost_so_far or new_cost < cost_so_far[nbr]:
                cost_so_far[nbr]=new_cost
                heapq.heappush(pq, (new_cost, nbr))
                came_from[nbr]=cur
    return None, float('inf'), nodes, time.time()-t0

def manhattan(a,b):
    (x1,y1),(x2,y2) = a,b
    return abs(x1-x2)+abs(y1-y2)

def astar(grid, start, goal, heuristic=manhattan):
    t0=time.time()
    pq=[]
    heapq.heappush(pq,(0+heuristic(start,goal),0,start))
    cost_so_far={start:0}
    came_from={}
    nodes=0
    while pq:
        f,c,cur = heapq.heappop(pq)
        nodes+=1
        if cur==goal:
            path=reconstruct_path(came_from,start,goal)
            return path, c, nodes, time.time()-t0
        for nbr in grid.neighbors(*cur):
            new_cost = c + grid.cost(*nbr)
            if nbr not in cost_so_far or new_cost < cost_so_far[nbr]:
                cost_so_far[nbr]=new_cost
                heapq.heappush(pq,(new_cost+heuristic(nbr,goal), new_cost, nbr))
                came_from[nbr]=cur
    return None, float('inf'), nodes, time.time()-t0
