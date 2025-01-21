## Merge Nodes in Between Zeros
**Problem Link:** [https://leetcode.com/problems/merge-nodes-in-between-zeros/description](https://leetcode.com/problems/merge-nodes-in-between-zeros/description)

**Problem Statement:**
- Input: A linked list where each node has a value and a next pointer.
- Constraints: The input linked list is non-empty and contains at least one node with a value of 0.
- Expected Output: A linked list where all nodes between two zeros are merged into a single node with the sum of their values.
- Key Requirements:
  - The merged nodes should be adjacent to the zeros.
  - Non-zero nodes outside the range of zeros should remain unchanged.
- Edge Cases:
  - A linked list with only one zero.
  - A linked list with multiple consecutive zeros.
  - A linked list with non-zero values at the beginning or end.
- Example Test Cases:
  - Input: `0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0 -> null`
    - Output: `0 -> 4 -> 0 -> 11 -> 0 -> null`
  - Input: `0 -> 1 -> 0 -> 3 -> 0 -> null`
    - Output: `0 -> 1 -> 0 -> 3 -> 0 -> null`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the linked list, identifying nodes between zeros, and merging them.
- We start by initializing variables to keep track of the current node, the sum of node values between zeros, and a flag to indicate whether we are currently between zeros.
- As we iterate, we check if a node's value is 0. If it is, we reset the sum and toggle the flag.
- When the flag is true (indicating we are between zeros), we add the current node's value to the sum.
- Once we encounter another zero, we create a new node with the sum of the values between the zeros and link it to the next node after the zero.
- We repeat this process until the end of the linked list.

```cpp
// Brute Force Implementation
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* mergeNodes(ListNode* head) {
    ListNode dummy(0);
    ListNode* curr = &dummy;
    curr->next = head;
    int sum = 0;
    bool betweenZeros = false;
    
    while (curr->next) {
        if (curr->next->val == 0) {
            if (betweenZeros) {
                ListNode* newNode = new ListNode(sum);
                newNode->next = curr->next->next;
                curr->next = newNode;
                sum = 0;
                betweenZeros = false;
            } else {
                betweenZeros = true;
            }
        } else if (betweenZeros) {
            sum += curr->next->val;
        }
        curr = curr->next;
    }
    
    return dummy.next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, since we make a single pass through the list.
> - **Space Complexity:** $O(1)$, not counting the output, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once. The space complexity is constant because we do not allocate any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution involves recognizing that we can solve this problem in a single pass through the linked list by maintaining a pointer to the last zero node encountered and another to the current node.
- We initialize two pointers, `lastZero` and `curr`, to the head of the list. We also keep track of the sum of node values between zeros.
- As we iterate, when we encounter a zero node, we update `lastZero` and reset the sum.
- For non-zero nodes, we add their value to the sum.
- When we encounter the next zero node, we create a new node with the sum of the values between the zeros and link it to the next node after the current zero node.
- We continue this process until the end of the linked list.
- This approach is optimal because it only requires a single pass through the list and uses a constant amount of extra memory.

```cpp
// Optimal Implementation
ListNode* mergeNodes(ListNode* head) {
    ListNode dummy(0);
    ListNode* curr = head;
    ListNode* lastZero = &dummy;
    int sum = 0;
    
    while (curr) {
        if (curr->val == 0) {
            if (sum != 0) {
                ListNode* newNode = new ListNode(sum);
                newNode->next = curr->next;
                lastZero->next = newNode;
                lastZero = newNode;
                sum = 0;
            } else {
                lastZero = curr;
            }
        } else {
            sum += curr->val;
        }
        curr = curr->next;
    }
    
    return dummy.next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, as we make a single pass through the list.
> - **Space Complexity:** $O(1)$, not counting the output, since we only use a constant amount of space.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is optimal because we do not use any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- The importance of single-pass algorithms for linked list problems.
- How to maintain pointers to relevant nodes (like the last zero node) to simplify the solution.
- The use of a dummy node to simplify edge cases like the head of the list.

**Mistakes to Avoid:**
- Not handling the edge case where the list starts or ends with zeros correctly.
- Forgetting to reset the sum after processing a group of nodes between zeros.
- Not considering the use of a dummy node to simplify the code.