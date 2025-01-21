## Delete Node in a Linked List
**Problem Link:** https://leetcode.com/problems/delete-node-in-a-linked-list/description

**Problem Statement:**
- Input: A node in a singly linked list.
- Output: The linked list after deleting the given node.
- Key requirements: 
  - You cannot modify the `ListNode` class.
  - You cannot return the modified linked list, you need to modify it in-place.
- Edge cases to consider: 
  - The given node is the only node in the linked list.
  - The given node is the head of the linked list.
  - The given node is the tail of the linked list.
- Example test cases: 
  - Deleting a node in the middle of the linked list.
  - Deleting the head of the linked list.
  - Deleting the tail of the linked list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the linked list to find the node to be deleted, then update the `next` pointer of the previous node to skip the node to be deleted.
- Step-by-step breakdown of the solution: 
  1. Start from the head of the linked list.
  2. Traverse the linked list until we find the node before the node to be deleted.
  3. Update the `next` pointer of the previous node to skip the node to be deleted.
- Why this approach comes to mind first: It's a straightforward approach that involves iterating through the linked list to find the node to be deleted.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
class Solution {
public:
    void deleteNode(ListNode* node) {
        // Check if the node is the only node in the linked list
        if (node->next == NULL) {
            // If the node is the only node, we cannot delete it
            return;
        }
        
        // Copy the data of the next node into the current node
        node->val = node->next->val;
        
        // Update the next pointer of the current node to skip the next node
        node->next = node->next->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are only updating the `val` and `next` pointers of the given node.
> - **Space Complexity:** $O(1)$, because we are not using any extra space.
> - **Why these complexities occur:** These complexities occur because we are not iterating through the linked list, and we are only updating the `val` and `next` pointers of the given node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since we cannot modify the `ListNode` class, we can copy the data of the next node into the current node, and then update the `next` pointer of the current node to skip the next node.
- Detailed breakdown of the approach: 
  1. Check if the node is the only node in the linked list.
  2. Copy the data of the next node into the current node.
  3. Update the `next` pointer of the current node to skip the next node.
- Proof of optimality: This approach is optimal because we are not iterating through the linked list, and we are only updating the `val` and `next` pointers of the given node.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    void deleteNode(ListNode* node) {
        // Check if the node is the only node in the linked list
        if (node->next == NULL) {
            // If the node is the only node, we cannot delete it
            return;
        }
        
        // Copy the data of the next node into the current node
        node->val = node->next->val;
        
        // Update the next pointer of the current node to skip the next node
        node->next = node->next->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are only updating the `val` and `next` pointers of the given node.
> - **Space Complexity:** $O(1)$, because we are not using any extra space.
> - **Optimality proof:** This approach is optimal because we are not iterating through the linked list, and we are only updating the `val` and `next` pointers of the given node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, in-place modification.
- Problem-solving patterns identified: Updating the `val` and `next` pointers of a node to delete it.
- Optimization techniques learned: Avoiding iteration through the linked list.
- Similar problems to practice: Deleting a node from a doubly linked list, deleting a node from a circular linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the node is the only node in the linked list.
- Edge cases to watch for: The given node is the head of the linked list, the given node is the tail of the linked list.
- Performance pitfalls: Iterating through the linked list to find the node to be deleted.
- Testing considerations: Test the solution with different edge cases, such as deleting the head, tail, or a node in the middle of the linked list.