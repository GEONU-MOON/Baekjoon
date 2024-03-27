import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]
distance = [0] * (N + 1)  # 거리 체크용
visit = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    tree[A].append(B)


def bfs(x, k):
    res = []  # 출력용
    queue = deque([x])
    visit[x] = True
    # 인접한 노드 거리 확인
    while queue:
        x = queue.popleft()
        for i in tree[x]: 
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                distance[i] = distance[x] + 1 # 처음 x를 기준으로 거리 체크
                if distance[i] == k: # 원하고자하는 거리인 i발견시 출력리스트에 추가
                    res.append(i)
    if len(res) == 0: # 출력할 도시가 없으면 -1 반환
        print(-1)
    else:
        res.sort() # 오름차순으로 출력
        for i in range(len(res)):
            print(res[i])


bfs(X, K)