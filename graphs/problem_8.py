
# https://takeuforward.org/plus/dsa/problems/topological-sort-or-kahns-algorithm (Topological Sort - DFS)

from typing import Dict, List
from collections import deque

class Solution:
  def _create_adj_list(self, V: int, adj: List[List[int]]) -> Dict[int, List[int]]:
    adj_list = {}
    for i in range(V):
      adj_list[i] = adj[i]
    return adj_list

  def topoSort(self, V, adj) -> List[int]:

    adj_list = self._create_adj_list(V, adj)
    visited = { }
    dq: deque = deque()


    for i in range(V):

      if visited.get(i):
        continue

      stack = [ i ]

      while len(stack):

        curr = stack.pop()

        for neighbor in adj_list.get(curr) or []:
          if neighbor not in visited:
            stack.append(neighbor)
            dq.appendleft(neighbor)
            visited[neighbor] = True

        if curr not in visited:
          dq.appendleft(curr)
          visited[curr] = True
 
    return dq

def main() -> None:
  solution = Solution()
  print(solution.topoSort(6, [[],[],[3],[1],[0,1],[0,2]]))
  print(solution.topoSort(4, [[],[0],[0],[0]]))

if __name__ == '__main__':
  main()
