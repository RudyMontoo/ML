from pyamaze import maze, agent

def DFS(m):
    start = (m.rows, m.cols)
    stack = [start]
    explored = [start]
    dfsPath = {}
    while len(stack) > 0:
        currCell = stack.pop()
        if currCell == (1,1):
            break
        for d in 'ESNW':  # East, South, North, West
            if m.maze_map[currCell][d] == 1:
                if d == 'E':
                    child = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    child = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    child = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    child = (currCell[0]+1, currCell[1])
                if child not in explored:
                    stack.append(child)
                    explored.append(child)
                    dfsPath[child] = currCell
    fwdPath = {}
    cell = (1,1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath

m = maze(5, 5)
m.CreateMaze()
path = DFS(m)
a = agent(m, footprints=True)
m.tracePath({a: path})
m.run()