
# https://takeuforward.org/plus/dsa/problems/detect-a-cycle-in-a-directed-graph (DFS)

from typing import Dict, List

class Solution:

  def _create_adj_list(self, N, adj) -> Dict[int, List[int]]:

    adj_list = { }
    for i in range(N):
      adj_list[i] = adj[i]

    return adj_list

  def isCyclic(self, N, adj) -> bool:

    adj_list = self._create_adj_list(N, adj)

    visited = { }
    mdfs_visited = { }
    entry_status = 0
    exit_status = 1

    for start_node in range(N):

      if visited.get(start_node):
        continue

      stack = [ (start_node, entry_status) ]

      while len(stack):

        curr_node, status = stack.pop()

        if status == entry_status:

          visited[curr_node] = True
          mdfs_visited[curr_node] = True

          stack.append((curr_node, exit_status))

          for neighbor in adj_list.get(curr_node) or []:

            if neighbor not in visited:
              stack.append((neighbor, entry_status))

            elif mdfs_visited.get(neighbor):
              return True

        if status == exit_status:

          mdfs_visited[curr_node] = False

    return False

def main() -> None:
  solution = Solution()
  test_cases = [
    {
      "V": 4,
      "adj": [[1], [2], [3], []],
      "expected": False
    },
    {
      "V": 3,
      "adj": [[1], [2], [0]],
      "expected": True
    },
    {
      "V": 3,
      "adj": [[0], [2], []],
      "expected": True
    },
    {
      "V": 4,
      "adj": [[1], [2], [3], [1]],
      "expected": True
    },
    {
      "V": 4,
      "adj": [[1, 2], [3], [3], []],
      "expected": False
    },
    {
      "V": 6,
      "adj": [[1], [2], [], [4], [5], [3]],
      "expected": True
    },
    {
      "V": 6,
      "adj": [[1], [2], [0], [4], [5], [3]],
      "expected": True
    },
    {
      "V": 7,
      "adj": [[1, 2], [3], [3], [4], [5], [3], []],
      "expected": True
    },
    {
      "V": 5,
      "adj": [[1, 2], [3], [3], [4], []],
      "expected": False
    },
    {
      "V": 6,
      "adj": [[1], [2], [3], [4], [2], []],
      "expected": True
    },
    {
      "V": 5,
      "adj": [[1], [], [2], [4], []],
      "expected": True
    },
    {
      "V": 5,
      "adj": [[1], [], [3], [4], [2]],
      "expected": True
    },
    {
      "V": 4,
      "adj": [[1, 2], [3], [3], []],
      "expected": False
    },
    {
      "V": 6,
      "adj": [[1], [2, 4], [3], [1], [5], []],
      "expected": True
    },
    {
      "V": 8,
      "adj": [[1], [2, 3], [4], [5], [6], [3], [7], []],
      "expected": True
    }
  ]

  for test_case in test_cases:
    print(solution.isCyclic(test_case['V'], test_case['adj']) == test_case['expected'])

if __name__ == '__main__':
  main()

