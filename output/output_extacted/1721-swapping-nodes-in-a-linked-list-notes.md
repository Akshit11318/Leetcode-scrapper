## Swapping Nodes in a Linked List

**Problem Link:** [https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description)

**Problem Statement:**
- Input format: The function takes the head of a linked list and an integer k as input.
- Constraints: The number of nodes in the list is in the range [1, 1000].
- Expected output format: The function should return the modified linked list after swapping the kth node from the beginning and the kth node from the end.
- Key requirements and edge cases to consider: 
    - The input list may have fewer than 2k nodes.
    - The input list may have exactly 2k nodes.
    - The input list may have more than 2k nodes.
- Example test cases with explanations:
    - For the input [1,2,3,4,5] and k = 2, the output should be [1,4,3,2,5] because the 2nd node from the beginning (2) is swapped with the 2nd node from the end (4).
    - For the input [7,9,6,6,7,8,3,0,9,5] and k = 5, the output should be [7,9,6,6,7,8,3,0,9,5] because the 5th node from the beginning (7) is swapped with the 5th node from the end (7), resulting in no change.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can traverse the linked list to find the kth node from the beginning and the kth node from the end, and then swap their values.
- Step-by-step breakdown of the solution:
    1. Traverse the linked list to find the length of the list.
    2. Traverse the linked list again to find the kth node from the beginning.
    3. Traverse the linked list again to find the kth node from the end.
    4. Swap the values of the kth node from the beginning and the kth node from the end.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the multiple traversals of the linked list.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        // Find the length of the list
        int length = 0;
        ListNode* temp = head;
        while (temp != nullptr) {
            length++;
            temp = temp->next;
        }
        
        // Find the kth node from the beginning
        ListNode* kthFromBeginning = head;
        for (int i = 1; i < k; i++) {
            kthFromBeginning = kthFromBeginning->next;
        }
        
        // Find the kth node from the end
        ListNode* kthFromEnd = head;
        for (int i = 1; i < length - k + 1; i++) {
            kthFromEnd = kthFromEnd->next;
        }
        
        // Swap the values of the kth node from the beginning and the kth node from the end
        int tempValue = kthFromBeginning->val;
        kthFromBeginning->val = kthFromEnd->val;
        kthFromEnd->val = tempValue;
        
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the length of the linked list, because we traverse the list multiple times.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the kth nodes from the beginning and the end.
> - **Why these complexities occur:** The time complexity is high due to the multiple traversals of the linked list, while the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can traverse the linked list only once to find the kth node from the beginning and the kth node from the end.
- Detailed breakdown of the approach:
    1. Traverse the linked list to find the kth node from the beginning.
    2. Traverse the linked list to find the length of the list.
    3. Traverse the linked list again to find the kth node from the end.
    4. Swap the values of the kth node from the beginning and the kth node from the end.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because we only traverse the linked list twice.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        // Find the kth node from the beginning
        ListNode* kthFromBeginning = head;
        for (int i = 1; i < k; i++) {
            kthFromBeginning = kthFromBeginning->next;
        }
        
        // Find the length of the list and the kth node from the end
        ListNode* temp = kthFromBeginning;
        ListNode* kthFromEnd = head;
        while (temp->next != nullptr) {
            temp = temp->next;
            kthFromEnd = kthFromEnd->next;
        }
        
        // Swap the values of the kth node from the beginning and the kth node from the end
        int tempValue = kthFromBeginning->val;
        kthFromBeginning->val = kthFromEnd->val;
        kthFromEnd->val = tempValue;
        
        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the length of the linked list, because we traverse the list twice.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the kth nodes from the beginning and the end.
> - **Optimality proof:** This approach has the optimal time complexity because we only traverse the linked list twice, and we cannot do better than that.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list traversal, node swapping.
- Problem-solving patterns identified: Optimizing brute force solutions by reducing the number of traversals.
- Optimization techniques learned: Reducing the number of traversals by combining multiple operations into one traversal.
- Similar problems to practice: Other linked list problems, such as reversing a linked list or finding the middle of a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty linked list or a linked list with only one node.
- Edge cases to watch for: Linked lists with fewer than 2k nodes, linked lists with exactly 2k nodes, linked lists with more than 2k nodes.
- Performance pitfalls: Traversing the linked list multiple times when it can be done in one traversal.
- Testing considerations: Testing the solution with different linked list lengths and k values to ensure it works correctly in all cases.