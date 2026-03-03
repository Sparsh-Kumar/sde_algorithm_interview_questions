
# https://takeuforward.org/plus/dsa/problems/detect-a-cycle-in-an-undirected-graph (DFS)

from typing import List, Dict

class Solution:

  def _create_adj_list(self, V, adj) -> Dict[int, List[int]]:
    adj_list = { }
    for i in range(V):
      adj_list[i] = adj[i]
    return adj_list

  def isCycle(self, V, adj) -> bool:
    
    is_cycle = False
    visited = { }
    stack = [ (0, -1) ]
    visited[0] = -1
    
    adj_list = self._create_adj_list(V, adj)

    while len(stack):

      curr, parent = stack.pop()

      print(curr)

      for neighbor in adj_list.get(curr) or []:
        if neighbor not in visited:
          visited[neighbor] = True
          stack.append((neighbor, curr))
        elif neighbor != parent:
          is_cycle = True
          return is_cycle
    
    return is_cycle


def main() -> None:
  solution = Solution()
  print(solution.isCycle(6, [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]))
  print(solution.isCycle(4, [[1, 2], [0], [0, 3], [2]]))

if __name__ == '__main__':
  main()
