## Maximize Sum of Array After K Negations

**Problem Link:** https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `nums` and an integer `k` as input. The goal is to maximize the sum of the array after `k` negations.
- Expected output format: The function should return the maximum sum of the array after `k` negations.
- Key requirements and edge cases to consider: The input array can be empty, and `k` can be greater than the length of the array. The function should handle these edge cases.
- Example test cases with explanations: 
    - If `nums = [4, 2, 3]` and `k = 1`, the function should return `7` because the maximum sum after one negation is `(-4) + 2 + 3 = 1`, but we can choose to negate the smallest number, `2`, to get `4 + (-2) + 3 = 5`.
    - If `nums = [3, -1, 2, -2]` and `k = 3`, the function should return `4` because the maximum sum after three negations is `(-3) + 1 + (-2) + 2 = 2`, but we can choose to negate the three smallest numbers, `-1`, `-2`, and `2`, to get `3 + 1 + 2 + 2 = 8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of `k` negations and calculating the sum for each combination.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of `k` indices from the array.
    2. For each combination, negate the corresponding elements in the array.
    3. Calculate the sum of the array after negation.
    4. Keep track of the maximum sum found.
- Why this approach comes to mind first: This approach is straightforward and ensures that all possible combinations are considered.

```cpp
#include <vector>
#include <algorithm>

int largestSumAfterKNegations(vector<int>& nums, int k) {
    int n = nums.size();
    int maxSum = INT_MIN;

    // Generate all possible combinations of k indices
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> temp = nums;
        int sum = 0;

        // Negate the corresponding elements for the current combination
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) && k > 0) {
                temp[i] = -temp[i];
                k--;
            }
        }

        // Calculate the sum of the array after negation
        for (int i = 0; i < n; i++) {
            sum += temp[i];
        }

        // Update the maximum sum
        maxSum = max(maxSum, sum);
    }

    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ because we generate all possible combinations of `n` indices and calculate the sum for each combination.
> - **Space Complexity:** $O(n)$ because we need to store the temporary array and the current combination.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations, which leads to an exponential time complexity. The space complexity is linear because we only need to store a few variables and the temporary array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves sorting the array in ascending order and negating the smallest `k` elements. If `k` is greater than the length of the array, we negate all elements and then negate the smallest `k % n` elements again.
- Detailed breakdown of the approach: 
    1. Sort the array in ascending order.
    2. Negate the smallest `k` elements.
    3. If `k` is greater than the length of the array, negate all elements and then negate the smallest `k % n` elements again.
- Proof of optimality: This approach is optimal because it ensures that the sum of the array is maximized by negating the smallest elements.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n)$ due to the sorting, which is the best possible time complexity for this problem.

```cpp
#include <vector>
#include <algorithm>

int largestSumAfterKNegations(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());

    for (int i = 0; i < k; i++) {
        if (i >= nums.size()) {
            break;
        }
        nums[i] = -nums[i];
    }

    if (k > nums.size()) {
        k %= nums.size();
        for (int i = 0; i < k; i++) {
            nums[i] = -nums[i];
        }
    }

    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
    }

    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ because we sort the array in ascending order.
> - **Space Complexity:** $O(1)$ because we only need to store a few variables.
> - **Optimality proof:** This approach is optimal because it ensures that the sum of the array is maximized by negating the smallest elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, negation, and optimization.
- Problem-solving patterns identified: the importance of considering edge cases and optimizing the solution.
- Optimization techniques learned: sorting and negating the smallest elements.
- Similar problems to practice: problems involving optimization and sorting.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases and not optimizing the solution.
- Edge cases to watch for: when `k` is greater than the length of the array.
- Performance pitfalls: not using an efficient sorting algorithm.
- Testing considerations: testing the solution with different inputs and edge cases.