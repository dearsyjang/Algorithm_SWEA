# 완전이진트리에서의 순회
def pre_order(v):
    global last
    if v <= last: # 마지막 정점번호 이내
        print(v) # visit(v)
        pre_order(v*2) # 왼쪽 자식정점 방문
        pre_order(v*2+1) # 오른쪽 자식정점 방문

    # tree1과 순회 구조는 동일, 전달방식이 다를 뿐!
    # 부모 자식 관계를 저장하는 방법이 다른 것!
    # tree1은 자식값을 저장하고 그 값을 가져온 것 / tree2는 연산해서 값 사용
    # tree1은 char1 char2를 값을 따로 만들어 저장해야 한다.

