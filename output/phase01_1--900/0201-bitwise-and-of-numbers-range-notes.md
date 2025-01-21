## Bitwise AND of Numbers Range

**Problem Link:** https://leetcode.com/problems/bitwise-and-of-numbers-range/description

**Problem Statement:**
- Given two integers `left` and `right`, return the bitwise AND of all numbers in the range `[left, right]`.
- Input format and constraints: `0 <= left <= right <= 2^31 - 1`.
- Expected output format: The bitwise AND of all numbers in the range.
- Key requirements and edge cases to consider: Handling cases where `left` equals `right`, and where the range includes numbers with varying bit patterns.
- Example test cases with explanations:
  - For `left = 5` and `right = 7`, the bitwise AND of all numbers in the range `[5, 7]` is `5 & 6 & 7 = 4`.
  - For `left = 1` and `right = 2`, the bitwise AND of all numbers in the range `[1, 2]` is `1 & 2 = 0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all numbers in the range `[left, right]` and compute the bitwise AND.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `result` with the first number in the range (`left`).
  2. Iterate from `left + 1` to `right` (inclusive).
  3. For each number `i` in the range, update `result` to be the bitwise AND of `result` and `i`.
- Why this approach comes to mind first: It directly implements the problem statement, computing the bitwise AND of all numbers in the given range.

```cpp
int rangeBitwiseAnd(int left, int right) {
    int result = left;
    for (int i = left + 1; i <= right; i++) {
        result = result & i;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n = right - left$. This is because in the worst case, we iterate through all numbers in the range.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result.
> - **Why these complexities occur:** The brute force approach has a linear time complexity because it checks every number in the range, and constant space complexity because it only uses a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The bitwise AND operation has the property that `a & b` will have all the bits set to 1 that are common to both `a` and `b` in their binary representations. For a range of numbers, the common prefix of their binary representations will give us the bitwise AND of all numbers in the range.
- Detailed breakdown of the approach:
  1. Find the common prefix of the binary representations of `left` and `right`.
  2. The bitwise AND of all numbers in the range `[left, right]` will be the number represented by this common prefix.
- Proof of optimality: This approach is optimal because it directly computes the bitwise AND without needing to iterate through all numbers in the range, reducing the time complexity significantly.
- Why further optimization is impossible: This approach already achieves the best possible time complexity by avoiding unnecessary iterations.

```cpp
int rangeBitwiseAnd(int left, int right) {
    int count = 0;
    // Find the common prefix length
    while (left != right) {
        left >>= 1;
        right >>= 1;
        count++;
    }
    // Shift back to the original position
    return left << count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the maximum possible value of `right`. This is because we are essentially performing a binary search on the bits of the numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** The time complexity is optimal because we are reducing the problem size by half with each iteration (by right-shifting both numbers), which is the fastest way to find the common prefix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, common prefix finding, and optimization techniques.
- Problem-solving patterns identified: Using properties of bitwise operations to simplify problems.
- Optimization techniques learned: Reducing problem size iteratively to achieve optimal time complexity.
- Similar problems to practice: Other problems involving bitwise operations and range computations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., when `left` equals `right`).
- Edge cases to watch for: Handling cases where the range includes numbers with varying bit patterns.
- Performance pitfalls: Using brute force approaches for large ranges, which can lead to significant performance issues.
- Testing considerations: Thoroughly testing the function with various ranges, including edge cases, to ensure correctness.