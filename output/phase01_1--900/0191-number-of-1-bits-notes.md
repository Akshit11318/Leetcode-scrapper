## Number of 1 Bits
**Problem Link:** https://leetcode.com/problems/number-of-1-bits/description

**Problem Statement:**
- Input format and constraints: The input is an integer `n`, and the constraint is that `n` is a 32-bit integer.
- Expected output format: The expected output is the number of 1 bits in the binary representation of `n`.
- Key requirements and edge cases to consider: The key requirement is to count the number of 1 bits in the binary representation of `n`. Edge cases include `n = 0`, `n = 1`, and `n = -1`.
- Example test cases with explanations:
  - `n = 11` (binary: `1011`), expected output: `3`
  - `n = 0` (binary: `0`), expected output: `0`
  - `n = 1` (binary: `1`), expected output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to convert the integer `n` to a binary string and then count the number of '1' characters in the string.
- Step-by-step breakdown of the solution:
  1. Convert `n` to a binary string.
  2. Initialize a counter to 0.
  3. Iterate through each character in the binary string.
  4. If the character is '1', increment the counter.
  5. Return the counter.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first thought.

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        // Convert n to a binary string
        string binaryString;
        while (n) {
            binaryString = (n % 2 == 0 ? "0" : "1") + binaryString;
            n /= 2;
        }
        
        // Initialize a counter to 0
        int count = 0;
        
        // Iterate through each character in the binary string
        for (char c : binaryString) {
            // If the character is '1', increment the counter
            if (c == '1') {
                count++;
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer. This is because we are iterating through each bit in the binary representation of $n$, and there are $\log n$ bits.
> - **Space Complexity:** $O(\log n)$, where $n$ is the input integer. This is because we are storing the binary representation of $n$ as a string, which requires $\log n$ space.
> - **Why these complexities occur:** The time and space complexities occur because we are iterating through each bit in the binary representation of $n$ and storing the binary representation as a string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use bitwise operations to count the number of 1 bits in the binary representation of `n`.
- Detailed breakdown of the approach:
  1. Initialize a counter to 0.
  2. While `n` is not 0, perform a bitwise AND operation between `n` and `n-1`. This operation clears the least significant 1 bit in `n`.
  3. Increment the counter.
  4. Repeat steps 2-3 until `n` is 0.
- Proof of optimality: This approach is optimal because it uses a constant amount of space and has a time complexity of $O(\log n)$, where $n$ is the input integer.
- Why further optimization is impossible: Further optimization is impossible because we must iterate through each bit in the binary representation of `n` to count the number of 1 bits.

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        // Initialize a counter to 0
        int count = 0;
        
        // While n is not 0
        while (n) {
            // Perform a bitwise AND operation between n and n-1
            // This operation clears the least significant 1 bit in n
            n &= n - 1;
            
            // Increment the counter
            count++;
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer. This is because we are iterating through each bit in the binary representation of $n$, and there are $\log n$ bits.
> - **Space Complexity:** $O(1)$, where $n$ is the input integer. This is because we are using a constant amount of space to store the counter.
> - **Optimality proof:** This approach is optimal because it uses a constant amount of space and has a time complexity of $O(\log n)$, where $n$ is the input integer.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, counting 1 bits in binary representation.
- Problem-solving patterns identified: Using bitwise operations to solve problems related to binary representation.
- Optimization techniques learned: Using bitwise operations to reduce time and space complexity.
- Similar problems to practice: Counting 0 bits in binary representation, finding the most significant bit in binary representation.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, using incorrect bitwise operations.
- Edge cases to watch for: `n = 0`, `n = 1`, `n = -1`.
- Performance pitfalls: Using unnecessary loops or conditional statements.
- Testing considerations: Testing with different input values, including edge cases.