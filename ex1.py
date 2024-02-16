import numpy as np
import timeit
import matplotlib.pyplot as plt
import scipy.optimize
import random

class Node:
    def __init__(self, val):
        self._val = val
        self._next = None
        self._prev = None

    def getVal(self):
        return self._val
    
    def setVal(self, val):
        self._val = val
        
    def getNext(self):
        return self._next
    
    def setNext(self,next):
        self._next = next
    
    def newNode(x):
        temp = Node(x)
        return temp

    def mid(first, last):
        if first == None:
            return None
        slow = first
        fast = first.getNext()
        
        while fast != last:
            fast = fast.getNext()
            
            if fast != last:
                slow = slow.getNext()
                fast = fast.getNext()
        return slow 
    
    def binary_search(head,num):

        start = head
        last = None

        while True:

            mid = Node.mid(start, last)

            if mid == None: 
                return None
            if mid.getVal() == num:
                return mid
            
            elif (mid.getVal() < num):
                start = mid.getNext()
            else:
                last = mid
            if not (last == None or last != start ):
                break
        return None


def binarysearch(data, first, last, key):
    if(first <= last):
        mid = (first+last) // 2
        if(key == data[mid]):
            return mid
        elif (key < data[mid]):
            return binarysearch(data, first, mid-1, key)
        elif (key > data[mid]):
            return binarysearch(data, mid+1, last, key)
    return -1

#4. The time complexity is O(n) because there is no way to access a random spot in a linked list. To find the midpoint, you must 
# traverse all elements of the array every time which is complexity O(n), thus even though the search is implemented recursively, 
# it still must traverse the entirety of the list every time, leading to a time complexity of O(n)

def generate_sorted_array(size):
    return sorted([random.randint(0, size*10) for _ in range(size)])

def generate_sorted_linked_list(size):
    head = Node.newNode(random.randint(0, size*10))
    current = head
    for _ in range(size - 1):
        current.setNext(Node.newNode(random.randint(current.getVal(), size*10)))
        current = current.getNext()
    return head



sizes = [1000, 2000, 4000, 8000]

linkedtimes = []
arraytimes = []

def measure_performances(sizes):
    for size in sizes:
        
        linked_list = generate_sorted_linked_list(size)
        array = generate_sorted_array(size)

        midval = size // 2

        element = random.randint(0, size)

        while element == midval:
            element = random.randint(0, size)

        linkedtotal = timeit.timeit(lambda: Node.binary_search(linked_list, element), number=100)

        arraytotal = timeit.timeit(lambda: binarysearch(array, 0, size-1, element), number=100)

        linkedavg = linkedtotal / 100
        arrayavg = arraytotal / 100

        linkedtimes.append(linkedavg)
        arraytimes.append(arrayavg)

measure_performances(sizes)

slope, intercept = np.polyfit(sizes, linkedtimes, 1)
plt.scatter(sizes, linkedtimes, label = 'Linked list times')
linevalues = [slope * x + intercept for x in sizes]
plt.plot(sizes, linevalues, 'r-', label = 'Linked list interpolation')

slope_linear, intercept_linear = np.polyfit(sizes, linkedtimes, 1)
linear_fit_values = [slope_linear * x + intercept_linear for x in sizes]

def func(n, a, b):
    return a * np.log2(n) + b

popt, pcov = scipy.optimize.curve_fit(func, sizes, arraytimes)

plt.scatter(sizes, arraytimes, label = 'Array times')
binary_linevalues = func(np.array(sizes), *popt)
plt.plot(sizes, binary_linevalues, 'b', label = 'Array interpolation')


plt.xlabel('Sizes')
plt.ylabel('Line Values')
plt.title('Plot of Binary Search for Linked List and Array')
plt.legend()
plt.show()

