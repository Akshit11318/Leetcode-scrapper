## Count Subarrays Where Max Element Appears At Least K Times

**Problem Link:** https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

**Problem Statement:**
- Input: An integer array `nums` and two integers `k` and `maxCount`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= k <= nums.length`, and `1 <= maxCount <= nums.length`.
- Expected Output: The number of subarrays where the maximum element appears at least `k` times and the maximum element does not exceed `maxCount`.
- Key Requirements:
  - Count subarrays with specific conditions.
  - Handle edge cases such as empty arrays, `k` larger than the array length, and `maxCount` being 0 or larger than the array length.
- Example Test Cases:
  - `nums = [1, 2, 3, 4, 5], k = 2, maxCount = 3` should return the count of subarrays where the max element appears at least `k` times and does not exceed `maxCount`.

### Brute Force Approach

**Explanation:**
- Initial thought process: For every possible subarray, find the maximum element and count its occurrences.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, find the maximum element.
  3. Count the occurrences of the maximum element in the subarray.
  4. Check if the maximum element does not exceed `maxCount` and its occurrences are at least `k`.
- Why this approach comes to mind first: It's straightforward and ensures all cases are considered.

```cpp
int numberOfSubarrays(vector<int>& nums, int k, int maxCount) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            int maxElement = *max_element(subarray.begin(), subarray.end());
            if (maxElement > maxCount) continue;
            int maxCountInSubarray = count(subarray.begin(), subarray.end(), maxElement);
            if (maxCountInSubarray >= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ due to generating all subarrays ($O(n^2)$) and then finding the maximum element and counting its occurrences in each subarray ($O(n)$).
> - **Space Complexity:** $O(n)$ for storing each subarray.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate all possible subarrays and additional operations to find the maximum element and count its occurrences in each subarray.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all subarrays and then checking conditions, maintain a sliding window and update the count of the maximum element within the window.
- Detailed breakdown:
  1. Initialize the window boundaries and the count of the maximum element.
  2. Expand the window to the right and update the count of the maximum element.
  3. When the window size exceeds `n`, shrink the window from the left.
  4. Check the conditions (max element count and max element value) within the window and update the result.
- Proof of optimality: This approach ensures that each element is processed at most twice (once when entering the window and once when leaving), leading to a significant reduction in time complexity.

```cpp
int numberOfSubarrays(vector<int>& nums, int k, int maxCount) {
    int n = nums.size();
    int count = 0;
    for (int maxVal = 1; maxVal <= maxCount; maxVal++) {
        int left = 0, maxCountInWindow = 0;
        for (int right = 0; right < n; right++) {
            if (nums[right] == maxVal) maxCountInWindow++;
            while (maxCountInWindow >= k) {
                count++;
                if (nums[left] == maxVal) maxCountInWindow--;
                left++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot maxCount)$, as for each possible maximum value up to `maxCount`, we potentially traverse the array once.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space.
> - **Optimality proof:** The optimal approach reduces the time complexity by focusing on the maximum element within a sliding window and only considering relevant maximum values up to `maxCount`, making it more efficient than the brute force approach.

### Final Notes

**Learning Points:**
- The importance of sliding window techniques in array and string problems.
- How to optimize problems by focusing on key constraints (in this case, the maximum element and its count).
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering edge cases such as an empty input array or `k` being larger than the array length.
- Failing to optimize the solution by directly applying a brute force approach without considering the problem's constraints and potential simplifications.
- Not validating the input and handling potential errors.