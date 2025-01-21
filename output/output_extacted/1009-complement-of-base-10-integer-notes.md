## Complement of Base 10 Integer
**Problem Link:** https://leetcode.com/problems/complement-of-base-10-integer/description

**Problem Statement:**
- Input: An integer `N`.
- Constraints: `0 <= N < 2^31`.
- Expected output: The complement of `N`.
- Key requirements: The complement of a number is obtained by flipping all its bits.
- Example test cases:
  - Input: `N = 5` (binary: 101), Output: `2` (binary: 010).
  - Input: `N = 1` (binary: 1), Output: `0` (binary: 0).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the complement of a number, we need to flip all its bits.
- Step-by-step breakdown:
  1. Determine the number of bits in `N`.
  2. Create a mask with all bits set to 1, up to the number of bits in `N`.
  3. Use the bitwise XOR operator (`^`) to flip all the bits of `N`.
- Why this approach comes to mind first: It directly addresses the problem statement by flipping all the bits.

```cpp
class Solution {
public:
    int findComplement(int N) {
        // Calculate the number of bits in N
        int numBits = log2(N) + 1;
        
        // Create a mask with all bits set to 1, up to the number of bits in N
        int mask = (1 << numBits) - 1;
        
        // Use bitwise XOR to flip all the bits of N
        return N ^ mask;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are performing a constant number of operations regardless of the size of the input.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** The operations involved (log2, left shift, and XOR) are constant time and do not depend on the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The number of bits in `N` can also be found by finding the smallest power of 2 that is greater than `N`.
- Detailed breakdown: 
  1. Calculate the number of bits in `N` by finding the smallest power of 2 greater than `N`.
  2. Create a mask with all bits set to 1 up to this power of 2.
  3. Flip all the bits of `N` using the XOR operator.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to find the complement.

```cpp
class Solution {
public:
    int findComplement(int N) {
        // Calculate the number of bits in N by finding the smallest power of 2 greater than N
        int bits = floor(log2(N)) + 1;
        
        // Create a mask with all bits set to 1 up to this power of 2
        int mask = (1 << bits) - 1;
        
        // Flip all the bits of N using XOR
        return N ^ mask;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as the operations are constant time.
> - **Space Complexity:** $O(1)$, using a constant amount of space.
> - **Optimality proof:** This is the best possible complexity because we are performing the minimum number of operations required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Bit manipulation, use of XOR for flipping bits, and calculating the number of bits in an integer.
- Problem-solving patterns: Identifying the smallest power of 2 greater than a given number and using it to create a mask.
- Optimization techniques: Minimizing the number of operations by directly calculating the required mask.

**Mistakes to Avoid:**
- Not considering the case where `N` is 0.
- Incorrectly calculating the number of bits in `N`.
- Forgetting to subtract 1 when creating the mask to ensure all bits are set to 1 up to the required number of bits.

By following these steps and understanding the concepts involved, you can efficiently solve the problem of finding the complement of a base 10 integer.