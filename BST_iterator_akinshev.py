class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class iterator:

    def __init__(self, head):
        self.head = head
        self.tree = self.get_generator(head)
        self.count = 0
        self.max_count = self.counting(head)

    def counting(self, head):
        i = 0
        if head.left is not None:
            i += self.counting(head.left)
        i += 1
        if head.right is not None:
            i += self.counting(head.right)
        return i

    def get_generator(self, head):
        if head.left is not None:
            yield from self.get_generator(head.left)
        yield head
        if head.right is not None:
            yield from self.get_generator(head.right)

    def __next__(self):
        if self.count < self.max_count:
            self.count += 1
            return self.tree.__next__()
        else:
            raise StopIteration

    def __iter__(self):
        return self

v1 = Node(1)
v2 = Node(2, v1)
v5 = Node(5)
v4 = Node(4, v2, v5)
v9 = Node(9)
v8 = Node(8, right=v9)
v7 = Node(7, v4, v8)
head = v7


for node in iterator(head):
    print(node.value)
