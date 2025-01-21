## 2 Keys Keyboard
**Problem Link:** https://leetcode.com/problems/2-keys-keyboard/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the number of characters to be copied. The goal is to find the minimum number of operations (copy and paste) required to fill the clipboard with `n` characters.
- Expected output format: The function should return the minimum number of operations required.
- Key requirements and edge cases to consider:
  - `n` is a positive integer.
  - The minimum number of operations is required.
- Example test cases with explanations:
  - If `n = 3`, the minimum number of operations is 3 (copy, copy, paste).
  - If `n = 6`, the minimum number of operations is 5 (copy, copy, paste, paste, paste).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of copy and paste operations to fill the clipboard with `n` characters.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `min_operations` to store the minimum number of operations.
  2. Iterate over all possible numbers of characters to copy (from 1 to `n`).
  3. For each number of characters to copy, calculate the number of operations required to fill the clipboard.
  4. Update `min_operations` if the current number of operations is less than the minimum found so far.
- Why this approach comes to mind first: The brute force approach is often the simplest to understand and implement, as it involves trying all possible solutions.

```cpp
int minSteps(int n) {
    int min_operations = n;
    for (int i = 1; i <= n; i++) {
        int operations = i;
        int remaining = n - i;
        while (remaining > 0) {
            if (remaining % i == 0) {
                operations += remaining / i;
                remaining = 0;
            } else {
                operations++;
                remaining--;
            }
        }
        min_operations = min(min_operations, operations);
    }
    return min_operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the input number, because in the worst case, we need to iterate over all numbers from 1 to `n`, and for each number, we perform a while loop that runs up to `n` times.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the minimum number of operations and other variables.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loop structure, and the space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum number of operations required to fill the clipboard with `i` characters, where `i` ranges from 1 to `n`.
- Detailed breakdown of the approach:
  1. Initialize an array `dp` of size `n + 1`, where `dp[i]` stores the minimum number of operations required to fill the clipboard with `i` characters.
  2. Initialize `dp[1] = 0`, because we need 0 operations to fill the clipboard with 1 character (we can simply copy it).
  3. Iterate over all numbers `i` from 2 to `n`.
  4. For each `i`, calculate the minimum number of operations required to fill the clipboard with `i` characters by considering all possible numbers of characters to copy.
  5. Update `dp[i]` with the minimum number of operations found.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible solutions and store the minimum number of operations required to fill the clipboard with `i` characters, making it an optimal solution.

```cpp
int minSteps(int n) {
    vector<int> dp(n + 1);
    for (int i = 2; i <= n; i++) {
        dp[i] = i;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                dp[i] = min(dp[i], dp[j] + i / j);
            }
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \sqrt{n})$, where $n$ is the input number, because we iterate over all numbers from 2 to `n`, and for each number, we perform a loop that runs up to the square root of `n`.
> - **Space Complexity:** $O(n)$, because we use an array of size `n + 1` to store the minimum number of operations required to fill the clipboard with `i` characters.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible solutions and store the minimum number of operations required to fill the clipboard with `i` characters, making it an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration, and minimization.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and storing the solutions to sub-problems to avoid redundant computation.
- Optimization techniques learned: Using dynamic programming to store the minimum number of operations required to fill the clipboard with `i` characters.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the coin change problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly, or not considering all possible solutions.
- Edge cases to watch for: Handling the case where `n` is 1, handling the case where `n` is a prime number, or handling the case where `n` is a power of a prime number.
- Performance pitfalls: Not using dynamic programming to store the minimum number of operations required to fill the clipboard with `i` characters, resulting in a time complexity of $O(n^2)$ or worse.
- Testing considerations: Testing the function with different inputs, including small inputs, large inputs, and edge cases, to ensure that it produces the correct output.