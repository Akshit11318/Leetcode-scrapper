## Count Square Sum Triples

**Problem Link:** https://leetcode.com/problems/count-square-sum-triples/description

**Problem Statement:**
- Input: An integer `n`.
- Output: The number of triplets `(a, b, c)` where `1 <= a, b, c <= n` and `a^2 + b^2 = c^2`.
- Key requirements and edge cases to consider: All `a`, `b`, and `c` must be within the range `[1, n]`.
- Example test cases with explanations:
  - For `n = 5`, the valid triplets are `(3, 4, 5)` and `(4, 3, 5)`, so the output is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to check every possible combination of `a`, `b`, and `c` within the given range to see if `a^2 + b^2 = c^2`.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible values of `a` from `1` to `n`.
  2. For each `a`, iterate over all possible values of `b` from `1` to `n`.
  3. For each pair of `a` and `b`, calculate `c` as the square root of `a^2 + b^2`.
  4. If `c` is an integer and within the range `[1, n]`, increment the count of valid triplets.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach that checks every possibility.

```cpp
int countTriples(int n) {
    int count = 0;
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            double c = sqrt(a * a + b * b);
            if (c == (int)c && c <= n) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because we have two nested loops each iterating up to `n`.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach involves checking every possible combination of `a` and `b`, leading to the quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible `a` and `b`, we can generate all possible `c` values (since `c` must be within the range `[1, n]`) and then check for each `c` if there exist `a` and `b` such that `a^2 + b^2 = c^2`.
- Detailed breakdown of the approach:
  1. Iterate over all possible values of `c` from `1` to `n`.
  2. For each `c`, iterate over all possible values of `a` from `1` to `c`.
  3. For each pair of `c` and `a`, calculate `b` as the square root of `c^2 - a^2`.
  4. If `b` is an integer and within the range `[1, n]`, increment the count of valid triplets.
- Proof of optimality: This approach is more efficient than the brute force because it reduces the number of iterations by only considering valid `c` values first, which are fewer than the combinations of `a` and `b`.

```cpp
int countTriples(int n) {
    int count = 0;
    for (int c = 1; c <= n; c++) {
        for (int a = 1; a <= c; a++) {
            double b = sqrt(c * c - a * a);
            if (b == (int)b && b <= n) {
                if (a < b) { // Count each pair only once
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because although we've rearranged the loops, we still potentially check every pair of numbers up to `n`.
> - **Space Complexity:** $O(1)$, because we still use a constant amount of space.
> - **Optimality proof:** While the time complexity remains $O(n^2)$, the approach is more efficient in practice because it reduces the number of square root calculations and avoids counting duplicate pairs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and optimization by reducing unnecessary calculations.
- Problem-solving patterns identified: The importance of considering all possible scenarios and optimizing based on the constraints given.
- Optimization techniques learned: Reducing the number of iterations and avoiding redundant calculations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, forgetting to check for integer values of calculated numbers, and counting duplicate pairs.
- Edge cases to watch for: Ensuring that all values of `a`, `b`, and `c` are within the specified range.
- Performance pitfalls: Avoiding unnecessary calculations and minimizing the number of iterations.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases.