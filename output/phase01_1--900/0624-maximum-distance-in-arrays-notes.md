## Maximum Distance in Arrays
**Problem Link:** https://leetcode.com/problems/maximum-distance-in-arrays/description

**Problem Statement:**
- Input format: You are given `m` arrays of integers, where each array represents a list of integers.
- Constraints: `1 <= m <= 10^4`, `1 <= n <= 10^4`, and `0 <= nums[i][j] <= 10^9`.
- Expected output format: The maximum distance between two elements in the arrays.
- Key requirements and edge cases to consider: The maximum distance is defined as the maximum absolute difference between two elements in the arrays.
- Example test cases with explanations:
  - `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`: The maximum distance is `9 - 1 = 8`.
  - `[[1, 1, 1], [1, 1, 1], [1, 1, 1]]`: The maximum distance is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum distance, we need to compare each element with every other element in the arrays.
- Step-by-step breakdown of the solution:
  1. Iterate over each array.
  2. For each array, iterate over each element.
  3. For each element, iterate over each array again.
  4. For each array, iterate over each element again.
  5. Calculate the absolute difference between the two elements.
  6. Update the maximum distance if the current difference is greater.
- Why this approach comes to mind first: It is a straightforward approach that ensures we compare every pair of elements.

```cpp
int maxDistance(vector<vector<int>>& arrays) {
    int maxDistance = 0;
    for (int i = 0; i < arrays.size(); i++) {
        for (int j = 0; j < arrays[i].size(); j++) {
            for (int k = 0; k < arrays.size(); k++) {
                for (int l = 0; l < arrays[k].size(); l++) {
                    maxDistance = max(maxDistance, abs(arrays[i][j] - arrays[k][l]));
                }
            }
        }
    }
    return maxDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2)$, where $m$ is the number of arrays and $n$ is the maximum size of an array. This is because we have four nested loops, each iterating over the arrays and their elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum distance.
> - **Why these complexities occur:** The time complexity is high because we compare every pair of elements, resulting in a quadratic number of comparisons. The space complexity is low because we only need to store a single variable to keep track of the maximum distance.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the maximum and minimum values in each array and then compare these values across arrays to find the maximum distance.
- Detailed breakdown of the approach:
  1. Iterate over each array to find the minimum and maximum values.
  2. Keep track of the overall minimum and maximum values across all arrays.
  3. The maximum distance is the difference between the overall maximum and minimum values.
- Proof of optimality: This approach ensures we find the maximum distance by considering the extreme values in each array and comparing them across arrays. It is optimal because it reduces the number of comparisons needed.
- Why further optimization is impossible: We must at least read the input once to find the minimum and maximum values, making this approach optimal in terms of time complexity.

```cpp
int maxDistance(vector<vector<int>>& arrays) {
    int minVal = INT_MAX;
    int maxVal = INT_MIN;
    for (auto& array : arrays) {
        int localMin = *min_element(array.begin(), array.end());
        int localMax = *max_element(array.begin(), array.end());
        minVal = min(minVal, localMin);
        maxVal = max(maxVal, localMax);
    }
    return maxVal - minVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of arrays and $n$ is the maximum size of an array. This is because we iterate over each array once to find the local minimum and maximum values.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum values.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity with respect to the total number of elements, which is the best we can achieve since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding minimum and maximum values in arrays and using these to calculate the maximum distance.
- Problem-solving patterns identified: Reducing the number of comparisons needed by focusing on extreme values.
- Optimization techniques learned: Avoiding unnecessary comparisons by using local minimum and maximum values.
- Similar problems to practice: Finding the maximum or minimum value in an array, or calculating distances between points in different dimensions.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize minimum and maximum values correctly, or not updating them properly during iteration.
- Edge cases to watch for: Empty arrays or arrays with a single element.
- Performance pitfalls: Using brute force approaches that result in high time complexities.
- Testing considerations: Ensure that the solution works correctly for arrays of different sizes and with different ranges of values.