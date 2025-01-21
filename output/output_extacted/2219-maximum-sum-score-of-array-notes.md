## Maximum Sum Score of Array
**Problem Link:** https://leetcode.com/problems/maximum-sum-score-of-array/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer array `nums` as input and an integer `k`. The array `nums` has a length of `n`, where `1 <= n <= 10^5`. The integer `k` satisfies `1 <= k <= n`.
- Expected output format: The function should return the maximum sum score that can be achieved.
- Key requirements and edge cases to consider: The array `nums` can contain both positive and negative numbers. The integer `k` represents the number of elements to be included in the sum.
- Example test cases with explanations: For example, given `nums = [1, 2, 3, 4, 5]` and `k = 3`, the maximum sum score is `15`, which can be achieved by including the elements `3`, `4`, and `5` in the sum.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible combinations of `k` elements from the array `nums` and calculating the sum of each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `k` elements from the array `nums`.
  2. For each combination, calculate the sum of the elements.
  3. Keep track of the maximum sum found so far.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, as it involves exhaustively exploring all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxSumScore(vector<int>& nums, int k) {
    int n = nums.size();
    int maxSum = INT_MIN;

    // Generate all possible combinations of k elements
    for (int i = 0; i < (1 << n); i++) {
        int sum = 0;
        int count = 0;

        // Calculate the sum of the current combination
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                sum += nums[j];
                count++;
            }
        }

        // Update the maximum sum if the current combination has k elements
        if (count == k) {
            maxSum = max(maxSum, sum);
        }
    }

    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the array `nums`. This is because we generate all possible combinations of `n` elements, and for each combination, we calculate the sum of the elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum and the current sum.
> - **Why these complexities occur:** The time complexity is high because we exhaustively explore all possible combinations of `n` elements. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves sorting the array `nums` in descending order and then selecting the first `k` elements.
- Detailed breakdown of the approach:
  1. Sort the array `nums` in descending order.
  2. Select the first `k` elements of the sorted array.
  3. Calculate the sum of the selected elements.
- Proof of optimality: This approach is optimal because it guarantees the maximum sum score. By sorting the array in descending order, we ensure that the largest elements are selected first, which maximizes the sum.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxSumScore(vector<int>& nums, int k) {
    sort(nums.rbegin(), nums.rend());
    int sum = 0;

    // Calculate the sum of the first k elements
    for (int i = 0; i < k; i++) {
        sum += nums[i];
    }

    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the array `nums`. This is because we sort the array using the `sort` function, which has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum.
> - **Optimality proof:** This approach is optimal because it guarantees the maximum sum score. By sorting the array in descending order, we ensure that the largest elements are selected first, which maximizes the sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, selection, and sum calculation.
- Problem-solving patterns identified: The problem involves finding the maximum sum score, which requires selecting the largest elements from the array.
- Optimization techniques learned: Sorting the array in descending order and selecting the first `k` elements is an efficient way to find the maximum sum score.
- Similar problems to practice: Other problems that involve finding the maximum sum score, such as finding the maximum sum of a subarray.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the array in descending order, not selecting the first `k` elements, and not calculating the sum correctly.
- Edge cases to watch for: The array `nums` can be empty, and the integer `k` can be larger than the length of the array.
- Performance pitfalls: Not using an efficient sorting algorithm, such as the `sort` function, can lead to poor performance.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it works correctly.