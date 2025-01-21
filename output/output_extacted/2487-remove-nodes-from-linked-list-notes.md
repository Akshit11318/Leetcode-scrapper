## Remove Nodes From Linked List
**Problem Link:** https://leetcode.com/problems/remove-nodes-from-linked-list/description

**Problem Statement:**
- Input: A linked list where each node has a value and a `next` pointer.
- Constraints: The list is non-empty, and the values are integers.
- Expected Output: The modified linked list with all nodes having values less than the next node removed.
- Key Requirements: The solution should handle edge cases such as a list with a single node or nodes with duplicate values.
- Example Test Cases:
  - Example 1: Input: `1 -> 2 -> 3 -> 4 -> 5`, Output: `1 -> 2 -> 3 -> 4 -> 5`
  - Example 2: Input: `5 -> 4 -> 3 -> 2 -> 1`, Output: `5`
  - Example 3: Input: `1 -> 3 -> 2 -> 4 -> 5`, Output: `1 -> 3 -> 4 -> 5`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the list and compare each node's value with the next node's value.
- If a node's value is greater than or equal to the next node's value, remove it from the list.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        // Create a dummy node to simplify edge cases
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* curr = head;

        while (curr) {
            if (curr->next && curr->val > curr->next->val) {
                // Remove the current node
                prev->next = curr->next;
                curr = prev->next;
            } else {
                prev = curr;
                curr = curr->next;
            }
        }

        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the list, because we make a single pass through the list.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the dummy node and pointers.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is constant because we don't allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack to keep track of the nodes in decreasing order.
- We iterate through the list and push nodes onto the stack if the current node's value is less than the top node's value on the stack.
- If the current node's value is greater than or equal to the top node's value, we pop nodes from the stack until we find a node with a value less than the current node's value or the stack is empty.
- This approach is optimal because it ensures that the resulting list is in decreasing order and we only make a single pass through the list.

```cpp
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        // Create a stack to store nodes in decreasing order
        stack<ListNode*> s;
        ListNode* curr = head;

        while (curr) {
            // Pop nodes from the stack if the current node's value is greater
            while (!s.empty() && s.top()->val <= curr->val) {
                s.pop();
            }
            // Push the current node onto the stack
            s.push(curr);
            curr = curr->next;
        }

        // Reconstruct the list from the stack
        ListNode* dummy = new ListNode(0);
        ListNode* prev = dummy;
        while (!s.empty()) {
            prev->next = s.top();
            s.pop();
            prev = prev->next;
        }
        prev->next = nullptr;

        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the list, because we make a single pass through the list.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, we might need to store all nodes in the stack.
> - **Optimality proof:** This approach is optimal because it ensures that the resulting list is in decreasing order and we only make a single pass through the list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: stack usage, linked list manipulation, and iterative approach.
- Problem-solving patterns identified: using a stack to keep track of nodes in decreasing order.
- Optimization techniques learned: reducing the number of passes through the list and minimizing the amount of extra space used.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty list or a list with a single node.
- Edge cases to watch for: duplicate values in the list, which can affect the correctness of the solution.
- Performance pitfalls: using an inefficient data structure, such as a linked list with random access, which can lead to poor performance.
- Testing considerations: thoroughly testing the solution with different input scenarios, including edge cases and large inputs.