## Power of Two
**Problem Link:** https://leetcode.com/problems/power-of-two/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `n` is a 32-bit signed integer.
- Expected output: A boolean indicating whether `n` is a power of two.
- Key requirements and edge cases: Consider `n` can be negative, zero, or positive. A power of two is defined as `2^x`, where `x` is a non-negative integer.
- Example test cases:
  - Input: `n = 1` Output: `true` Explanation: `2^0 = 1`.
  - Input: `n = 16` Output: `true` Explanation: `2^4 = 16`.
  - Input: `n = 218` Output: `false`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Check all possible powers of two up to `n`.
- Step-by-step breakdown:
  1. Start with `x = 0`.
  2. Calculate `2^x`.
  3. If `2^x` equals `n`, return `true`.
  4. If `2^x` exceeds `n`, return `false`.
- Why this approach comes to mind first: It directly checks the definition of a power of two.

```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false; // Edge case: Negative numbers and zero are not powers of two.
        int x = 0;
        while (true) {
            int power = 1 << x; // Calculate 2^x using bit shift.
            if (power == n) return true;
            if (power > n) return false;
            x++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ because in the worst case, we need to check up to $\log_2 n$ powers of two.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is logarithmic because the number of iterations is proportional to the number of bits required to represent `n`, which is $\log_2 n$. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: A power of two in binary representation has exactly one `1` bit (the bit in the place that corresponds to that power of two).
- Detailed breakdown: Use bit manipulation to count the number of `1` bits in the binary representation of `n`.
- Proof of optimality: This approach directly checks the binary representation, which is the most efficient way to determine if a number is a power of two.
- Why further optimization is impossible: This approach has a constant time complexity, which is the best possible.

```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) return false; // Edge case: Negative numbers and zero are not powers of two.
        return (n & (n - 1)) == 0; // Bit manipulation to check if n is a power of two.
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the operation is constant time.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** The time complexity is constant because we perform a fixed number of operations regardless of the input size. The space complexity is constant for the same reason.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation and the properties of powers of two.
- Problem-solving patterns identified: Checking for edge cases and using the properties of binary numbers.
- Optimization techniques learned: Using bit manipulation for efficiency.
- Similar problems to practice: Checking if a number is a power of three, or finding the next power of two.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for edge cases like negative numbers and zero.
- Edge cases to watch for: Negative numbers, zero, and the case where `n` is not an integer.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Test with negative numbers, zero, and positive numbers that are and are not powers of two.