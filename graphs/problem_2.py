
# https://takeuforward.org/plus/dsa/problems/traversal-techniques

from collections import deque
from typing import Dict, List

class Solution:

  def _create_adj_list(self, adj) -> Dict[int, List[int]]:
    adj_list = {}
    for edges in adj:
      [ edge_a, edge_b ] = edges
      if not adj_list.get(edge_a):
        adj_list[edge_a] = []
      if not adj_list.get(edge_b):
        adj_list[edge_b] = []
      adj_list[edge_a].append(edge_b)
      adj_list[edge_b].append(edge_a)
    return adj_list

  def dfsOfGraph(self, V, adj) -> List[int]:
    adj_list = self._create_adj_list(adj)

    visited: Dict[int, bool] = { }
    stack: List[int] = [ 0 ]
    visited[0] = True
    traced_path: List[int] = []

    while len(stack):
      curr = stack.pop()
      traced_path.append(curr)
      for neighbor in adj_list.get(curr) or []:
        if neighbor not in visited:
          visited[neighbor] = True
          stack.append(neighbor)

    return traced_path


  def bfsOfGraph(self, V, adj) -> None:
    adj_list = self._create_adj_list(adj)

    visited: Dict[int, bool] = { }
    dq: deque = deque()
    dq.append(0)
    visited[0] = True
    traced_path: List[int] = []

    while len(dq):
      curr = dq.popleft()
      traced_path.append(curr)
      for neighbor in adj_list.get(curr) or []:
        if neighbor not in visited:
          visited[neighbor] = True
          dq.append(neighbor)
    
    return traced_path

def main() -> None:
  solution = Solution()
  print(solution.dfsOfGraph(5, [[0,1],[0,2],[0,3],[2,4]]))
  print(solution.bfsOfGraph(5, [[0,1],[0,2],[0,3],[2,4]]))

if __name__ == '__main__':
  main()


