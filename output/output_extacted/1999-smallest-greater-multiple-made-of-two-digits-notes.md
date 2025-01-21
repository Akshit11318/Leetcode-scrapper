## Smallest Greater Multiple Made of Two Digits

**Problem Link:** https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, where `1 <= n <= 1000`. The goal is to find the smallest integer that is greater than or equal to `n` and can be represented as the concatenation of two digits, `a` and `b`, such that `a` is not equal to `b`.
- Expected output format: The output should be the smallest integer that satisfies the given conditions.
- Key requirements and edge cases to consider: The integer `n` can range from 1 to 1000, and `a` and `b` must be different digits. If no such integer exists, the output should be `-1`.
- Example test cases with explanations:
  - Input: `n = 1`, Output: `10`
  - Input: `n = 9`, Output: `10`
  - Input: `n = 10`, Output: `12`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by checking all integers greater than or equal to `n` and verifying if they can be represented as the concatenation of two different digits.
- Step-by-step breakdown of the solution:
  1. Iterate over all integers starting from `n`.
  2. For each integer, convert it to a string to easily extract its digits.
  3. Check if the integer has at least two digits and if the digits are different.
  4. If the conditions are met, return the integer as it is the smallest greater multiple made of two digits.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it involves checking all possible integers until the conditions are met.

```cpp
class Solution {
public:
    int nextBeautifulNumber(int n) {
        while (true) {
            n++;
            string str = to_string(n);
            if (str.length() >= 2) {
                bool differentDigits = false;
                for (int i = 0; i < str.length(); i++) {
                    for (int j = i + 1; j < str.length(); j++) {
                        if (str[i] != str[j]) {
                            differentDigits = true;
                            break;
                        }
                    }
                    if (differentDigits) break;
                }
                if (differentDigits) return n;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the input number and $m$ is the number of digits in $n$. This is because in the worst case, we might need to check all integers up to $n$, and for each integer, we perform a nested loop to compare its digits.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the input and the result.
> - **Why these complexities occur:** The time complexity is high due to the brute force nature of the algorithm, where we potentially check every integer greater than or equal to $n$. The space complexity is low because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all integers greater than or equal to `n`, we can start by checking all possible two-digit numbers and then move on to three-digit numbers if necessary.
- Detailed breakdown of the approach:
  1. Iterate over all possible two-digit numbers (10 to 99).
  2. For each two-digit number, check if its digits are different.
  3. If the conditions are met and the number is greater than or equal to `n`, return the number as it is the smallest greater multiple made of two digits.
  4. If no such two-digit number is found, repeat the process for three-digit numbers.
- Proof of optimality: This approach is optimal because it checks all possible numbers in ascending order and stops as soon as it finds a number that meets the conditions.

```cpp
class Solution {
public:
    int nextBeautifulNumber(int n) {
        for (int i = max(10, n); i <= 999; i++) {
            string str = to_string(i);
            bool differentDigits = true;
            for (int j = 0; j < str.length(); j++) {
                for (int k = j + 1; k < str.length(); k++) {
                    if (str[j] == str[k]) {
                        differentDigits = false;
                        break;
                    }
                }
                if (!differentDigits) break;
            }
            if (differentDigits) return i;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2)$, where $m$ is the number of digits in the largest possible number (999). This is because in the worst case, we need to check all numbers up to 999, and for each number, we perform a nested loop to compare its digits.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the input and the result.
> - **Optimality proof:** This approach is optimal because it checks all possible numbers in ascending order and stops as soon as it finds a number that meets the conditions, resulting in the smallest possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Brute force approach, optimized approach using iteration and string manipulation.
- Problem-solving patterns identified: Checking all possible numbers in ascending order and stopping as soon as the conditions are met.
- Optimization techniques learned: Reducing the search space by starting from the smallest possible number and using string manipulation to compare digits.
- Similar problems to practice: Finding the smallest number with a certain property, such as the smallest number with all distinct digits.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as numbers with less than two digits.
- Edge cases to watch for: Numbers with repeated digits, numbers with less than two digits.
- Performance pitfalls: Using a brute force approach that checks all possible numbers without optimization.
- Testing considerations: Testing the function with different inputs, including edge cases and large numbers.