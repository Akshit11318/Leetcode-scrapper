## Ways to Split Array into Good Subarrays
**Problem Link:** https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= k <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The number of ways to split `nums` into `k` non-empty subarrays such that the sum of elements in each subarray is equal.
- Key Requirements: The sum of elements in each subarray must be equal, and the number of subarrays must be exactly `k`.
- Edge Cases: Handle cases where `k` is greater than the length of `nums`, or where the sum of `nums` is not divisible by `k`.
- Example Test Cases:
  - `nums = [10, 10, 10, 7, 7, 7], k = 3`: Output `2`.
  - `nums = [10, 10, 10, 7, 7, 7], k = 2`: Output `0`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible subarrays and checking if their sums are equal.
- This approach involves iterating over all possible start and end indices for each subarray.
- It comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
int waysToSplit(vector<int>& nums, int k) {
    int n = nums.size();
    long long totalSum = 0;
    for (int num : nums) totalSum += num;

    if (totalSum % k != 0) return 0;

    long long targetSum = totalSum / k;
    int count = 0;

    // Generate all possible subarrays
    for (int i = 0; i < (1 << n); i++) {
        vector<int> subarray;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) subarray.push_back(nums[j]);
        }

        // Check if the subarray sum equals the target sum
        long long subarraySum = 0;
        for (int num : subarray) subarraySum += num;
        if (subarraySum == targetSum) {
            // Check if we can split the remaining array into k-1 subarrays
            vector<int> remainingArray;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) == 0) remainingArray.push_back(nums[j]);
            }
            if (canSplit(remainingArray, k - 1, targetSum)) count++;
        }
    }

    return count;
}

bool canSplit(vector<int>& nums, int k, long long targetSum) {
    if (k == 0) return nums.empty();
    long long currentSum = 0;
    for (int num : nums) {
        currentSum += num;
        if (currentSum == targetSum) {
            vector<int> remainingArray;
            for (int i = currentSum; i < nums.size(); i++) remainingArray.push_back(nums[i]);
            if (canSplit(remainingArray, k - 1, targetSum)) return true;
        }
        if (currentSum > targetSum) return false;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot k)$, where $n$ is the length of `nums`. This is because we generate all possible subarrays and check if their sums are equal.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we store the subarray and the remaining array.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays, which leads to exponential time complexity. The space complexity is linear because we store the subarray and the remaining array.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a prefix sum array to calculate the sum of each subarray in constant time.
- We iterate over all possible start indices for the first subarray and calculate the sum of the remaining array.
- We use a hashmap to store the count of subarrays with a given sum.
- We iterate over the remaining array and update the count of subarrays with a given sum.

```cpp
int waysToSplit(vector<int>& nums, int k) {
    int n = nums.size();
    long long totalSum = 0;
    for (int num : nums) totalSum += num;

    if (totalSum % k != 0) return 0;

    long long targetSum = totalSum / k;
    vector<long long> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + nums[i];

    int count = 0;
    for (int i = 0; i < n; i++) {
        long long currentSum = prefixSum[i + 1];
        if (currentSum == targetSum) {
            int remainingCount = k - 1;
            long long remainingSum = totalSum - currentSum;
            if (canSplit(prefixSum, i + 1, remainingCount, remainingSum, targetSum)) count++;
        }
    }

    return count;
}

bool canSplit(vector<long long>& prefixSum, int start, int k, long long remainingSum, long long targetSum) {
    if (k == 0) return remainingSum == 0;
    for (int i = start; i < prefixSum.size(); i++) {
        long long currentSum = prefixSum[i] - prefixSum[start];
        if (currentSum == targetSum) {
            if (canSplit(prefixSum, i, k - 1, remainingSum - targetSum, targetSum)) return true;
        }
        if (currentSum > targetSum) break;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of `nums`. This is because we iterate over all possible start indices for the first subarray and calculate the sum of the remaining array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we store the prefix sum array.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n^2 \cdot k)$, which is better than the brute force approach. This is because we use a prefix sum array to calculate the sum of each subarray in constant time.

---

### Final Notes

**Learning Points:**
- The problem requires generating all possible subarrays and checking if their sums are equal.
- The brute force approach has an exponential time complexity, while the optimal approach has a time complexity of $O(n^2 \cdot k)$.
- The use of a prefix sum array can significantly improve the time complexity of the solution.

**Mistakes to Avoid:**
- Not considering the case where the sum of `nums` is not divisible by `k`.
- Not using a prefix sum array to calculate the sum of each subarray in constant time.
- Not iterating over all possible start indices for the first subarray.
- Not using a hashmap to store the count of subarrays with a given sum.

**Similar Problems to Practice:**
- [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/)
- [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)