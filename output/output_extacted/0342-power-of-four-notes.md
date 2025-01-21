## Power of Four

**Problem Link:** [https://leetcode.com/problems/power-of-four/description](https://leetcode.com/problems/power-of-four/description)

**Problem Statement:**
- Input: An integer `n`.
- Output: A boolean indicating whether `n` is a power of four.
- Key requirements: Determine if `n` can be expressed as $4^x$, where `x` is an integer.
- Edge cases: `n` can be any integer, including negative numbers and zero.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all powers of four until we reach or exceed `n`.
- Step-by-step breakdown: 
  1. Initialize a variable `i` to 0.
  2. Calculate $4^i$ and compare it with `n`.
  3. If $4^i$ equals `n`, return true.
  4. If $4^i` exceeds `n`, return false.
- Why this approach comes to mind first: It's a straightforward method to check if a number is a power of four by iterating through powers of four.

```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0) return false;
        int i = 0;
        while (true) {
            double power = pow(4, i);
            if (power == n) return true;
            if (power > n) return false;
            i++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log_4{n})$, because we're essentially checking powers of four up to `n`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is logarithmic because we're exponentially increasing the value of $4^i$ with each iteration, and we stop as soon as we reach or exceed `n`. The space complexity is constant because we only use a fixed amount of space to store our variables.

### Optimal Approach (Required)

**Explanation:**
- Key insight: A number is a power of four if it is a power of two and its binary representation has an odd number of zeros after the first '1'.
- Detailed breakdown: 
  1. Check if `n` is a power of two by using the bitwise AND operator `&`. If `n` is a power of two, then `n & (n - 1)` will be zero.
  2. Check if the number of zeros after the first '1' in the binary representation of `n` is odd. This can be done by counting the number of zeros after the first '1' or by using bitwise operations to check if the position of the '1' is at an odd position (1-based indexing).
- Proof of optimality: This approach is optimal because it reduces the problem to two simple bitwise operations and does not require iterating through powers of four or using any additional data structures.

```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0) return false;
        // Check if n is a power of two
        if ((n & (n - 1)) != 0) return false;
        // Check if the number of zeros after the first '1' is odd
        return (n & 0xAAAAAAAA) == 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're performing a constant number of operations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it uses a constant number of operations and does not require any additional data structures, making it the most efficient solution possible.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Bit manipulation, powers of two, and powers of four.
- Problem-solving patterns: Using bitwise operations to solve problems related to binary representations.
- Optimization techniques: Reducing the problem to simpler sub-problems and using bitwise operations to improve efficiency.
- Similar problems to practice: Checking if a number is a power of two, checking if a number is a perfect square.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as negative numbers or zero.
- Edge cases to watch for: Negative numbers, zero, and numbers that are not powers of four.
- Performance pitfalls: Using inefficient algorithms, such as iterating through powers of four.
- Testing considerations: Testing with a variety of inputs, including edge cases and large numbers.