import sys

N, M, V = map(int, sys.stdin.readline().split()) #정점의 개수, 간선의 개수, 탐색 시작할 정점의 번호
graph_list = [set([]) for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph_list[a].add(b)
    graph_list[b].add(a)

def DFS(graph_list, start_node) :
    visit_node = []
    stack = [start_node]

    while stack :
        node = stack.pop()
        if node not in visit_node :
            visit_node.append(node)
            stack += sorted(list(graph_list[node] - set(visit_node)), reverse=True)
            #방금 넣은 node에 연결된 다른 노드 중 방문하지 않은 것들만 스택에 역순정렬해서 넣는다.
    return visit_node

def BFS(graph_list, start_node) :
    visit_node = []
    queue = [start_node]

    while queue :
        node = queue.pop(0)
        if node not in visit_node :
            visit_node.append(node)
            queue += sorted(list(graph_list[node] - set(visit_node)))

    return visit_node

for i in list(DFS(graph_list, V)) :
    print(i, end =" ")
print()
for j in list(BFS(graph_list, V)) :
    print(j, end = " ")