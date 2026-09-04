"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]


"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []

    # 시작 지점을 visited에 삽입
    visited.append(start)
    queue=deque() #deque는 클래스 자체여서 객체를 실제로 만들고 사용해야 함.
    i=0

    while len(visited)<len(graph):
        # 시작 지점과 연결된 정점들을 deque에 삽입 
        for num in graph[visited[i]]:
            queue.append(num)
        
        # for value in queue:
        while queue: # 🚨 queue 순회 시, for 문이 아닌 큐가 빌때까지 하나씩 꺼내쓰는 방식 사용해야 
            current=queue.popleft()
            if current not in visited:
                visited.append(current)
        i+=1
    
   
    pass

   
    pass
    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

