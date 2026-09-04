"""
[이진 검색 트리 - Binary Search Tree (BST)]

문제 설명:
- 이진 검색 트리에서 값을 검색합니다.
- BST 특징: 왼쪽 자식 < 부모 < 오른쪽 자식
- 이 특성을 이용하여 빠른 검색이 가능합니다.
- 왼쪽 서브트리의 모든 값 < 현재 노드 값
- 오른쪽 서브트리의 모든 값 > 현재 노드 값

입력:
- root: 트리의 루트 노드
- target: 찾을 값

출력:
- True: 값이 존재
- False: 값이 없음

예제:
트리:
      5
     / \
    3   7
   / \
  2   4

찾는 값: 4 → True
찾는 값: 6 → False


"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ✔️ 반복문으로도 구현할 수 있음. 
def search_bst(root, target):
    """
    BST에서 값 검색
    
    Args:
        root: 트리 루트
        target: 찾을 값
    
    Returns:
        True/False
    """

    if root is None: return False

    if target>root.value:
        # print(f"오른쪽 target:{target},root:{root.value}")

        # ⭐️ 재귀 호출을 해놓고 return을 안함 
        # 반환하지 않으면 재귀 호출에서 얻은 결과가 바깥 함수로 전달되지 않는다. 
        return search_bst(root.right,target) 
    if target<root.value:
        # print(f"왼쪽 target:{target},root:{root.value}")
        return search_bst(root.left,target)
    else:
        return True

def search_bst2(root,target):
    if root is None: return False

    while True:
        if root.value==target: return True
        elif root.value>target: root=root.left
        else: root=root.right
    pass
    
    
    pass

# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")


