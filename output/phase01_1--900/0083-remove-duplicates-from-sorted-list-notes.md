## Remove Duplicates from Sorted List

**Problem Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/description

**Problem Statement:**
- Input format: A sorted linked list where each node has a unique value and a pointer to the next node.
- Constraints: The linked list may contain duplicates.
- Expected output format: The modified linked list with all duplicates removed.
- Key requirements and edge cases to consider: 
  - Handle empty linked lists.
  - Handle linked lists with all unique elements.
  - Handle linked lists with all duplicate elements.
- Example test cases with explanations:
  - For a linked list `1 -> 1 -> 2 -> 3 -> 3 -> 4`, the output should be `1 -> 2 -> 3 -> 4`.
  - For an empty linked list, the output should be an empty linked list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a new linked list and only add nodes from the original list if they are not already in the new list.
- Step-by-step breakdown of the solution:
  1. Initialize an empty linked list.
  2. Iterate over the original linked list.
  3. For each node, check if its value is already in the new linked list.
  4. If not, add the node to the new linked list.
- Why this approach comes to mind first: It's a straightforward approach that checks for duplicates by scanning the new list for each node in the original list.

```cpp
// Brute force implementation
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* deleteDuplicates(ListNode* head) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* current = dummy;
    while (current->next) {
        ListNode* runner = current;
        while (runner->next && runner->next->val == current->next->val) {
            runner = runner->next;
        }
        if (runner == current) {
            current = current->next;
        } else {
            current->next = runner->next;
        }
    }
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the linked list. This is because in the worst case, for each node, we potentially scan the rest of the list.
> - **Space Complexity:** $O(1)$, not counting the space needed for the output, as we only use a constant amount of space to store the `current` and `runner` pointers.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loop structure, where the inner loop scans the list for each node in the outer loop. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the list is already sorted, we can simply compare adjacent nodes to find duplicates.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `current` and `next`, to the head of the list.
  2. Iterate over the list, moving `current` and `next` one step at a time.
  3. If the values at `current` and `next` are the same, skip `next` by setting `current->next` to `next->next`.
  4. Otherwise, move `current` to `next`.
- Proof of optimality: This solution has a linear time complexity because it only requires a single pass through the list, and it uses constant space because it only uses a fixed amount of space to store the pointers.

```cpp
// Optimal implementation
ListNode* deleteDuplicates(ListNode* head) {
    if (!head || !head->next) return head;
    ListNode* current = head;
    while (current->next) {
        if (current->val == current->next->val) {
            current->next = current->next->next;
        } else {
            current = current->next;
        }
    }
    return head;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we make a single pass through the list.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `current` pointer.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem, which is linear. It also uses the minimum amount of space required, which is constant.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
  - **_Two-pointer technique_**: Using two pointers to traverse a data structure, in this case, a linked list.
  - **_In-place modification_**: Modifying the input data structure directly without creating additional data structures.
- Problem-solving patterns identified:
  - **_Simplifying the problem_**: Breaking down the problem into simpler sub-problems, such as removing duplicates from a sorted list.
- Optimization techniques learned:
  - **_Reducing time complexity_**: Improving the time complexity of an algorithm by reducing the number of operations or using more efficient data structures.
- Similar problems to practice:
  - **_Removing duplicates from an unsorted list_**: A variation of the problem where the input list is not sorted.

**Mistakes to Avoid:**
- Common implementation errors:
  - **_Not handling edge cases_**: Failing to consider special cases, such as an empty input list or a list with all duplicate elements.
  - **_Using excessive memory_**: Creating unnecessary data structures or using more memory than required, which can lead to performance issues.
- Performance pitfalls:
  - **_Using inefficient algorithms_**: Choosing an algorithm with a high time or space complexity, which can lead to slow performance or memory issues.
- Testing considerations:
  - **_Testing edge cases_**: Ensuring that the solution works correctly for special cases, such as empty input or input with all duplicate elements.
  - **_Testing performance_**: Verifying that the solution performs well for large input sizes or complex scenarios.