## Print Immutable Linked List in Reverse
**Problem Link:** https://leetcode.com/problems/print-immutable-linked-list-in-reverse/description

**Problem Statement:**
- Input format and constraints: The problem involves a singly linked list where each node has an integer value and a pointer to the next node. The linked list is immutable, and we cannot modify it. We need to print the values of the nodes in reverse order.
- Expected output format: The output should be a list of integers representing the values of the nodes in the linked list, printed in reverse order.
- Key requirements and edge cases to consider: We should handle the case where the linked list is empty and the case where the linked list has only one node. We should also consider the case where the linked list has multiple nodes.
- Example test cases with explanations:
    - Example 1: Input: `1 -> 2 -> 3 -> 4 -> 5`, Output: `[5, 4, 3, 2, 1]`
    - Example 2: Input: `1 -> 2 -> 3`, Output: `[3, 2, 1]`
    - Example 3: Input: `1`, Output: `[1]`
    - Example 4: Input: `empty list`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To print the linked list in reverse order, we can first traverse the linked list and store the values of the nodes in a vector. Then, we can iterate over the vector in reverse order and print the values.
- Step-by-step breakdown of the solution:
    1. Traverse the linked list and store the values of the nodes in a vector.
    2. Iterate over the vector in reverse order.
    3. Print the values of the nodes.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. It involves a simple traversal of the linked list and a reverse iteration over a vector.

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> printLinkedListInReverse(ListNode* head) {
        vector<int> values;
        while (head) {
            values.push_back(head->val);
            head = head->next;
        }
        reverse(values.begin(), values.end());
        return values;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we traverse the linked list once and iterate over the vector once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we store the values of the nodes in a vector.
> - **Why these complexities occur:** The time complexity occurs because we perform two linear operations: traversing the linked list and iterating over the vector. The space complexity occurs because we store the values of the nodes in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a recursive approach to print the linked list in reverse order. We can recursively traverse the linked list and print the values of the nodes when we return from the recursive calls.
- Detailed breakdown of the approach:
    1. Recursively traverse the linked list.
    2. Print the values of the nodes when we return from the recursive calls.
- Proof of optimality: This approach is optimal because it only requires a single pass through the linked list and does not require any additional space.

```cpp
class Solution {
public:
    vector<int> printLinkedListInReverse(ListNode* head) {
        vector<int> values;
        traverse(head, values);
        return values;
    }
    
    void traverse(ListNode* node, vector<int>& values) {
        if (!node) return;
        traverse(node->next, values);
        values.push_back(node->val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we recursively traverse the linked list once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we store the values of the nodes in a vector and use recursive function calls.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the linked list and does not require any additional space beyond the recursive function calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive traversal, reverse iteration.
- Problem-solving patterns identified: Using recursive function calls to simplify the solution.
- Optimization techniques learned: Using a single pass through the linked list to reduce time complexity.
- Similar problems to practice: Printing a linked list in reverse order, reversing a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case in recursive functions, not checking for null pointers.
- Edge cases to watch for: Empty linked lists, linked lists with only one node.
- Performance pitfalls: Using unnecessary loops or recursive function calls.
- Testing considerations: Testing with different input sizes, testing with edge cases.