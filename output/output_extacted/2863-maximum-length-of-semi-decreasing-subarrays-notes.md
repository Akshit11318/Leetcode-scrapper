## Maximum Length of Semi-Decreasing Subarrays

**Problem Link:** https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`.
- Expected Output: The maximum length of a semi-decreasing subarray.
- Key Requirements: A semi-decreasing subarray is defined as a subarray where every element is less than or equal to the previous element, or every element is greater than or equal to the previous element.
- Example Test Cases:
  - Input: `nums = [1,2,3,4,5]`
    - Output: `5`
    - Explanation: The entire array is a semi-decreasing subarray.
  - Input: `nums = [5,4,3,2,1]`
    - Output: `5`
    - Explanation: The entire array is a semi-decreasing subarray.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum length of a semi-decreasing subarray, we can check every possible subarray and determine if it is semi-decreasing.
- Step-by-step breakdown:
  1. Generate all possible subarrays from the input array.
  2. For each subarray, check if it is semi-decreasing by comparing adjacent elements.
  3. Keep track of the maximum length of semi-decreasing subarrays found.

```cpp
int maxLength(vector<int>& nums) {
    int maxLen = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            if (isSemiDecreasing(subarray)) {
                maxLen = max(maxLen, (int)subarray.size());
            }
        }
    }
    return maxLen;
}

bool isSemiDecreasing(vector<int>& arr) {
    bool isIncreasing = true;
    bool isDecreasing = true;
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > arr[i - 1]) {
            isDecreasing = false;
        }
        if (arr[i] < arr[i - 1]) {
            isIncreasing = false;
        }
    }
    return isIncreasing || isDecreasing;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we are generating all possible subarrays ($O(n^2)$) and for each subarray, we are checking if it is semi-decreasing ($O(n)$).
> - **Space Complexity:** $O(n)$, as we are storing each subarray.
> - **Why these complexities occur:** The brute force approach involves checking every possible subarray, which leads to high time complexity. The space complexity is due to storing each subarray.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can solve this problem more efficiently by maintaining two arrays: one for the length of the longest increasing subarray ending at each position and one for the length of the longest decreasing subarray ending at each position.
- Detailed breakdown:
  1. Initialize two arrays `inc` and `dec` of the same length as the input array, with all elements initialized to 1.
  2. Iterate through the input array from left to right, updating `inc` and `dec` based on whether the current element is greater than or equal to the previous element (for `inc`) or less than or equal to the previous element (for `dec`).
  3. Keep track of the maximum value in both `inc` and `dec` arrays.

```cpp
int maxLength(vector<int>& nums) {
    int n = nums.size();
    vector<int> inc(n, 1), dec(n, 1);
    int maxLen = 1;
    
    for (int i = 1; i < n; i++) {
        if (nums[i] >= nums[i - 1]) {
            inc[i] = inc[i - 1] + 1;
        }
        if (nums[i] <= nums[i - 1]) {
            dec[i] = dec[i - 1] + 1;
        }
        maxLen = max(maxLen, max(inc[i], dec[i]));
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are making a single pass through the array.
> - **Space Complexity:** $O(n)$, as we are maintaining two arrays of the same length as the input array.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array and maintains the necessary information to find the maximum length of a semi-decreasing subarray.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and maintaining auxiliary arrays to track relevant information.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts (e.g., finding longest increasing and decreasing subarrays).
- Optimization techniques learned: Reducing time complexity by avoiding redundant calculations and using auxiliary arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing arrays correctly, not updating auxiliary arrays correctly.
- Edge cases to watch for: Empty input array, single-element input array.
- Performance pitfalls: Using brute force approaches for large input sizes.
- Testing considerations: Testing with various input sizes, including edge cases.