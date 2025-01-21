## Insertion Sort List

**Problem Link:** https://leetcode.com/problems/insertion-sort-list/description

**Problem Statement:**
- Input: A linked list with integer values.
- Constraints: The linked list can be empty or contain any number of nodes.
- Expected Output: The sorted linked list in ascending order.
- Key Requirements: Sort the linked list using the insertion sort algorithm.
- Edge Cases: Handle empty lists, lists with one node, and lists with duplicate values.

**Example Test Cases:**
- Input: `4 -> 2 -> 1 -> 3`, Output: `1 -> 2 -> 3 -> 4`
- Input: `-1 -> 5 -> 3 -> 4 -> 0`, Output: `-1 -> 0 -> 3 -> 4 -> 5`
- Input: ``, Output: `` (empty list)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the list and compare each node with the previous nodes to find its correct position.
- Step-by-step breakdown:
  1. Start with the head of the list.
  2. For each node, compare its value with the values of the previous nodes.
  3. If a node's value is smaller than a previous node's value, shift the previous node's value to the next node until we find the correct position for the current node.
- Why this approach comes to mind first: It's a straightforward implementation of the insertion sort algorithm for a linked list.

```cpp
// Brute Force Approach
ListNode* insertionSortList(ListNode* head) {
    // Create a new dummy node to simplify some corner cases such as a list with only one node
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    
    // Traverse the list
    ListNode* current = head;
    while (current) {
        // If the next node's value is smaller than the current node's value, we need to insert it before the current node
        if (current->next && current->next->val < current->val) {
            ListNode* nextNode = current->next;
            ListNode* prev = dummy;
            // Find the correct position for the next node
            while (prev->next && prev->next->val < nextNode->val) {
                prev = prev->next;
            }
            // Insert the next node at the correct position
            current->next = nextNode->next;
            nextNode->next = prev->next;
            prev->next = nextNode;
        } else {
            current = current->next;
        }
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the list. This is because we are iterating through the list and for each node, we are potentially iterating through the previous nodes to find its correct position.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the dummy node and other variables.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loop structure, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of shifting nodes around when we find a node that needs to be inserted before previous nodes, we can maintain a sorted list up to the current node and insert the next node into its correct position in the sorted part of the list.
- Detailed breakdown:
  1. Start with a dummy node that points to the head of the list.
  2. Iterate through the list. For each node, find its correct position in the sorted part of the list (from the dummy node to the previous node) and insert it there.
- Proof of optimality: This approach still has a time complexity of $O(n^2)$ in the worst case because we are potentially searching through the entire sorted part of the list for each node. However, it's more efficient in practice because it avoids unnecessary node shifts.

```cpp
// Optimal Approach
ListNode* insertionSortList(ListNode* head) {
    ListNode* dummy = new ListNode(0);
    ListNode* current = head;
    
    while (current) {
        ListNode* pre = dummy;
        // Find the correct position for the current node in the sorted part of the list
        while (pre->next && pre->next->val < current->val) {
            pre = pre->next;
        }
        // Insert the current node at the correct position
        ListNode* temp = current->next;
        current->next = pre->next;
        pre->next = current;
        current = temp;
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the list. This is because in the worst case, for each node, we are searching through the entire sorted part of the list to find its correct position.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the dummy node and other variables.
> - **Optimality proof:** This is the optimal approach for sorting a linked list using the insertion sort algorithm because it minimizes the number of node shifts and comparisons needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Insertion sort, linked list manipulation.
- Problem-solving patterns identified: Iterating through a list and maintaining a sorted subset.
- Optimization techniques learned: Minimizing node shifts in a linked list.
- Similar problems to practice: Sorting arrays or other data structures using insertion sort.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating node pointers, not handling edge cases (e.g., empty list, list with one node).
- Edge cases to watch for: Empty lists, lists with duplicate values, lists with negative values.
- Performance pitfalls: Using inefficient algorithms or data structures for large inputs.
- Testing considerations: Thoroughly testing the function with various input cases, including edge cases.