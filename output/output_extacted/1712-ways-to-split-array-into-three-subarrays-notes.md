## Ways to Split Array into Three Subarrays
**Problem Link:** https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: The number of ways to split the array into three non-empty subarrays such that the sum of elements in each subarray is equal.
- Constraints: The length of the array `nums` is between 3 and 10^5.
- Expected Output: The number of ways to split the array into three subarrays with equal sums.

**Key Requirements and Edge Cases:**
- The array must be split into exactly three non-empty subarrays.
- The sum of elements in each subarray must be equal.
- The order of elements within each subarray does not matter.
- The input array may contain duplicate elements.

**Example Test Cases:**
- `nums = [0,2,1,-6,6,-7,9,1,2,0,1]`: The output should be `10`.
- `nums = [0,2,1,-6,6,7,9,-1,2,0,1]`: The output should be `0`.
- `nums = [3,2,1]`: The output should be `1`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible ways to split the array into three subarrays and check if the sums of elements in each subarray are equal.
- This approach involves iterating over all possible split points and calculating the sums of elements in each subarray.

```cpp
int waysToSplit(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 1; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int sum1 = 0, sum2 = 0, sum3 = 0;
            for (int k = 0; k < i; k++) sum1 += nums[k];
            for (int k = i; k < j; k++) sum2 += nums[k];
            for (int k = j; k < n; k++) sum3 += nums[k];
            if (sum1 == sum2 && sum2 == sum3) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops: two loops to iterate over all possible split points, and one loop to calculate the sum of elements in each subarray.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of ways to split the array.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible ways to split the array, resulting in a cubic number of operations. The space complexity is low because we only need to store a single variable to count the number of ways to split the array.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to calculate the prefix sum of the array, which allows us to calculate the sum of elements in each subarray in constant time.
- We then iterate over all possible split points and check if the sums of elements in each subarray are equal.

```cpp
int waysToSplit(vector<int>& nums) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + nums[i];
    int count = 0;
    for (int i = 1; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int sum1 = prefixSum[i], sum2 = prefixSum[j] - prefixSum[i], sum3 = prefixSum[n] - prefixSum[j];
            if (sum1 == sum2 && sum2 == sum3) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we have two nested loops: one loop to iterate over all possible split points, and one loop to calculate the sum of elements in each subarray.
> - **Space Complexity:** $O(n)$, as we need to store the prefix sum of the array.
> - **Optimality proof:** This approach is optimal because we have reduced the time complexity from $O(n^3)$ to $O(n^2)$, and we cannot do better than this because we need to iterate over all possible split points to find the correct splits.

---

### Final Notes

**Learning Points:**
- The importance of calculating prefix sums to reduce the time complexity of the algorithm.
- How to iterate over all possible split points to find the correct splits.
- The trade-off between time and space complexity in the optimal approach.

**Mistakes to Avoid:**
- Not calculating the prefix sum of the array, resulting in a high time complexity.
- Not checking if the sums of elements in each subarray are equal, resulting in incorrect results.
- Not considering the edge cases, such as an empty input array or an array with a single element.