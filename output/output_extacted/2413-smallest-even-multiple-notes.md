## Smallest Even Multiple
**Problem Link:** https://leetcode.com/problems/smallest-even-multiple/description

**Problem Statement:**
- Input format and constraints: Given two integers `n` and `k`, find the smallest even multiple of `n` that is greater than or equal to `k`.
- Expected output format: The smallest even multiple as an integer.
- Key requirements and edge cases to consider: Handling cases where `n` or `k` is 0 or negative, and ensuring the result is indeed an even multiple of `n`.
- Example test cases with explanations:
  - For `n = 2` and `k = 10`, the smallest even multiple of `n` greater than or equal to `k` is `10`.
  - For `n = 3` and `k = 4`, the smallest even multiple of `n` greater than or equal to `k` is `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by checking each multiple of `n` to see if it is greater than or equal to `k` and if it's even.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `multiple` to `n`.
  2. Enter a loop that continues until `multiple` is greater than or equal to `k`.
  3. Inside the loop, check if `multiple` is even. If it is, return `multiple`.
  4. If `multiple` is not even, increment `multiple` by `n` and continue the loop.
- Why this approach comes to mind first: It's straightforward and easy to understand, making it a natural first attempt.

```cpp
int smallestEvenMultiple(int n, int k) {
    int multiple = n;
    while (multiple < k) {
        multiple += n;
    }
    // If multiple is not even, find the next even multiple
    if (multiple % 2 != 0) {
        multiple += n;
    }
    return multiple;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{k}{n})$ because in the worst case, we might need to iterate up to `k` with a step of `n`.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is due to the loop that increments `multiple` by `n` until it's greater than or equal to `k`, and the space complexity is constant because we don't use any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each multiple of `n` individually, we can calculate the smallest even multiple directly by first finding the smallest multiple of `n` that is greater than or equal to `k`, and then adjusting it to be even if necessary.
- Detailed breakdown of the approach:
  1. Calculate the smallest multiple of `n` that is greater than or equal to `k` using the formula `(k + n - 1) / n * n`.
  2. If this multiple is not even, the next even multiple can be found by adding `n` to it.
- Proof of optimality: This approach is optimal because it directly calculates the desired result without unnecessary iterations, reducing the time complexity to a constant.
- Why further optimization is impossible: This solution already has a constant time complexity, which is the best possible time complexity for an algorithm.

```cpp
int smallestEvenMultiple(int n, int k) {
    int multiple = (k + n - 1) / n * n; // Smallest multiple of n >= k
    return (multiple % 2 == 0) ? multiple : multiple + n;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the calculation is constant time.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This solution is optimal because it achieves the task in constant time, which is the lowest possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct calculation, optimization of iterative processes.
- Problem-solving patterns identified: Looking for mathematical formulas or properties that can simplify the solution.
- Optimization techniques learned: Reducing the number of iterations or eliminating them altogether when possible.
- Similar problems to practice: Other problems involving multiples, divisibility, or optimization of iterative processes.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., `n` or `k` being 0 or negative).
- Edge cases to watch for: Ensuring the solution works correctly for all possible inputs, including boundary cases.
- Performance pitfalls: Using iterative solutions when a direct calculation is possible.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases.