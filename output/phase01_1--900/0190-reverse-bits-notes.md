## Reverse Bits

**Problem Link:** [https://leetcode.com/problems/reverse-bits/description](https://leetcode.com/problems/reverse-bits/description)

**Problem Statement:**
- Input format: An unsigned 32-bit integer `n`.
- Constraints: `0 <= n < 2^32`.
- Expected output format: The integer with its bits reversed.
- Key requirements and edge cases to consider: The function should reverse the bits of the input integer and return the resulting integer.
- Example test cases with explanations:
  - Input: `n = 43261596` (binary: `00101011 11100100 00000010 01111000`)
  - Expected Output: `964176192` (binary: `00111001 00001011 11110000 10101000`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the integer to a binary string, reverse the string, and then convert it back to an integer.
- Step-by-step breakdown of the solution:
  1. Convert the integer `n` to a binary string.
  2. Reverse the binary string.
  3. Convert the reversed binary string back to an integer.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        string binary = bitset<32>(n).to_string();
        string reversed = "";
        for (int i = 31; i >= 0; i--) {
            reversed += binary[i];
        }
        return stol(reversed, 0, 2);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are always dealing with a fixed-size binary string (32 bits).
> - **Space Complexity:** $O(1)$ because the space used does not grow with the size of the input.
> - **Why these complexities occur:** The conversion to and from binary string and the reversal operation take constant time and space because the size of the input is fixed (32 bits).

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the integer to a string, we can use bitwise operations to reverse the bits directly.
- Detailed breakdown of the approach:
  1. Initialize a variable `result` to 0.
  2. For each bit in `n` (from right to left), perform the following steps:
    - Use the bitwise AND operator `&` with `1` to check if the current bit is `1`.
    - If the bit is `1`, use the bitwise OR operator `|` to set the corresponding bit in `result`.
    - Shift the bit in `result` to the left by one position using the left shift operator `<<`.
    - Shift the bit in `n` to the right by one position using the right shift operator `>>`.
  3. After all bits have been processed, return `result`.
- Proof of optimality: This approach is optimal because it directly manipulates the bits of the integer using bitwise operations, which is the most efficient way to reverse the bits of an integer.

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>= 1;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are always dealing with a fixed-size integer (32 bits).
> - **Space Complexity:** $O(1)$ because the space used does not grow with the size of the input.
> - **Optimality proof:** This approach is optimal because it uses a constant number of operations to reverse the bits of the integer, regardless of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, bit manipulation.
- Problem-solving patterns identified: Direct manipulation of bits using bitwise operations.
- Optimization techniques learned: Avoiding unnecessary conversions to and from strings.
- Similar problems to practice: Other bit manipulation problems, such as checking if a number is a power of 2 or counting the number of set bits in an integer.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as when the input is 0.
- Edge cases to watch for: When the input is 0 or when the input has only one bit set.
- Performance pitfalls: Using unnecessary conversions to and from strings, which can be slow.
- Testing considerations: Testing with a variety of inputs, including edge cases and large inputs.