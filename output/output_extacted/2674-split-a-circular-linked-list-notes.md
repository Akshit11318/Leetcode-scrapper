## Split a Circular Linked List
**Problem Link:** https://leetcode.com/problems/split-a-circular-linked-list/description

**Problem Statement:**
- Input format: The head of a circular linked list.
- Constraints: The number of nodes in the list is in the range [1, 5 * 10^4].
- Expected output format: Two heads of the split circular linked lists.
- Key requirements: The original list should be split into two circular linked lists, and the second list should be made up of the last half of the nodes of the original list. If the number of nodes in the original list is odd, the extra node should go to the first list.
- Example test cases:
  - Example 1: Input: 0 -> 1 -> 2 -> 3 -> 0, Output: 0 -> 1 -> 0, 2 -> 3 -> 2
  - Example 2: Input: 2 -> 4 -> 1 -> 5 -> 2, Output: 2 -> 4 -> 2, 1 -> 5 -> 1

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can start by counting the number of nodes in the circular linked list. Then, we can calculate the middle index and split the list into two halves.
- Step-by-step breakdown of the solution:
  1. Count the number of nodes in the circular linked list.
  2. Calculate the middle index of the list.
  3. Find the node at the middle index and split the list into two halves.
  4. Connect the last node of the first half to the first node of the first half to form a circular linked list.
  5. Connect the last node of the second half to the first node of the second half to form a circular linked list.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* splitCircularLinkedList(ListNode* head) {
        if (!head || !head->next) return head;

        // Count the number of nodes in the circular linked list
        int count = 1;
        ListNode* current = head;
        while (current->next != head) {
            count++;
            current = current->next;
        }

        // Calculate the middle index
        int mid = count / 2;

        // Find the node at the middle index
        ListNode* midNode = head;
        for (int i = 0; i < mid; i++) {
            midNode = midNode->next;
        }

        // Split the list into two halves
        ListNode* secondHalf = midNode->next;
        midNode->next = head;

        // Find the last node of the second half
        current = secondHalf;
        while (current->next != head) {
            current = current->next;
        }

        // Connect the last node of the second half to the first node of the second half
        current->next = secondHalf;

        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the circular linked list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers.
> - **Why these complexities occur:** We need to traverse the entire list to count the number of nodes and find the middle index, which takes $O(n)$ time. The space complexity is $O(1)$ because we only use a constant amount of space to store the pointers.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use the slow and fast pointer technique to find the middle node of the circular linked list in one pass.
- Detailed breakdown of the approach:
  1. Initialize two pointers, slow and fast, to the head of the list.
  2. Move the fast pointer two steps at a time, and move the slow pointer one step at a time.
  3. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
  4. Split the list into two halves at the middle node.
  5. Connect the last node of the first half to the first node of the first half to form a circular linked list.
  6. Connect the last node of the second half to the first node of the second half to form a circular linked list.

```cpp
class Solution {
public:
    ListNode* splitCircularLinkedList(ListNode* head) {
        if (!head || !head->next) return head;

        // Use slow and fast pointer technique to find the middle node
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != head && fast->next->next != head) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Split the list into two halves
        ListNode* secondHalf = slow->next;
        slow->next = head;

        // Find the last node of the second half
        ListNode* current = secondHalf;
        while (current->next != head) {
            current = current->next;
        }

        // Connect the last node of the second half to the first node of the second half
        current->next = secondHalf;

        return head;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the circular linked list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers.
> - **Optimality proof:** We cannot do better than $O(n)$ time complexity because we need to traverse the entire list to find the middle node. The space complexity is optimal because we only use a constant amount of space to store the pointers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Slow and fast pointer technique, circular linked list traversal.
- Problem-solving patterns identified: Using slow and fast pointers to find the middle node of a circular linked list.
- Optimization techniques learned: Using slow and fast pointers to reduce the number of traversals.
- Similar problems to practice: Find the middle node of a circular linked list, detect cycle in a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty list or a list with only one node.
- Edge cases to watch for: Lists with an odd number of nodes, lists with an even number of nodes.
- Performance pitfalls: Using a naive approach that requires multiple traversals of the list.
- Testing considerations: Test the solution with different types of input, including edge cases and large inputs.