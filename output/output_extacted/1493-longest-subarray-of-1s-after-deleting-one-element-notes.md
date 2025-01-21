## Longest Subarray of 1s After Deleting One Element

**Problem Link:** https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description

**Problem Statement:**
- Input: An array of integers `nums` containing only 0s and 1s.
- Output: The length of the longest subarray that can be achieved by deleting at most one element.
- Key requirements and edge cases to consider: The input array may contain zeros, and we can delete at most one element to maximize the subarray length.
- Example test cases:
  - Input: `nums = [1,1,0,1]`
    - Output: `3`
    - Explanation: We can delete the zero to get a subarray `[1,1,1]`.
  - Input: `nums = [0,1,1,1,0,1,1,0,1]`
    - Output: `5`
    - Explanation: We can delete one of the zeros to get a subarray `[1,1,1,1,1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible subarrays and check if deleting one element can make it a subarray of all ones.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array.
  2. For each subarray, try deleting each element and check if the remaining elements are all ones.
  3. Keep track of the maximum length of such a subarray.
- Why this approach comes to mind first: It is straightforward to think about generating all possible subarrays and checking each one, but this approach is inefficient due to its high time complexity.

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                vector<int> subarray = vector<int>(nums.begin() + i, nums.begin() + j + 1);
                for (int k = 0; k < subarray.size(); k++) {
                    vector<int> temp = subarray;
                    temp.erase(temp.begin() + k);
                    if (all_of(temp.begin(), temp.end(), [](int x) { return x == 1; })) {
                        maxLen = max(maxLen, (int)temp.size());
                    }
                }
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we generate all possible subarrays ($O(n^2)$) and for each subarray, we try deleting each element ($O(n)$).
> - **Space Complexity:** $O(n)$, as we store each subarray.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays and checking each one, resulting in high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to track the maximum length of a subarray with at most one zero.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Move the `right` pointer to the right and keep track of the number of zeros in the current window.
  3. If the number of zeros exceeds one, move the `left` pointer to the right until the number of zeros is at most one.
  4. Keep track of the maximum length of such a window.
- Why further optimization is impossible: The optimal approach has a time complexity of $O(n)$, which is the minimum required to scan the input array.

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        int left = 0;
        int zeros = 0;
        for (int right = 0; right < n; right++) {
            if (nums[right] == 0) {
                zeros++;
            }
            while (zeros > 1) {
                if (nums[left] == 0) {
                    zeros--;
                }
                left++;
            }
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen - 1; // subtract 1 because we can't delete an element from an array of all ones
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the pointers and the count of zeros.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, which is the minimum required to scan the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, two-pointer technique.
- Problem-solving patterns identified: Using a sliding window to track the maximum length of a subarray with certain properties.
- Optimization techniques learned: Reducing the time complexity by using a sliding window approach instead of generating all possible subarrays.
- Similar problems to practice: Longest Substring Without Repeating Characters, Minimum Window Substring.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as an empty input array.
- Edge cases to watch for: Input arrays with all zeros or all ones.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Test the solution with input arrays of varying sizes and compositions.