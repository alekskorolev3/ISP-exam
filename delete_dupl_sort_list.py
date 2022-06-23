class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def delete_duplicates(head: Node) -> Node:
    while head.next is not None:
        if head.value == head.next.value:
            head.next = head.next.next
        else:
            head = head.next


a = Node(2)
a.next = Node(3, Node(3, Node(3, Node(4))))

delete_duplicates(a)

while a is not None:
    print(a.value)
    a = a.next

