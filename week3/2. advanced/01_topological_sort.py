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

    # 큐 생성 
    queue=deque()
    arr=[0]*vertices

    # 각 노드의 진입 차수를 큐 형태로 정리.
    # index=노드 번호, 리스트 값 = 진입 차수 개수 
    for edge in edges:
        start,end=edge 
        arr[end]+=1 #진입 차수를 큐에 추가

    # 큐에서 진입차수가 0인 것부터 꺼내서 위상 정렬 실행
    for index in range(len(arr)):
        if arr[index]==0:
            # 진입차수가 0인 걸 queue에 삽입 
            queue.append(index)
            # print("큐에 원소가 추가됨!")
            # print(f"queue:{queue}")
            # print(f"arr:{arr}")

            # edges에서 선택한 노드와 연결된 간선의 노드를 찾기 
            for edge in edges:
                start,end=edge
                if start==index:
                    arr[end]-=1 # 연결된 간선 제거

    return list(queue)
        

  
    pass
    
  
    pass
    
   
    pass
    
  
    
   
    pass
    
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
