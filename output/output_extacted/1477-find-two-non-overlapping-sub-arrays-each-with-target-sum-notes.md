## Find Two Non-Overlapping Sub-Arrays Each with Target Sum

**Problem Link:** https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description

**Problem Statement:**
- Input: An integer array `nums` and a target integer `target`.
- Constraints: `2 <= nums.length <= 10^5`, `-1 <= nums[i] <= 1`, and `1 <= target <= 10^6`.
- Expected Output: The length of the shortest subarray that has a sum equal to `target` and the length of the shortest subarray that starts after the first subarray and also has a sum equal to `target`. If no such subarrays exist, return `-1`.
- Key Requirements: Find two non-overlapping subarrays, each with a sum equal to `target`.
- Example Test Cases:
  - Example 1: `nums = [1,3,2,1,3,4,1,3,4,1,3,4], target = 6`
    - Output: `3`
    - Explanation: The two subarrays are `[3,1,3]` and `[4,1,3]`.
  - Example 2: `nums = [7,3,1,5,4,8], target = 8`
    - Output: `1`
    - Explanation: The two subarrays are `[8]` and `[8]`.
  - Example 3: `nums = [4,3,2,6,2,3,4], target = 6`
    - Output: `-1`
    - Explanation: There are no two subarrays with sum `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can use a brute force approach by iterating over all possible subarrays and checking if their sum equals `target`.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible subarrays.
  2. For each subarray, calculate its sum.
  3. Check if the sum equals `target`.
  4. If it does, store the subarray's length.
  5. Repeat steps 1-4 to find the second subarray.
  6. If both subarrays are found and do not overlap, return their lengths.

```cpp
int minSumOfLengths(vector<int>& nums, int target) {
    int n = nums.size();
    int min_len = INT_MAX;
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            if (sum == target) {
                int len1 = j - i + 1;
                for (int k = j + 1; k < n; k++) {
                    int sum2 = 0;
                    for (int l = k; l < n; l++) {
                        sum2 += nums[l];
                        if (sum2 == target) {
                            int len2 = l - k + 1;
                            min_len = min(min_len, len1 + len2);
                        }
                    }
                }
            }
        }
    }
    return min_len == INT_MAX ? -1 : min_len;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$
> - **Space Complexity:** $O(1)$
> - **Why these complexities occur:** The brute force approach involves four nested loops, resulting in a time complexity of $O(n^4)$. The space complexity is $O(1)$ because we only use a constant amount of space to store the minimum length.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a prefix sum array to efficiently calculate the sum of any subarray.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array.
  2. Initialize a hashmap to store the shortest subarray length for each prefix sum.
  3. Iterate over the prefix sum array to find the shortest subarray with sum `target`.
  4. For each subarray found, check if there is another non-overlapping subarray with sum `target`.
  5. Update the minimum length if a shorter combination is found.

```cpp
int minSumOfLengths(vector<int>& nums, int target) {
    int n = nums.size();
    int min_len = INT_MAX;
    vector<int> prefix_sum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefix_sum[i + 1] = prefix_sum[i] + nums[i];
    }
    vector<int> shortest(n + 1, INT_MAX);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            int sum = prefix_sum[j] - prefix_sum[i];
            if (sum == target) {
                shortest[j] = min(shortest[j], j - i);
            }
        }
    }
    for (int i = 1; i < n; i++) {
        if (shortest[i] != INT_MAX && shortest[i + 1] != INT_MAX) {
            min_len = min(min_len, shortest[i] + shortest[i + 1]);
        }
    }
    return min_len == INT_MAX ? -1 : min_len;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$
> - **Space Complexity:** $O(n)$
> - **Optimality proof:** This approach is optimal because we only need to iterate over the prefix sum array once to find all possible subarrays with sum `target`, and then iterate over the shortest subarray lengths to find the minimum combination. This reduces the time complexity from $O(n^4)$ to $O(n^2)$.