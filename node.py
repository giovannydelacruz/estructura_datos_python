class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# from node import Node
# node1 = None
# node2 = Node("A", None)
# node3 = Node("B", node2)

# for count in range(1,5):
#     head = Node(count, head)

# while head != None:
#     print(head.data)
#     head = head.next