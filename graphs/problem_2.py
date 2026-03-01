# Question : https://takeuforward.org/plus/dsa/problems/traversal-techniques

from typing import Dict, List

class Node:
  def __init__(self, cargo : float = 0, next : "Node | None" = None, prev: "Node | None" = None) -> None:
    self._cargo = cargo
    self._next = next
    self._prev = prev

  def set_cargo(self, cargo: float = 0) -> None:
    self._cargo = cargo

  def set_next(self, next : "Node | None" = None) -> None:
    self._next = next

  def set_prev(self, prev: "Node | None" = None) -> None:
    self._prev = prev

  def get_cargo(self) -> float:
    return self._cargo

  def get_next(self) -> "Node | None":
    return self._next

  def get_prev(self) -> "Node | None":
    return self._prev

  def __del__(self) -> None:
    pass

class Stack:
  def __init__(self) -> None:
    self._top = None
    self._stack_length = 0

  def push(self, cargo: float = 0) -> None:
    node = Node(cargo)
    if not self._top:
      self._top = node
    else:
      node.set_next(self._top)
      self._top = node
    self._stack_length += 1
    return

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

class Queue:
  def __init__(self) -> None:
    self._front = None
    self._rear = None
    self._queue_length = 0

  def enqueue(self, cargo : float = 0) -> None:
    node = Node(cargo)
    if not self._front and not self._rear:
      self._front = node
      self._rear = node
      self._front.set_prev(self._rear)
      self._rear.set_next(self._front)
    else:
      node.set_next(self._rear)
      self._rear.set_prev(node)
      self._rear = node
    self._queue_length += 1

  def dequeue(self) -> "Node | None":
    if not self._front:
      return None
    front_cargo = self._front.get_cargo()
    self._front = self._front.get_prev()
    self._queue_length -= 1
    return front_cargo

  def is_empty(self) -> bool:
    return not self._queue_length

  def __del__(self) -> None:
    pass

def depth_first_search_traversal(adj_list: Dict[Node, List[Node]], starting_node: Node | None = None) -> None:
  pass

def breadth_first_search_traversal(adj_list: Dict[Node, List[Node]], starting_node: Node | None = None) -> None:
  pass

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

  depth_first_search_traversal(adj_list, node_1)
  breadth_first_search_traversal(adj_list, node_1)

if __name__ == '__main__':
  main()
