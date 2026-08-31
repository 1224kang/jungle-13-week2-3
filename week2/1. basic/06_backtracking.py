"""
[백트래킹 - 조합 생성]

▣ 문제 설명
- 1, 2, ..., n 의 숫자 중에서 k 개를 골라 만들 수 있는 모든 "조합" 을 출력합니다.
- 조합은 "순서 없이 어떤 것을 골랐는가" 만 따집니다.
  예) [1, 2] 와 [2, 1] 은 같은 조합으로 봅니다.

▣ 입력
- n: 전체 숫자 개수 (1, 2, ..., n)
- k: 그 중 골라야 할 개수

▣ 출력
- 가능한 모든 조합을 담은 리스트.

▣ 작은 예시 (n = 4, k = 2)
가능한 조합:
    [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
모두 6 개.


"""


def combinations(n: int, k: int) -> list:
    """
    1 부터 n 까지 숫자 중 k 개를 선택하는 모든 조합을 반환합니다.

    Args:
        n: 전체 숫자 개수 (1, 2, ..., n)
        k: 선택할 개수

    Returns:
        모든 조합을 담은 리스트(예: [[1,2], [1,3], ...])
    """

    for i in range (1,n):
       backtrack(i,[])
       

    result = []  # 완성된 조합을 모아 둘 곳

    def backtrack(start: int, current_combination: list) -> None:
        """
        재귀(백트래킹) 헬퍼 함수.

        Args:
            start: 이번에 시도해볼 수 있는 가장 작은 숫자
            current_combination: 지금까지 골라 둔 숫자들 (탐색 중)
        """

        
                

      
        pass  

      
        pass

            

    backtrack(1, [])
    return result


# ============================================================================
# (이 함수는 직접 채울 필요 없음 — itertools 로 만든 비교/검증용 정답)
# ============================================================================
def combinations_itertools_compare(n: int, k: int) -> list:
    """파이썬 표준 라이브러리로 만든 동일 결과 (정답 비교용)"""
    from itertools import combinations as comb
    return [list(c) for c in comb(range(1, n + 1), k)]


# ============================================================================
# 테스트 케이스
# ============================================================================
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 테스트 케이스 1 ===")
    n1, k1 = 4, 2
    result1 = combinations(n1, k1)
    print(f"C({n1}, {k1}) = {result1}")
    print(f"총 {len(result1)}개의 조합")
    print()

    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    n2, k2 = 5, 3
    result2 = combinations(n2, k2)
    print(f"C({n2}, {k2}) = {result2}")
    print(f"총 {len(result2)}개의 조합")
    print()

    # 테스트 케이스 3
    print("=== 테스트 케이스 3 ===")
    n3, k3 = 3, 1
    result3 = combinations(n3, k3)
    print(f"C({n3}, {k3}) = {result3}")
    print(f"총 {len(result3)}개의 조합")
    print()

    # 테스트 케이스 4
    print("=== 테스트 케이스 4 ===")
    n4, k4 = 4, 4
    result4 = combinations(n4, k4)
    print(f"C({n4}, {k4}) = {result4}")
    print(f"총 {len(result4)}개의 조합")
