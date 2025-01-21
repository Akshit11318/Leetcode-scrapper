## Check Balanced String
**Problem Link:** https://leetcode.com/problems/check-balanced-string/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only `L` and `R` characters. The length of the string is between 1 and 100.
- Expected output format: A boolean indicating whether the string is balanced.
- Key requirements and edge cases to consider: A string is balanced if it has an equal number of `L` and `R` characters and every prefix of the string has at least as many `L`s as `R`s.
- Example test cases with explanations:
  - Input: `s = "RL"` Output: `true` Explanation: The string has an equal number of `L` and `R` characters and every prefix has at least as many `L`s as `R`s.
  - Input: `s = "LLR"` Output: `false` Explanation: The string does not have an equal number of `L` and `R` characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to check every prefix of the string to ensure that it has at least as many `L`s as `R`s. Then, we need to verify that the entire string has an equal number of `L` and `R` characters.
- Step-by-step breakdown of the solution:
  1. Iterate over the string to count the total number of `L` and `R` characters.
  2. Iterate over each prefix of the string and count the number of `L` and `R` characters in the prefix.
  3. Check if the prefix has at least as many `L`s as `R`s.
- Why this approach comes to mind first: It is a straightforward approach that checks every condition mentioned in the problem statement.

```cpp
class Solution {
public:
    bool balancedStringSplit(string s) {
        int count = 0;
        int total = 0;
        for (char c : s) {
            if (c == 'L') {
                count++;
            } else {
                count--;
            }
            if (count == 0) {
                total++;
            }
        }
        return total > 0 && total == count == 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are iterating over the string once.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the count of `L` and `R` characters.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the string once, and the space complexity is constant because we are using a fixed amount of space to store the counts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can simplify the problem by maintaining a count of `L` and `R` characters as we iterate over the string. When the count becomes zero, it means we have found a balanced substring.
- Detailed breakdown of the approach:
  1. Initialize a count variable to zero.
  2. Iterate over the string. If the character is `L`, increment the count. If the character is `R`, decrement the count.
  3. If the count becomes zero, it means we have found a balanced substring, so increment the total count.
- Proof of optimality: This approach is optimal because it only requires a single pass over the string, resulting in a linear time complexity.

```cpp
class Solution {
public:
    bool balancedStringSplit(string s) {
        int count = 0;
        int total = 0;
        for (char c : s) {
            if (c == 'L') {
                count++;
            } else {
                count--;
            }
            if (count == 0) {
                total++;
            }
        }
        return total > 0 && count == 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are iterating over the string once.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the count of `L` and `R` characters.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the string, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of maintaining a count of characters as we iterate over a string.
- Problem-solving patterns identified: The problem requires identifying a pattern in the string, specifically the balance between `L` and `R` characters.
- Optimization techniques learned: The problem demonstrates the importance of simplifying the problem statement and identifying key insights that lead to an optimal solution.
- Similar problems to practice: Other problems that involve maintaining counts or identifying patterns in strings.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize variables or not checking for edge cases.
- Edge cases to watch for: The problem requires checking for edge cases such as an empty string or a string with only one character.
- Performance pitfalls: Using inefficient algorithms or data structures that result in high time or space complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly.