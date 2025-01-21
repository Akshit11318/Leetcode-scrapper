## Number of Ways Where Square of Number is Equal to Product of Two Numbers

**Problem Link:** https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/description

**Problem Statement:**
- Input: Two integers `a` and `b`, representing the range of numbers from `1` to `b` (inclusive).
- Constraints: `1 <= a <= b <= 10^5`.
- Expected output: The number of pairs `(x, y)` where `1 <= x <= a`, `1 <= y <= b`, and `x * x == x * y`.
- Key requirements: Count the pairs where the square of a number `x` is equal to the product of `x` and `y`.
- Edge cases: Consider when `a` equals `b`, and when `a` is much smaller than `b`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible pairs `(x, y)` and check if `x * x == x * y`.
- Step-by-step breakdown: For each `x` from `1` to `a`, iterate through all `y` from `1` to `b`, and check the condition.
- Why this approach comes to mind first: It's straightforward and doesn't require any mathematical insights beyond the problem statement.

```cpp
int numTriplets(int a, int b) {
    int count = 0;
    for (int x = 1; x <= a; x++) {
        for (int y = 1; y <= b; y++) {
            if (x * x == x * y) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(a \cdot b)$ because for each `x`, we iterate through all `y`.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The nested loops cause the time complexity, while the constant space usage is due to only needing a single variable to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Realize that `x * x == x * y` simplifies to `x == y` when `x` is not zero, because we can divide both sides by `x`. Since `x` ranges from `1` to `a`, `x` is never zero.
- Detailed breakdown: We only need to count how many `x` values are within the range of `1` to `b` because for each such `x`, there's exactly one `y` (`y = x`) that satisfies the condition.
- Proof of optimality: This approach is optimal because it reduces the problem to a simple range check, eliminating the need for nested loops.

```cpp
int numTriplets(int a, int b) {
    return min(a, b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we perform a constant number of operations.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This is the best possible complexity because we've reduced the problem to a simple comparison, which cannot be further optimized.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Simplifying the problem statement through mathematical insights.
- Problem-solving pattern: Looking for ways to reduce the dimensionality of the problem (in this case, from pairs `(x, y)` to individual `x` values).
- Optimization technique: Eliminating unnecessary iterations by understanding the problem's constraints and applying mathematical logic.

**Mistakes to Avoid:**
- Common implementation error: Not considering the simplification of the equation, leading to an overly complex solution.
- Edge case to watch for: When `a` equals `b`, the function should return `a` (or `b`), which the optimal solution correctly handles.
- Performance pitfall: Using the brute force approach for large inputs, which would result in inefficient computation.