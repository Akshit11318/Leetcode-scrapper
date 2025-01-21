## Rotate List
**Problem Link:** https://leetcode.com/problems/rotate-list/description

**Problem Statement:**
- Input format and constraints: Given the head of a list and an integer `k`, rotate the list to the right by `k` places.
- Expected output format: The head of the rotated list.
- Key requirements and edge cases to consider:
  - `1 <= k <= 2 * 10^5`
  - `0 <= list length <= 500`
  - `1 <= node value <= 100`
- Example test cases with explanations:
  - Example 1: `[1, 2, 3, 4, 5]`, `k = 2`, rotated list: `[4, 5, 1, 2, 3]`
  - Example 2: `[1, 2, 3, 4, 5]`, `k = 5`, rotated list: `[1, 2, 3, 4, 5]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simply cut the list at the `k`-th position from the end and append the cut portion to the front of the remaining list.
- Step-by-step breakdown of the solution:
  1. Find the length of the list.
  2. Calculate the actual number of positions to rotate, considering cases where `k` is greater than the list length.
  3. Cut the list at the calculated position from the end.
  4. Append the cut portion to the front of the remaining list.
- Why this approach comes to mind first: It's a straightforward, intuitive solution that directly addresses the problem statement.

```cpp
// Brute Force Approach
ListNode* rotateRight(ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;

    int length = 1;
    ListNode* tail = head;
    // Find the length of the list and the tail node
    while (tail->next) {
        tail = tail->next;
        length++;
    }

    k = k % length; // Handle cases where k > length
    if (k == 0) return head; // If k is a multiple of length, no rotation needed

    // Find the new tail node
    ListNode* newTail = head;
    for (int i = 0; i < length - k - 1; i++) {
        newTail = newTail->next;
    }

    // Rotate the list
    ListNode* newHead = newTail->next;
    newTail->next = nullptr;
    tail->next = head;

    return newHead;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the list. We traverse the list to find its length and then to rotate it.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store pointers and variables.
> - **Why these complexities occur:** The time complexity is linear because we need to traverse the list at least once to find its length and then again to perform the rotation. The space complexity is constant because we don't allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of cutting the list and appending, we can connect the tail of the list to the head, forming a circular list, and then find the new tail and head positions based on the rotation.
- Detailed breakdown of the approach:
  1. Connect the tail of the list to the head to form a circular list.
  2. Calculate the new tail position based on the rotation.
  3. Break the circular list at the new tail position to get the rotated list.
- Proof of optimality: This approach still requires traversing the list once to find its length and connect the tail to the head, but it avoids the need to cut and append the list, making it more efficient in terms of operations.

```cpp
// Optimal Approach
ListNode* rotateRight(ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;

    // Find the length of the list and connect the tail to the head
    int length = 1;
    ListNode* tail = head;
    while (tail->next) {
        tail = tail->next;
        length++;
    }
    tail->next = head; // Form a circular list

    // Calculate the new tail position
    k = k % length;
    if (k == 0) return head; // If k is a multiple of length, no rotation needed

    // Find the new tail position
    ListNode* newTail = head;
    for (int i = 0; i < length - k - 1; i++) {
        newTail = newTail->next;
    }

    // Find the new head position
    ListNode* newHead = newTail->next;

    // Break the circular list at the new tail position
    newTail->next = nullptr;

    return newHead;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the list. We traverse the list to find its length and connect the tail to the head, and then again to find the new tail and head positions.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store pointers and variables.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to rotate the list. By forming a circular list and then breaking it at the new tail position, we avoid the need to cut and append the list, reducing the number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, circular list formation, and rotation.
- Problem-solving patterns identified: Breaking down complex problems into simpler steps and finding efficient solutions.
- Optimization techniques learned: Minimizing the number of operations required to solve a problem.
- Similar problems to practice: Other linked list problems, such as reversing a linked list or finding the middle of a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty list or a list with a single node.
- Edge cases to watch for: Cases where `k` is greater than the length of the list, or where the list has a single node.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with different input cases, including edge cases and large inputs.