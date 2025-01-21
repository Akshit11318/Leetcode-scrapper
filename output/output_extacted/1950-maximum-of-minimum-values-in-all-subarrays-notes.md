## Maximum of Minimum Values in All Subarrays

**Problem Link:** https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, return the maximum of the minimum values in all subarrays of size `k`.
- Input format and constraints: `nums` is an array of integers, and `k` is an integer where `1 <= k <= nums.size()`.
- Expected output format: The maximum of the minimum values in all subarrays of size `k`.
- Key requirements and edge cases to consider: Handling edge cases where `k` equals `1` or `nums.size()`, and ensuring the solution works for arrays of varying lengths.
- Example test cases with explanations:
  - For `nums = [1, 3, 2]` and `k = 2`, the subarrays are `[1, 3]` and `[3, 2]`. The minimum values are `1` and `2`, respectively. Thus, the maximum of these minimum values is `2`.
  - For `nums = [1, 2, 3, 4, 5]` and `k = 3`, the subarrays are `[1, 2, 3]`, `[2, 3, 4]`, and `[3, 4, 5]`. The minimum values are `1`, `2`, and `3`, respectively. Thus, the maximum of these minimum values is `3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray of size `k` within the given array `nums`.
- For each subarray, find the minimum value.
- Keep track of the maximum of these minimum values across all subarrays.
- This approach comes to mind first because it directly addresses the problem statement by examining every subarray.

```cpp
#include <vector>
#include <algorithm>

int maximumOfMinimumValuesInAllSubarrays(std::vector<int>& nums, int k) {
    int maxMin = INT_MIN;
    for (int i = 0; i <= nums.size() - k; ++i) {
        int minVal = INT_MAX;
        for (int j = i; j < i + k; ++j) {
            minVal = std::min(minVal, nums[j]);
        }
        maxMin = std::max(maxMin, minVal);
    }
    return maxMin;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of `nums`, because for each starting index `i`, we potentially scan `k` elements to find the minimum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum minimum value and the current minimum value for each subarray.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, and the lack of additional data structures beyond a few variables results in the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to efficiently calculate the minimum values of subarrays.
- Maintain a window of size `k` and slide it over the array, updating the minimum value within the window as we move.
- This approach is optimal because it avoids redundant calculations by only considering each element as it enters or leaves the window.
- Proof of optimality: This approach has a linear time complexity because each element is visited at most twice (once when entering the window and once when leaving), making it the most efficient possible solution given the need to examine each element.

```cpp
#include <vector>
#include <algorithm>

int maximumOfMinimumValuesInAllSubarrays(std::vector<int>& nums, int k) {
    int maxMin = INT_MIN;
    int windowMin = INT_MAX;
    for (int i = 0; i < nums.size(); ++i) {
        // Update windowMin for the current window
        if (i >= k) {
            if (nums[i - k] == windowMin) {
                windowMin = *std::min_element(nums.begin() + i - k + 1, nums.begin() + i + 1);
            }
        }
        windowMin = std::min(windowMin, nums[i]);
        
        // Update maxMin if we've completed a window of size k
        if (i >= k - 1) {
            maxMin = std::max(maxMin, windowMin);
        }
    }
    return maxMin;
}
```

However, a simpler and more efficient implementation using the sliding window concept and `std::deque` for tracking the minimum values within the window can be achieved:

```cpp
#include <vector>
#include <deque>
#include <algorithm>

int maximumOfMinimumValuesInAllSubarrays(std::vector<int>& nums, int k) {
    std::deque<int> dq;
    int maxMin = INT_MIN;
    
    for (int i = 0; i < nums.size(); ++i) {
        // Remove elements from the back of dq that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }
        
        // Remove elements from the back of dq that are larger than the current element
        while (!dq.empty() && nums[dq.back()] > nums[i]) {
            dq.pop_back();
        }
        
        // Add the current element to the back of dq
        dq.push_back(i);
        
        // Update maxMin if we've completed a window of size k
        if (i >= k - 1) {
            maxMin = std::max(maxMin, nums[dq.front()]);
        }
    }
    return maxMin;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because each element is pushed and popped from the deque exactly once.
> - **Space Complexity:** $O(k)$, for storing the indices of the elements in the deque.
> - **Optimality proof:** This is the most efficient solution because it only requires a single pass through the array and uses a deque to efficiently track the minimum value within the sliding window.

---

### Final Notes

**Learning Points:**
- The importance of the sliding window technique for problems involving subarrays.
- How to use `std::deque` for efficiently tracking the minimum or maximum values within a window.
- The trade-off between brute force and optimal solutions in terms of complexity and readability.

**Mistakes to Avoid:**
- Failing to consider edge cases, such as when `k` equals `1` or `nums.size()`.
- Not optimizing the solution for the specific constraints of the problem.
- Overcomplicating the solution with unnecessary data structures or algorithms.
- Not testing the solution thoroughly with different input sizes and edge cases.