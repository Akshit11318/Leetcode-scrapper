## Minimum Time to Make Array Sum at Most X

**Problem Link:** https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `x`.
- Expected output: The minimum number of operations required to make the sum of the array at most `x`.
- Key requirements: Each operation can either be adding `1` to an element or subtracting `1` from an element in the array.
- Edge cases: The input array can be empty, and `x` can be less than `0`.

**Example Test Cases:**

- `nums = [1, 2, 3], x = 6`: The array sum is `6`, which is already at most `x`, so the minimum time is `0`.
- `nums = [1, 2, 3], x = 5`: To make the sum at most `5`, we need to subtract `1` from the last element, so the minimum time is `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of adding or subtracting `1` from each element in the array until the sum is at most `x`.
- We use a recursive approach to explore all possible combinations.

```cpp
#include <vector>
#include <numeric>

class Solution {
public:
    int minTime(std::vector<int>& nums, int x) {
        std::sort(nums.begin(), nums.end());
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        if (sum <= x) return 0;
        
        int res = INT_MAX;
        dfs(nums, 0, sum, 0, x, res);
        return res;
    }
    
    void dfs(std::vector<int>& nums, int idx, int sum, int time, int x, int& res) {
        if (idx == nums.size() || time >= res) return;
        if (sum <= x) {
            res = std::min(res, time);
            return;
        }
        
        // Try subtracting 1 from the current element
        if (nums[idx] > 0) {
            nums[idx]--;
            dfs(nums, idx, sum - 1, time + 1, x, res);
            nums[idx]++;
        }
        
        // Move to the next element
        dfs(nums, idx + 1, sum, time, x, res);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the array. This is because we try all possible combinations of adding or subtracting `1` from each element.
> - **Space Complexity:** $O(n)$, which is the maximum recursion depth.
> - **Why these complexities occur:** The recursive approach tries all possible combinations, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach, where we always subtract `1` from the largest element in the array until the sum is at most `x`.
- We use a priority queue to efficiently find the largest element in the array.

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    int minTime(std::vector<int>& nums, int x) {
        std::priority_queue<int> pq;
        for (int num : nums) pq.push(num);
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        int time = 0;
        
        while (sum > x) {
            int maxVal = pq.top();
            pq.pop();
            sum -= maxVal;
            maxVal--;
            sum += maxVal;
            pq.push(maxVal);
            time++;
        }
        
        return time;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + k \log n)$, where $n$ is the number of elements in the array and $k$ is the number of operations required. This is because we use a priority queue to find the largest element in the array.
> - **Space Complexity:** $O(n)$, which is the space required by the priority queue.
> - **Optimality proof:** This approach is optimal because we always subtract `1` from the largest element in the array, which minimizes the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy approach, priority queue.
- Problem-solving patterns identified: always try to minimize the number of operations required.
- Optimization techniques learned: use a priority queue to efficiently find the largest element in the array.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty array or `x` less than `0`.
- Edge cases to watch for: an empty array, `x` less than `0`, or an array with all elements equal to `0`.
- Performance pitfalls: using a recursive approach without memoization, which can result in exponential time complexity.
- Testing considerations: test the solution with different input arrays and values of `x`.