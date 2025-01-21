## Fibonacci Number
**Problem Link:** https://leetcode.com/problems/fibonacci-number/description

**Problem Statement:**
- Input format and constraints: The function `fib` takes an integer `n` as input, where `n` is a non-negative integer. The constraint is `0 <= n <= 30`.
- Expected output format: The function should return the `n`-th Fibonacci number.
- Key requirements and edge cases to consider: The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1. The base cases are `fib(0) = 0` and `fib(1) = 1`.
- Example test cases with explanations:
  - `fib(0)` should return `0`.
  - `fib(1)` should return `1`.
  - `fib(2)` should return `1`, because `fib(2) = fib(1) + fib(0) = 1 + 0 = 1`.
  - `fib(3)` should return `2`, because `fib(3) = fib(2) + fib(1) = 1 + 1 = 2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to recursively calculate the `n`-th Fibonacci number by summing the two preceding ones.
- Step-by-step breakdown of the solution: 
  1. Define the base cases for the recursion: `fib(0) = 0` and `fib(1) = 1`.
  2. For any `n > 1`, calculate `fib(n)` as `fib(n-1) + fib(n-2)`.
- Why this approach comes to mind first: It directly follows the definition of the Fibonacci sequence.

```cpp
int fib(int n) {
    if (n <= 1) {
        return n; // Base cases: fib(0) = 0, fib(1) = 1
    }
    return fib(n-1) + fib(n-2); // Recursive case
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, because each call to `fib(n)` results in two more calls, leading to exponential growth in the number of operations.
> - **Space Complexity:** $O(n)$, due to the recursion stack.
> - **Why these complexities occur:** The recursive approach leads to a lot of repeated work, as the same subproblems are solved multiple times. This inefficiency is the main reason for the high time complexity.

---

### Better Approach

**Explanation:**
- Key insight that leads to improvement: Instead of recalculating the same Fibonacci numbers multiple times, we can store the results of previous calculations to avoid redundant work.
- How it improves upon the brute force: By storing the results of subproblems, we can solve each subproblem only once and then reuse its result, significantly reducing the number of operations.
- Why this isn't yet the optimal solution: While this approach improves the time complexity, it still involves recursive function calls, which can be less efficient than an iterative solution.

```cpp
int fib(int n) {
    if (n <= 1) {
        return n; // Base cases
    }
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b; // The nth Fibonacci number
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we only need to iterate up to `n` to calculate the `n`-th Fibonacci number.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the last two Fibonacci numbers.
> - **Improvement over brute force:** This approach reduces the time complexity from exponential to linear, making it much more efficient for large values of `n`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the better approach, but recognizing that an iterative solution can be more efficient than recursion due to the overhead of function calls.
- Detailed breakdown of the approach: 
  1. Initialize the first two Fibonacci numbers, `a` and `b`, to `0` and `1`, respectively.
  2. Iterate from `2` to `n`, updating `a` and `b` in each iteration to hold the last two Fibonacci numbers.
  3. After the loop, `b` will hold the `n`-th Fibonacci number.
- Proof of optimality: This solution has a linear time complexity and uses constant space, which is optimal for calculating a single Fibonacci number, as we must at least read the input and write the output.

```cpp
int fib(int n) {
    if (n <= 1) {
        return n; // Base cases
    }
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b; // The nth Fibonacci number
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we only need to iterate up to `n` to calculate the `n`-th Fibonacci number.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the last two Fibonacci numbers.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for calculating a Fibonacci number, given that we must perform at least `n` operations to compute the `n`-th number in the sequence.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, memoization (implicit in the iterative solution), and dynamic programming.
- Problem-solving patterns identified: The Fibonacci sequence problem illustrates the importance of recognizing patterns and applying dynamic programming principles to avoid redundant calculations.
- Optimization techniques learned: Avoiding redundant work by storing intermediate results, and preferring iterative solutions over recursive ones for performance.
- Similar problems to practice: Other problems that involve sequences or series, such as calculating the `n`-th term in a different sequence, or problems that can be solved using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle base cases correctly, or not updating variables properly in the iterative solution.
- Edge cases to watch for: The input `n` being `0` or `1`, and ensuring the solution works correctly for these base cases.
- Performance pitfalls: Using a naive recursive approach without memoization for large inputs, leading to exponential time complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases like `0` and `1`, and larger values of `n` to ensure correctness and performance.