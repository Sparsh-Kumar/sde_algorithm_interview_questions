
# https://takeuforward.org/plus/dsa/problems/topological-sort-or-kahns-algorithm (Topological Sort - BFS)

from typing import Dict, List
from collections import deque

class Solution:
  def _create_adj_list(self, V: int, adj: List[List[int]]) -> Dict[int, List[int]]:
    adj_list: Dict[int, List[int]] = { }
    for i in range(V):
      adj_list[i] = adj[i]
    return adj_list

  def _get_indegree(self, V: int, adj_list: Dict[int, List[int]]) -> List[int]:
    indegree = [0] * V
    for i in range(V):
      edges = adj_list.get(i)
      for edge in edges:
        indegree[edge] += 1
    return indegree

  def topoSort(self, V: int, adj: List[List[int]]) -> List[int]:
    adj_list = self._create_adj_list(V, adj)
    indegree = self._get_indegree(V, adj_list)
    dq: deque = deque()
    topo = []

    for i in range(V):
      if not indegree[i]:
        dq.appendleft(i)
  
    while len(dq):

      curr = dq.pop()
      topo.append(curr)

      neighbors = adj_list.get(curr) or []
      for neighbor in neighbors:
        indegree[neighbor] -= 1
        if not indegree[neighbor]:
          dq.appendleft(neighbor)
    
    return topo

def main() -> None:
  solution = Solution()
  print(solution.topoSort(6, [[],[],[3],[1],[0,1],[0,2]]))
  print(solution.topoSort(4, [[],[0],[0],[0]]))

if __name__ == '__main__':
  main()


