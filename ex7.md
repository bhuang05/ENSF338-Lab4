### 1

---

The first loop runs _self.get_size()_ times, which is an $O(n)$ operation.

The method _get_element_at_pos_ is an $O(n)$ operation because finding a specific node in a linked list requires $O(n)$. So when i = self.get_size(), the list must traverse all the way to the end of the linked list to retrieve this element.

The rest of the code just manipulates pointers to create a new reversed linked list.

The function _reverse()_ has a time complexity of $O(n^2)$, as there is a nested traversal within the loop which includes traversing the original list backwards **and** traversing the list to get an element at a specific position.

### 2

---

Rather than creating a new linked list, we can reverse the pointers of each node in place which will result in a time complexity of $O(n)$.

The function _get_element_at_pos_
is the reason why the implemenation above is $O(n^2)$. Thus, by removing the need for finding the element at i, the function can then have a time complexity of $O(n)$.
