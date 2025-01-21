## Maximum Value of an Ordered Triplet I
**Problem Link:** https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description

**Problem Statement:**
- Given an array of integers `nums`, find the maximum value of an ordered triplet `(a, b, c)` where `a < b < c` and `a`, `b`, `c` are all in `nums`.
- Input format: `nums` is an array of integers.
- Constraints: `3 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected output format: The maximum value of `c` in the ordered triplet.
- Key requirements and edge cases to consider: The triplet must be ordered, and all elements must be distinct.

### Brute Force Approach

**Explanation:**
- The initial thought process is to check all possible triplets in the array.
- Step-by-step breakdown:
  1. Generate all possible triplets from the array.
  2. For each triplet, check if the elements are ordered (`a < b < c`).
  3. If the triplet is ordered, update the maximum value of `c` if necessary.

```cpp
class Solution {
public:
    int maximumValue(vector<int>& nums) {
        int maxC = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] < nums[j] && nums[j] < nums[k]) {
                        maxC = max(maxC, nums[k]);
                    }
                }
            }
        }
        return maxC;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because we have three nested loops iterating over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum value of `c`.
> - **Why these complexities occur:** The brute force approach checks all possible triplets, resulting in a cubic time complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single pass through the array to keep track of the maximum values seen so far.
- Step-by-step breakdown:
  1. Initialize variables to store the maximum values of `a` and `b` seen so far.
  2. Iterate through the array, updating the maximum values of `a` and `b` as necessary.
  3. For each element, check if it is greater than the current maximum value of `b`. If so, update the maximum value of `c`.

```cpp
class Solution {
public:
    int maximumValue(vector<int>& nums) {
        int maxA = INT_MIN, maxB = INT_MIN, maxC = INT_MIN;
        for (int num : nums) {
            if (num > maxC) {
                maxC = num;
            }
            if (num < maxC && num > maxB) {
                maxB = num;
            }
            if (num < maxB && num > maxA) {
                maxA = num;
            }
        }
        return maxC;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum values.
> - **Optimality proof:** This approach is optimal because it uses a single pass through the array, minimizing the time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: single-pass iteration, maximum value tracking.
- Problem-solving patterns identified: using variables to store maximum values seen so far.
- Optimization techniques learned: reducing the number of iterations to improve time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not updating the maximum values correctly.
- Edge cases to watch for: handling duplicate elements, empty arrays.
- Performance pitfalls: using unnecessary iterations or data structures.
- Testing considerations: testing with different input sizes, edge cases.