## Odd Even Linked List

**Problem Link:** https://leetcode.com/problems/odd-even-linked-list/description

**Problem Statement:**
- Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list.
- The **odd indices** are the nodes at indices 1, 3, 5, ..., and the **even indices** are the nodes at indices 0, 2, 4, ....
- The input linked list will have at least one node, and the nodes will have unique values.
- The expected output is the head of the modified linked list.

**Example Test Cases:**
- Example 1: Given the linked list `1 -> 2 -> 3 -> 4 -> 5`, the output should be `1 -> 3 -> 5 -> 2 -> 4`.
- Example 2: Given the linked list `2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7`, the output should be `2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the linked list and store the nodes in two separate lists, one for odd indices and one for even indices.
- Then, we can concatenate these two lists to get the modified linked list.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
// Brute Force Approach
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        
        // Store nodes in two separate lists
        vector<ListNode*> odd;
        vector<ListNode*> even;
        
        ListNode* curr = head;
        int index = 0;
        
        while (curr) {
            if (index % 2 == 0) {
                even.push_back(curr);
            } else {
                odd.push_back(curr);
            }
            curr = curr->next;
            index++;
        }
        
        // Concatenate the two lists
        for (int i = 0; i < odd.size() - 1; i++) {
            odd[i]->next = odd[i + 1];
        }
        for (int i = 0; i < even.size() - 1; i++) {
            even[i]->next = even[i + 1];
        }
        
        // Connect the last node of the odd list to the first node of the even list
        if (!odd.empty() && !even.empty()) {
            odd.back()->next = even[0];
            even.back()->next = nullptr;
        }
        
        return odd.empty() ? even[0] : odd[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because we traverse the linked list once and perform constant time operations for each node.
> - **Space Complexity:** $O(n)$, because we store the nodes in two separate lists.
> - **Why these complexities occur:** These complexities occur because we need to traverse the entire linked list to store the nodes in two separate lists, and we need to store all the nodes in the lists.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use two pointers, `odd` and `even`, to keep track of the last node in the odd list and the last node in the even list, respectively.
- We can then traverse the linked list and move the nodes to their respective lists in a single pass.
- This approach is optimal because it only requires a single pass through the linked list and uses a constant amount of extra space.

```cpp
// Optimal Approach
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        
        odd->next = evenHead;
        
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because we traverse the linked list once and perform constant time operations for each node.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of extra space to store the `odd` and `even` pointers.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the linked list and uses a constant amount of extra space, which is the minimum required to solve the problem.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of two pointers to keep track of the last node in two separate lists.
- The problem-solving pattern identified is to use a single pass through the linked list to move nodes to their respective lists.
- The optimization technique learned is to use a constant amount of extra space to store the `odd` and `even` pointers.

**Mistakes to Avoid:**
- A common implementation error is to forget to update the `next` pointer of the last node in the odd list to point to the first node in the even list.
- An edge case to watch for is when the linked list has only one node, in which case the function should return the head of the linked list as is.
- A performance pitfall is to use a brute force approach that requires storing all the nodes in two separate lists, which can be inefficient for large linked lists.