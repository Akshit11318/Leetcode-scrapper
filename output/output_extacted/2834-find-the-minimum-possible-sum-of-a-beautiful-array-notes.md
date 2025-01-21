## Find the Minimum Possible Sum of a Beautiful Array

**Problem Link:** https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, where `n` is the number of elements in the beautiful array.
- Expected output format: The minimum possible sum of a beautiful array of length `n`.
- Key requirements and edge cases to consider: A beautiful array is defined as an array where the sum of the elements in the array equals the length of the array times the minimum element in the array. The goal is to minimize this sum.
- Example test cases with explanations:
  - For `n = 2`, a beautiful array could be `[1, 1]` with a sum of `2`, which is the minimum possible sum for `n = 2`.
  - For `n = 3`, a beautiful array could be `[1, 1, 1]` with a sum of `3`, which is the minimum possible sum for `n = 3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible arrays of length `n` and check if each array is beautiful. If it is, calculate its sum.
- Step-by-step breakdown of the solution:
  1. Generate all possible arrays of length `n`.
  2. For each array, check if it is beautiful by verifying if the sum of its elements equals `n` times the minimum element in the array.
  3. If an array is beautiful, calculate its sum.
  4. Keep track of the minimum sum found among all beautiful arrays.
- Why this approach comes to mind first: It is a straightforward approach that checks all possibilities, ensuring that no potential solution is overlooked.

```cpp
#include <iostream>
#include <vector>
#include <climits>

int findMinSum(int n) {
    int minSum = INT_MAX;
    // Generate all possible arrays of length n
    for (int i = 0; i < (1 << n); ++i) {
        std::vector<int> arr;
        for (int j = 0; j < n; ++j) {
            if ((i & (1 << j)) != 0) {
                arr.push_back(1);
            } else {
                arr.push_back(0);
            }
        }
        // Check if the array is beautiful and update minSum if necessary
        int sum = 0;
        int minVal = INT_MAX;
        for (int val : arr) {
            sum += val;
            minVal = std::min(minVal, val);
        }
        if (sum == n * minVal) {
            minSum = std::min(minSum, sum);
        }
    }
    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the array. This is because we generate all possible arrays of length `n` (which is $2^n$) and for each array, we perform operations that take $O(n)$ time.
> - **Space Complexity:** $O(n)$, for storing the current array being processed.
> - **Why these complexities occur:** The exponential time complexity is due to the generation of all possible arrays, and the linear space complexity is for storing each array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: A beautiful array can be constructed by filling it with the smallest possible number (1) to minimize the sum, as the sum of the array must equal `n` times the minimum element.
- Detailed breakdown of the approach:
  1. The minimum element in the beautiful array should be 1 to minimize the sum.
  2. Since the sum of the array must equal `n` times the minimum element, and the minimum element is 1, the sum must be `n`.
  3. Therefore, the minimum possible sum of a beautiful array of length `n` is `n`.

```cpp
int findMinSum(int n) {
    return n;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as the solution involves a constant-time operation.
> - **Space Complexity:** $O(1)$, as no additional space is used.
> - **Optimality proof:** This solution is optimal because it directly calculates the minimum possible sum based on the definition of a beautiful array, without needing to generate or check any arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Understanding the definition of a beautiful array and leveraging this definition to directly calculate the minimum possible sum.
- Problem-solving patterns identified: Identifying key insights that simplify the problem and lead to an optimal solution.
- Optimization techniques learned: Avoiding brute-force approaches by leveraging problem-specific insights.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the brute-force approach or misunderstanding the definition of a beautiful array.
- Edge cases to watch for: Ensuring that the solution handles the case where `n` is 0 or negative, although these cases are not specified in the problem.
- Performance pitfalls: Failing to recognize the exponential time complexity of the brute-force approach and its impracticality for large `n`.
- Testing considerations: Testing the solution with various values of `n` to ensure it correctly calculates the minimum possible sum.