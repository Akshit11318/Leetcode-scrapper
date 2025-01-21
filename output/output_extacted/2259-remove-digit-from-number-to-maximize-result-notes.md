## Remove Digit From Number To Maximize Result
**Problem Link:** https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description

**Problem Statement:**
- Input: A string `number` representing a non-negative integer.
- Output: The maximum possible integer after removing one digit from `number`.
- Constraints: `2 <= number.length <= 100`, `number` consists of digits `0-9`.
- Key Requirements: The goal is to remove one digit to maximize the resulting integer.
- Example Test Cases:
  - Input: `number = "1231"`
    - Output: `"231"`
    - Explanation: Removing the first digit (`1`) results in `231`, which is the maximum possible integer after removing one digit.
  - Input: `number = "551"`
    - Output: `"51"`
    - Explanation: Removing the first digit (`5`) or the second digit (`5`) results in `51`, which is the maximum possible integer after removing one digit.

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: For each digit in the `number`, try removing it and compare the resulting integers.
- Step-by-Step Breakdown:
  1. Iterate over each digit in `number`.
  2. Create a new string by removing the current digit.
  3. Convert the new string to an integer and compare it with the current maximum.
  4. Update the maximum if the new integer is larger.
- Why This Approach Comes to Mind First: It's straightforward to think about trying all possible removals to find the maximum.

```cpp
string removeDigit(string number) {
    string maxResult = "";
    for (int i = 0; i < number.length(); i++) {
        string newNumber = number.substr(0, i) + number.substr(i + 1);
        if (newNumber > maxResult) {
            maxResult = newNumber;
        }
    }
    return maxResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `number`. This is because we are iterating over each digit once.
> - **Space Complexity:** $O(n)$, as we are creating new strings for each possible removal.
> - **Why These Complexities Occur:** The iteration over each digit and the creation of new strings for comparison lead to these complexities.

---

### Optimal Approach

**Explanation:**
- Key Insight: We only need to compare the current digit with the next digit. If the current digit is greater than the next digit, we can remove the current digit and return the result. If we reach the end without finding such a pair, we remove the last digit.
- Detailed Breakdown:
  1. Iterate over each digit in `number`.
  2. Compare the current digit with the next digit.
  3. If the current digit is greater than the next digit, remove the current digit and return the result.
  4. If no such pair is found, remove the last digit.
- Proof of Optimality: This approach is optimal because it only requires a single pass through the string, and by comparing adjacent digits, we can ensure that we are removing the digit that results in the maximum possible integer.

```cpp
string removeDigit(string number) {
    for (int i = 0; i < number.length() - 1; i++) {
        if (number[i] > number[i + 1]) {
            return number.substr(0, i) + number.substr(i + 1);
        }
    }
    return number.substr(0, number.length() - 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `number`. This is because we are making a single pass through the string.
> - **Space Complexity:** $O(n)$, as we are creating a new string for the result.
> - **Optimality Proof:** This approach is optimal because it achieves the same result as the brute force approach but with a single pass, reducing unnecessary comparisons and string creations.

---

### Final Notes

**Learning Points:**
- Key Algorithmic Concepts: Iteration, string manipulation, and comparison.
- Problem-Solving Patterns: Identifying key insights to simplify the problem and reduce unnecessary computations.
- Optimization Techniques: Avoiding redundant operations and focusing on critical comparisons.

**Mistakes to Avoid:**
- Common Implementation Errors: Not handling edge cases (e.g., removing the last digit when necessary).
- Performance Pitfalls: Using inefficient algorithms that lead to high time or space complexity.
- Testing Considerations: Ensuring that the solution works for all possible inputs, including edge cases.