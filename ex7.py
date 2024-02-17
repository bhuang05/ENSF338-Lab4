class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size


    def get_element_at_position(self, pos):
        current = self.head
        for i in range(pos):
            current = current.next
        return current

    # Old reverse implemnetation
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size() - 1, -1, -1):
            currNode = self.get_element_at_position(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # Generated with ChatGPT.
    def optimized_reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

sizes = [1000, 2000, 3000, 4000]
old_reversed_lists = []
new_reversed_lists = []

for size in sizes:
    old_reverse = LinkedList()
    for i in range(size):
        old_reverse.insert_tail(Node(i))
    old_reversed_lists.append(old_reverse)

for size in sizes:
    new_reverse = LinkedList()
    for i in range(size):
        new_reverse.insert_tail(Node(i))
    new_reversed_lists.append(new_reverse)




# Example usage:
sll = LinkedList()
sll.insert_tail(Node(1))
sll.insert_tail(Node(2))
sll.insert_tail(Node(3))
sll.insert_tail(Node(4))

print("Original List:")
sll.print_list()

sll.reverse()

print("Reversed List:")
sll.print_list()


sll2 = LinkedList()
sll2.insert_tail(Node(1))
sll2.insert_tail(Node(2))
sll2.insert_tail(Node(3))
sll2.insert_tail(Node(4))


print("Original List2:")
sll2.print_list()

sll2.optimized_reverse()

print("Reversed List2:")
sll.print_list()
