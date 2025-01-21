# Find the Key of the Numbers
**Problem Link:** https://leetcode.com/problems/find-the-key-of-the-numbers/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, the task is to find the key of the numbers from `1` to `n`.
- Expected output format: The key is calculated based on the sum of the numbers.
- Key requirements and edge cases to consider: The input `n` can be any positive integer.
- Example test cases with explanations:
  - For `n = 1`, the key is `1` because the sum of numbers from `1` to `1` is `1`.
  - For `n = 2`, the key is `3` because the sum of numbers from `1` to `2` is `1 + 2 = 3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the sum of all numbers from `1` to `n` using a loop.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `sum` to store the sum of numbers.
  2. Iterate over the range from `1` to `n` (inclusive) using a loop.
  3. In each iteration, add the current number to the `sum`.
  4. After the loop, the `sum` variable will hold the key of the numbers.
- Why this approach comes to mind first: It is the most straightforward way to calculate the sum of a series of numbers.

```cpp
int findTheKey(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number. This is because we are iterating over the range from `1` to `n` using a loop.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input, making it constant. This is because we are only using a fixed amount of space to store the sum and the loop variable.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each number in the range from `1` to `n`. The space complexity is constant because we are not using any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The sum of the first `n` natural numbers can be calculated using the formula $\frac{n(n + 1)}{2}$.
- Detailed breakdown of the approach:
  1. Use the formula $\frac{n(n + 1)}{2}$ to calculate the sum directly without needing a loop.
- Proof of optimality: This approach is optimal because it reduces the time complexity from linear to constant, making it much more efficient for large inputs.
- Why further optimization is impossible: This formula is a mathematical constant-time solution to calculate the sum of the first `n` natural numbers, making further optimization unnecessary.

```cpp
int findTheKey(int n) {
    return n * (n + 1) / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, which means the time required does not change with the size of the input, making it constant. This is because we are using a mathematical formula that can be computed in a single step.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input, making it constant. This is because we are not using any data structures that grow with the size of the input.
> - **Optimality proof:** The formula used is a direct mathematical calculation that does not depend on the size of the input, making it the most efficient solution possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of mathematical formulas to optimize solutions.
- Problem-solving patterns identified: Recognizing when a problem can be solved using a mathematical formula rather than iteration.
- Optimization techniques learned: Using constant-time formulas to replace linear-time loops.
- Similar problems to practice: Finding the sum of squares of the first `n` natural numbers, finding the sum of cubes, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for integer overflow when using the formula for large inputs.
- Edge cases to watch for: Handling the case when `n` is 0 or negative, as the formula does not apply in these cases.
- Performance pitfalls: Failing to recognize the opportunity to use a constant-time formula and instead using a loop.
- Testing considerations: Testing the function with both small and large inputs to ensure it works correctly and efficiently in all cases.