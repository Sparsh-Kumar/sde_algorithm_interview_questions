# Question : https://takeuforward.org/plus/dsa/problems/clone-graph

from typing import Dict, List

class Node:
  def __init__(self, cargo : float = 0, next: "Node | None" = None) -> None:
    self._cargo = cargo
    self._next = next

  def set_cargo(self, cargo : float = 0) -> None:
    self._cargo = cargo

  def set_next(self, node : "Node | None" = None) -> None:
    self._next = node

  def get_cargo(self) -> float:
    return self._cargo

  def get_next(self) -> "Node | None":
    return self._next

  def __del__(self) -> None:
    pass


class Stack:

  def __init__(self) -> None:
    self._top = None
    self._stack_length = 0

  def push(self, cargo : float = 0) -> None:
    node = Node(cargo)
    if not self._top:
      self._top = node
    else:
      node.set_next(self._top)
      self._top = node
    self._stack_length += 1

  def pop(self) -> "Node | None":

    if not self._top:
      return None

    top_node_cargo = self._top.get_cargo()
    self._top = self._top.get_next()
    self._stack_length -= 1
    return top_node_cargo

  def is_empty(self) -> bool:
    return not self._top and not self._stack_length

  def __del__(self) -> None:
    pass


def buildAdjList(edge_list: List[List[float]] = []) -> Dict[float, List[float]]:
  adj_list = {}
  for edge in edge_list:
    [first_edge, second_edge] = edge
    if not adj_list.get(first_edge):
      adj_list[first_edge] = []
    if not adj_list.get(second_edge):
      adj_list[second_edge] = []
    adj_list[first_edge].append(second_edge)
    adj_list[second_edge].append(first_edge)
  return adj_list

def depth_first_search_graph_clone(adj_list = {}, node : float = 0, visited = set()) -> None:
  graph : Dict[Node, List[Node]] = {}
  stack = Stack()
  stack.push(node)
  while not stack.is_empty():
    node = stack.pop()
    cargo = node.get_cargo()
    if node in visited:
      continue
    if not graph.get(cargo):
      graph[cargo] = []
    visited.add(node)
    for neighbour in adj_list.get(node):
      graph[cargo].append(neighbour.get_cargo())
      stack.push(neighbour)
  return graph

def main() -> None:
  node_1 = Node(1)
  node_2 = Node(2)
  node_3 = Node(3)
  node_4 = Node(4)
  adj_list = {
    node_1: [node_2, node_4],
    node_2: [node_1, node_3],
    node_3: [node_2, node_4],
    node_4: [node_1, node_3]
  }
  cloned_graph = depth_first_search_graph_clone(adj_list, node_1)
  print(cloned_graph)

if __name__ == '__main__':
  main()


