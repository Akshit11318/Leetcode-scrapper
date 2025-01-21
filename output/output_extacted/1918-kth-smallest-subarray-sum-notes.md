## Kth Smallest Subarray Sum
**Problem Link:** https://leetcode.com/problems/kth-smallest-subarray-sum/description

**Problem Statement:**
- Input: An integer array `nums` and two integers `k` and `target`.
- Constraints: $1 \leq nums.length \leq 100$, $1 \leq k \leq \frac{(100 \times 100)}{2}$, $1 \leq nums[i] \leq 100$, $1 \leq target \leq 10000$.
- Expected Output: The `kth` smallest sum of a subarray, if such a sum exists. Otherwise, return `-1`.
- Key Requirements: Find the `kth` smallest sum of all possible subarrays, considering all possible subarray lengths and positions within the array.
- Edge Cases: Handling cases where `k` exceeds the number of possible subarrays or when no subarray sum equals the target.

**Example Test Cases:**
- Example 1: `nums = [2,1,3]`, `k = 4`, `target = 7`. The smallest sums of subarrays are: `[2, 1, 3, 3, 4, 5, 6]`. The 4th smallest sum is 6, so return `6`.
- Example 2: `nums = [2,1,3]`, `k = 5`, `target = 7`. There are only 7 sums, and the 5th smallest is 7, so return `7`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible subarrays, calculate their sums, and then sort these sums to find the `kth` smallest.
- This approach involves iterating over all possible start and end indices for subarrays, calculating their sums, and storing these sums in a data structure like a vector.
- It comes to mind first because it directly addresses the problem statement without requiring complex optimizations.

```cpp
#include <vector>
#include <algorithm>

int kthSmallestSubarraySum(vector<int>& nums, int k, int target) {
    int n = nums.size();
    vector<int> sums;

    // Generate all possible subarray sums
    for (int start = 0; start < n; start++) {
        int sum = 0;
        for (int end = start; end < n; end++) {
            sum += nums[end];
            sums.push_back(sum);
        }
    }

    // Sort the sums
    sort(sums.begin(), sums.end());

    // Check if kth smallest sum exists and return it
    if (k <= sums.size()) {
        return sums[k-1];
    } else {
        return -1;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log(n^2))$ due to generating $n^2$ sums and sorting them. Here, $n$ is the size of the input array `nums`.
> - **Space Complexity:** $O(n^2)$ for storing all possible subarray sums in the `sums` vector.
> - **Why these complexities occur:** The brute force approach involves iterating over the array in a nested manner to generate all possible subarrays, leading to quadratic time complexity in generating sums. The sorting step adds a logarithmic factor to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a priority queue to efficiently find the `kth` smallest sum without needing to generate and sort all sums.
- This approach involves maintaining a priority queue of the smallest sums encountered so far, starting with sums of individual elements and iteratively expanding to larger subarrays.
- It is optimal because it avoids unnecessary computations and directly targets the `kth` smallest sum.

```cpp
#include <queue>
#include <vector>

int kthSmallestSubarraySum(vector<int>& nums, int k, int target) {
    int n = nums.size();
    priority_queue<int, vector<int>, greater<int>> pq;

    // Initialize with sums of individual elements
    for (int i = 0; i < n; i++) {
        pq.push(nums[i]);
    }

    // Expand to larger subarrays
    for (int i = 0; i < k - 1; i++) {
        int top = pq.top();
        pq.pop();

        for (int j = 0; j < n; j++) {
            if (top + nums[j] <= target) {
                pq.push(top + nums[j]);
            }
        }
    }

    // The kth smallest sum is at the top of the priority queue
    return pq.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk \log(nk))$ due to the priority queue operations and the loop over `k`.
> - **Space Complexity:** $O(nk)$ for storing elements in the priority queue.
> - **Optimality proof:** This approach is optimal because it directly targets the `kth` smallest sum without generating unnecessary sums, achieving a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated include the use of priority queues for efficient selection of the smallest elements.
- Problem-solving patterns identified include the importance of avoiding unnecessary computations and directly targeting the desired outcome.
- Optimization techniques learned include using data structures like priority queues to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of edge cases, such as when `k` exceeds the number of possible subarrays.
- Performance pitfalls include using inefficient algorithms that generate unnecessary sums, leading to high time complexity.
- Testing considerations include thoroughly testing the function with various inputs to ensure correctness and efficiency.