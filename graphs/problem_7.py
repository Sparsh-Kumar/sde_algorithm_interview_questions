
# https://takeuforward.org/plus/dsa/problems/detect-a-cycle-in-a-directed-graph (BFS)

from typing import Dict, List
from collections import deque

class Solution:
  def _create_adj_list(self, V: int, adj: List[List[int]]) -> Dict[int, List[int]]:
    adj_list: Dict[int, List[int]] = { }
    for i in range(V):
      adj_list[i] = adj[i]
    return adj_list

  def _create_indegree(self, V: int, adj_list: Dict[int, List[int]]) -> List:
    indegree = [0] * V
    for i in range(V):
      for edge in adj_list.get(i) or []:
        indegree[edge] += 1
    return indegree

  def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
    adj_list = self._create_adj_list(V, adj)
    indegree = self._create_indegree(V, adj_list)
    dq: deque = deque()
    topo = []

    for i in range(V):
      if not indegree[i]:
        dq.appendleft(i)

    while len(dq):
      curr = dq.pop()
      topo.append(curr)
      for neighbor in adj_list.get(curr) or []:
        indegree[neighbor] -= 1
        if not indegree[neighbor]:
          dq.appendleft(neighbor)

    return len(topo) != V

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

