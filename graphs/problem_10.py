
# https://takeuforward.org/plus/dsa/problems/bipartite-graph (Bipartite Graph using DFS)

from typing import Dict, List

class Solution:

  def _create_adj_list(self, V: int, adj: List[List[int]]) -> Dict[int, List[int]]:
    adj_list = { }
    for edges in adj:
      [ edge_a, edge_b ] = edges
      if not adj_list.get(edge_a):
        adj_list[edge_a] = []
      if not adj_list.get(edge_b):
        adj_list[edge_b] = []
      adj_list[edge_a].append(edge_b)
      adj_list[edge_b].append(edge_a)
    return adj_list

  def _get_correct_color(self, parent_color: str = 'G') -> str:
    correct_color: str = 'G'
    if parent_color == 'G':
      correct_color = 'Y'
    if parent_color == 'Y':
      correct_color = 'G'
    return correct_color

  def isBipartite(self, V: int, adj: List[List[int]]) -> bool:
    adj_list = self._create_adj_list(V, adj)

    visited = { }

    for start_node in range(V):

      if visited.get(start_node):
        continue

      stack = [ ( start_node, 'G') ]

      while len(stack):

        current_node, color = stack.pop()

        if not visited.get(current_node):
          visited[current_node] = color
        
        for neighbor in adj_list.get(current_node) or []:
          correct_color = self._get_correct_color(color)

          if not visited.get(neighbor):
            stack.append((neighbor, correct_color))
          else:
            neighbor_color = visited.get(neighbor)
            if neighbor_color != correct_color:
              return False

    return True

def main() -> None:
  solution = Solution()
  test_cases = test_cases = [
    {
      "V": 0,
      "adj": [],
      "expected": True
    },
    {
      "V": 1,
      "adj": [],
      "expected": True
    },
    {
      "V": 2,
      "adj": [[0,1]],
      "expected": True
    },
    {
      "V": 3,
      "adj": [],
      "expected": True
    },
    {
      "V": 4,
      "adj": [[0,1],[1,2],[2,3]],
      "expected": True
    },
    {
      "V": 4,
      "adj": [[0,1],[1,2],[2,3],[3,0]],
      "expected": True
    },
    {
      "V": 3,
      "adj": [[0,1],[1,2],[2,0]],
      "expected": False
    },
    {
      "V": 5,
      "adj": [[0,1],[1,2],[2,3],[3,4],[4,0]],
      "expected": False
    },
    {
      "V": 5,
      "adj": [[0,1],[0,2],[1,3],[1,4]],
      "expected": True
    },
    {
      "V": 6,
      "adj": [[0,1],[2,3]],
      "expected": True
    },
    {
      "V": 7,
      "adj": [[0,1],[1,2],[2,0],[3,4],[4,5]],
      "expected": False
    },
    {
      "V": 6,
      "adj": [[0,1],[2,3],[4,5]],
      "expected": True
    },
    {
      "V": 3,
      "adj": [[0,0]],
      "expected": False
    },
    {
      "V": 3,
      "adj": [[0,1],[0,1],[1,2]],
      "expected": True
    },
    {
      "V": 3,
      "adj": [[0,1],[1,2],[0,2]],
      "expected": False
    },
    {
      "V": 4,
      "adj": [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],
      "expected": False
    },
    {
      "V": 6,
      "adj": [[0,3],[0,4],[1,4],[1,5],[2,5]],
      "expected": True
    },
    {
      "V": 6,
      "adj": [[0,3],[0,4],[1,4],[2,5],[3,1]],
      "expected": True
    },
    {
      "V": 10,
      "adj": [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]],
      "expected": True
    },
    {
      "V": 6,
      "adj": [[0,1],[1,2],[2,3],[3,1],[3,4],[4,5]],
      "expected": False
    }
  ]

  for test_case in test_cases:
    print(solution.isBipartite(test_case['V'], test_case['adj']) == test_case['expected'])

if __name__ == '__main__':
  main()

