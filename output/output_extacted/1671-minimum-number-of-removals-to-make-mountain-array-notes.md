## Minimum Number of Removals to Make Mountain Array

**Problem Link:** https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 1000$, $1 \leq nums[i] \leq 1000$.
- Expected output format: The minimum number of elements to remove to make `nums` a mountain array.
- Key requirements: A mountain array is an array that increases and then decreases. After increasing, it must decrease. It cannot decrease after increasing, then increase again.
- Example test cases:
  - Input: `nums = [2,1,1,5,6,2,3,1]`
    - Output: `3`
    - Explanation: Remove the elements 1 at index 1 and 2, and the element 3 at index 6 to get a mountain array `[2,5,6,2,1]`.
  - Input: `nums = [4,3,2,1,1,2,3]`
    - Output: `4`
    - Explanation: Remove the first four elements to get a mountain array `[1,2,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of elements to remove and check if the remaining array is a mountain array.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the input array.
  2. For each subset, check if it is a mountain array.
  3. If it is a mountain array, calculate the number of elements removed to get this subset.
  4. Keep track of the minimum number of elements removed.
- Why this approach comes to mind first: It is a straightforward approach that considers all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isMountainArray(vector<int>& nums) {
    int n = nums.size();
    if (n < 3) return false;
    int i = 0;
    // Find the peak
    while (i < n - 1 && nums[i] < nums[i + 1]) i++;
    if (i == 0 || i == n - 1) return false;
    // Check if it decreases after the peak
    while (i < n - 1 && nums[i] > nums[i + 1]) i++;
    return i == n - 1;
}

int minimumRemovals(vector<int>& nums) {
    int n = nums.size();
    int minRemovals = n;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) subset.push_back(nums[i]);
        }
        if (isMountainArray(subset)) {
            int removals = n - subset.size();
            minRemovals = min(minRemovals, removals);
        }
    }
    return minRemovals;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible subsets of the input array and check each subset.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we need to store the subset of the input array.
> - **Why these complexities occur:** These complexities occur because we are generating all possible subsets of the input array, which has a time complexity of $O(2^n)$, and then checking each subset, which has a time complexity of $O(n)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible subsets, we can use dynamic programming to find the longest increasing and decreasing subsequences.
- Detailed breakdown of the approach:
  1. Find the longest increasing subsequence ending at each position.
  2. Find the longest decreasing subsequence starting at each position.
  3. For each position, calculate the length of the mountain array that can be formed by combining the increasing and decreasing subsequences.
  4. Keep track of the maximum length of the mountain array.
- Proof of optimality: This approach is optimal because it considers all possible mountain arrays that can be formed by removing elements from the input array.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minimumRemovals(vector<int>& nums) {
    int n = nums.size();
    vector<int> increase(n, 1);
    vector<int> decrease(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) increase[i] = max(increase[i], increase[j] + 1);
        }
    }
    for (int i = n - 2; i >= 0; i--) {
        for (int j = n - 1; j > i; j--) {
            if (nums[i] > nums[j]) decrease[i] = max(decrease[i], decrease[j] + 1);
        }
    }
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        maxLen = max(maxLen, increase[i] + decrease[i] - 1);
    }
    return n - maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are using two nested loops to find the longest increasing and decreasing subsequences.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we need to store the lengths of the increasing and decreasing subsequences.
> - **Optimality proof:** This approach is optimal because it considers all possible mountain arrays that can be formed by removing elements from the input array, and it does so in a time complexity that is polynomial in the length of the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, longest increasing and decreasing subsequences.
- Problem-solving patterns identified: Using dynamic programming to find the optimal solution.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity of the solution.
- Similar problems to practice: Finding the longest increasing subsequence, finding the longest decreasing subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible mountain arrays, not using dynamic programming to reduce the time complexity.
- Edge cases to watch for: Input arrays with duplicate elements, input arrays with a length of 1 or 2.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different input arrays, testing the solution with edge cases.