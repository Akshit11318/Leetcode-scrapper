## Minimize XOR
**Problem Link:** https://leetcode.com/problems/minimize-xor/description

**Problem Statement:**
- Input format: Two integers `num1` and `num2`.
- Constraints: $0 \leq num1, num2 \leq 10^9$.
- Expected output format: The minimum XOR sum between `num1` and `num2`.
- Key requirements and edge cases to consider: All possible bit combinations of `num1` and `num2`.
- Example test cases with explanations: For `num1 = 1` and `num2 = 12`, the minimum XOR sum is `7` because the binary representation of `1` is `0001` and the binary representation of `12` is `1100`. The minimum XOR sum is achieved by finding a number that has the same bits as `num1` where `num2` has `0`s and different bits where `num2` has `1`s.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible numbers and calculate the XOR sum with `num2`.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible numbers from `0` to `2^31 - 1`.
  2. For each number, calculate the XOR sum with `num2`.
  3. Keep track of the minimum XOR sum.
- Why this approach comes to mind first: It is straightforward and guarantees finding the minimum XOR sum.

```cpp
class Solution {
public:
    int minimumXORSum(int num1, int num2) {
        int minSum = INT_MAX;
        for (int i = 0; i <= (1 << 31) - 1; i++) {
            int xorSum = i ^ num2;
            minSum = min(minSum, xorSum);
        }
        return minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{31})$ because we iterate over all possible integers.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach tries all possible numbers, resulting in exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We only need to consider the bits of `num1` and `num2` to find the minimum XOR sum.
- Detailed breakdown of the approach:
  1. Convert `num1` and `num2` to binary strings.
  2. Iterate over the bits of `num1` and `num2` from left to right.
  3. For each bit, if the bit in `num2` is `1`, set the corresponding bit in `num1` to `0` to minimize the XOR sum.
- Proof of optimality: This approach considers all possible bit combinations of `num1` and `num2` and minimizes the XOR sum by setting the bits of `num1` to `0` where `num2` has `1`s.

```cpp
class Solution {
public:
    int minimumXORSum(int num1, int num2) {
        int minSum = 0;
        for (int i = 31; i >= 0; i--) {
            int bit1 = (num1 >> i) & 1;
            int bit2 = (num2 >> i) & 1;
            if (bit2 == 1) {
                minSum += (bit1 ^ 0);
            }
        }
        return minSum;
    }
};
```

However, this can be optimized to directly calculate the result without iteration.

```cpp
class Solution {
public:
    int minimumXORSum(int num1, int num2) {
        return num1 & (~num2);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we only perform a constant number of operations.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This approach directly calculates the minimum XOR sum by considering the bits of `num1` and `num2`, resulting in constant time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation and XOR operation.
- Problem-solving patterns identified: Considering the bits of the input numbers to minimize the XOR sum.
- Optimization techniques learned: Using bit manipulation to directly calculate the result.
- Similar problems to practice: Other bit manipulation problems, such as finding the maximum XOR sum.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the bits of the input numbers.
- Edge cases to watch for: When `num1` or `num2` is `0`.
- Performance pitfalls: Using the brute force approach, which has exponential time complexity.
- Testing considerations: Testing with different input values to ensure the solution works correctly.