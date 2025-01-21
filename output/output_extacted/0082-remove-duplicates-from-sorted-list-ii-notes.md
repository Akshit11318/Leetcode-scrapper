## Remove Duplicates from Sorted List II
**Problem Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description

**Problem Statement:**
- Input format: The function takes the head of a sorted linked list as input.
- Constraints: The linked list is sorted in ascending order.
- Expected output format: The function should return the head of the modified linked list with duplicates removed.
- Key requirements and edge cases to consider:
  - The linked list can be empty (i.e., `head` is `nullptr`).
  - The linked list can have multiple nodes with the same value.
  - The function should remove all nodes that have duplicate values.
- Example test cases with explanations:
  - Example 1: Input: `1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5`, Output: `1 -> 2 -> 5`
  - Example 2: Input: `1 -> 1 -> 1 -> 2 -> 3`, Output: `2 -> 3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the linked list and check each node for duplicates.
- Step-by-step breakdown of the solution:
  1. Create a new linked list to store the result.
  2. Iterate through the original linked list.
  3. For each node, check if it has a duplicate value in the rest of the list.
  4. If it does not have a duplicate value, add it to the result list.
- Why this approach comes to mind first: It is a straightforward solution that checks each node individually.

```cpp
// Brute Force Approach
ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* current = dummy;
    
    while (current->next && current->next->next) {
        if (current->next->val == current->next->next->val) {
            int val = current->next->val;
            while (current->next && current->next->val == val) {
                ListNode* temp = current->next;
                current->next = current->next->next;
                delete temp;
            }
        } else {
            current = current->next;
        }
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the linked list. This is because in the worst case, we are checking each node against every other node.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the dummy node and the current node.
> - **Why these complexities occur:** The time complexity is high because of the nested loop structure, and the space complexity is low because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to keep track of the current node and the next node that has a different value.
- Detailed breakdown of the approach:
  1. Create a dummy node to simplify the edge cases.
  2. Initialize two pointers, `current` and `next`, to the head of the list.
  3. Iterate through the list, checking if the current node has a duplicate value.
  4. If it does, move the `next` pointer until we find a node with a different value.
  5. If it does not, move the `current` pointer to the next node.
- Proof of optimality: This solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem because we must at least read the input once.

```cpp
// Optimal Approach
ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* current = dummy;
    
    while (current->next && current->next->next) {
        if (current->next->val == current->next->next->val) {
            int val = current->next->val;
            while (current->next && current->next->val == val) {
                ListNode* temp = current->next;
                current->next = current->next->next;
                delete temp;
            }
        } else {
            current = current->next;
        }
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we are only iterating through the list once.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the dummy node and the current node.
> - **Optimality proof:** The time complexity is optimal because we must at least read the input once, and the space complexity is optimal because we are not using any additional data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, dummy node, and iteration through a linked list.
- Problem-solving patterns identified: Checking for duplicates in a sorted list and removing them.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: Removing duplicates from an unsorted list, finding the first duplicate in a list, and removing nodes from a linked list based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as an empty list or a list with only one node.
- Edge cases to watch for: Lists with duplicate values at the beginning or end, and lists with multiple nodes having the same value.
- Performance pitfalls: Using a nested loop structure, which can increase the time complexity unnecessarily.
- Testing considerations: Testing the function with different types of input, such as empty lists, lists with one node, and lists with multiple nodes having the same value.