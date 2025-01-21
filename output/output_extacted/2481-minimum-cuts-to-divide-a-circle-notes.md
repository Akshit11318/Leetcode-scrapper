## Minimum Cuts to Divide a Circle
**Problem Link:** https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/description

**Problem Statement:**
- Input: An integer `n` representing the number of straight cuts made on a circle.
- Expected Output: The minimum number of cuts required to divide the circle into `n` equal parts.
- Key Requirements: 
  - Each cut must be a straight line.
  - Each cut must divide the circle into two parts.
- Edge Cases: 
  - `n` is a positive integer.
  - The circle is initially undivided.

**Example Test Cases:**
- For `n = 4`, the minimum number of cuts required is 2, because two cuts can divide the circle into four equal parts.
- For `n = 6`, the minimum number of cuts required is 3, because three cuts can divide the circle into six equal parts.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of cuts and find the minimum number of cuts required to divide the circle into `n` equal parts.
- However, this approach is impractical because the number of possible combinations is too large.

```cpp
int numberOfCuts(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return n / 2;
    return (n + 1) / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the solution only involves a constant number of operations.
> - **Space Complexity:** $O(1)$, because the solution only uses a constant amount of space.
> - **Why these complexities occur:** The solution involves a simple calculation based on the input `n`, which does not depend on the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that the minimum number of cuts required to divide the circle into `n` equal parts is equal to the minimum number of lines required to divide the circle into `n` equal parts.
- This can be achieved by using a simple formula: if `n` is even, the minimum number of cuts is `n / 2`; if `n` is odd, the minimum number of cuts is `(n + 1) / 2`.

```cpp
int numberOfCuts(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return n / 2;
    return (n + 1) / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the solution only involves a constant number of operations.
> - **Space Complexity:** $O(1)$, because the solution only uses a constant amount of space.
> - **Optimality proof:** The solution is optimal because it uses the minimum number of cuts required to divide the circle into `n` equal parts.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of **divisibility** and **parity** in solving problems.
- The solution involves a simple **formula-based approach** that can be used to solve similar problems.
- The problem requires **critical thinking** and **analytical skills** to arrive at the optimal solution.

**Mistakes to Avoid:**
- **Overcomplicating the problem**: The solution is simple and involves a straightforward calculation.
- **Not considering edge cases**: The solution must handle edge cases such as `n <= 1` and `n == 2`.
- **Not optimizing the solution**: The solution must be optimized to use the minimum number of cuts required to divide the circle into `n` equal parts.