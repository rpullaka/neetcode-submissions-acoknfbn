from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        # graph = [[0] * n] * n
        graph = [[0] * n for _ in range(n)]
        # [graph[v][ch] = 1 for [v,ch] in edges]  #[Miss] Cannot assign inside a list comprehension
        for [v,ch] in edges:
            graph[v][ch] = 1
            graph[ch][v] = 1    #[Miss] Should set 1 both ways
        
        visited = [False] * n 
        parent = [-1] * n
        
        def bfs(start) -> bool:
            Q = deque([start])
            visited[start] = True
            while Q:
                v = Q.popleft()
                # visited[v] = True #[Miss] Visited = True should be set before it gets put into the queue
                for ch in range(n):
                    # if ch != v and graph[v][ch] == 1 and graph[v][ch] != parent[v]:   #[Bug] See line below
                    if ch != v and graph[v][ch] == 1 and ch != parent[v]:
                        if visited[ch]:
                            return False
                        parent[ch] = v
                        visited[ch] = True
                        Q.append(ch)
            return True
        
        n_comps = 0
        for v in range(n):
            if n_comps > 1:
                return False
            if not visited[v]:
                n_comps += 1
                if not bfs(v):
                    return False
        return True