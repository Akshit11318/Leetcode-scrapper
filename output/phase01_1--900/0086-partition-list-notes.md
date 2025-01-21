## Partition List
**Problem Link:** https://leetcode.com/problems/partition-list/description

**Problem Statement:**
- Input: A linked list and an integer `x`.
- Constraints: The linked list can have up to 200 nodes, and each node's value is between 0 and 1000.
- Expected Output: Modify the linked list such that all nodes with values less than `x` come before nodes with values greater than or equal to `x`.
- Key Requirements:
  - The relative order of nodes with values less than `x` must be preserved.
  - The relative order of nodes with values greater than or equal to `x` must be preserved.
- Edge Cases:
  - An empty linked list.
  - A linked list with all nodes having values less than `x`.
  - A linked list with all nodes having values greater than or equal to `x`.
- Example Test Cases:
  - Input: `head = [1,4,3,2,5,2]`, `x = 3`.
    Output: `[1,2,2,4,3,5]`.
  - Input: `head = [2,1]`, `x = 2`.
    Output: `[1,2]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the linked list and separating nodes into two categories: those with values less than `x` and those with values greater than or equal to `x`.
- We then reorder these nodes to meet the problem's requirements.
- This approach comes to mind first because it directly addresses the problem statement without requiring complex data structures or algorithms.

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
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes to simplify some corner cases such as lists with only one node, or removing the head of the list.
        ListNode* before_head = new ListNode(0);
        ListNode* before = before_head;
        ListNode* after_head = new ListNode(0);
        ListNode* after = after_head;

        // Partition list.
        while (head) {
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } else {
                after->next = head;
                after = after->next;
            }

            head = head->next;
        }

        after->next = nullptr;
        before->next = after_head->next;

        ListNode* newHead = before_head->next;
        delete before_head;
        delete after_head;

        return newHead;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. We make one pass through the list.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, as we use a constant amount of space to store our dummy nodes and pointers.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once. The space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach provided above. It involves creating two dummy nodes to help manage the before and after lists, then iterating through the original list to partition nodes based on the given value `x`.
- This approach is optimal because it achieves the required partitioning in a single pass through the list, using a minimal amount of extra space.
- Further optimization is not possible because we must at least look at each node once to determine its placement.

```cpp
// The code provided in the brute force section is already optimal.
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is optimal as we must examine each node.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output. This is optimal as we only use a constant amount of space.
> - **Optimality proof:** The time complexity is optimal because any algorithm must at least read the input, which takes $O(n)$ time. The space complexity is optimal because we only use a constant amount of extra space, regardless of the input size.

---

### Final Notes

**Learning Points:**
- This problem demonstrates the use of dummy nodes to simplify edge cases in linked list problems.
- It highlights the importance of considering the relative order of nodes in partitioning problems.
- The solution shows how to achieve optimal time and space complexity by making a single pass through the list and using minimal extra space.

**Mistakes to Avoid:**
- Failing to preserve the relative order of nodes within each partition.
- Not handling edge cases such as an empty list or a list with a single node.
- Using more space or time than necessary by not optimizing the partitioning process.