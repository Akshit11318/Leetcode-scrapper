## Remove Nth Node From End of List
**Problem Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/description

**Problem Statement:**
- Input: The head of a linked list and an integer `n`.
- Constraints: The number of nodes in the list is `sz`.
- Expected Output: The head of the modified linked list after removing the nth node from the end.
- Key Requirements: 
    - Handle edge cases where `n` equals `1` or `sz`.
    - Ensure the solution works for lists with any number of nodes.
- Example Test Cases:
    - For a list `1 -> 2 -> 3 -> 4 -> 5`, removing the `2nd` node from the end results in `1 -> 2 -> 3 -> 5`.
    - For a list `1`, removing the `1st` node from the end results in an empty list.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves calculating the length of the list and then finding the node to be removed based on its position from the end.
- Step-by-step breakdown:
    1. Traverse the list to calculate its length.
    2. Determine the position of the node to be removed from the beginning based on `n` and the list length.
    3. Traverse the list again to find the node before the one to be removed.
    4. Update the `next` pointer of the found node to skip the node to be removed.

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Calculate the length of the list
        int length = 0;
        ListNode* temp = head;
        while (temp) {
            length++;
            temp = temp->next;
        }
        
        // Handle edge case where n equals the length of the list
        if (n == length) {
            return head->next;
        }
        
        // Find the node before the one to be removed
        ListNode* prev = head;
        for (int i = 0; i < length - n - 1; i++) {
            prev = prev->next;
        }
        
        // Remove the nth node from the end
        prev->next = prev->next->next;
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(sz)$, where $sz$ is the number of nodes in the list, because we traverse the list twice.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the temporary node and the length of the list.
> - **Why these complexities occur:** The time complexity is linear due to the two traversals of the list, and the space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use two pointers that are `n` steps apart. When the leading pointer reaches the end of the list, the trailing pointer will be at the node before the one to be removed.
- Detailed breakdown:
    1. Initialize two pointers, `lead` and `trail`, both pointing to the head of the list.
    2. Move `lead` `n` steps forward.
    3. Move both pointers one step at a time until `lead` reaches the end of the list.
    4. Update the `next` pointer of the node before the one to be removed to skip the node to be removed.

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Initialize two pointers
        ListNode* lead = head;
        ListNode* trail = head;
        
        // Move the lead pointer n steps forward
        for (int i = 0; i < n; i++) {
            lead = lead->next;
        }
        
        // If the lead pointer has reached the end, it means we need to remove the head
        if (!lead) {
            return head->next;
        }
        
        // Move both pointers until the lead pointer reaches the end
        while (lead->next) {
            lead = lead->next;
            trail = trail->next;
        }
        
        // Remove the nth node from the end
        trail->next = trail->next->next;
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(sz)$, where $sz$ is the number of nodes in the list, as we traverse the list once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the two pointers.
> - **Optimality proof:** This solution is optimal because it only requires a single traversal of the list, and we cannot do better than linear time for this problem since we must at least look at each node once.

---

### Final Notes

**Learning Points:**
- The importance of understanding the structure of the problem, in this case, a linked list.
- How to use two pointers to solve problems involving relative positioning in a list.
- The value of optimizing solutions by reducing the number of traversals or operations.

**Mistakes to Avoid:**
- Not handling edge cases properly, such as when `n` equals `1` or the length of the list.
- Failing to update pointers correctly when removing a node from a linked list.
- Not considering the implications of list length and the position of the node to be removed on the algorithm's complexity.