## Remove Duplicates from an Unsorted Linked List

**Problem Link:** https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description

**Problem Statement:**
- Input: The head of an unsorted linked list.
- Output: The head of the modified linked list with duplicates removed.
- Key requirements and edge cases to consider:
  - Handle empty linked lists.
  - Identify and remove duplicate nodes based on node values.
- Example test cases with explanations:
  - A linked list with no duplicates.
  - A linked list with consecutive duplicates.
  - A linked list with non-consecutive duplicates.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the linked list and for each node, check every other node to see if there's a duplicate. If a duplicate is found, remove it.
- Step-by-step breakdown of the solution:
  1. Start from the head of the list.
  2. For each node, iterate through the rest of the list to check for duplicates.
  3. If a duplicate is found, remove it by updating the `next` pointer of the previous node.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every node against every other node.

```cpp
// Brute force implementation
ListNode* deleteDuplicatesUnsorted(ListNode* head) {
    if (!head || !head->next) return head;
    
    ListNode* current = head;
    while (current) {
        ListNode* runner = current;
        while (runner->next) {
            if (runner->next->val == current->val) {
                // Remove the duplicate node
                ListNode* temp = runner->next;
                runner->next = runner->next->next;
                delete temp;
            } else {
                runner = runner->next;
            }
        }
        current = current->next;
    }
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the linked list. This is because for each node, we potentially iterate through the rest of the list.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, as we only use a constant amount of space to store the pointers.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity. The space complexity is constant because we're modifying the existing list and not using any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `std::unordered_set` to keep track of node values we've seen so far. This allows us to check for duplicates in constant time.
- Detailed breakdown of the approach:
  1. Create an empty `std::unordered_set` to store unique node values.
  2. Initialize a dummy node that points to the head of the list.
  3. Iterate through the list. For each node, check if its value is in the set.
  4. If the value is not in the set, add it and move to the next node.
  5. If the value is in the set, remove the current node by updating the `next` pointer of the previous node.
- Proof of optimality: This approach ensures that we only need to traverse the list once, resulting in linear time complexity.

```cpp
// Optimal implementation
ListNode* deleteDuplicatesUnsorted(ListNode* head) {
    if (!head || !head->next) return head;
    
    std::unordered_set<int> seen;
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* prev = dummy;
    while (prev->next) {
        if (seen.find(prev->next->val) != seen.end()) {
            // Remove the duplicate node
            ListNode* temp = prev->next;
            prev->next = prev->next->next;
            delete temp;
        } else {
            seen.insert(prev->next->val);
            prev = prev->next;
        }
    }
    head = dummy->next;
    delete dummy;
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we make a single pass through the list.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every node's value in the set.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least look at each node once to determine if it's a duplicate.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set for efficient lookup and removal of duplicates.
- Problem-solving patterns identified: Iterating through a list and using a secondary data structure to track seen elements.
- Optimization techniques learned: Reducing time complexity by using a set instead of nested loops.
- Similar problems to practice: Other problems involving linked lists and duplicate removal.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like an empty list or a list with a single node.
- Edge cases to watch for: Duplicates at the beginning or end of the list.
- Performance pitfalls: Using nested loops for duplicate checking, leading to quadratic time complexity.
- Testing considerations: Ensure to test with various scenarios, including lists with no duplicates, consecutive duplicates, and non-consecutive duplicates.