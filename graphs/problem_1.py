
# https://takeuforward.org/plus/dsa/problems/clone-graph

from typing import Optional

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

    if not node:
      return None

    visited = { }
    stack = [ node ]
    visited[node] = Node(node.val)

    while len(stack):

      curr = stack.pop()

      for neighbor in curr.neighbors:

        if neighbor not in visited:
          visited[neighbor] = Node(neighbor.val)
          stack.append(neighbor)

        visited[curr].neighbors.append(visited[neighbor])
    
    return visited[node]


def main() -> None:
  node_1 = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  node_4 = Node(4)
  node_1.neighbors = [ node_2, node_4 ]
  node_2.neighbors = [ node_1, node_3 ]
  node_3.neighbors = [ node_2, node_4 ]
  node_4.neighbors = [ node_1, node_3 ]
  solution = Solution()
  print(solution.cloneGraph(node_1))

if __name__ == '__main__':
  main()

