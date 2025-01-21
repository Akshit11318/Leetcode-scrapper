## Add Two Numbers

**Problem Link:** [https://leetcode.com/problems/add-two-numbers/description](https://leetcode.com/problems/add-two-numbers/description)

**Problem Statement:**
- Input format and constraints: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
- Expected output format: The output linked list should also have digits stored in reverse order.
- Key requirements and edge cases to consider: Handle cases where one list is longer than the other, and the sum of two digits is greater than 9, requiring a carry-over to the next digit.
- Example test cases with explanations:
  - Example 1: Input: `l1 = [2,4,3]`, `l2 = [5,6,4]`, Output: `[7,0,8]`, Explanation: 342 + 465 = 807.
  - Example 2: Input: `l1 = [0]`, `l2 = [0]`, Output: `[0]`, Explanation: 0 + 0 = 0.
  - Example 3: Input: `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`, Output: `[8,9,9,9,0,0,0,1]`, Explanation: 9999999 + 9999 = 10009998.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the linked lists to integers, add them, and then convert the result back to a linked list.
- Step-by-step breakdown of the solution:
  1. Traverse each linked list to convert them into integers.
  2. Add the two integers together.
  3. Convert the sum back into a linked list.
- Why this approach comes to mind first: It directly addresses the problem by performing the addition as we would with normal numbers, but it's inefficient due to the conversion process.

```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int num1 = 0, num2 = 0;
        int factor = 1;
        
        // Convert l1 to integer
        while (l1) {
            num1 += l1->val * factor;
            factor *= 10;
            l1 = l1->next;
        }
        
        factor = 1;
        // Convert l2 to integer
        while (l2) {
            num2 += l2->val * factor;
            factor *= 10;
            l2 = l2->next;
        }
        
        int sum = num1 + num2;
        if (sum == 0) return new ListNode(0);
        
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        while (sum > 0) {
            current->next = new ListNode(sum % 10);
            sum /= 10;
            current = current->next;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\max(m, n))$, where $m$ and $n$ are the lengths of the linked lists, because we potentially traverse each list once to convert to integers and once more to construct the result list.
> - **Space Complexity:** $O(\max(m, n))$, because in the worst case, the sum could have a length equal to the longer of the two input lists plus one (for a carry-over).
> - **Why these complexities occur:** The conversion from linked list to integer and back to linked list involves iterating over the lists, hence the time complexity. The space complexity is due to storing the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the linked lists to integers, we can add the numbers digit by digit, similar to how we would add numbers manually. This approach avoids the potential overflow issue when dealing with very large numbers and is more efficient.
- Detailed breakdown of the approach:
  1. Initialize a dummy node to simplify the code.
  2. Iterate through both linked lists simultaneously, adding corresponding nodes' values along with any carry from the previous addition.
  3. Create new nodes with the sum of the current nodes and the carry, updating the carry for the next iteration.
  4. If one list is longer than the other, continue adding the remaining nodes with a carry if necessary.
- Proof of optimality: This approach has a linear time complexity with respect to the length of the input lists and only requires a constant amount of extra space for the dummy node and variables, making it optimal for this problem.

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        while (l1 || l2 || carry) {
            int sum = 0;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            sum += carry;
            
            current->next = new ListNode(sum % 10);
            carry = sum / 10;
            current = current->next;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\max(m, n))$, where $m$ and $n$ are the lengths of the linked lists, because we traverse each list once.
> - **Space Complexity:** $O(\max(m, n))$, because we create a new linked list that could be as long as the longer input list plus one for a potential carry-over.
> - **Optimality proof:** This approach directly adds the numbers without converting them to integers, avoiding potential overflows and minimizing the number of operations, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, iterative approach for adding numbers digit by digit.
- Problem-solving patterns identified: Breaking down complex problems into simpler, manageable parts (in this case, adding numbers digit by digit).
- Optimization techniques learned: Avoiding unnecessary conversions and using iterative approaches to reduce complexity.
- Similar problems to practice: Other linked list problems, such as merging two sorted lists or reversing a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the carry-over correctly, not checking for `NULL` pointers before accessing node values.
- Edge cases to watch for: Lists of different lengths, lists with all zeros, lists with very large numbers.
- Performance pitfalls: Converting linked lists to integers for addition, which could lead to overflow issues and is inefficient.
- Testing considerations: Ensure to test with various input scenarios, including edge cases, to guarantee the solution's robustness.