"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]


"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """

    queue=deque() 
    indegree=[0]*vertices # 진입차수를 저장하는 역할 
    edges_list=[[] for _ in range(vertices)]
    result=[]

    # 인접 리스트 만들기 
    for start,end in edges:
        edges_list[start].append(end)

    # 진입 차수 계산 
    for start,end in edges:
        indegree[end]+=1

    # ⭐️ 처음부터 진입 차수가 0인 노드 큐에 삽입 
    for node in range(vertices):
        if indegree[node]==0:
            queue.append(node)

    # 큐가 빌 때까지 반복 
    while queue:
        current=queue.popleft()
        result.append(current)

        # for start,end in edges:
        for next_node in edges_list[current]:
            # if start==current:
                indegree[next_node]-=1 # 간선 제거 

                # 새롭게 진입 차수가 0이 되면 큐에 추가 
                if indegree[next_node]==0:
                    queue.append(next_node)

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3 
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
