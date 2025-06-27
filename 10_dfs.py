def dfs(maze, n):
    if maze[1][1] == 1 or maze[n][n] == 1:
        return "SAD"
    
    stack = [(1, 1)]
    visited = [[False] * (n + 1) for _ in range(n+1)]
    visited[1][1] = True

    while stack:
        r, c = stack.pop()
        if r == n and c == n:
            return "HAPPY"
        


if __name__ == "__main__":
    n = int(input())
    maze = [0]
    for _ in range(n):
        maze.append([0] + list(map(int, input().split())))
