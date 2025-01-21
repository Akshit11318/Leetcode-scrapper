## Length of Longest Subarray with At Most K Frequency
**Problem Link:** https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= k <= 10^5`.
- Expected output format: The length of the longest subarray with at most `k` frequency.
- Key requirements and edge cases to consider: Handle empty arrays, arrays with a single element, and arrays with all elements having a frequency greater than `k`.
- Example test cases with explanations:
  - `nums = [1,2,1,2,3,2,2,1,2], k = 2`, the longest subarray with at most `k` frequency is `[1,2,1,2,3,2,2,1,2]`.
  - `nums = [1,2,1,2,1,2,1,2], k = 1`, the longest subarray with at most `k` frequency is `[1]` or `[2]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subarrays, calculate the frequency of each element in the subarray, and check if the maximum frequency is less than or equal to `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, calculate the frequency of each element.
  3. Check if the maximum frequency is less than or equal to `k`.
  4. Update the maximum length of the subarray if the current subarray meets the condition.
- Why this approach comes to mind first: It's a straightforward and intuitive approach, but it's not efficient due to the high number of subarrays and frequency calculations.

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int maxLength = 0;
        for (int i = 0; i < nums.size(); i++) {
            unordered_map<int, int> freq;
            for (int j = i; j < nums.size(); j++) {
                freq[nums[j]]++;
                if (freq[nums[j]] > k) {
                    break;
                }
                maxLength = max(maxLength, j - i + 1);
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we're generating all possible subarrays and calculating the frequency of each element in the subarray.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we're using a hash map to store the frequency of each element in the subarray.
> - **Why these complexities occur:** The high time complexity is due to the nested loops used to generate all possible subarrays, and the space complexity is due to the hash map used to store the frequency of each element.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach with a hash map to store the frequency of each element in the current window.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Use a hash map to store the frequency of each element in the current window.
  3. Move the `right` pointer to the right and update the frequency of the elements in the window.
  4. If the maximum frequency in the window exceeds `k`, move the `left` pointer to the right and update the frequency of the elements in the window.
  5. Update the maximum length of the subarray if the current window meets the condition.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and uses a hash map to store the frequency of each element in the current window.

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int maxLength = 0;
        int left = 0;
        unordered_map<int, int> freq;
        for (int right = 0; right < nums.size(); right++) {
            freq[nums[right]]++;
            while (freq[nums[right]] > k) {
                freq[nums[left]]--;
                if (freq[nums[left]] == 0) {
                    freq.erase(nums[left]);
                }
                left++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we're only making a single pass through the array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we're using a hash map to store the frequency of each element in the current window.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array and uses a hash map to store the frequency of each element in the current window, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, hash map usage, and frequency calculation.
- Problem-solving patterns identified: Using a sliding window approach to reduce the time complexity of the problem.
- Optimization techniques learned: Using a hash map to store the frequency of each element in the current window.
- Similar problems to practice: Other problems that involve finding the longest subarray with certain properties, such as the longest subarray with at most `k` distinct elements.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency of the elements in the window correctly, or not moving the `left` pointer correctly.
- Edge cases to watch for: Handling empty arrays, arrays with a single element, and arrays with all elements having a frequency greater than `k`.
- Performance pitfalls: Using a brute force approach that results in a high time complexity.
- Testing considerations: Testing the solution with different input arrays and values of `k` to ensure that it works correctly in all cases.