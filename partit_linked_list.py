class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def partition(head: Node, x: int) -> Node:
    less_list = None
    less_head = None
    gr_list = None
    gr_head = None
    current = head

    while current is not None:
        if current.value < x:
            if less_head is None:
                less_head = current
                less_list = current
            else:
                less_list.next = current
                less_list = less_list.next
        else:
            if gr_head is None:
                gr_head = current
                gr_list = current
            else:
                gr_list.next = current
                gr_list = gr_list.next
        current = current.next

    if less_head is None:
        return less_head
    if gr_head is None:
        return gr_head
    less_list.next = gr_head
    gr_list.next = None
    return less_head


def print_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next


a = Node(1)
a.next = Node(4, Node(3, Node(2, Node(5, Node(2)))))

# print_list(a)

print_list(partition(a, 3))
