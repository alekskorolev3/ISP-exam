class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def bst_generator(head):
#     def rec(node):
#         if node.left is not None:
#             yield rec(node.left)
#         yield node
#
#         if node.right is not None:
#             yield rec(node.right)
#
#     yield from rec(head)

def bst_generator(head):
    if head.left is not None:
        yield from bst_generator(head.left)
    yield head
    if head.right is not None:
        yield from bst_generator(head.right)


v1 = Node(1)
v2 = Node(2, v1)
v5 = Node(5)
v4 = Node(4, v2, v5)
v9 = Node(9)
v8 = Node(8, right=v9)
v7 = Node(7, v4, v8)
head = v7

for node in bst_generator(head):
    print(node.value)
