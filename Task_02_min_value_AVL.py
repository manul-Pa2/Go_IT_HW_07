from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    height: int = 1  # пріоритет для AVL


def find_min(root: Optional[Node]) -> int:
    """Повертає мінімальний ключ у дереві, і для BST, і для AVL."""
    if root is None:
        raise ValueError("Дерево порожнє")

    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur.key
  
#----------------------------

# +рекурсія (як у Таск_01)
def find_min_recursive(root: Optional[Node]) -> int:
    if root is None:
        raise ValueError("Дерево порожнє")
    return root.key if root.left is None else find_min_recursive(root.left)
