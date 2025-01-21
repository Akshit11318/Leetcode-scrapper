## Maximum Subarray Sum with Length Divisible by K

**Problem Link:** https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description

**Problem Statement:**
- Given an array `nums` of integers and an integer `k`, find the maximum sum of a subarray with a length that is divisible by `k`.
- Input constraints: `1 <= nums.length <= 10^5` and `1 <= k <= nums.length`.
- Expected output: The maximum sum of a subarray with a length divisible by `k`.
- Key requirements: The subarray must have a length that is a multiple of `k`.
- Edge cases: Consider arrays with negative numbers, arrays with all positive numbers, and cases where `k` is 1 or equal to the length of the array.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible subarrays of `nums` and calculating their sums.
- For each subarray, we check if its length is divisible by `k`.
- If it is, we update our maximum sum if the current subarray's sum is larger.

```cpp
class Solution {
public:
    int maxSubarraySumK(vector<int>& nums, int k) {
        int maxSum = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                int sum = 0;
                for (int l = i; l <= j; l++) {
                    sum += nums[l];
                }
                if ((j - i + 1) % k == 0) {
                    maxSum = max(maxSum, sum);
                }
            }
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because we have three nested loops: one for the start of the subarray, one for the end, and one to calculate the sum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum.
> - **Why these complexities occur:** The brute force approach involves checking all possible subarrays, which leads to the cubic time complexity due to the nested loops.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array to efficiently calculate the sum of any subarray in $O(1)$ time.
- We then use a hash map to store the prefix sums modulo `k` and their corresponding indices.
- For each prefix sum, we check if there exists a previous prefix sum that is equal to the current prefix sum modulo `k`. If so, we update our maximum sum.

```cpp
class Solution {
public:
    int maxSubarraySumK(vector<int>& nums, int k) {
        int maxSum = INT_MIN;
        int prefixSum = 0;
        unordered_map<int, int> prefixSums;
        prefixSums[0] = -1; // Base case for sum starting from index 0
        for (int i = 0; i < nums.size(); i++) {
            prefixSum += nums[i];
            int remainder = prefixSum % k;
            if (prefixSums.find(remainder) != prefixSums.end()) {
                maxSum = max(maxSum, prefixSum - (prefixSums[remainder] == -1 ? 0 : prefixSums[remainder]));
            } else {
                prefixSums[remainder] = prefixSum;
            }
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every prefix sum in the hash map.
> - **Optimality proof:** This approach is optimal because we only make a single pass through the array, and for each element, we perform a constant amount of work.

---

### Final Notes

**Learning Points:**
- The importance of using prefix sums to efficiently calculate subarray sums.
- The utility of hash maps in storing and retrieving values in constant time.
- The concept of using modulo arithmetic to reduce the search space.

**Mistakes to Avoid:**
- Not considering the use of prefix sums to simplify the calculation of subarray sums.
- Not using a hash map to store and retrieve prefix sums modulo `k`.
- Not handling edge cases, such as when `k` is 1 or equal to the length of the array.