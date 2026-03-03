
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


