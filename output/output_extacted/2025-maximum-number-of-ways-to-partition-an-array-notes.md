## Maximum Number of Ways to Partition an Array
**Problem Link:** https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 10^6`, and `1 <= k <= 10^9`.
- Expected Output: The maximum number of ways to partition `nums` into two non-empty arrays such that the sum of elements in each array is at most `k`.
- Key Requirements and Edge Cases: The arrays must be non-empty, and the sum of elements in each array must not exceed `k`.

**Example Test Cases:**
- `nums = [1, 2, 3, 4], k = 5`: The maximum number of ways is 2 (`[1, 4]` and `[2, 3]` or `[1, 2]` and `[3, 4]`).
- `nums = [1, 2, 3, 4], k = 6`: The maximum number of ways is 4 (`[1, 5]`, `[2, 4]`, `[1, 2, 3]`, and `[4]` or `[1, 2, 4]`, `[3]` or `[1, 3, 4]`, `[2]` or `[1, 4]`, `[2, 3]`).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible partitions of the input array and check if the sum of elements in each partition does not exceed `k`.
- The brute force approach involves generating all possible subsets of the input array and checking if the sum of elements in each subset does not exceed `k`.
- This approach comes to mind first because it is straightforward and does not require any additional insights or techniques.

```cpp
class Solution {
public:
    int waysToPartition(vector<int>& nums, int k) {
        int n = nums.size();
        int maxWays = 0;
        // Generate all possible subsets
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> subset;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    subset.push_back(nums[i]);
                }
            }
            // Check if the sum of elements in the subset does not exceed k
            int sum = 0;
            for (int num : subset) {
                sum += num;
            }
            if (sum <= k) {
                // Check if the sum of elements in the remaining subset does not exceed k
                int remainingSum = 0;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) == 0) {
                        remainingSum += nums[i];
                    }
                }
                if (remainingSum <= k) {
                    maxWays++;
                }
            }
        }
        return maxWays;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible subsets of the input array and check if the sum of elements in each subset does not exceed `k`.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we store the current subset in a vector.
> - **Why these complexities occur:** The time complexity is high because we generate all possible subsets of the input array, which has a time complexity of $O(2^n)$. The space complexity is low because we only store the current subset in a vector.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a prefix sum array to store the cumulative sum of elements in the input array.
- We can then use a hashmap to store the frequency of each prefix sum.
- The optimal approach involves iterating over the input array and updating the frequency of each prefix sum in the hashmap.
- We can then use the hashmap to find the maximum number of ways to partition the input array such that the sum of elements in each array does not exceed `k`.

```cpp
class Solution {
public:
    int waysToPartition(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        unordered_map<int, int> freq;
        for (int i = 0; i <= n; i++) {
            freq[prefixSum[i]]++;
        }
        int maxWays = 0;
        for (int i = 1; i <= n; i++) {
            int sum = prefixSum[i];
            if (sum <= k) {
                maxWays += freq[prefixSum[n] - sum];
            }
        }
        return maxWays;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we iterate over the input array once to update the frequency of each prefix sum in the hashmap.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we store the frequency of each prefix sum in a hashmap.
> - **Optimality proof:** The time complexity is optimal because we only iterate over the input array once. The space complexity is optimal because we only store the frequency of each prefix sum in a hashmap.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum array, hashmap, and frequency counting.
- Problem-solving patterns identified: using a hashmap to store frequency of each prefix sum.
- Optimization techniques learned: using a prefix sum array to reduce time complexity.
- Similar problems to practice: problems involving prefix sum arrays and hashmap.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the frequency of each prefix sum in the hashmap.
- Edge cases to watch for: handling cases where the sum of elements in each array exceeds `k`.
- Performance pitfalls: using a brute force approach instead of an optimal approach.
- Testing considerations: testing cases with large input arrays and large values of `k`.