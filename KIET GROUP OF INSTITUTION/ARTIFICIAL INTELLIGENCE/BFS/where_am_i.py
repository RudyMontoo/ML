from pyamaze import maze, agent

def BFS(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
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
                    frontier.append(child)
                    explored.append(child)
                    bfsPath[child] = currCell
    fwdPath = {}
    cell = (1,1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath

m = maze(5, 5)
m.CreateMaze()
path = BFS(m)
a = agent(m, footprints=True)
m.tracePath({a: path})
m.run()