## Reverse Linked List II

**Problem Link:** https://leetcode.com/problems/reverse-linked-list-ii/description

**Problem Statement:**
- Input: The head of a singly linked list and two integers `left` and `right` (1-indexed).
- Constraints: The number of nodes in the list is `n`, `1 <= n <= 500`, `1 <= left <= right <= n`.
- Expected output: The head of the modified linked list after reversing the nodes from the `left` index to the `right` index.
- Key requirements: Reverse the specified segment of the linked list in-place.
- Example test cases:
  - Input: `head = [1,2,3,4,5]`, `left = 2`, `right = 4`. Output: `[1,4,3,2,5]`.
  - Input: `head = [5]`, `left = 1`, `right = 1`. Output: `[5]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves reversing the entire linked list and then adjusting the reversed segment to match the required indices. However, this approach is inefficient and not straightforward to implement.
- A simpler brute force approach would involve traversing the linked list to the `left` index, reversing the segment up to the `right` index, and then reconnecting the nodes to maintain the original list structure outside the reversed segment.
- This approach comes to mind first because it directly addresses the requirement of reversing a segment of the linked list.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;
        
        ListNode dummy(0);
        dummy.next = head;
        ListNode* pre = &dummy;
        
        // Move pre to the node before the start of the segment to reverse
        for (int i = 0; i < left - 1; i++) {
            pre = pre->next;
        }
        
        ListNode* curr = pre->next;
        // Reverse the segment
        for (int i = 0; i < right - left; i++) {
            ListNode* temp = curr->next;
            curr->next = temp->next;
            temp->next = pre->next;
            pre->next = temp;
        }
        
        return dummy.next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, because in the worst case, we traverse the entire list.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the dummy node and other pointers.
> - **Why these complexities occur:** The time complexity is linear because we potentially traverse the entire list to find the segment to reverse and to reverse it. The space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is similar to the brute force approach but is more efficient in practice because it minimizes the number of operations required to reverse the segment.
- We use a dummy node to simplify the handling of the head of the list and to avoid special casing when the segment to reverse starts at the head.
- We find the node before the start of the segment to reverse (`pre`) and then reverse the links between the nodes in the segment.
- This approach is optimal because it only requires a single pass through the list and uses a constant amount of extra space.

```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;
        
        ListNode dummy(0);
        dummy.next = head;
        ListNode* pre = &dummy;
        
        // Move pre to the node before the start of the segment to reverse
        for (int i = 0; i < left - 1; i++) {
            pre = pre->next;
        }
        
        ListNode* curr = pre->next;
        // Reverse the segment
        for (int i = 0; i < right - left; i++) {
            ListNode* temp = curr->next;
            curr->next = temp->next;
            temp->next = pre->next;
            pre->next = temp;
        }
        
        return dummy.next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Optimality proof:** This is the optimal solution because it achieves the lowest possible time complexity ($O(n)$) for this problem, as we must at least read the input once. The space complexity is also optimal ($O(1)$) because we only use a constant amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Linked list traversal, reversing a segment of a linked list.
- Problem-solving patterns: Using a dummy node to simplify edge cases, reversing links between nodes.
- Optimization techniques: Minimizing the number of operations required to reverse the segment.
- Similar problems to practice: Reversing a linked list, rotating a linked list.

**Mistakes to Avoid:**
- Not handling edge cases properly (e.g., when the segment to reverse starts at the head or is the entire list).
- Not using a dummy node to simplify the code.
- Not reversing the links correctly, leading to incorrect results or crashes.
- Not testing the solution thoroughly with different inputs.