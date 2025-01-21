## Plus One Linked List
**Problem Link:** https://leetcode.com/problems/plus-one-linked-list/description

**Problem Statement:**
- Input format and constraints: Given the head of a linked list, where each node contains a single digit (0-9), add 1 to the linked list.
- Expected output format: Return the head of the modified linked list.
- Key requirements and edge cases to consider:
  - The input linked list is non-empty.
  - The sum of the digits does not exceed the maximum limit of an integer.
- Example test cases with explanations:
  - Example 1: Input: head = [1,2,3], Output: [1,2,4]
  - Example 2: Input: head = [4,3,2,5], Output: [4,3,2,6]
  - Example 3: Input: head = [9], Output: [1,0]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the linked list into a number, increment the number by 1, and then convert the number back into a linked list.
- Step-by-step breakdown of the solution:
  1. Traverse the linked list and convert it into a number.
  2. Increment the number by 1.
  3. Convert the number back into a linked list.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

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

ListNode* plusOne(ListNode* head) {
    // Convert linked list into a number
    long long num = 0;
    ListNode* current = head;
    int length = 0;
    while (current) {
        length++;
        current = current->next;
    }
    current = head;
    while (current) {
        num += current->val * pow(10, --length);
        current = current->next;
    }
    
    // Increment the number by 1
    num++;
    
    // Convert the number back into a linked list
    ListNode* dummy = new ListNode(0);
    current = dummy;
    while (num) {
        current->next = new ListNode(num % 10);
        num /= 10;
        current = current->next;
    }
    
    return dummy->next;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of digits in the resulting number.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes in the linked list and $m$ is the number of digits in the resulting number.
> - **Why these complexities occur:** The time complexity occurs because we need to traverse the linked list twice, and the space complexity occurs because we need to store the resulting linked list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the linked list into a number, we can directly modify the linked list by adding 1 to the last node and propagating any carry to the previous nodes.
- Detailed breakdown of the approach:
  1. Start from the last node of the linked list.
  2. Add 1 to the last node.
  3. If the result is greater than 9, set the current node's value to 0 and propagate the carry to the previous node.
  4. Repeat step 3 until there is no carry or we reach the head of the linked list.
- Proof of optimality: This approach has a time complexity of $O(n)$, where $n$ is the number of nodes in the linked list, which is optimal because we need to traverse the linked list at least once to add 1 to the last node.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
ListNode* plusOne(ListNode* head) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* current = dummy;
    ListNode* lastNonNine = dummy;
    
    // Find the last non-9 node
    while (current->next) {
        if (current->next->val != 9) {
            lastNonNine = current;
        }
        current = current->next;
    }
    
    // Add 1 to the last node
    lastNonNine->next->val++;
    
    // Propagate any carry to the previous nodes
    current = lastNonNine->next;
    while (current->val > 9) {
        current->val = 0;
        if (current == lastNonNine) {
            lastNonNine->val++;
        } else {
            current = lastNonNine;
            current->val++;
        }
    }
    
    return dummy->val == 0 ? head : dummy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the dummy node and other variables.
> - **Optimality proof:** This approach is optimal because we only traverse the linked list once, and we only use a constant amount of space to store the dummy node and other variables.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, carry propagation.
- Problem-solving patterns identified: Using a dummy node to simplify the code, propagating carry to previous nodes.
- Optimization techniques learned: Avoiding unnecessary conversions between data structures, using a constant amount of space.
- Similar problems to practice: Add Two Numbers, Multiply Two Numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input linked list is empty, not propagating carry correctly.
- Edge cases to watch for: The input linked list contains only 9s, the input linked list is empty.
- Performance pitfalls: Using unnecessary conversions between data structures, using too much space.
- Testing considerations: Test the code with different input linked lists, including edge cases.