## Smallest Number with All Set Bits
**Problem Link:** https://leetcode.com/problems/smallest-number-with-all-set-bits/description

**Problem Statement:**
- Given an integer `k`, return the smallest integer `x` such that `x` has exactly `k` set bits in its binary representation.
- Input: `k` is an integer between `1` and `30` (inclusive).
- Expected output: The smallest integer `x` with `k` set bits in its binary representation.
- Key requirements and edge cases to consider: The smallest possible integer with `k` set bits is when all set bits are to the right of the least significant bit, but this approach doesn't work when we need to minimize the value. Instead, we need to consider placing the set bits in positions that give the smallest possible value, starting from the least significant bit and moving to the left.
- Example test cases with explanations:
  - For `k = 1`, the smallest number is `1` because its binary representation is `1`, which has exactly one set bit.
  - For `k = 2`, the smallest number is `3` because its binary representation is `11`, which has exactly two set bits.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start with the smallest possible number and incrementally check each number to see if it has `k` set bits. This involves converting each number to binary and counting the set bits.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `num` to `1`.
  2. Loop indefinitely until a number with `k` set bits is found.
  3. In each iteration, convert `num` to its binary representation and count the number of set bits.
  4. If the number of set bits equals `k`, return `num`.
  5. Otherwise, increment `num` by `1`.
- Why this approach comes to mind first: It's a straightforward method that checks every possible number until it finds one that meets the condition.

```cpp
int smallestNumberWithKSetBits(int k) {
    int num = 1;
    while (true) {
        // Convert num to binary and count set bits
        int setBits = 0;
        int temp = num;
        while (temp) {
            setBits += temp & 1;
            temp >>= 1;
        }
        if (setBits == k) {
            return num;
        }
        num++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{31} \cdot log(2^{31}))$ because in the worst case, we might need to check all numbers up to $2^{31}$ (the maximum value for a 32-bit signed integer), and for each number, we perform a binary conversion and set bit count, which takes $log(2^{31})$ time.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach is inefficient because it checks every possible number, leading to an exponential time complexity. The set bit count operation within the loop contributes to the logarithmic factor in the time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: To minimize the value of the number with `k` set bits, we should place the set bits in the highest possible positions, starting from the right (least significant bit) and moving to the left. However, simply placing `k` ones in a row from the right does not give the smallest number because it does not consider the place value system of binary numbers. A more efficient approach involves using the properties of binary numbers and the concept of place value to construct the smallest number with `k` set bits.
- Detailed breakdown of the approach:
  1. Initialize `result` to `0`.
  2. Loop `k` times:
     - In each iteration, calculate the next position to place a set bit. This can be done by finding the least significant bit that is `0` in the current `result` (since we want to minimize the value of `x`, we start filling from the right).
     - Update `result` by setting the bit at the calculated position to `1`.
- Proof of optimality: This approach is optimal because it ensures that the set bits are placed in the highest possible positions (from right to left), thus minimizing the value of the resulting number.
- Why further optimization is impossible: This approach already considers the optimal placement of set bits to minimize the number's value, making further optimization unnecessary.

```cpp
int smallestNumberWithKSetBits(int k) {
    int result = 0;
    for (int i = 0; i < k; i++) {
        result |= 1 << i;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$ because we perform a constant amount of work for each of the `k` iterations.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it directly constructs the smallest possible number with `k` set bits by placing the set bits in the lowest possible positions, thus minimizing the value of the resulting number.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, understanding of binary representation, and optimization techniques.
- Problem-solving patterns identified: The importance of understanding the problem constraints and applying bit manipulation techniques to solve problems related to binary representations.
- Optimization techniques learned: Placing set bits in the highest possible positions to minimize the value of a binary number.
- Similar problems to practice: Problems involving bit manipulation, such as finding the number of set bits in a given integer or determining if a number is a power of two.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when `k` is `0` or greater than `30`.
- Edge cases to watch for: The input range of `k` and ensuring the result does not exceed the maximum value for a 32-bit signed integer.
- Performance pitfalls: Using inefficient algorithms that check every possible number, as seen in the brute force approach.
- Testing considerations: Thoroughly testing the function with different values of `k`, including edge cases, to ensure correctness and efficiency.