## Concatenation of Consecutive Binary Numbers

**Problem Link:** https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, where `1 <= n <= 1000000`.
- Expected output format: The function should return a decimal number representing the concatenation of binary representations of numbers from `1` to `n`.
- Key requirements and edge cases to consider: The function should handle large inputs efficiently and return the correct decimal representation.
- Example test cases with explanations: For example, if `n = 1`, the output should be `1` (binary representation of `1` is `1`). If `n = 3`, the output should be `11011` (binary representation of `1`, `10`, and `11` concatenated).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to convert each number from `1` to `n` into its binary representation and then concatenate these binary strings.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the concatenated binary representation.
  2. Loop through each number from `1` to `n`.
  3. For each number, convert it to its binary representation and append it to the concatenated string.
- Why this approach comes to mind first: It directly follows from understanding the problem statement and is the most intuitive way to tackle the problem.

```cpp
int concatenatedBinary(int n) {
    long long result = 0; // Use long long to handle large numbers
    for (int i = 1; i <= n; i++) {
        string binary = bitset<32>(i).to_string(); // Convert to binary and remove leading zeros
        binary = binary.substr(binary.find('1')); // Remove leading zeros
        for (char c : binary) {
            result = (result << 1) | (c - '0'); // Shift left and append the new bit
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times \log n)$, where $\log n$ comes from the binary representation of each number.
> - **Space Complexity:** $O(\log n)$, as we store the binary representation of the largest number.
> - **Why these complexities occur:** The time complexity is due to the loop over all numbers and the conversion to binary. The space complexity is due to storing the binary representation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of concatenating strings, we can directly manipulate bits to achieve the concatenation effect. This approach avoids the overhead of string operations.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the result, which will be the concatenated binary representation.
  2. Loop through each number from `1` to `n`.
  3. For each number, calculate its binary length (number of bits).
  4. Shift the current result to the left by the number of bits in the current number, making space for the new number's binary representation.
  5. Use bitwise OR operation to append the current number's binary representation to the result.
- Proof of optimality: This approach directly manipulates bits, avoiding the overhead of string concatenation and conversion, making it the most efficient solution.

```cpp
int concatenatedBinary(int n) {
    long long result = 0;
    int length = 0; // Length of the current binary representation
    for (int i = 1; i <= n; i++) {
        if ((i & (i - 1)) == 0) { // Check if i is a power of 2
            length++; // Increase the length of binary representation
        }
        result = ((result << length) | i); // Shift and append
    }
    return result % (1e9 + 7); // Apply modulo to avoid overflow
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we loop through each number once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to concatenate the binary representations, directly manipulating bits.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, efficient string concatenation through bit shifting.
- Problem-solving patterns identified: Looking for ways to avoid string operations in favor of bit manipulation for efficiency.
- Optimization techniques learned: Using bit shifting to concatenate binary representations, avoiding unnecessary conversions.
- Similar problems to practice: Other problems involving bit manipulation and efficient string operations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle overflow, incorrectly calculating binary lengths.
- Edge cases to watch for: Handling numbers that are powers of 2, ensuring correct bit shifting.
- Performance pitfalls: Using string concatenation instead of bit manipulation, not applying modulo to avoid overflow.
- Testing considerations: Thoroughly testing with large inputs to ensure efficiency and correctness.