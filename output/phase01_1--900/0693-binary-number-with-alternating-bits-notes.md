## Binary Number with Alternating Bits

**Problem Link:** https://leetcode.com/problems/binary-number-with-alternating-bits/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 2^31 - 1`.
- Expected output: `true` if the binary representation of `n` has alternating bits, `false` otherwise.
- Key requirements: The binary representation should have alternating bits, starting from either 0 or 1.
- Example test cases:
  - Input: `5` (Binary: `101`), Output: `true`
  - Input: `7` (Binary: `111`), Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the integer to a binary string and then check each character.
- Step-by-step breakdown:
  1. Convert the integer to a binary string.
  2. Iterate through the string, checking each bit.
  3. If any two consecutive bits are the same, return `false`.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem.

```cpp
class Solution {
public:
    bool hasAlternatingBits(int n) {
        // Convert the integer to a binary string
        string binaryStr;
        while (n > 0) {
            binaryStr = (n % 2 == 0 ? "0" : "1") + binaryStr;
            n /= 2;
        }

        // Iterate through the string, checking each bit
        for (int i = 1; i < binaryStr.length(); i++) {
            if (binaryStr[i] == binaryStr[i - 1]) {
                return false;
            }
        }

        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the input integer. This is because we're converting the integer to a binary string, which takes $log(n)$ time.
> - **Space Complexity:** $O(log(n))$, as we're storing the binary string.
> - **Why these complexities occur:** The conversion to binary string and the iteration through the string both depend on the number of bits in the binary representation of $n$, which is $log(n)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of converting the integer to a binary string, we can use bitwise operations to check the bits directly.
- Detailed breakdown:
  1. Initialize a variable to store the last seen bit.
  2. Iterate through the bits of the integer using bitwise operations.
  3. Check each bit against the last seen bit.
- Why this is optimal: It avoids the overhead of string conversion and uses constant space.

```cpp
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int lastBit = -1;
        while (n > 0) {
            int currentBit = n & 1;
            if (lastBit != -1 && currentBit == lastBit) {
                return false;
            }
            lastBit = currentBit;
            n >>= 1;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, as we're iterating through the bits of the integer.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space.
> - **Optimality proof:** This is the most efficient way to solve the problem, as we're avoiding unnecessary overhead and using bitwise operations directly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Bitwise operations, iteration through bits.
- Problem-solving patterns: Avoiding unnecessary overhead, using bitwise operations for bit-level operations.
- Optimization techniques: Using bitwise operations instead of string conversion.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not initializing variables correctly.
- Edge cases to watch for: Input of 0, input of 1.
- Performance pitfalls: Using string conversion instead of bitwise operations.
- Testing considerations: Test with different inputs, including edge cases.