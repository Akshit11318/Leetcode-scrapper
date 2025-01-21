## Counting Bits
**Problem Link:** https://leetcode.com/problems/counting-bits/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, return an array of size `n + 1`, where each element `i` represents the number of bits that are set to 1 in the binary representation of `i`.
- Expected output format: An array of integers, where each integer is the count of bits set to 1 in its index's binary representation.
- Key requirements and edge cases to consider: The input integer `n` can range from 0 to $2^{15}-1$. We need to consider how to efficiently calculate the number of set bits for each number up to `n`.
- Example test cases with explanations: For example, given `n = 5`, the binary representations of numbers from 0 to 5 are: `0b0`, `0b1`, `0b10`, `0b11`, `0b100`, `0b101`. The corresponding counts of bits set to 1 are: 0, 1, 1, 2, 1, 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to iterate through each number from 0 to `n`, convert it to its binary representation, and then count the number of bits set to 1.
- Step-by-step breakdown of the solution:
  1. Iterate through each number `i` from 0 to `n`.
  2. Convert `i` to its binary representation.
  3. Count the number of bits set to 1 in the binary representation of `i`.
  4. Store this count in an array at index `i`.
- Why this approach comes to mind first: This approach is intuitive because it directly addresses the problem statement by calculating the number of set bits for each number individually.

```cpp
vector<int> countBits(int n) {
    vector<int> result(n + 1);
    for (int i = 0; i <= n; i++) {
        int count = 0;
        int num = i;
        while (num) {
            count += num & 1;
            num >>= 1;
        }
        result[i] = count;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the input integer. This is because for each number up to `n`, we potentially iterate through all its bits (up to $\log n$ bits for the number `n` itself).
> - **Space Complexity:** $O(n)$, as we store the count of set bits for each number up to `n` in an array.
> - **Why these complexities occur:** The time complexity is dominated by the bit counting operation for each number, and the space complexity is due to the storage of the result array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that the binary representation of a number can be related to the binary representation of its half (integer division by 2) plus one if the number is odd. This relationship allows us to build the counts of set bits iteratively, starting from the base case of `0b0` having 0 bits set.
- Detailed breakdown of the approach:
  1. Initialize an array `result` of size `n + 1` with all elements set to 0.
  2. For each number `i` from 1 to `n`, calculate the count of set bits by considering two cases:
    - If `i` is even, the count of set bits is the same as that of `i / 2`.
    - If `i` is odd, the count of set bits is one more than that of `i / 2`.
  3. Store the calculated count in `result[i]`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the numbers from 0 to `n`, and each operation within the loop is constant time, leading to a linear time complexity.

```cpp
vector<int> countBits(int n) {
    vector<int> result(n + 1);
    for (int i = 1; i <= n; i++) {
        result[i] = result[i >> 1] + (i & 1);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we only need to iterate through the numbers from 1 to `n` once.
> - **Space Complexity:** $O(n)$, for storing the counts of set bits in the `result` array.
> - **Optimality proof:** This is the best possible time complexity because we must at least consider each number up to `n` once to calculate its count of set bits.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, dynamic programming (in the sense of building up a solution iteratively from smaller sub-problems).
- Problem-solving patterns identified: Recognizing relationships between the binary representations of numbers and their halves.
- Optimization techniques learned: Avoiding redundant calculations by leveraging previously computed results.
- Similar problems to practice: Other problems involving bit manipulation and dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (like `n = 0`), or incorrectly calculating the count of set bits.
- Edge cases to watch for: The case when `n = 0`, and ensuring the array is initialized with enough space.
- Performance pitfalls: Using inefficient algorithms that result in higher time complexities, such as iterating through each bit of each number without leveraging any relationships between numbers.
- Testing considerations: Ensure to test the function with various inputs, including edge cases like `n = 0` and larger values of `n` to verify correctness and performance.