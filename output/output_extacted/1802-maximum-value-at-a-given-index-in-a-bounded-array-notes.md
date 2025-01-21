## Maximum Value at a Given Index in a Bounded Array

**Problem Link:** https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description

**Problem Statement:**
- Input: An integer `n` representing the size of the array, an integer `index` representing the index at which to find the maximum value, and an integer `maxSum` representing the maximum sum of the array.
- Expected output: The maximum value at the given index in a bounded array.
- Key requirements and edge cases to consider: The array can only contain non-negative integers, and the sum of the array elements must not exceed `maxSum`.
- Example test cases with explanations:
  - `n = 4, index = 2, maxSum = 6`: The maximum value at index 2 is 2.
  - `n = 6, index = 1, maxSum = 10`: The maximum value at index 1 is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible arrays of size `n` with non-negative integers, and for each array, calculate the sum and check if it does not exceed `maxSum`.
- Step-by-step breakdown of the solution:
  1. Generate all possible arrays of size `n`.
  2. For each array, calculate the sum of its elements.
  3. Check if the sum does not exceed `maxSum`.
  4. If the sum is valid, update the maximum value at the given index.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible solutions.

```cpp
class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        int result = 0;
        for (int i = 0; i <= maxSum; i++) {
            for (int j = 0; j < n; j++) {
                int sum = 0;
                for (int k = 0; k < n; k++) {
                    if (k <= j) {
                        sum += max(0, i - (j - k));
                    } else {
                        sum += max(0, i - (k - j));
                    }
                }
                if (sum <= maxSum) {
                    result = max(result, i);
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot maxSum^2)$, where $n$ is the size of the array and $maxSum$ is the maximum sum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible arrays and calculate the sum for each array. The space complexity occurs because we only use a constant amount of space to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The maximum value at the given index can be calculated using a mathematical formula based on the size of the array and the maximum sum.
- Detailed breakdown of the approach:
  1. Calculate the maximum value at the given index using the formula: `result = (maxSum - n + 1) / (n + 1)`.
  2. If the result is greater than `maxSum - n + 1`, update the result to `maxSum - n + 1`.
- Proof of optimality: The formula is derived from the fact that the sum of the array elements must not exceed `maxSum`, and the maximum value at the given index is achieved when the array elements are distributed evenly.
- Why further optimization is impossible: The formula is already optimized, and further optimization would require a different approach.

```cpp
class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        int left = max(0, index);
        int right = max(0, n - index - 1);
        int sum = left + right + 1;
        int result = (maxSum - sum) / n + 1;
        return min(result, maxSum - n + 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only use a constant amount of time to calculate the result.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result.
> - **Optimality proof:** The formula is derived from the fact that the sum of the array elements must not exceed `maxSum`, and the maximum value at the given index is achieved when the array elements are distributed evenly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Mathematical formula derivation, optimization techniques.
- Problem-solving patterns identified: Using mathematical formulas to solve problems, optimizing solutions.
- Optimization techniques learned: Deriving mathematical formulas, using optimization techniques to improve solutions.
- Similar problems to practice: Problems that involve deriving mathematical formulas, optimizing solutions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using optimization techniques.
- Edge cases to watch for: Cases where the input values are extreme, cases where the solution is not optimal.
- Performance pitfalls: Not using optimization techniques, not checking for edge cases.
- Testing considerations: Testing with extreme input values, testing with edge cases.