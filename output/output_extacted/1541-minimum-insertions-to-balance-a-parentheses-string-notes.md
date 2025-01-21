## Minimum Insertions to Balance a Parentheses String

**Problem Link:** https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description

**Problem Statement:**
- Input: A string `s` consisting of parentheses.
- Constraints: The string only contains `(` and `)`.
- Expected Output: The minimum number of insertions required to balance the string.
- Key Requirements: Balance the string by inserting the minimum number of parentheses.
- Edge Cases: Empty string, single parenthesis, already balanced string.
- Example Test Cases:
  - `s = "(()))"`: Expected output `1` because we need to insert one `(` to balance the string.
  - `s = "())"(`: Expected output `2` because we need to insert two `)` to balance the string.
  - `s = "((("`: Expected output `3` because we need to insert three `)` to balance the string.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible insertions of parentheses and check if the string is balanced.
- Step-by-step breakdown of the solution:
  1. Generate all possible insertions of parentheses.
  2. For each insertion, check if the string is balanced.
  3. If the string is balanced, count the number of insertions.
- Why this approach comes to mind first: It's a straightforward approach to try all possible solutions.

```cpp
class Solution {
public:
    int minInsertions(string s) {
        int minInsertions = INT_MAX;
        int n = s.length();
        for (int mask = 0; mask < (1 << n); mask++) {
            string temp = s;
            int insertions = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    temp.insert(i, "(");
                    insertions++;
                }
            }
            if (isBalanced(temp)) {
                minInsertions = min(minInsertions, insertions);
            }
        }
        return minInsertions;
    }
    
    bool isBalanced(string s) {
        int balance = 0;
        for (char c : s) {
            if (c == '(') {
                balance++;
            } else {
                balance--;
            }
            if (balance < 0) {
                return false;
            }
        }
        return balance == 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ where $n$ is the length of the string. This is because we're generating all possible insertions and checking if the string is balanced for each insertion.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the string. This is because we're storing the temporary string with insertions.
> - **Why these complexities occur:** The time complexity is high because we're trying all possible insertions, and the space complexity is linear because we're storing the temporary string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to keep track of the opening parentheses that don't have a corresponding closing parenthesis yet.
- Detailed breakdown of the approach:
  1. Initialize a stack to store the opening parentheses.
  2. Iterate through the string. If we encounter an opening parenthesis, push it onto the stack.
  3. If we encounter a closing parenthesis, check if the stack is empty. If it's empty, it means we don't have a corresponding opening parenthesis, so we need to insert one. If it's not empty, pop the opening parenthesis from the stack.
  4. After iterating through the string, the number of opening parentheses left in the stack is the number of closing parentheses we need to insert.
- Proof of optimality: This approach is optimal because we're only inserting parentheses when necessary, and we're not trying all possible insertions.

```cpp
class Solution {
public:
    int minInsertions(string s) {
        int insertions = 0;
        int balance = 0;
        for (char c : s) {
            if (c == '(') {
                balance++;
            } else {
                if (balance == 0) {
                    insertions++;
                    balance++;
                }
                balance--;
            }
        }
        return insertions + balance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because we're iterating through the string once.
> - **Space Complexity:** $O(1)$ because we're only using a constant amount of space to store the balance and insertions.
> - **Optimality proof:** This approach is optimal because we're only inserting parentheses when necessary, and we're not trying all possible insertions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack, iteration, and optimization.
- Problem-solving patterns identified: Using a stack to keep track of opening parentheses, and iterating through the string to find the minimum number of insertions.
- Optimization techniques learned: Avoiding unnecessary insertions by only inserting when necessary.
- Similar problems to practice: Other string manipulation problems that require finding the minimum number of operations to achieve a certain goal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty string or a string with only one parenthesis.
- Edge cases to watch for: Empty string, single parenthesis, already balanced string.
- Performance pitfalls: Trying all possible insertions, which can lead to high time complexity.
- Testing considerations: Testing with different inputs, such as an empty string, a string with only one parenthesis, and a string that is already balanced.