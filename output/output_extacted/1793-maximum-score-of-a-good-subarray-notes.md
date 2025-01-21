## Maximum Score of a Good Subarray
**Problem Link:** https://leetcode.com/problems/maximum-score-of-a-good-subarray/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `k`, find the maximum score of a good subarray.
- Expected output format: Return the maximum score of a good subarray.
- Key requirements and edge cases to consider: 
  - A good subarray is a subarray where `min` is the minimum value in the subarray, and `max` is the maximum value in the subarray, such that `max - min <= k`.
  - The score of a subarray is the length of the subarray.
  - The subarray must have at least one element.
- Example test cases with explanations: 
  - For `nums = [1, 4, 3, 7, 4, 5]` and `k = 3`, the maximum score is `3` for the subarray `[4, 3, 4]`.
  - For `nums = [5, 5, 5]` and `k = 0`, the maximum score is `1` for any subarray containing a single element.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each possible subarray, calculate `min` and `max`, then check if `max - min <= k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, find `min` and `max`.
  3. If `max - min <= k`, calculate the score of the subarray (which is its length).
  4. Keep track of the maximum score found.
- Why this approach comes to mind first: It is straightforward to check every possible subarray and calculate its score.

```cpp
int maximumScore(vector<int>& nums, int k) {
    int maxScore = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            int minVal = INT_MAX, maxVal = INT_MIN;
            for (int m = i; m <= j; m++) {
                minVal = min(minVal, nums[m]);
                maxVal = max(maxVal, nums[m]);
            }
            if (maxVal - minVal <= k) {
                maxScore = max(maxScore, j - i + 1);
            }
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`, because we are generating all possible subarrays ($O(n^2)$) and then finding `min` and `max` for each subarray ($O(n)$).
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we are using a constant amount of space to store `maxScore`, `minVal`, `maxVal`, and loop variables.
> - **Why these complexities occur:** The brute force approach involves checking all possible subarrays and calculating their scores, leading to cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach to efficiently find the maximum score of a good subarray.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of `nums`.
  2. Initialize `minVal` and `maxVal` to `nums[left]`.
  3. Expand the window to the right by moving `right` and updating `minVal` and `maxVal`.
  4. If `maxVal - minVal > k`, shrink the window from the left by moving `left` and updating `minVal` and `maxVal`.
  5. Keep track of the maximum score (window size) found.
- Proof of optimality: This approach ensures that we consider all possible subarrays in $O(n)$ time, because each element is visited at most twice (once by `right` and once by `left`).

```cpp
int maximumScore(vector<int>& nums, int k) {
    int maxScore = 0;
    int left = 0, right = 0;
    int minVal = INT_MAX, maxVal = INT_MIN;
    while (right < nums.size()) {
        minVal = min(minVal, nums[right]);
        maxVal = max(maxVal, nums[right]);
        while (maxVal - minVal > k) {
            if (nums[left] == minVal) {
                minVal = INT_MAX;
                for (int i = left + 1; i <= right; i++) {
                    minVal = min(minVal, nums[i]);
                }
            }
            if (nums[left] == maxVal) {
                maxVal = INT_MIN;
                for (int i = left + 1; i <= right; i++) {
                    maxVal = max(maxVal, nums[i]);
                }
            }
            left++;
        }
        maxScore = max(maxScore, right - left + 1);
        right++;
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we are visiting each element at most twice.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we are using a constant amount of space to store `maxScore`, `minVal`, `maxVal`, `left`, and `right`.
> - **Optimality proof:** This approach ensures that we consider all possible subarrays in linear time, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, efficient subarray processing.
- Problem-solving patterns identified: Using a sliding window to reduce time complexity.
- Optimization techniques learned: Avoiding unnecessary calculations by maintaining `minVal` and `maxVal` within the window.
- Similar problems to practice: Other problems involving subarray processing and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating `minVal` and `maxVal` when shrinking the window.
- Edge cases to watch for: Handling empty input arrays or arrays with a single element.
- Performance pitfalls: Using a brute force approach for large inputs, leading to excessive time complexity.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases.