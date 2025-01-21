## Sqrt(x)
**Problem Link:** https://leetcode.com/problems/sqrtx/description

**Problem Statement:**
- Input: `x`, a non-negative integer.
- Output: The integer square root of `x`.
- Key requirements: The integer square root is the largest integer whose square is less than or equal to `x`.
- Example test cases:
  - Input: `x = 4`, Output: `2` because `2^2 = 4`.
  - Input: `x = 8`, Output: `2` because `2^2 = 4 < 8 < 3^2 = 9`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every integer from `0` to `x` to see if its square is less than or equal to `x`.
- Step-by-step breakdown:
  1. Start with `i = 0`.
  2. Check if `i^2 <= x`.
  3. If true, increment `i` and repeat step 2.
  4. The last `i` for which `i^2 <= x` is the integer square root of `x`.
- This approach comes to mind first because it directly addresses the problem statement without requiring any additional mathematical insights.

```cpp
int mySqrt(int x) {
    int i = 0;
    while (i * i <= x) {
        i++;
    }
    return i - 1; // Because we went one step too far
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{x})$ because in the worst case, we iterate up to the square root of `x`.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is directly related to the number of iterations in the while loop, which is proportional to the square root of `x`. The space complexity is constant because we do not allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary search approach. We know that the square root of `x` must lie between `0` and `x`. By repeatedly dividing this range in half, we can efficiently find the integer square root.
- Detailed breakdown:
  1. Initialize `low = 0` and `high = x`.
  2. While `low <= high`, calculate `mid = (low + high) / 2`.
  3. If `mid * mid <= x`, then the square root could be `mid` or higher, so update `low = mid + 1`.
  4. Otherwise, update `high = mid - 1`.
  5. The integer square root of `x` is `low - 1` because `low` is the first value where `low * low > x`.
- This is the optimal solution because binary search reduces the search space by half with each iteration, leading to a logarithmic time complexity.

```cpp
int mySqrt(int x) {
    if (x < 2) return x; // 0 or 1
    int low = 2, high = x / 2;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        long square = (long) mid * mid; // Cast to long to avoid overflow
        if (square == x) return mid;
        if (square < x) low = mid + 1;
        else high = mid - 1;
    }
    return high; // high is the largest integer whose square is less than x
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log x)$ because we use binary search to find the integer square root.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This is the best possible time complexity for this problem because any algorithm must at least read the input, which takes $\Omega(\log x)$ time. Binary search is optimal for finding an element in a sorted array, and our problem can be reduced to this by considering the array of squares of integers up to `x`.

---

### Final Notes

**Learning Points:**
- The importance of **binary search** in reducing the time complexity of problems involving searching or finding elements within a range.
- How to apply **mathematical insights** (e.g., recognizing that the integer square root of `x` must lie within a certain range) to optimize solutions.
- **Optimization techniques** such as reducing the search space and using efficient algorithms.

**Mistakes to Avoid:**
- Not considering **overflow** when dealing with large numbers (e.g., when calculating `mid * mid`).
- Not handling **edge cases** properly (e.g., `x = 0` or `x = 1`).
- Not recognizing the potential for **optimization** through the use of more efficient algorithms like binary search.