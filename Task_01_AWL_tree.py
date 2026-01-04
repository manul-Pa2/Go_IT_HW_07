# звичайна функція (працює з будь-яким вузлом, де є right і value/key)
def find_max(root):
    """
    Повертає найбільше значення в BST/AVL
    root: корінь дерева або None
    """
    if root is None:
        return None  # або ValueError

    current = root
    while current.right is not None:
        current = current.right

    # зазначив класичні найчастіші назви поля
    if hasattr(current, "value"):
        return current.value
    if hasattr(current, "key"):
        return current.key
    return current.data  # якщо поле називається data


#-------------------------------------------- 

# У завданні не було сказано чи використовувати рекурсію, якщо так, то ось:
def find_max_recursive(node):
    if node is None:
        return None
    return find_max_recursive(node.right) if node.right else (node.value if hasattr(node, "value") else node.key)
