## Using a Robot to Print the Lexicographically Smallest String

**Problem Link:** https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description

**Problem Statement:**
- Input format: `s` - the string to be printed.
- Constraints: `1 <= s.length <= 100`.
- Expected output format: The lexicographically smallest string that can be printed using the robot.
- Key requirements: Use a robot to print the lexicographically smallest string. The robot can only move right or left.
- Edge cases: Handle strings with repeated characters, strings with only one character, and strings with all unique characters.
- Example test cases:
  - Input: `s = "aaa"`
    Output: `"aaa"`
  - Input: `s = "abc"`
    Output: `"abc"`
  - Input: `s = "cba"`
    Output: `"abc"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible permutations of the string and find the lexicographically smallest one.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input string.
  2. Sort the permutations in lexicographical order.
  3. Return the first permutation, which is the lexicographically smallest.
- Why this approach comes to mind first: It is a straightforward approach that guarantees finding the lexicographically smallest string.

```cpp
#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    string robotWithString(string s) {
        int n = s.length();
        string res = "";
        vector<char> stack;
        
        for (int i = 0; i < n; i++) {
            stack.push_back(s[i]);
            while (!stack.empty() && (stack.back() <= s[i] || i == n - 1)) {
                res += stack.back();
                stack.pop_back();
            }
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of permutations.
> - **Space Complexity:** $O(n!)$ for storing all permutations.
> - **Why these complexities occur:** The brute force approach requires generating all permutations, which has a factorial time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a stack to keep track of characters that are smaller than or equal to the current character. When a smaller character is found, pop the stack and append the characters to the result.
- Detailed breakdown of the approach:
  1. Initialize an empty stack and result string.
  2. Iterate through the input string. For each character:
    - Push the character onto the stack.
    - While the stack is not empty and the top of the stack is smaller than or equal to the current character, pop the stack and append the character to the result.
  3. Return the result string.
- Proof of optimality: This approach has a linear time complexity because it only requires a single pass through the input string.

```cpp
class Solution {
public:
    string robotWithString(string s) {
        int n = s.length();
        string res = "";
        vector<char> stack;
        
        for (int i = 0; i < n; i++) {
            stack.push_back(s[i]);
            while (!stack.empty() && (i == n - 1 || stack.back() <= s[i + 1])) {
                res += stack.back();
                stack.pop_back();
            }
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(n)$ for the stack.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string and uses a stack to efficiently keep track of characters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to keep track of characters, iterating through the input string, and popping the stack when a smaller character is found.
- Problem-solving patterns identified: Using a stack to solve problems involving characters or strings.
- Optimization techniques learned: Reducing the time complexity from $O(n \log n)$ to $O(n)$ by using a stack.

**Mistakes to Avoid:**
- Not using a stack to keep track of characters.
- Not popping the stack when a smaller character is found.
- Not handling edge cases, such as strings with repeated characters or strings with only one character.