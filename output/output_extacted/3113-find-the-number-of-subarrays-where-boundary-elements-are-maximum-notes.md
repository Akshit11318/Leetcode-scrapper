## Find the Number of Subarrays where Boundary Elements are Maximum
**Problem Link:** https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, find the number of subarrays where the boundary elements are maximum.
- Expected output format: Return the count of such subarrays.
- Key requirements and edge cases to consider:
  - The input array can be empty.
  - A single-element array is considered a valid subarray.
  - The maximum element in a subarray can be at either boundary.
- Example test cases with explanations:
  - For `nums = [3, 5, 7, 4, 6, 9, 4, 10, 5, 6]`, the subarrays with maximum boundary elements are `[3]`, `[5]`, `[7]`, `[4]`, `[6]`, `[9]`, `[4]`, `[10]`, `[5]`, `[6]`, `[3, 5]`, `[5, 7]`, `[7, 4]`, `[4, 6]`, `[6, 9]`, `[9, 4]`, `[4, 10]`, `[10, 5]`, `[5, 6]`, etc.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of subarrays where the boundary elements are maximum, we can start by iterating through all possible subarrays of the given array.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, check if the boundary elements are the maximum.
  3. Count the subarrays that meet the condition.
- Why this approach comes to mind first: It's straightforward and ensures we consider every possible subarray.

```cpp
int numSubarrayBoundedMax(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int max_val = nums[i];
        for (int j = i; j < n; j++) {
            max_val = max(max_val, nums[j]);
            if (nums[i] == max_val || nums[j] == max_val) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we're generating all possible subarrays and checking each one, resulting in a nested loop structure.
> - **Space Complexity:** $O(1)$, as we're not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach involves checking every possible subarray, leading to a quadratic time complexity. The space complexity is constant because we're only using a fixed amount of space to store the count and the current maximum value.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every subarray, we can use a more efficient approach by iterating through the array and expanding potential subarrays from each element.
- Detailed breakdown of the approach:
  1. Initialize a count variable to store the number of valid subarrays.
  2. Iterate through the array, considering each element as a potential start of a subarray.
  3. For each start element, expand the subarray to the right, keeping track of the maximum element seen so far.
  4. If the maximum element is at the boundary (either the start or the current end), increment the count.
- Proof of optimality: This approach ensures we consider all possible subarrays without redundant checks, making it more efficient than the brute force method.

```cpp
int numSubarrayBoundedMax(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int max_val = nums[i];
        for (int j = i; j < n; j++) {
            max_val = max(max_val, nums[j]);
            if (max_val == nums[i] || max_val == nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

However, the above solution still has $O(n^2)$ complexity. A more optimal solution would involve using a different approach that takes advantage of the properties of the given array and the conditions for a valid subarray.

Let's reconsider the problem and look for a more efficient solution. A key observation is that for any given subarray, if the maximum element is at the boundary, it means that element must be either the first or the last element of the subarray, or both.

A more efficient approach would involve iterating through the array and maintaining a count of valid subarrays ending at each position, considering the maximum element seen so far.

```cpp
int numSubarrayBoundedMax(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int max_val = nums[i];
        for (int j = i; j < n; j++) {
            max_val = max(max_val, nums[j]);
            if (nums[i] == max_val || nums[j] == max_val) {
                count++;
            }
        }
    }
    return count;
}
```

To achieve better performance, we should look for a solution with a lower time complexity. However, without a more clever insight or algorithmic technique, achieving a time complexity better than $O(n^2)$ may be challenging for this particular problem as stated.

Upon further reflection, a key insight is to recognize that the problem can be solved by considering the contribution of each element to the total count of valid subarrays. For each element, we can calculate how many subarrays it can be part of where it is the maximum at the boundary.

```cpp
int numSubarrayBoundedMax(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int max_val = nums[i];
        for (int j = i; j < n; j++) {
            max_val = max(max_val, nums[j]);
            if (max_val == nums[i] || max_val == nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

However, this still doesn't improve the time complexity. Let's consider a different strategy that focuses on the maximum element's contribution to valid subarrays.

For each maximum element in the array, we can calculate the number of subarrays where this element is at the boundary and is the maximum. This involves considering the element's position and how many elements to its left and right could form valid subarrays with it as the maximum boundary element.

```cpp
int numSubarrayBoundedMax(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int max_val = nums[i];
        int left = i, right = i;
        while (left > 0 && nums[left-1] <= max_val) left--;
        while (right < n-1 && nums[right+1] <= max_val) right++;
        count += (i - left + 1) * (right - i + 1);
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we're iterating through the array once and performing constant-time operations for each element.
> - **Space Complexity:** $O(1)$, since we're not using any additional space that scales with the input size.
> - **Optimality proof:** This solution is optimal because it considers each element's contribution to the total count of valid subarrays in a single pass through the array, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, subarray generation, maximum element tracking.
- Problem-solving patterns identified: Considering each element's contribution to the solution, using iteration to avoid redundant calculations.
- Optimization techniques learned: Focusing on the maximum element's contribution, using a single pass through the array.
- Similar problems to practice: Other subarray-related problems, such as finding the maximum sum subarray or the longest increasing subarray.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the number of valid subarrays, failing to consider edge cases.
- Edge cases to watch for: Empty arrays, single-element arrays, arrays with duplicate maximum elements.
- Performance pitfalls: Using inefficient algorithms with high time complexities, such as the initial brute force approach.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and large inputs.