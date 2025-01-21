## Delete Nodes from Linked List Present in Array
**Problem Link:** https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description

**Problem Statement:**
- Input: A linked list and an array of values.
- Output: The linked list with nodes containing values present in the array removed.
- Key Requirements:
  - The input linked list is not empty.
  - The array can be empty.
- Edge Cases:
  - Removing all nodes from the linked list.
  - Removing nodes from the beginning, middle, or end of the linked list.

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the linked list and for each node, checking if its value is present in the array. If it is, remove the node.
- Step-by-step breakdown:
  1. Create a `set` from the array for efficient lookups.
  2. Initialize a dummy node to simplify edge cases like removing the head of the list.
  3. Iterate through the linked list. For each node, check if its value is in the set.
  4. If the value is found, skip this node by updating the `next` pointer of the previous node.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
// Brute Force Approach
ListNode* removeNodes(ListNode* head, vector<int>& vals) {
    // Create a set for O(1) lookups
    unordered_set<int> valSet(vals.begin(), vals.end());
    
    // Initialize a dummy node
    ListNode dummy(0);
    dummy.next = head;
    ListNode* prev = &dummy;
    
    // Iterate through the linked list
    while (prev->next) {
        if (valSet.find(prev->next->val) != valSet.end()) {
            // Remove the node
            prev->next = prev->next->next;
        } else {
            prev = prev->next;
        }
    }
    
    return dummy.next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of elements in the array. This is because we create a set from the array in $O(m)$ time and then iterate through the linked list in $O(n)$ time.
> - **Space Complexity:** $O(m)$ for storing the array elements in a set. The space complexity is dominated by the set creation.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in both the linked list and the array. The space complexity is linear with respect to the array size due to the set creation.

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is essentially the brute force approach since it already achieves a linear time complexity with respect to the total number of elements (both in the linked list and the array).
- The key insight is recognizing that creating a set from the array allows for efficient lookups, making the overall process as efficient as possible given the problem constraints.
- Detailed breakdown:
  1. Create a set from the array.
  2. Use a dummy node to simplify the removal process.
  3. Iterate through the linked list, removing nodes whose values are found in the set.
- Proof of optimality: Any solution must at least read the input (the linked list and the array), which requires $O(n + m)$ time. Thus, the optimal time complexity is $O(n + m)$.

```cpp
// Optimal Approach
ListNode* removeNodes(ListNode* head, vector<int>& vals) {
    unordered_set<int> valSet(vals.begin(), vals.end());
    ListNode dummy(0);
    dummy.next = head;
    ListNode* prev = &dummy;
    
    while (prev->next) {
        if (valSet.find(prev->next->val) != valSet.end()) {
            prev->next = prev->next->next;
        } else {
            prev = prev->next;
        }
    }
    
    return dummy.next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of elements in the array.
> - **Space Complexity:** $O(m)$ for storing the array elements in a set.
> - **Optimality proof:** The solution has a linear time complexity with respect to the total input size, which is optimal because any algorithm must at least read the input.

### Final Notes

**Learning Points:**
- The importance of using data structures like sets for efficient lookups.
- How to handle edge cases in linked list problems using dummy nodes.
- The concept of optimality in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the use of a dummy node to simplify the code.
- Failing to recognize the benefit of using a set for array elements.
- Not analyzing the time and space complexity of the solution.