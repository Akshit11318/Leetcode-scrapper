## Split Array into Maximum Number of Subarrays
**Problem Link:** https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/description

**Problem Statement:**
- Input: An array of integers `nums` and an array of integers `left` and `right`, where `left[i]` and `right[i]` represent the range of indices for the `i-th` subarray.
- Constraints: `1 <= nums.length <= 10^4`, `nums.length == left.length == right.length`, `0 <= left[i] < right[i] < nums.length`.
- Expected Output: The maximum number of subarrays that can be split from the given array `nums` based on the given `left` and `right` indices.
- Key Requirements:
  - The subarrays must not overlap.
  - Each subarray must be a valid range within the `nums` array as defined by `left` and `right`.
- Edge Cases:
  - When `left[i]` is equal to `right[i]`, it means the subarray has only one element.
  - When `left[i]` is greater than `right[i]`, it's an invalid input.
- Example Test Cases:
  - `nums = [1, 2, 3, 4, 5], left = [0, 1, 1], right = [2, 2, 3]`. The maximum number of subarrays is 2 because we can split the array into `[1, 2, 3]` and `[2, 3, 4]`, but these overlap, so we actually consider non-overlapping ranges like `[1, 2]` and `[3, 4, 5]`, which gives us 2 subarrays.
  - `nums = [1, 2, 3], left = [0, 0], right = [1, 2]`. The maximum number of subarrays is 2, considering ranges `[1, 2]` and `[3]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible combination of non-overlapping subarrays.
- We generate all possible subarrays based on `left` and `right` indices and then filter out the overlapping ones.
- This approach comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxNumOfSubarrays(std::vector<int>& nums, std::vector<int>& left, std::vector<int>& right) {
        int n = nums.size();
        int maxSubarrays = 0;
        
        // Generate all possible subarrays
        for (int mask = 1; mask < (1 << n); ++mask) {
            std::vector<std::pair<int, int>> subarrays;
            bool isValid = true;
            
            // Check each bit in the mask to decide whether to include the element in the current subarray
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    // If the bit is set, add the element to the current subarray
                    if (subarrays.empty() || subarrays.back().second + 1 == i) {
                        if (subarrays.empty()) {
                            subarrays.push_back({i, i});
                        } else {
                            subarrays.back().second = i;
                        }
                    } else {
                        // If the element cannot be added to the current subarray, start a new subarray
                        subarrays.push_back({i, i});
                    }
                }
            }
            
            // Check if the subarrays are valid based on left and right indices
            for (int i = 0; i < subarrays.size(); ++i) {
                if (subarrays[i].first < left[i] || subarrays[i].second > right[i]) {
                    isValid = false;
                    break;
                }
            }
            
            // Update maxSubarrays if the current combination is valid and has more subarrays
            if (isValid && subarrays.size() > maxSubarrays) {
                maxSubarrays = subarrays.size();
            }
        }
        
        return maxSubarrays;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in `nums`. This is because we generate all possible subsets of the array (which is $2^n$) and for each subset, we potentially iterate through all elements to check for validity.
> - **Space Complexity:** $O(n)$, as we store the subarrays generated from the mask.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of subarrays and checking each for validity, leading to exponential time complexity. The space complexity is linear due to the storage of subarrays.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to recognize that this problem can be solved using a greedy approach, focusing on maximizing the number of non-overlapping subarrays.
- We iterate through the `left` and `right` indices, keeping track of the end of the last selected subarray. We always choose the subarray that ends earliest and does not overlap with previously selected subarrays.
- This approach ensures we maximize the number of subarrays because we are always choosing the subarray that allows for the most subsequent subarrays to be added.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxNumOfSubarrays(std::vector<int>& nums, std::vector<int>& left, std::vector<int>& right) {
        int n = nums.size();
        std::vector<std::pair<int, int>> intervals;
        for (int i = 0; i < n; ++i) {
            intervals.push_back({left[i], right[i]});
        }
        
        // Sort intervals by their end points
        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            return a.second < b.second;
        });
        
        int maxSubarrays = 0;
        int lastEnd = -1;
        
        for (const auto& interval : intervals) {
            if (interval.first > lastEnd) {
                maxSubarrays++;
                lastEnd = interval.second;
            }
        }
        
        return maxSubarrays;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in `nums`. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, for storing the intervals.
> - **Optimality proof:** This approach is optimal because it ensures that we always choose the subarray that allows for the maximum number of subsequent subarrays to be added, thus maximizing the total number of subarrays.

---

### Final Notes

**Learning Points:**
- The importance of recognizing the problem type (in this case, a variant of interval scheduling).
- How to apply a greedy algorithm to solve problems involving maximizing the number of non-overlapping intervals.
- The role of sorting in simplifying the problem and making it more tractable.

**Mistakes to Avoid:**
- Overcomplicating the problem by considering all possible combinations without first exploring simpler, more efficient approaches.
- Not recognizing the greedy nature of the problem, which leads to a much simpler and more efficient solution.
- Failing to validate the input and handle edge cases properly.