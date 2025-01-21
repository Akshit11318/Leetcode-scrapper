## Digit Count in Range
**Problem Link:** https://leetcode.com/problems/digit-count-in-range/description

**Problem Statement:**
- Input format: Two integers `lower` and `upper` representing the range.
- Constraints: `1 <= lower <= upper <= 10^9`.
- Expected output format: The number of digits in the range `[lower, upper]`.
- Key requirements and edge cases to consider: Handling cases where `lower` equals `upper`, and ensuring accurate counting when `lower` or `upper` has varying numbers of digits.
- Example test cases with explanations:
  - For `lower = 1` and `upper = 13`, the output should be `19` because the numbers from 1 to 13 have 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 = 91 digits in total.
  - For `lower = 10` and `upper = 20`, the output should be `20` because each of the numbers from 10 to 20 has 2 digits.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each number in the range and count the digits of each number.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable to store the total number of digits.
  2. Iterate through each number in the range `[lower, upper]`.
  3. For each number, convert it to a string to easily count its digits.
  4. Add the count of digits of the current number to the total counter.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
int countDigitsInRange(int lower, int upper) {
    int totalDigits = 0;
    for (int i = lower; i <= upper; i++) {
        string numStr = to_string(i);
        totalDigits += numStr.length();
    }
    return totalDigits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the range of numbers (`upper - lower + 1`) and $m$ is the average number of digits in a number in the range. In the worst case, $m$ can be up to $9$ for numbers up to $10^9$.
> - **Space Complexity:** $O(m)$ for storing the string representation of each number.
> - **Why these complexities occur:** The brute force approach involves iterating through each number in the range and converting it to a string, which leads to the time complexity. The space complexity is due to the temporary storage of string representations of numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of counting digits for each number individually, calculate the total number of digits for each digit length separately (e.g., all 1-digit numbers, all 2-digit numbers, etc.).
- Detailed breakdown of the approach:
  1. Calculate the number of digits for numbers with 1 digit.
  2. For numbers with 2 to 9 digits, calculate the number of such numbers and multiply by the digit length.
  3. Handle the range `[lower, upper]` specifically by calculating the digits for the partial ranges at the start and end.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the need to iterate through each number and instead uses mathematical calculations to derive the total number of digits.

```cpp
int countDigitsInRange(int lower, int upper) {
    int totalDigits = 0;
    for (int digitLength = 1; digitLength <= 9; digitLength++) {
        int start = pow(10, digitLength - 1);
        int end = pow(10, digitLength) - 1;
        
        // Adjust for partial ranges
        if (start > upper) break;
        if (end < lower) continue;
        
        int count = min(end, upper) - max(start, lower) + 1;
        totalDigits += count * digitLength;
    }
    return totalDigits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are only iterating up to a constant number of times (9 times for digit lengths 1 through 9), regardless of the input size.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it avoids the need to iterate through each number in the range, instead using mathematical formulas to calculate the total number of digits directly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Mathematical calculation of digit counts, handling of partial ranges.
- Problem-solving patterns identified: Avoiding brute force iteration by using mathematical insights.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary iterations.
- Similar problems to practice: Other problems involving counting or calculating properties of numbers within a range.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., `lower` equals `upper`, or when `lower` or `upper` is at the boundary of a digit length change).
- Edge cases to watch for: Partial ranges at the start or end of the digit length ranges.
- Performance pitfalls: Using brute force iteration instead of mathematical calculations.
- Testing considerations: Thoroughly testing with different ranges, especially around the boundaries of digit lengths.