## Delete N Nodes After M Nodes of a Linked List

**Problem Link:** https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description

**Problem Statement:**
- Input format: A linked list and two integers `m` and `n`.
- Constraints: `1 <= m + n <= 1000` and the number of nodes in the linked list is at most `1000`.
- Expected output format: The modified linked list after deleting `n` nodes after every `m` nodes.
- Key requirements and edge cases to consider: Handling cases where `m` or `n` is 0, and when the linked list has fewer than `m + n` nodes.
- Example test cases with explanations:
  - Test case 1: `head = [1,2,3,4,5,6,7,8,9,10]`, `m = 2`, `n = 3`. Expected output: `[1,2,6,7,10]`.
  - Test case 2: `head = [1,2,3,4,5,6,7,8,9,10]`, `m = 1`, `n = 1`. Expected output: `[1,3,5,7,9]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the linked list and keep track of the current position. When the position is a multiple of `m`, start deleting `n` nodes.
- Step-by-step breakdown of the solution:
  1. Initialize a pointer to the head of the linked list.
  2. Initialize counters for the current position and the number of nodes to delete.
  3. Iterate through the linked list. For each node, increment the position counter.
  4. If the position counter is a multiple of `m + n`, reset the position counter and the delete counter.
  5. If the position counter is a multiple of `m` and the delete counter is less than `n`, delete the current node and increment the delete counter.
- Why this approach comes to mind first: It directly implements the problem statement, making it an intuitive first attempt.

```cpp
// Brute force implementation
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* deleteNodes(ListNode* head, int m, int n) {
    if (!head || m == 0 || n == 0) return head;

    ListNode dummy(0);
    dummy.next = head;
    ListNode* curr = &dummy;
    int pos = 0;

    while (curr->next) {
        pos++;
        if (pos % (m + n) == m) {
            for (int i = 0; i < n && curr->next; i++) {
                curr->next = curr->next->next;
            }
            pos = 0;
        } else {
            curr = curr->next;
        }
    }

    return dummy.next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(L)$, where $L$ is the length of the linked list. This is because we potentially visit each node once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the dummy node and pointers.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the linked list, and the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating through the linked list and checking the position at each node, we can directly skip `m` nodes and then delete `n` nodes. This approach avoids unnecessary iterations and directly achieves the desired result.
- Detailed breakdown of the approach:
  1. Initialize a dummy node that points to the head of the linked list.
  2. Initialize a pointer to the dummy node.
  3. Iterate through the linked list. For each node, check if we need to delete `n` nodes after `m` nodes.
  4. If we need to delete `n` nodes, skip `m` nodes and then delete `n` nodes by updating the `next` pointer of the current node.
- Proof of optimality: This approach has the same time complexity as the brute force approach but with less overhead, making it more efficient in practice.

```cpp
// Optimal implementation
ListNode* deleteNodes(ListNode* head, int m, int n) {
    if (!head || m == 0 || n == 0) return head;

    ListNode dummy(0);
    dummy.next = head;
    ListNode* curr = &dummy;

    while (curr->next) {
        // Skip m nodes
        for (int i = 0; i < m - 1 && curr->next; i++) {
            curr = curr->next;
        }

        if (!curr->next) break;

        // Delete n nodes
        ListNode* temp = curr->next;
        for (int i = 0; i < n && temp->next; i++) {
            temp = temp->next;
        }

        // Update next pointer
        curr->next = temp->next;
        curr = temp->next;
    }

    return dummy.next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(L)$, where $L$ is the length of the linked list. This is because we potentially visit each node once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the dummy node and pointers.
> - **Optimality proof:** The time complexity is optimal because we must visit each node at least once to determine whether to delete it. The space complexity is optimal because we only use a fixed amount of space regardless of the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, iteration, and pointer management.
- Problem-solving patterns identified: Iterating through a linked list and updating pointers to achieve a desired result.
- Optimization techniques learned: Reducing unnecessary iterations and directly achieving the desired result.
- Similar problems to practice: Other linked list manipulation problems, such as inserting or deleting nodes at specific positions.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty linked list or `m` or `n` being 0.
- Edge cases to watch for: Handling cases where the linked list has fewer than `m + n` nodes.
- Performance pitfalls: Using unnecessary iterations or recursive function calls, which can lead to poor performance for large input sizes.
- Testing considerations: Thoroughly testing the implementation with various input sizes and edge cases to ensure correctness and performance.