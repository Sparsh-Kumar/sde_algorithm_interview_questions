# Question : https://takeuforward.org/plus/dsa/problems/clone-graph

class Node:
  def __init__(self, cargo = None, next = None) -> None:
    self._cargo = cargo
    self._next = next
  def __del__(self) -> None:
    pass


