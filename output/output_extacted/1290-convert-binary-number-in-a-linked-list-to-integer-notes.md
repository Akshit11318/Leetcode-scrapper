## Convert Binary Number in a Linked List to Integer
**Problem Link:** https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description

**Problem Statement:**
- Input: A linked list where each node represents a binary digit (0 or 1).
- Output: The decimal equivalent of the binary number represented by the linked list.
- Key Requirements: Traverse the linked list, construct the binary number, and convert it to decimal.
- Edge Cases: Empty linked list, linked list with a single node, linked list with multiple nodes.

**Example Test Cases:**
- Input: `1 -> 0 -> 1` (head node is 1, next node is 0, next node is 1)
  - Output: `5` (because `101` in binary is `5` in decimal)
- Input: `0 -> 0` (head node is 0, next node is 0)
  - Output: `0`
- Input: `1 -> 1 -> 1 -> 1 -> 1` (five nodes all with value 1)
  - Output: `31` (because `11111` in binary is `31` in decimal)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the linked list, store the binary digits, and then convert the binary number to decimal.
- Step-by-step breakdown:
  1. Traverse the linked list and store each node's value in a string or array.
  2. Convert the binary string to a decimal number using the standard method of binary to decimal conversion (e.g., using `stoi` function with base 2 in C++).
- This approach comes to mind first because it directly addresses the problem statement by first collecting all the binary digits and then converting them to decimal.

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        string binaryStr = "";
        while (head) {
            binaryStr += to_string(head->val);
            head = head->next;
        }
        return stoi(binaryStr, 0, 2); // Convert binary string to decimal
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. This is because we traverse the linked list once to construct the binary string.
> - **Space Complexity:** $O(n)$, as we store the binary digits in a string. The length of the string is equal to the number of nodes in the linked list.
> - **Why these complexities occur:** The time complexity is linear because we visit each node exactly once. The space complexity is also linear because we store each node's value in the string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to calculate the decimal value directly while traversing the linked list, without storing all the binary digits.
- Detailed breakdown:
  1. Initialize a variable `decimalValue` to 0.
  2. Traverse the linked list. For each node, left shift the current `decimalValue` by 1 bit (which is equivalent to multiplying by 2) and then add the value of the current node.
- This approach is optimal because it eliminates the need to store the binary string and directly calculates the decimal equivalent.

```cpp
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int decimalValue = 0;
        while (head) {
            decimalValue = (decimalValue << 1) | head->val; // Left shift and add the current node's value
            head = head->next;
        }
        return decimalValue;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list. We still traverse the linked list once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `decimalValue` variable.
> - **Optimality proof:** This is the best possible complexity because we must at least traverse the linked list once to read all the binary digits. The space complexity is optimal because we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Direct calculation can often reduce space complexity.
- Bit manipulation operations (like left shift) can be used to efficiently calculate decimal values from binary representations.
- Optimal solutions often involve processing data in a single pass.

**Mistakes to Avoid:**
- Not considering the possibility of using bit manipulation to directly calculate the decimal value.
- Not optimizing space complexity by storing unnecessary data.
- Not handling edge cases such as an empty linked list.

**Similar Problems to Practice:**
- Other problems involving linked lists and bit manipulation, such as reversing a linked list or checking if a linked list has a cycle.