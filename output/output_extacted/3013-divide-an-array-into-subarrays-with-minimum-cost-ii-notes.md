## Divide Array Into Chunks to Minimize Maximum Sum
**Problem Link:** https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description

**Problem Statement:**
- Given an array `nums` and an integer `k`, divide the array into `k` non-empty subarrays such that the maximum sum of the subarrays is minimized.
- Input: `nums = [1,2,3,4,5]`, `k = 2`
- Output: `9`
- Key requirements: The array must be divided into exactly `k` subarrays.
- Example test cases:
  - `nums = [1,2,3,4,5]`, `k = 2`, output: `9`
  - `nums = [1,2,3,4,5]`, `k = 3`, output: `6`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible combinations of subarrays and calculating the maximum sum for each combination.
- The brute force approach involves using recursion to generate all possible combinations of subarrays.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        function<int(int, int)> dfs = [&](int start, int groups) {
            if (start == n) {
                return groups == 0 ? 0 : INT_MAX;
            }
            if (groups == 0) {
                return INT_MAX;
            }
            int res = INT_MAX;
            int sum = 0;
            for (int i = start; i < n; i++) {
                sum += nums[i];
                res = min(res, max(sum, dfs(i + 1, groups - 1)));
            }
            return res;
        };
        
        return dfs(0, k);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^k)$, where $n$ is the number of elements in the array. This is because in the worst case, we are generating all possible combinations of subarrays.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are using a recursive function call stack to store the intermediate results.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of subarrays, which results in an exponential time complexity. The space complexity is linear due to the recursive function call stack.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a binary search approach to find the minimum maximum sum.
- We can use a binary search approach to find the minimum maximum sum by maintaining a search range `[low, high]`, where `low` is the minimum possible maximum sum and `high` is the maximum possible maximum sum.
- We can calculate the minimum possible maximum sum by dividing the total sum of the array by `k`, and the maximum possible maximum sum by taking the maximum element of the array.
- We can then use a binary search approach to find the minimum maximum sum within the search range.

```cpp
class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        int low = *max_element(nums.begin(), nums.end());
        int high = accumulate(nums.begin(), nums.end(), 0);
        
        function<bool(int)> check = [&](int mid) {
            int groups = 1;
            int sum = 0;
            for (int num : nums) {
                sum += num;
                if (sum > mid) {
                    groups++;
                    sum = num;
                }
            }
            return groups <= k;
        };
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log S)$, where $n$ is the number of elements in the array and $S$ is the sum of all elements in the array. This is because we are using a binary search approach to find the minimum maximum sum.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in the array. This is because we are not using any extra space that scales with the input size.
> - **Optimality proof:** The binary search approach is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: binary search, recursive functions.
- Problem-solving patterns identified: using a search range to find the minimum maximum sum.
- Optimization techniques learned: reducing the search space using a binary search approach.
- Similar problems to practice: [LeetCode 410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/).

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty array or `k` being greater than the number of elements in the array.
- Edge cases to watch for: the array being empty, `k` being greater than the number of elements in the array.
- Performance pitfalls: using a brute force approach, which results in an exponential time complexity.
- Testing considerations: testing the function with different inputs, such as an empty array, an array with a single element, and an array with multiple elements.