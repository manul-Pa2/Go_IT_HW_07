from typing import Optional, List

def sum_tree_iterative(root: Optional[Node]) -> int:
    if root is None:
        return 0

    total = 0
    stack: List[Node] = [root]

    while stack:
        node = stack.pop()
        total += node.key
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return total
