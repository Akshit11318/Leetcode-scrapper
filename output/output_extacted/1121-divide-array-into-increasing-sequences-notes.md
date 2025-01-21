## Divide Array into Increasing Sequences

**Problem Link:** https://leetcode.com/problems/divide-array-into-increasing-sequences/description

**Problem Statement:**
- Input: A list of integers `nums`.
- Output: The length of the longest increasing subsequence of `nums`.
- Key requirements: 
    - A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
    - An increasing subsequence is one where every element is greater than its previous element.
- Example test cases: 
    - Input: `nums = [1,2]`, Output: `1`
    - Input: `nums = [1,2,3]`, Output: `1`
    - Input: `nums = [1,3,5,4,7]`, Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences and check if they are increasing.
- We can use recursion or bit manipulation to generate all subsequences.
- For each subsequence, we check if it's increasing by comparing adjacent elements.

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> nums(n + 1, 0);
        for (int i = 0; i < ranges.size(); i++) {
            int left = max(0, i - ranges[i]);
            int right = min(n, i + ranges[i]);
            nums[left] = max(nums[left], right);
        }
        int cnt = 0, pre = 0, far = 0;
        for (int i = 0; i < n; i++) {
            far = max(far, nums[i]);
            if (i == pre) {
                cnt++;
                pre = far;
            }
        }
        return cnt;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because we're generating all possible subsequences, which has exponential time complexity.
> - **Space Complexity:** $O(2^n)$, as we're storing all subsequences in memory.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible subsequences, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the length of the longest increasing subsequence ending at each position.
- We initialize an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`.
- We iterate through the array and update `dp[i]` if we find a smaller element that can extend the increasing subsequence.

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> nums(n + 1, 0);
        for (int i = 0; i < ranges.size(); i++) {
            int left = max(0, i - ranges[i]);
            int right = min(n, i + ranges[i]);
            nums[left] = max(nums[left], right);
        }
        int cnt = 0, pre = 0, far = 0;
        for (int i = 0; i < n; i++) {
            far = max(far, nums[i]);
            if (i == pre) {
                cnt++;
                pre = far;
            }
        }
        return cnt;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we're iterating through the array once.
> - **Space Complexity:** $O(n)$, as we're storing the `dp` array in memory.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the length of the longest increasing subsequence ending at each position, which avoids redundant computation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, greedy algorithm.
- Problem-solving patterns identified: using dynamic programming to store the length of the longest increasing subsequence ending at each position.
- Optimization techniques learned: avoiding redundant computation by storing intermediate results.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the `dp` array, incorrect update of the `dp` array.
- Edge cases to watch for: empty input array, array with a single element.
- Performance pitfalls: using a brute force approach, not using dynamic programming to store intermediate results.
- Testing considerations: testing with large input arrays, testing with arrays containing duplicate elements.