### 1

---

_Advantages and disadvatnages of arrays_
Since arrays are linear, random access data structures, you can access an element directly with their indices which is $O(1)$. However, since arrays have a fixed length, this can result in a waste of space. Also, inserting and deleting elements in the worst case is $O(n)$, which can be a costly operation.

_Advantages and disadvantages linked lists_
Unlike arrays and their fixed size when they are declared, linked lists can dynamically resize themselves so no memory is wasted. Another advantage is that if the element is at the head or tail (if the tail pointer is included in the implementation), this results in a $O(1)$ operation. However, some disadvantages are when traversal is needed to find an element that is not at the head or tail which results in a $O(n)$ operation in the average and worst case.

---

### 2

---

If the index of the element that we want to delete/insert into is known, then we can delete this element and move all the elements after the specified index to the right which would be an $O(n)$ operation. We then can insert the element into the array which is an $O(1)$ operation since we know the index where we want to insert the element.

---

### 3

---

#### Insertion Sort

Insertion sort can be implemented into a doubly linked list, as we can traverse either forwards or backwards to iteratively insert elements into their correct positions. One implementation can be an in-place insertion sort which modifies the existing list by rearranging its nodes directly by mainting two pointers which point to the sorted and unsorted portions of the list. Although insertion sort is feasible, it is not the most efficient as the time complexity for swapping elements with insertion sort is $O(n^2)$. This cost will get worse as the size of the list gets larger as well.

#### Merge Sort

Merge sort can also be implemented into a doubly linked list. Compared to insertion sort, merge sort is more feasible for larger list sizes as it has a time complexity of $O(n log(n))$. Merge sort is more efficient as it takes a divide and conquer approach which improves the performance of the algorithm. The implementation of merge sort for a doubly linked list is much more complicated than insertion sort as splitting a linked list in two requires the handling of many pointers, as well as implementing a recursive function to sort the halved lists.

### 4

As mentioned above, insertion sort in a doubly linked list has a time complexity of $O(n^2)$ and merge sort in a doubly linked list has a time complexity of $O(n log(n))$. Similar to a regular array, insertion sort in its average case has a time complexity $O(n^2)$ and merge sort in its average case has a time complexity of $O(n log(n))$.

Thus, there is no difference in time complexity.
