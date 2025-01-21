## Reverse Linked List
**Problem Link:** https://leetcode.com/problems/reverse-linked-list/description

**Problem Statement:**
- Input format: A linked list defined by a `ListNode` class, where each node contains an integer value and a pointer to the next node.
- Constraints: The number of nodes in the list is in the range $[0, 5000]$.
- Expected output format: The head of the reversed linked list.
- Key requirements and edge cases to consider: Handling empty lists, lists with one node, and lists with multiple nodes.
- Example test cases with explanations:
  - Input: `1 -> 2 -> 3 -> 4 -> 5`
  - Output: `5 -> 4 -> 3 -> 2 -> 1`
  - Explanation: The linked list is reversed, and the head of the reversed list is returned.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To reverse a linked list, we can traverse the list, storing each node's value in a data structure like a vector or array, and then create a new linked list in reverse order.
- Step-by-step breakdown of the solution:
  1. Create a vector to store the values of the nodes.
  2. Traverse the linked list, pushing each node's value into the vector.
  3. Create a new linked list by iterating over the vector in reverse order, setting each node's value and next pointer accordingly.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that doesn't require manipulating the original list's pointers directly.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        vector<int> values;
        // Traverse the list and store values in a vector
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }
        
        // Create a new list in reverse order
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        for (int i = values.size() - 1; i >= 0; i--) {
            curr->next = new ListNode(values[i]);
            curr = curr->next;
        }
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the list, because we traverse the list once to store values and then iterate over the stored values to create the new list.
> - **Space Complexity:** $O(n)$, as we store all node values in a vector.
> - **Why these complexities occur:** The time complexity is linear due to the two passes over the data (once to store, once to create the new list), and the space complexity is linear because we store all node values in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all node values and then creating a new list, we can reverse the list in-place by updating the `next` pointers of the nodes as we traverse the list.
- Detailed breakdown of the approach:
  1. Initialize three pointers: `prev`, `curr`, and `next`. Set `prev` to `nullptr` and `curr` to the head of the list.
  2. Traverse the list. For each node, do the following:
     - Store the next node in `next` before we overwrite `curr->next`.
     - Reverse the `next` pointer of the current node by setting `curr->next` to `prev`.
     - Move `prev` and `curr` one step forward.
  3. When the loop ends, `prev` will be pointing to the new head of the reversed list.
- Proof of optimality: This approach only requires a single pass through the list, and it only uses a constant amount of extra space to store the pointers.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the list, because we make a single pass through the list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers.
> - **Optimality proof:** This is the most efficient solution because it achieves the reversal in a single pass with minimal extra space, making it optimal in terms of both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, in-place reversal, and pointer management.
- Problem-solving patterns identified: The importance of considering both time and space complexity, and the value of finding solutions that minimize both.
- Optimization techniques learned: In-place modification, reducing the number of passes through the data, and minimizing extra memory usage.
- Similar problems to practice: Other linked list problems, such as inserting, deleting, or sorting nodes.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update pointers correctly, not handling edge cases like empty lists or lists with one node.
- Edge cases to watch for: Lists with zero, one, or two nodes, as these can have unique handling requirements.
- Performance pitfalls: Using excessive extra memory or making unnecessary passes through the data, which can significantly impact performance for large inputs.
- Testing considerations: Thoroughly testing with various input sizes and edge cases to ensure the solution is robust and correct.