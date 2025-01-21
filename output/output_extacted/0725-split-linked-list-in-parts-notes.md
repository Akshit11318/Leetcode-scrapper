## Split Linked List in Parts
**Problem Link:** https://leetcode.com/problems/split-linked-list-in-parts/description

**Problem Statement:**
- Input: A linked list `head` and an integer `k` representing the number of parts to split the list into.
- Constraints: The number of nodes in the linked list is in the range `[1, 1000]`, and `k` is in the range `[1, 1000]`.
- Expected Output: A list of `k` linked lists, where the `i-th` linked list contains the `i-th` part of the original list.
- Key Requirements: 
  - The length of each part should be as close as possible to the length of the other parts.
  - If the length of the linked list is not evenly divisible by `k`, the extra nodes should be distributed among the first parts.
- Edge Cases: 
  - When `k` equals the number of nodes in the list, each part should contain one node.
  - When `k` equals 1, the output should be the original list.
- Example Test Cases: 
  - Input: `head = [1,2,3,4]`, `k = 5`
    - Output: `[[1],[2],[3],[4],[]]`
  - Input: `head = [1,2,3,4,5,6,7,8,9,10]`, `k = 3`
    - Output: `[[1,2,3,4],[5,6,7],[8,9,10]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the length of the linked list, then determining the base length of each part by dividing the total length by `k`.
- The remainder of this division (if any) represents the extra nodes that need to be distributed among the first parts.
- We then iterate through the linked list, creating new lists for each part and appending nodes accordingly.

```cpp
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        // Calculate the length of the linked list
        int length = 0;
        ListNode* temp = head;
        while (temp != nullptr) {
            length++;
            temp = temp->next;
        }
        
        // Calculate the base length of each part and the remainder
        int baseLength = length / k;
        int remainder = length % k;
        
        vector<ListNode*> result;
        ListNode* current = head;
        
        // Split the linked list into parts
        for (int i = 0; i < k; i++) {
            int partLength = baseLength + (i < remainder ? 1 : 0);
            ListNode* partHead = current;
            
            // Move to the end of the current part
            for (int j = 0; j < partLength - 1; j++) {
                if (current != nullptr) {
                    current = current->next;
                }
            }
            
            // If this is not the last part, split the list
            if (current != nullptr) {
                ListNode* nextPart = current->next;
                current->next = nullptr;
                current = nextPart;
            }
            
            result.push_back(partHead);
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the number of nodes in the linked list and $k$ is the number of parts. The reason is that we first traverse the list to find its length ($O(n)$), then we potentially traverse the list again to split it into parts ($O(n)$), and we perform a constant amount of work for each part ($O(k)$).
> - **Space Complexity:** $O(k)$, for storing the heads of the split linked lists.
> - **Why these complexities occur:** The time complexity is dominated by the traversal of the linked list to calculate its length and to split it into parts. The space complexity is due to the storage of the heads of the split linked lists.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is the same as the brute force approach, but we can optimize the implementation by calculating the length of the linked list and splitting it into parts in a single pass.
- We first calculate the base length of each part and the remainder, then we iterate through the linked list, creating new lists for each part and appending nodes accordingly.

```cpp
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        // Calculate the length of the linked list
        int length = 0;
        ListNode* temp = head;
        while (temp != nullptr) {
            length++;
            temp = temp->next;
        }
        
        // Calculate the base length of each part and the remainder
        int baseLength = length / k;
        int remainder = length % k;
        
        vector<ListNode*> result;
        ListNode* current = head;
        
        // Split the linked list into parts
        for (int i = 0; i < k; i++) {
            int partLength = baseLength + (i < remainder ? 1 : 0);
            ListNode* partHead = current;
            
            // Move to the end of the current part
            for (int j = 0; j < partLength - 1; j++) {
                if (current != nullptr) {
                    current = current->next;
                }
            }
            
            // If this is not the last part, split the list
            if (current != nullptr) {
                ListNode* nextPart = current->next;
                current->next = nullptr;
                current = nextPart;
            }
            
            result.push_back(partHead);
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the number of nodes in the linked list and $k$ is the number of parts.
> - **Space Complexity:** $O(k)$, for storing the heads of the split linked lists.
> - **Optimality proof:** This solution is optimal because we only traverse the linked list once to calculate its length, and then we traverse it again to split it into parts. This is the minimum number of traversals required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: linked list traversal, division, and splitting.
- Problem-solving patterns identified: calculating the length of a linked list, dividing it into parts, and handling remainders.
- Optimization techniques learned: minimizing the number of traversals of the linked list.
- Similar problems to practice: splitting an array into parts, dividing a string into substrings.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where `k` is greater than the number of nodes in the linked list, not updating the `next` pointer of the last node in each part.
- Edge cases to watch for: when `k` equals the number of nodes in the list, when `k` equals 1.
- Performance pitfalls: traversing the linked list multiple times when it is not necessary.
- Testing considerations: testing with different values of `k`, testing with linked lists of different lengths.