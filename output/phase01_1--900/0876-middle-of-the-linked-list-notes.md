## Middle of the Linked List

**Problem Link:** [https://leetcode.com/problems/middle-of-the-linked-list/description](https://leetcode.com/problems/middle-of-the-linked-list/description)

**Problem Statement:**
- Input: The head of a singly linked list.
- Constraints: The number of nodes in the list is in the range $[1, 100]$.
- Expected Output: The middle node of the linked list.
- Key Requirements and Edge Cases:
  - Handle lists with an odd number of nodes.
  - Handle lists with an even number of nodes.
- Example Test Cases:
  - For the list `1 -> 2 -> 3 -> 4 -> 5`, the output should be `3`.
  - For the list `1 -> 2 -> 3 -> 4`, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the linked list to count the number of nodes.
- Then, traverse the list again to find the middle node.
- This approach comes to mind first because it directly addresses the requirement to find the middle node.

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
    ListNode* middleNode(ListNode* head) {
        // Count the number of nodes in the list
        int count = 0;
        ListNode* temp = head;
        while (temp != nullptr) {
            count++;
            temp = temp->next;
        }
        
        // Find the middle node
        int middleIndex = count / 2;
        temp = head;
        for (int i = 0; i < middleIndex; i++) {
            temp = temp->next;
        }
        
        return temp;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n) + O(n/2) = O(2n) = O(n)$, where $n$ is the number of nodes in the list. The first $O(n)$ comes from counting the nodes, and the second $O(n/2)$ comes from finding the middle node.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and the temporary node pointer.
> - **Why these complexities occur:** The time complexity occurs because we traverse the list twice: once to count the nodes and once to find the middle node. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use two pointers, one moving twice as fast as the other.
- When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
- This approach is optimal because it only requires a single pass through the list.

```cpp
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the list. We only traverse the list once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the slow and fast pointers.
> - **Optimality proof:** This approach is optimal because we only need to traverse the list once to find the middle node. Any approach that requires multiple passes through the list will be less efficient.

---

### Final Notes

**Learning Points:**
- The **two-pointer technique** is useful for finding the middle of a linked list.
- **Single-pass algorithms** are often more efficient than multi-pass algorithms.
- **Optimality** can be proven by showing that an algorithm has the best possible time or space complexity.

**Mistakes to Avoid:**
- **Not checking for null pointers** can lead to runtime errors.
- **Not handling edge cases** can lead to incorrect results.
- **Not optimizing algorithms** can lead to poor performance.