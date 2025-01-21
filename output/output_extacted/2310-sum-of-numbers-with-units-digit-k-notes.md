## Sum of Numbers with Units Digit K
**Problem Link:** https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/description

**Problem Statement:**
- Input format and constraints: Given an integer `k`, find the sum of all numbers with a units digit of `k` that are less than or equal to `n`.
- Expected output format: Return the sum as an integer.
- Key requirements and edge cases to consider: 
  - `1 <= k <= 9`
  - `0 <= n <= 10^5`
  - Handle cases where `n` is less than `k`.
- Example test cases with explanations:
  - For `k = 3` and `n = 10`, the numbers with a units digit of `3` are `3` and `13`, so the sum is `3 + 13 = 16`.
  - For `k = 5` and `n = 20`, the numbers with a units digit of `5` are `5` and `15`, so the sum is `5 + 15 = 20`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over all numbers from `1` to `n`, and for each number, check if its units digit is `k`. If it is, add it to the sum.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `sum` to `0`.
  2. Iterate over all numbers from `1` to `n`.
  3. For each number `i`, check if its units digit is `k` by using the modulo operator (`i % 10 == k`).
  4. If the units digit is `k`, add `i` to the `sum`.
- Why this approach comes to mind first: It's a straightforward approach that checks every possible number.

```cpp
int sumOfNumbersWithUnitsDigitK(int k, int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 10 == k) {
            sum += i;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we're iterating over all numbers from `1` to `n`.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the `sum` variable.
> - **Why these complexities occur:** The time complexity is linear because we're checking every number, and the space complexity is constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use the formula for the sum of an arithmetic series to calculate the sum of numbers with a units digit of `k`.
- Detailed breakdown of the approach:
  1. Calculate the number of terms in the series. The first term is `k`, and the last term is the largest number less than or equal to `n` that has a units digit of `k`.
  2. Use the formula for the sum of an arithmetic series: `sum = (n * (a1 + an)) / 2`, where `n` is the number of terms, `a1` is the first term, and `an` is the last term.
- Proof of optimality: This approach is optimal because it avoids iterating over all numbers, instead using a mathematical formula to calculate the sum directly.
- Why further optimization is impossible: This approach has a constant time complexity, which is the best possible time complexity for this problem.

```cpp
int sumOfNumbersWithUnitsDigitK(int k, int n) {
    int firstTerm = k;
    int lastTerm = (n / 10) * 10 + k;
    if (lastTerm > n) {
        lastTerm -= 10;
    }
    int numTerms = (lastTerm - firstTerm) / 10 + 1;
    int sum = (numTerms * (firstTerm + lastTerm)) / 2;
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're using a constant number of operations to calculate the sum.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it uses a mathematical formula to calculate the sum directly, avoiding the need to iterate over all numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using mathematical formulas to optimize solutions.
- Problem-solving patterns identified: Looking for patterns in the input data to avoid unnecessary iterations.
- Optimization techniques learned: Using arithmetic series formulas to calculate sums.
- Similar problems to practice: Other problems that involve calculating sums or using mathematical formulas to optimize solutions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as when `n` is less than `k`.
- Edge cases to watch for: When `n` is less than `k`, or when `k` is greater than `9`.
- Performance pitfalls: Using unnecessary iterations or data structures that scale with the input size.
- Testing considerations: Testing the solution with different values of `k` and `n` to ensure it handles all edge cases correctly.