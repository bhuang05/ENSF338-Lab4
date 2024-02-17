import timeit
import matplotlib.pyplot as plt

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


# Creating list sizes of 1000, 2000, 3000, 4000
sizes = [1000, 2000, 3000, 4000]
old_reversed_lists = []
new_reversed_lists = []


# Appending the linkedlists of different sizes to another list
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

# Timing the old and new reverse functions 100 times each
old_reverse_times = []
new_reverse_times = []

for i in range(len(sizes)):
    old_reverse_times.append(timeit.timeit(old_reversed_lists[i].reverse, number=100))
    new_reverse_times.append(timeit.timeit(new_reversed_lists[i].optimized_reverse, number=100))

# Plotting the times
plt.plot(sizes, old_reverse_times, label="Old Reverse")
plt.plot(sizes, new_reverse_times, label="New Reverse")
plt.xlabel("Size of List")
plt.ylabel("Time")
plt.title("Old vs New Reverse")
plt.legend()
plt.show()
