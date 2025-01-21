## Double a Number Represented as a Linked List

**Problem Link:** https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description

**Problem Statement:**
- Input format and constraints: The input is a non-empty linked list representing a non-negative integer. Each node in the linked list represents a digit in the number, and the digits are stored in reverse order (i.e., the least significant digit is at the head of the list). The number of nodes in the list is at most 100.
- Expected output format: The output should be the head of the modified linked list representing the doubled number.
- Key requirements and edge cases to consider: The input linked list may contain a large number of nodes, and the output linked list should also represent the doubled number in the same format.
- Example test cases with explanations: 
    - Example 1: Input: 1 -> 2 -> 3 (which represents the number 321), Output: 6 -> 4 -> 3 (which represents the number 643, which is twice 321).
    - Example 2: Input: 1 -> 2 -> 9 (which represents the number 921), Output: 8 -> 4 -> 9 (which represents the number 849, but the correct output should be 8 -> 4 -> 1 -> 8 since 921 * 2 = 1842).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves converting the linked list to an integer, doubling the integer, and then converting the result back to a linked list.
- Step-by-step breakdown of the solution:
    1. Traverse the linked list and convert it to an integer.
    2. Double the integer.
    3. Convert the doubled integer back to a linked list.
- Why this approach comes to mind first: This approach is straightforward and involves basic operations such as converting between data types and performing arithmetic operations.

```cpp
// Brute force approach
class Solution {
public:
    ListNode* doubleNumber(ListNode* head) {
        // Convert linked list to integer
        int num = 0;
        while (head) {
            num = num * 10 + head->val;
            head = head->next;
        }

        // Double the integer
        num *= 2;

        // Convert doubled integer back to linked list
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        if (num == 0) {
            curr->next = new ListNode(0);
        } else {
            while (num > 0) {
                curr->next = new ListNode(num % 10);
                num /= 10;
                curr = curr->next;
            }
        }

        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the input linked list and $m$ is the number of digits in the doubled number.
> - **Space Complexity:** $O(m)$, where $m$ is the number of digits in the doubled number.
> - **Why these complexities occur:** The time complexity is due to the traversal of the input linked list and the construction of the output linked list. The space complexity is due to the storage of the output linked list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the linked list to an integer and back, we can directly manipulate the digits in the linked list to double the number.
- Detailed breakdown of the approach:
    1. Traverse the linked list and keep track of the carry from the previous digit.
    2. For each digit, double the digit and add the carry from the previous digit.
    3. Update the carry for the next digit.
    4. Create new nodes for the output linked list as necessary.
- Proof of optimality: This approach has the same time complexity as the brute force approach but avoids the overhead of converting between data types and uses less memory since we only need to store the output linked list.

```cpp
// Optimal approach
class Solution {
public:
    ListNode* doubleNumber(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0;

        while (head) {
            int val = head->val * 2 + carry;
            carry = val / 10;
            val %= 10;

            curr->next = new ListNode(val);
            curr = curr->next;
            head = head->next;
        }

        if (carry > 0) {
            curr->next = new ListNode(carry);
        }

        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the input linked list.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the input linked list.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input linked list and uses a constant amount of extra memory to store the carry.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked lists, arithmetic operations, and carry propagation.
- Problem-solving patterns identified: Avoiding unnecessary conversions between data types and using iterative approaches instead of recursive ones.
- Optimization techniques learned: Reducing memory usage by avoiding unnecessary conversions and using iterative approaches.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the carry from the previous digit, not updating the carry correctly, and not creating new nodes for the output linked list as necessary.
- Edge cases to watch for: Handling the case where the input linked list is empty, handling the case where the doubled number has more digits than the input linked list, and handling the case where the carry is non-zero at the end of the iteration.
- Performance pitfalls: Using recursive approaches instead of iterative ones, using unnecessary conversions between data types, and not optimizing memory usage.
- Testing considerations: Testing the function with different input linked lists, including empty lists, lists with a single node, and lists with multiple nodes, and verifying that the output linked list represents the correct doubled number.