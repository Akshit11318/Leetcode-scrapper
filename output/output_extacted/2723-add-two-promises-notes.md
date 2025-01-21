## Add Two Promises

**Problem Link:** https://leetcode.com/problems/add-two-promises/description

**Problem Statement:**
- Input format and constraints: The problem involves adding two promises (numbers) represented as linked lists. Each node in the linked list represents a digit in the number, and the digits are stored in reverse order (i.e., the least significant digit is at the head of the list). The numbers are non-negative.
- Expected output format: The result should be returned as a linked list in the same format, representing the sum of the input numbers.
- Key requirements and edge cases to consider: 
  - Handle cases where one or both input lists are empty.
  - Manage the carry from one digit to the next.
  - Ensure the output list is correctly ordered.
- Example test cases with explanations:
  - Example 1: Input: `l1 = [2,4,3]`, `l2 = [5,6,4]`. Output: `[7,0,8]`. Explanation: 342 + 465 = 807.
  - Example 2: Input: `l1 = [0]`, `l2 = [0]`. Output: `[0]`. Explanation: 0 + 0 = 0.
  - Example 3: Input: `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`. Output: `[8,9,9,9,0,0,0,1]`. Explanation: 9999999 + 9999 = 10009998.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by converting each linked list into a number, adding the numbers, and then converting the sum back into a linked list. This involves iterating through each list to calculate the number, handling the addition, and then creating a new linked list from the sum.
- Step-by-step breakdown of the solution:
  1. Traverse each linked list to calculate the corresponding numbers.
  2. Add the two numbers together.
  3. Convert the sum back into a linked list.
- Why this approach comes to mind first: It's a straightforward way to handle the addition by leveraging familiar arithmetic operations on integers.

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
        long long num1 = 0, num2 = 0;
        int factor = 1;
        
        // Calculate the number from the first linked list
        while (l1) {
            num1 += l1->val * factor;
            factor *= 10;
            l1 = l1->next;
        }
        
        factor = 1;
        // Calculate the number from the second linked list
        while (l2) {
            num2 += l2->val * factor;
            factor *= 10;
            l2 = l2->next;
        }
        
        // Add the numbers
        long long sum = num1 + num2;
        
        // Convert the sum back into a linked list
        if (sum == 0) return new ListNode(0);
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        while (sum > 0) {
            current->next = new ListNode(sum % 10);
            current = current->next;
            sum /= 10;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(m, n))$, where $m$ and $n$ are the lengths of the input linked lists, because we traverse each list once to calculate the numbers and then once more to create the output list.
> - **Space Complexity:** $O(max(m, n))$, because in the worst case, the output linked list could be as long as the sum of the lengths of the input lists (consider the case where each digit in both lists is 9).
> - **Why these complexities occur:** These complexities arise from the need to traverse the input lists to calculate the numbers and then create the output list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the entire linked lists into numbers, we can add the numbers digit by digit, starting from the least significant digit (the head of the lists). This approach avoids the potential overflow issue when dealing with very large numbers.
- Detailed breakdown of the approach:
  1. Initialize a dummy node for the result list and a carry variable.
  2. Iterate through both linked lists, adding corresponding digits along with the carry from the previous step.
  3. Update the carry for the next iteration.
  4. If one list is longer than the other, continue adding the remaining digits from the longer list.
  5. If there's a carry after processing all nodes, add it as the most significant digit.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input lists, resulting in a linear time complexity.

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        // Add corresponding digits from both lists
        while (l1 || l2 || carry) {
            int sum = carry;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            // Update carry and create a new node with the digit
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
        }
        
        return dummy->next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(m, n))$, where $m$ and $n$ are the lengths of the input linked lists. This is because we make a single pass through both lists.
> - **Space Complexity:** $O(max(m, n))$, as we create a new linked list that can be as long as the maximum length of the input lists plus one (for the carry).
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem by only requiring a single pass through the input data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linked list manipulation, iterative approach to addition.
- Problem-solving patterns identified: Breaking down complex problems into simpler, manageable parts (in this case, adding digits one by one).
- Optimization techniques learned: Avoiding unnecessary conversions and leveraging the structure of the input data to simplify the solution.
- Similar problems to practice: Other linked list problems, such as reversing a linked list or finding the middle element.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the carry, not checking for `NULL` pointers when traversing the lists.
- Edge cases to watch for: Lists of different lengths, lists with all 9s, empty lists.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Ensure to test with various input scenarios, including edge cases, to validate the solution's correctness and robustness.