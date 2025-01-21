## Maximize Subarray Sum After Removing All Occurrences of One Element

**Problem Link:** https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `x`.
- Output: The maximum subarray sum after removing all occurrences of `x` from `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, and `1 <= x <= 10^5`.
- Key requirements: Remove all occurrences of `x` and find the maximum subarray sum.

**Example Test Cases:**
- Input: `nums = [1, 2, 2, 3], x = 2`, Output: `4` (after removing `2`, the array becomes `[1, 3]`, and the maximum subarray sum is `1 + 3 = 4`).
- Input: `nums = [1, 2, 3, 4], x = 5`, Output: `10` (no elements are removed, and the maximum subarray sum is `1 + 2 + 3 + 4 = 10`).

---

### Brute Force Approach

**Explanation:**
- Remove all occurrences of `x` from the array.
- Use Kadane's algorithm to find the maximum subarray sum.
- This approach is straightforward but may not be efficient for large inputs.

```cpp
vector<int> removeElement(vector<int>& nums, int x) {
    vector<int> newNums;
    for (int num : nums) {
        if (num != x) {
            newNums.push_back(num);
        }
    }
    return newNums;
}

int maxSubArray(vector<int>& nums) {
    if (nums.empty()) {
        return 0;
    }
    int maxSum = nums[0];
    int currentSum = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    return maxSum;
}

int maximumSum(vector<int>& nums, int x) {
    vector<int> newNums = removeElement(nums, x);
    return maxSubArray(newNums);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ (removing elements) + $O(n)$ (Kadane's algorithm) = $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(n)$ (new array without `x`).
> - **Why these complexities occur:** Removing elements and applying Kadane's algorithm both require a single pass through the array.

---

### Optimal Approach (Required)

**Explanation:**
- Modify Kadane's algorithm to ignore `x` and calculate the maximum subarray sum in a single pass.
- Initialize `maxSum` and `currentSum` to negative infinity.
- Iterate through the array, updating `currentSum` and `maxSum` accordingly.

```cpp
int maximumSum(vector<int>& nums, int x) {
    int maxSum = INT_MIN;
    int currentSum = 0;
    for (int num : nums) {
        if (num == x) {
            currentSum = 0;
        } else {
            currentSum = max(num, currentSum + num);
            maxSum = max(maxSum, currentSum);
        }
    }
    return maxSum == INT_MIN ? 0 : maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(1)$ (constant space).
> - **Optimality proof:** This approach calculates the maximum subarray sum in a single pass, ignoring `x`, which is the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- Modified Kadane's algorithm to ignore a specific element.
- Calculated the maximum subarray sum in a single pass.
- Handled edge cases where the maximum subarray sum is zero.

**Mistakes to Avoid:**
- Failing to handle edge cases where the maximum subarray sum is zero.
- Using unnecessary extra space to store the new array without `x`.
- Not modifying Kadane's algorithm to ignore `x` and calculate the maximum subarray sum in a single pass.