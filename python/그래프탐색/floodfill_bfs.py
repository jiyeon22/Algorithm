from collections import deque
n = int(input()) #배열 크기 n
x, y = map(int, input().split()) #1-based 기준 좌표
x, y = x-1, y-1 # 0-based 기준좌표

m = [] 
v = [[0]*n for _ in range(n)] #방문 여부 체크용 배열

for _ in range(n):
    m.append(list(map(int, input().split()))) # 각 행 입력

k = m[x][y] #기준 위치의 값

#상, 우, 하, 좌 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0 # 가장 큰 덩어리 크기

for i in range(n):
    for j in range(n):
        if v[i][j] or m[i][j] != k:
            continue #현재 반복문의 남은 부분을 건너 뛰고, 다음 반복으로 바로 넘어가는 것.
        q = deque()
        count = 0
        v[i][j] = 1
        q.append([i,j])
        while q:
            cx, cy = q.popleft()
            count += 1 
            for z in range(4): 
                nx, ny = cx +dx[z], cy + dy[z]
                if nx < 0 or ny < 0 or nx >=n or ny >=n:
                    continue
                if v[nx][ny] or m[nx][ny] != k:
                    continue
                v[nx][ny] = 1
                q.append([nx,ny])
        result = max(result, count)

print(result)