## Widest Pair of Indices with Equal Range Sum

**Problem Link:** https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/description

**Problem Statement:**
- Given a 0-indexed integer array `nums`, find the **widest** pair of indices `(left, right)` such that the sum of the elements in the range `[left, right]` is **equal**.
- Return the width of this pair, which is defined as `right - left`.
- If no such pair exists, return `0`.
- Input format and constraints:
  - `1 <= nums.length <= 10^5`
  - `-10^5 <= nums[i] <= 10^5`
- Expected output format:
  - A single integer representing the width of the widest pair of indices with equal range sum.

**Example Test Cases:**
- Input: `nums = [1, 2, 3, 4, 5]`
  - Output: `0`
- Input: `nums = [1, 1, 1, 1, 1]`
  - Output: `4`

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible pair of indices `(left, right)` in the array to see if the sum of the elements in the range `[left, right]` is equal to the sum of the elements in the range `[left, right]` when reversed.
- However, since we need to find the pair with the maximum width, we can simply compare each pair of indices and calculate the sum of the elements in between them.
- If the sums are equal, we update our maximum width if the current width is larger.

```cpp
class Solution {
public:
    int widestPairIndices(vector<int>& nums) {
        int n = nums.size();
        int maxWidth = 0;
        
        for (int left = 0; left < n; left++) {
            for (int right = left; right < n; right++) {
                int sum1 = 0, sum2 = 0;
                for (int i = left; i <= right; i++) {
                    sum1 += nums[i];
                }
                int j = right;
                for (int i = left; i <= right; i++) {
                    sum2 += nums[j--];
                }
                if (sum1 == sum2) {
                    maxWidth = max(maxWidth, right - left);
                }
            }
        }
        
        return maxWidth;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array. This is because for each pair of indices, we are calculating the sum of the elements in between them, which takes $O(n)$ time. The outer two loops also run in $O(n^2)$ time.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The high time complexity occurs because we are using a brute force approach, checking every possible pair of indices and calculating the sum of the elements in between them. The space complexity is low because we are only using a constant amount of space to store our variables.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that we don't need to calculate the sum of the elements in the range `[left, right]` for each pair of indices. Instead, we can use a prefix sum array to store the cumulative sum of the elements up to each index.
- We can then use a hash map to store the prefix sums we have seen so far and their corresponding indices.
- For each prefix sum, we check if we have seen it before. If we have, we update our maximum width if the current width is larger.
- This approach allows us to find the widest pair of indices with equal range sum in linear time.

```cpp
class Solution {
public:
    int widestPairIndices(vector<int>& nums) {
        int n = nums.size();
        int maxWidth = 0;
        unordered_map<int, int> prefixSums;
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (prefixSums.find(sum) != prefixSums.end()) {
                maxWidth = max(maxWidth, i - prefixSums[sum]);
            } else {
                prefixSums[sum] = i;
            }
        }
        
        return maxWidth;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are only iterating through the array once.
> - **Space Complexity:** $O(n)$, as we are using a hash map to store the prefix sums and their corresponding indices.
> - **Optimality proof:** This approach is optimal because we are only iterating through the array once and using a hash map to store the prefix sums, which allows us to find the widest pair of indices with equal range sum in linear time.

### Final Notes

**Learning Points:**
- The importance of using prefix sums to avoid recalculating sums for each pair of indices.
- The use of hash maps to store prefix sums and their corresponding indices, allowing for efficient lookups and updates.
- The trade-off between time and space complexity, as we are using extra space to store the prefix sums and their indices, but reducing the time complexity from $O(n^3)$ to $O(n)$.

**Mistakes to Avoid:**
- Not using prefix sums to avoid recalculating sums for each pair of indices, leading to high time complexity.
- Not using a hash map to store prefix sums and their corresponding indices, leading to inefficient lookups and updates.
- Not considering the trade-off between time and space complexity, leading to suboptimal solutions.