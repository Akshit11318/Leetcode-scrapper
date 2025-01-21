## Linked List Cycle II
**Problem Link:** https://leetcode.com/problems/linked-list-cycle-ii/description

**Problem Statement:**
- Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `nullptr`.
- The linked list is represented as a sequence of nodes where each node has a unique integer value.
- The input linked list will have at least one node and will not have more than $10^4$ nodes.
- Each node has a unique integer value in the range $[-2^{31}, 2^{31} - 1]$.
- `pos` is -1 or a valid index in the linked list.

**Expected Output Format:**
- The function should return the node where the cycle begins. If there is no cycle, return `nullptr`.

**Key Requirements and Edge Cases to Consider:**
- Handle the case where there is no cycle in the linked list.
- Handle the case where the cycle begins at the head of the linked list.
- Handle the case where the cycle begins at a node other than the head.

**Example Test Cases with Explanations:**
- Example 1:
    - Input: `head = [3,2,0,-4]`, `pos = 1`
    - Output: `tail connects to node index 1`
    - Explanation: There is a cycle in the linked list, where the tail connects to the second node.
- Example 2:
    - Input: `head = [1,2]`, `pos = 0`
    - Output: `tail connects to node index 0`
    - Explanation: There is a cycle in the linked list, where the tail connects to the head.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to use a `HashSet` to store the nodes we have visited.
- We iterate through the linked list, and for each node, we check if it is already in the `HashSet`.
- If it is, we return the node as the start of the cycle.
- If we reach the end of the linked list without finding a cycle, we return `nullptr`.

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> visited;
        while (head) {
            if (visited.find(head) != visited.end()) {
                return head;
            }
            visited.insert(head);
            head = head->next;
        }
        return nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, since we visit each node at most once.
> - **Space Complexity:** $O(n)$, since in the worst case, we store all nodes in the `HashSet`.
> - **Why these complexities occur:** The time complexity is linear because we only visit each node once, and the space complexity is also linear because we store each node in the `HashSet`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use Floyd's Tortoise and Hare algorithm, also known as the "slow and fast pointers" technique.
- We use two pointers, `slow` and `fast`, both starting at the head of the linked list.
- In each iteration, `slow` moves one step at a time, while `fast` moves two steps at a time.
- If there is a cycle, `fast` will eventually catch up to `slow` within the cycle.
- Once `fast` catches up to `slow`, we reset `slow` to the head of the linked list and keep `fast` at the meeting point.
- We then move both `slow` and `fast` one step at a time. The point where they meet again is the start of the cycle.

```cpp
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) {
            return nullptr;
        }
        ListNode *slow = head;
        ListNode *fast = head->next;
        while (slow != fast) {
            if (!fast || !fast->next) {
                return nullptr;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, since we visit each node at most once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the `slow` and `fast` pointers.
> - **Optimality proof:** This is the optimal solution because we only visit each node at most once, and we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is Floyd's Tortoise and Hare algorithm.
- The problem-solving pattern identified is the use of slow and fast pointers to detect cycles in linked lists.
- The optimization technique learned is to use a constant amount of space to store pointers instead of storing all nodes in a `HashSet`.

**Mistakes to Avoid:**
- A common implementation error is to not handle the case where the linked list has only one node.
- An edge case to watch for is when the cycle begins at the head of the linked list.
- A performance pitfall is to use a `HashSet` to store all nodes, which can lead to high memory usage for large linked lists.