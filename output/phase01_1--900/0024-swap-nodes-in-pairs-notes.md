## Swap Nodes in Pairs

**Problem Link:** https://leetcode.com/problems/swap-nodes-in-pairs/description

**Problem Statement:**
- Input: The head of a linked list.
- Constraints: The number of nodes in the list is in the range $[0, 100]$.
- Expected Output: The head of the modified linked list where every two adjacent nodes are swapped.
- Key Requirements:
  - Swap adjacent nodes in pairs.
  - Handle edge cases such as an empty list, a list with one node, and a list with an odd number of nodes.
- Example Test Cases:
  - For the input `1 -> 2 -> 3 -> 4`, the output should be `2 -> 1 -> 4 -> 3`.
  - For the input `1 -> 2 -> 3`, the output should be `2 -> 1 -> 3`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the linked list and swap each pair of adjacent nodes.
- This involves keeping track of the current node and the next node, then swapping their positions in the list.
- This approach comes to mind first because it directly addresses the requirement to swap adjacent nodes.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head; // Base case: if the list has 0 or 1 node, return as is.
        }
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* current = dummy;
        
        while (current->next && current->next->next) {
            ListNode* first = current->next;
            ListNode* second = current->next->next;
            
            // Swap the nodes
            first->next = second->next;
            current->next = second;
            current->next->next = first;
            
            // Move to the next pair
            current = first;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, since we are potentially visiting each node once.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with the input size, only a constant amount of space for the dummy node and other variables.
> - **Why these complexities occur:** The time complexity is linear because we are iterating through the list once, and the space complexity is constant because we are only using a fixed amount of space regardless of the input size.

### Optimal Approach (Required)

The provided brute force approach is already optimal for this problem, as it directly addresses the requirement to swap adjacent nodes in a single pass through the list. The use of a dummy node simplifies the handling of the head of the list and reduces the number of edge cases to consider.

However, for clarity and adherence to the template, let's reiterate the optimal approach:

**Explanation:**
- The key insight is to use a dummy node to simplify the swapping process, especially when dealing with the head of the list.
- The detailed breakdown involves iterating through the list, swapping each pair of nodes, and then moving on to the next pair.
- Proof of optimality lies in the fact that we are only visiting each node once and using a constant amount of additional space, making the solution both time and space efficient.

```cpp
// Same code as provided in the brute force approach
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space.
> - **Optimality proof:** This is the best possible complexity for this problem because we must at least visit each node once to swap them, and we are doing so in a single pass with minimal additional space.

### Final Notes

**Learning Points:**
- Key algorithmic concept: Iterating through a linked list and swapping nodes.
- Problem-solving pattern: Using a dummy node to simplify edge cases.
- Optimization technique: Minimizing the number of passes through the data structure.

**Mistakes to Avoid:**
- Not handling edge cases such as an empty list or a list with one node.
- Not using a dummy node, which can complicate the swapping logic for the head of the list.
- Incorrectly updating the `next` pointers during the swapping process.