## Delete the Middle Node of a Linked List

**Problem Link:** https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description

**Problem Statement:**
- Input format: a linked list with a `head` node and a `node` to be deleted.
- Constraints: The node to be deleted is guaranteed to be a middle node (not the head or tail node) of the linked list.
- Expected output format: the modified linked list after deleting the given node.
- Key requirements: delete the given node from the linked list without accessing the `head` of the list.
- Example test cases: 
    - Example 1: Input: head = [1,3,4,7,1,2,6], node = 3, Output: [1,3,4,7,1,2]
    - Example 2: Input: head = [1,5,9,1,2,5,6], node = 5, Output: [1,5,9,1,2]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One approach is to traverse the linked list to find the node before the node to be deleted and then update its `next` pointer to skip the node to be deleted.
- Step-by-step breakdown of the solution:
    1. Traverse the linked list to find the node before the node to be deleted.
    2. Update the `next` pointer of the previous node to skip the node to be deleted.
- Why this approach comes to mind first: This is a straightforward approach that involves finding the previous node and updating its `next` pointer.

```cpp
// Brute Force Approach
ListNode* deleteMiddleNode(ListNode* head, ListNode* node) {
    // Find the node before the node to be deleted
    ListNode* prev = head;
    while (prev->next != node) {
        prev = prev->next;
    }
    
    // Update the next pointer of the previous node
    prev->next = node->next;
    
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we need to traverse the linked list to find the node before the node to be deleted.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the previous node.
> - **Why these complexities occur:** The time complexity occurs because we need to traverse the linked list, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since we can't access the `head` of the linked list, we can't use the brute force approach. Instead, we can copy the data from the next node to the node to be deleted and then update the `next` pointer of the node to be deleted to skip the next node.
- Detailed breakdown of the approach:
    1. Copy the data from the next node to the node to be deleted.
    2. Update the `next` pointer of the node to be deleted to skip the next node.
- Proof of optimality: This approach is optimal because we don't need to traverse the linked list to find the node before the node to be deleted. We can simply copy the data from the next node and update the `next` pointer.

```cpp
// Optimal Approach
void deleteNode(ListNode* node) {
    // Copy the data from the next node to the node to be deleted
    node->val = node->next->val;
    
    // Update the next pointer of the node to be deleted to skip the next node
    node->next = node->next->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only perform a constant amount of work to copy the data and update the `next` pointer.
> - **Space Complexity:** $O(1)$, as we don't use any additional space.
> - **Optimality proof:** This approach is optimal because we don't need to traverse the linked list, and we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: linked list manipulation, data copying, and pointer updating.
- Problem-solving patterns identified: using insights to simplify the problem and finding optimal solutions.
- Optimization techniques learned: reducing time complexity by avoiding unnecessary traversals.
- Similar problems to practice: linked list problems, such as deleting a node from a linked list.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the `next` pointer, not checking for edge cases.
- Edge cases to watch for: deleting the head or tail node of the linked list.
- Performance pitfalls: using inefficient algorithms that have high time or space complexity.
- Testing considerations: testing the solution with different input scenarios, including edge cases.