## Number Complement

**Problem Link:** https://leetcode.com/problems/number-complement/description

**Problem Statement:**
- Input format: An integer `N`.
- Constraints: `1 <= N <= 10^9`.
- Expected output format: The complement of `N`.
- Key requirements and edge cases to consider: The complement of a number is obtained by flipping all its bits from left to right.
- Example test cases with explanations:
  - Input: `5` (binary `101`), Output: `2` (binary `010`).
  - Input: `1` (binary `1`), Output: `0` (binary `0`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the integer to binary, flip each bit, and then convert back to decimal.
- Step-by-step breakdown of the solution:
  1. Convert the integer to a binary string.
  2. Flip each bit in the binary string (i.e., `0` becomes `1` and vice versa).
  3. Convert the flipped binary string back to an integer.
- Why this approach comes to mind first: It directly follows from the definition of a number's complement.

```cpp
class Solution {
public:
    int findComplement(int N) {
        // Convert integer to binary string
        string binary = "";
        while (N > 0) {
            binary = (N % 2 == 0 ? "0" : "1") + binary;
            N /= 2;
        }
        
        // Flip each bit in the binary string
        for (int i = 0; i < binary.length(); i++) {
            binary[i] = (binary[i] == '0') ? '1' : '0';
        }
        
        // Convert flipped binary string back to integer
        int complement = 0;
        for (int i = 0; i < binary.length(); i++) {
            complement = complement * 2 + (binary[i] - '0');
        }
        
        return complement;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log N)$, where $\log N$ represents the number of bits in $N$. This is because we process each bit of $N$ once.
> - **Space Complexity:** $O(\log N)$, as we need to store the binary representation of $N$.
> - **Why these complexities occur:** The number of operations (conversions and bit flips) is directly proportional to the number of bits in $N$, leading to a logarithmic complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of explicitly converting to binary and flipping bits, we can use bitwise operations to achieve the same result more efficiently.
- Detailed breakdown of the approach:
  1. Calculate the number of bits in $N$.
  2. Create a mask with all bits set to 1 up to the number of bits in $N$.
  3. Use the bitwise XOR operation between $N$ and the mask to flip all bits in $N$.
- Proof of optimality: This approach minimizes the number of operations required to flip the bits, making it more efficient than the brute force method.
- Why further optimization is impossible: We must at least examine each bit of $N$ once to flip it, so the logarithmic time complexity is inherent.

```cpp
class Solution {
public:
    int findComplement(int N) {
        // Calculate number of bits in N
        int bits = log2(N) + 1;
        
        // Create a mask with all bits set to 1 up to the number of bits in N
        int mask = (1 << bits) - 1;
        
        // Use bitwise XOR to flip all bits in N
        return N ^ mask;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log N)$, where $\log N$ represents the number of bits in $N$. This is because calculating the number of bits and performing the XOR operation take logarithmic time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the mask and other variables.
> - **Optimality proof:** The bitwise XOR operation directly achieves the bit flipping required for the complement, making it the most efficient approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, logarithmic complexity, and optimization through bitwise operations.
- Problem-solving patterns identified: Direct calculation vs. bitwise manipulation for efficiency.
- Optimization techniques learned: Using bitwise XOR for flipping bits.
- Similar problems to practice: Other bit manipulation problems, such as checking if a number is a power of 2 or counting the number of 1 bits.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the number of bits or misunderstanding how bitwise XOR works.
- Edge cases to watch for: Numbers with a large number of bits, which can affect the calculation of the mask.
- Performance pitfalls: Using explicit binary conversion instead of bitwise operations.
- Testing considerations: Ensure to test with numbers of varying bit lengths to cover all edge cases.