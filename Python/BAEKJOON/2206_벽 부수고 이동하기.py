import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def BFS(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        if a == N - 1 and b == M - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
    return -1

print(BFS(0, 0, 0))