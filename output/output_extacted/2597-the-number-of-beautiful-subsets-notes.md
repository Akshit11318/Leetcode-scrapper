## The Number of Beautiful Subsets
**Problem Link:** https://leetcode.com/problems/the-number-of-beautiful-subsets/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of size `n` and an integer `k`, find the number of beautiful subsets of size `k`.
- Expected output format: The number of beautiful subsets.
- Key requirements and edge cases to consider: A beautiful subset is defined as a subset where the difference between the maximum and minimum element is at most `1`.
- Example test cases with explanations: For example, if `nums = [1, 2, 3, 3]` and `k = 3`, then the number of beautiful subsets is `2`, which are `[1, 2, 3]` and `[2, 3, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of size `k` and check if each subset is beautiful.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of size `k` using a recursive approach or bit manipulation.
  2. For each subset, calculate the difference between the maximum and minimum element.
  3. If the difference is at most `1`, increment the count of beautiful subsets.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int beautifulSubsets(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    vector<int> subset(k);
    sort(nums.begin(), nums.end());
    
    function<void(int)> backtrack = [&](int start) {
        if (start == k) {
            int maxVal = subset[0];
            int minVal = subset[0];
            for (int i = 1; i < k; i++) {
                maxVal = max(maxVal, subset[i]);
                minVal = min(minVal, subset[i]);
            }
            if (maxVal - minVal <= 1) {
                count++;
            }
        } else {
            for (int i = start; i < n; i++) {
                subset[start] = nums[i];
                backtrack(start + 1);
            }
        }
    };
    
    backtrack(0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot n^{k-1})$, where $n$ is the size of the input array. This is because we generate all possible subsets of size `k` and check each subset.
> - **Space Complexity:** $O(k)$, where $k$ is the size of the subset. This is because we use a recursive approach to generate subsets.
> - **Why these complexities occur:** The time complexity is high because we generate all possible subsets, and the space complexity is low because we only need to store the current subset.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a bitmask to generate all possible subsets of size `k` and check if each subset is beautiful.
- Detailed breakdown of the approach:
  1. Initialize a bitmask `mask` to `0`.
  2. Iterate over all possible values of `mask` using a loop.
  3. For each `mask`, check if it represents a subset of size `k` by counting the number of set bits.
  4. If it does, calculate the maximum and minimum elements in the subset.
  5. If the difference between the maximum and minimum elements is at most `1`, increment the count of beautiful subsets.
- Proof of optimality: This approach is optimal because it generates all possible subsets of size `k` in a efficient way using a bitmask.

```cpp
#include <vector>
using namespace std;

int beautifulSubsets(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    sort(nums.begin(), nums.end());
    
    for (int mask = 0; mask < (1 << n); mask++) {
        int subsetSize = 0;
        int maxVal = INT_MIN;
        int minVal = INT_MAX;
        
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsetSize++;
                maxVal = max(maxVal, nums[i]);
                minVal = min(minVal, nums[i]);
            }
        }
        
        if (subsetSize == k && maxVal - minVal <= 1) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the size of the input array. This is because we iterate over all possible values of the bitmask.
> - **Space Complexity:** $O(1)$, where `k` is the size of the subset. This is because we only need to store the current subset.
> - **Optimality proof:** This approach is optimal because it generates all possible subsets of size `k` in a efficient way using a bitmask.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmask, subset generation, and subset checking.
- Problem-solving patterns identified: Using a bitmask to generate all possible subsets and checking each subset.
- Optimization techniques learned: Using a bitmask to generate subsets instead of recursive approach.
- Similar problems to practice: Other subset generation problems, such as finding the number of subsets with a given sum.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the size of the subset before checking if it is beautiful.
- Edge cases to watch for: Empty input array, `k` is greater than the size of the input array.
- Performance pitfalls: Using a recursive approach to generate subsets, which can lead to high time complexity.
- Testing considerations: Test the function with different input arrays and values of `k`.