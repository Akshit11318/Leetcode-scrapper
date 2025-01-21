## Reorder List
**Problem Link:** [https://leetcode.com/problems/reorder-list/description](https://leetcode.com/problems/reorder-list/description)

**Problem Statement:**
- Input format and constraints: The problem takes a singly linked list as input and requires reordering the nodes such that the first node is followed by the last node, then the second node, and so on.
- Expected output format: The modified linked list with the nodes reordered.
- Key requirements and edge cases to consider: The input linked list can be empty or contain only one node. The solution should handle these edge cases correctly.
- Example test cases with explanations:
  - Input: `1 -> 2 -> 3 -> 4`, Output: `1 -> 4 -> 2 -> 3`
  - Input: `1 -> 2 -> 3 -> 4 -> 5`, Output: `1 -> 5 -> 2 -> 4 -> 3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to store the nodes of the linked list in a vector or array, and then reorder the nodes based on their indices.
- Step-by-step breakdown of the solution:
  1. Traverse the linked list and store the nodes in a vector.
  2. Initialize two pointers, one at the beginning and one at the end of the vector.
  3. Reorder the nodes by iterating through the vector and linking the nodes in the desired order.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first step in solving the problem.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void reorderList(ListNode* head) {
    if (!head || !head->next) return;

    vector<ListNode*> nodes;
    ListNode* curr = head;
    while (curr) {
        nodes.push_back(curr);
        curr = curr->next;
    }

    int i = 0, j = nodes.size() - 1;
    while (i < j) {
        nodes[i]->next = nodes[j];
        i++;
        if (i == j) break;
        nodes[j]->next = nodes[i];
        j--;
    }
    nodes[i]->next = NULL;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, since we need to traverse the list twice: once to store the nodes and once to reorder them.
> - **Space Complexity:** $O(n)$, as we need to store all the nodes in the vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node in the list. The space complexity is also linear because we need to store all the nodes in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all the nodes in a vector, we can find the middle of the linked list and reverse the second half. Then, we can reorder the nodes by iterating through the first half and the reversed second half.
- Detailed breakdown of the approach:
  1. Find the middle of the linked list using the slow and fast pointer technique.
  2. Reverse the second half of the linked list.
  3. Reorder the nodes by iterating through the first half and the reversed second half.
- Proof of optimality: This approach is optimal because it only requires a single pass through the linked list to find the middle and reverse the second half, and then another pass to reorder the nodes.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
void reorderList(ListNode* head) {
    if (!head || !head->next) return;

    // Find the middle of the linked list
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
    ListNode* second = slow->next;
    slow->next = NULL;
    ListNode* prev = NULL;
    while (second) {
        ListNode* next = second->next;
        second->next = prev;
        prev = second;
        second = next;
    }

    // Reorder the nodes
    ListNode* first = head;
    while (prev) {
        ListNode* temp1 = first->next;
        ListNode* temp2 = prev->next;
        first->next = prev;
        prev->next = temp1;
        first = temp1;
        prev = temp2;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list, since we need to traverse the list three times: once to find the middle, once to reverse the second half, and once to reorder the nodes.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node in the list. The space complexity is constant because we only use a fixed amount of space to store the pointers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, slow and fast pointer technique, reversing a linked list.
- Problem-solving patterns identified: Finding the middle of a linked list, reversing a linked list, reordering nodes.
- Optimization techniques learned: Reducing space complexity by avoiding unnecessary data structures.
- Similar problems to practice: Reverse Linked List, Rotate List, Merge Two Sorted Lists.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty linked list or a linked list with only one node.
- Edge cases to watch for: Linked lists with an odd or even number of nodes.
- Performance pitfalls: Using unnecessary data structures or algorithms that have high time or space complexity.
- Testing considerations: Thoroughly testing the solution with different input scenarios, including edge cases.