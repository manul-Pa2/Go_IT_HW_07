#      10
#     /  \
#    5   15
#   / \    \
#  2  7    20

root = Node(10,
            left=Node(5, Node(2), Node(7)),
            right=Node(15, None, Node(20)))

print(sum_tree(root))           # 59
print(sum_tree_iterative(root)) # 59
