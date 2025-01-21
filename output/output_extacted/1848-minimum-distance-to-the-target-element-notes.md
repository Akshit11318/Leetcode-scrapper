## Minimum Distance to the Target Element
**Problem Link:** https://leetcode.com/problems/minimum-distance-to-the-target-element/description

**Problem Statement:**
- Input: A sorted array `nums` and two integers `target` and `index`.
- Constraints: The array `nums` has `n` elements, where `1 <= n <= 10^5`. The integers `target` and `index` are within the range of the array indices.
- Expected Output: The minimum distance from `index` to the target element in the array `nums`.
- Key Requirements: Find the closest occurrence of the `target` element to the given `index` in the sorted array.
- Example Test Cases:
  - `nums = [1, 2, 3, 4, 5], target = 5, index = 3`. The minimum distance is `0` because the target element is at the given index.
  - `nums = [1, 1, 1, 1, 1], target = 1, index = 2`. The minimum distance is `0` because the target element is at the given index.
  - `nums = [1, 2, 3, 4, 5], target = 1, index = 4`. The minimum distance is `3` because the target element is at index `0`, which is `4` positions away from the given index.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the array to find the target element and calculating the distance from the given index to each occurrence of the target.
- Step-by-step breakdown:
  1. Iterate through the array `nums` to find all occurrences of the `target` element.
  2. For each occurrence, calculate the absolute difference between the current index and the given `index`.
  3. Keep track of the minimum distance found during the iteration.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement by examining every element in the array.

```cpp
int getMinDistance(vector<int>& nums, int target, int index) {
    int minDistance = INT_MAX;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == target) {
            minDistance = min(minDistance, abs(i - index));
        }
    }
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array `nums`. This is because we potentially iterate through every element in the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum distance and other variables, regardless of the input size.
> - **Why these complexities occur:** The brute force approach involves a linear scan of the array, resulting in linear time complexity. The space complexity is constant because we only use a fixed amount of space to store variables, not dependent on the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Since the array is sorted, we can use binary search to find the first and last occurrences of the target element efficiently.
- Detailed breakdown:
  1. Use binary search to find the first occurrence of the target element in the array.
  2. Use binary search again to find the last occurrence of the target element in the array.
  3. Calculate the distances from the given index to the first and last occurrences of the target element.
  4. Return the minimum of these distances.
- Proof of optimality: This approach is optimal because it leverages the sorted nature of the array to reduce the search space from linear to logarithmic, significantly improving efficiency for large inputs.

```cpp
int getMinDistance(vector<int>& nums, int target, int index) {
    auto firstOccurrence = lower_bound(nums.begin(), nums.end(), target);
    auto lastOccurrence = upper_bound(nums.begin(), nums.end(), target);
    
    int minDistance = INT_MAX;
    if (firstOccurrence != nums.end() && *firstOccurrence == target) {
        minDistance = min(minDistance, abs(distance(nums.begin(), firstOccurrence) - index));
    }
    if (lastOccurrence != nums.end() && *(lastOccurrence - 1) == target) {
        minDistance = min(minDistance, abs(distance(nums.begin(), lastOccurrence - 1) - index));
    }
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array `nums`. This is because we use binary search to find the first and last occurrences of the target element.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the iterators and other variables, regardless of the input size.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from linear to logarithmic by leveraging the sorted nature of the array, making it the most efficient solution for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and its application in finding elements in sorted arrays.
- Problem-solving patterns identified: Leveraging the properties of the input data (sorted array) to improve efficiency.
- Optimization techniques learned: Using binary search to reduce the search space and improve time complexity.

**Mistakes to Avoid:**
- Not considering the sorted nature of the array, leading to a brute force approach with higher time complexity.
- Not using binary search correctly to find the first and last occurrences of the target element.
- Not calculating distances correctly from the given index to the occurrences of the target element.