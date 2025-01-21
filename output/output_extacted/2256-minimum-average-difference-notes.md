## Minimum Average Difference
**Problem Link:** https://leetcode.com/problems/minimum-average-difference/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` of size `n`, find the minimum average difference between the average of the first `i` elements and the average of the last `n - i` elements.
- Expected output format: Return the index `i` that minimizes the average difference.
- Key requirements and edge cases to consider: The average difference is calculated as the absolute difference between the average of the first `i` elements and the average of the last `n - i` elements.
- Example test cases with explanations: For example, given `nums = [2,5,3,9,5,6]`, the minimum average difference is achieved at index `3`, where the average of the first `3` elements is `(2 + 5 + 3) / 3 = 10 / 3` and the average of the last `3` elements is `(9 + 5 + 6) / 3 = 20 / 3`, resulting in an average difference of `|10 / 3 - 20 / 3| = 10 / 3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the average of the first `i` elements and the average of the last `n - i` elements for each `i`, and find the `i` that minimizes the average difference.
- Step-by-step breakdown of the solution:
  1. Iterate over each index `i` in the array.
  2. Calculate the sum of the first `i` elements and the sum of the last `n - i` elements.
  3. Calculate the average of the first `i` elements and the average of the last `n - i` elements.
  4. Calculate the average difference between the two averages.
  5. Keep track of the minimum average difference and the corresponding index `i`.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the average difference for each possible split of the array.

```cpp
int minimumAverageDifference(vector<int>& nums) {
    int n = nums.size();
    int minDiff = INT_MAX;
    int minIndex = -1;
    for (int i = 0; i < n; i++) {
        long long sum1 = 0;
        long long sum2 = 0;
        for (int j = 0; j <= i; j++) {
            sum1 += nums[j];
        }
        for (int j = i + 1; j < n; j++) {
            sum2 += nums[j];
        }
        long long avg1 = sum1 / (i + 1);
        long long avg2 = (i == n - 1) ? 0 : sum2 / (n - i - 1);
        long long diff = abs(avg1 - avg2);
        if (diff < minDiff) {
            minDiff = diff;
            minIndex = i;
        }
    }
    return minIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we have two nested loops, each iterating over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum difference and the corresponding index.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the space complexity is constant because we only use a fixed amount of space to store the minimum difference and the corresponding index.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the prefix sum of the array to avoid recalculating the sum of the first `i` elements for each `i`.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum of the array.
  2. Iterate over each index `i` in the array.
  3. Calculate the average of the first `i` elements using the prefix sum.
  4. Calculate the average of the last `n - i` elements using the total sum and the prefix sum.
  5. Calculate the average difference between the two averages.
  6. Keep track of the minimum average difference and the corresponding index `i`.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we must at least read the input array once.

```cpp
int minimumAverageDifference(vector<int>& nums) {
    int n = nums.size();
    vector<long long> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    int minDiff = INT_MAX;
    int minIndex = -1;
    for (int i = 0; i < n; i++) {
        long long avg1 = prefixSum[i + 1] / (i + 1);
        long long avg2 = (i == n - 1) ? 0 : (prefixSum[n] - prefixSum[i + 1]) / (n - i - 1);
        long long diff = abs(avg1 - avg2);
        if (diff < minDiff) {
            minDiff = diff;
            minIndex = i;
        }
    }
    return minIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we have a single loop iterating over the array.
> - **Space Complexity:** $O(n)$, as we use a prefix sum array of size $n + 1$.
> - **Optimality proof:** This approach is optimal because we must at least read the input array once, and we only use a single loop to calculate the minimum average difference.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum, average calculation, and minimum difference calculation.
- Problem-solving patterns identified: using prefix sum to avoid recalculating sums, and iterating over the array to find the minimum difference.
- Optimization techniques learned: using prefix sum to reduce time complexity from $O(n^2)$ to $O(n)$.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where `i == n - 1` correctly, and not using `long long` to avoid overflow.
- Edge cases to watch for: handling the case where `i == n - 1` correctly, and avoiding overflow when calculating the average difference.
- Performance pitfalls: using nested loops instead of prefix sum, and not using `long long` to avoid overflow.
- Testing considerations: testing the function with different input arrays, including edge cases such as an empty array and an array with a single element.