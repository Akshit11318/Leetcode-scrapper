## Add Strings
**Problem Link:** https://leetcode.com/problems/add-strings/description

**Problem Statement:**
- Input format and constraints: The problem requires adding two numbers represented as strings. The input strings `num1` and `num2` consist only of digits `0-9` and do not contain any leading zeros except for the number zero itself.
- Expected output format: The result should be returned as a string.
- Key requirements and edge cases to consider: Handling carry-over when the sum of digits exceeds 9, ensuring no leading zeros in the result unless the result is zero.
- Example test cases with explanations:
  - Example 1: `num1 = "123"`, `num2 = "456"` -> Output: `"579"`
  - Example 2: `num1 = "999"`, `num2 = "1"` -> Output: `"1000"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One might initially think of converting the strings to integers, adding them, and then converting the result back to a string. However, this approach could lead to overflow issues for large numbers.
- Step-by-step breakdown of the solution:
  1. Convert strings to lists of integers for easier manipulation.
  2. Initialize result list and carry variable.
  3. Iterate through both numbers from right to left, adding corresponding digits along with any carry.
  4. Update carry for the next iteration.
  5. Append the result of each addition to the result list.
  6. Reverse the result list and join it into a string.
- Why this approach comes to mind first: It's straightforward and mimics the manual process of adding numbers.

```cpp
string addStrings(string num1, string num2) {
    // Initialize variables
    int i = num1.size() - 1, j = num2.size() - 1;
    int carry = 0;
    string result = "";

    // Iterate through both numbers
    while (i >= 0 || j >= 0 || carry) {
        // Calculate sum of current digits and carry
        int sum = carry;
        if (i >= 0) sum += num1[i--] - '0';
        if (j >= 0) sum += num2[j--] - '0';

        // Update carry and append result
        carry = sum / 10;
        result = to_string(sum % 10) + result;
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(m, n))$ where $m$ and $n$ are the lengths of the input strings. This is because we potentially iterate through each character in both strings once.
> - **Space Complexity:** $O(max(m, n))$ as well, for storing the result string.
> - **Why these complexities occur:** The iteration through the strings and the construction of the result string dictate these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The insight here is the same as in the brute force approach but optimized by avoiding unnecessary conversions and directly manipulating the strings as lists of digits.
- Detailed breakdown of the approach: The provided brute force approach is already optimal for this problem. It directly manipulates the strings, avoids unnecessary conversions, and handles carry-over efficiently.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input strings, and it uses a minimal amount of extra space to store the result.

```cpp
string addStrings(string num1, string num2) {
    int i = num1.size() - 1, j = num2.size() - 1;
    int carry = 0;
    string result = "";

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += num1[i--] - '0';
        if (j >= 0) sum += num2[j--] - '0';

        carry = sum / 10;
        result = to_string(sum % 10) + result;
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(m, n))$ where $m$ and $n$ are the lengths of the input strings.
> - **Space Complexity:** $O(max(m, n))$ for storing the result string.
> - **Optimality proof:** The approach is optimal because it achieves the minimum possible time complexity for this problem by only iterating through the input strings once and using minimal extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, carry-over handling, and string manipulation.
- Problem-solving patterns identified: Breaking down complex operations into simpler steps (e.g., adding numbers digit by digit).
- Optimization techniques learned: Avoiding unnecessary conversions and using minimal extra space.
- Similar problems to practice: Other string manipulation and arithmetic problems, such as multiplying strings or validating numeric strings.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of carry-over, not checking for edge cases (like one string being longer than the other), and not validating inputs.
- Edge cases to watch for: Leading zeros, very large numbers, and empty strings.
- Performance pitfalls: Using overly complex data structures or algorithms that scale poorly with input size.
- Testing considerations: Thoroughly testing with a variety of inputs, including edge cases and large inputs, to ensure correctness and performance.