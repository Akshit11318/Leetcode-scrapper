## Peaks in Array
**Problem Link:** https://leetcode.com/problems/peaks-in-array/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, find all the peaks in the array. A peak is an element which is not smaller than its neighbors.
- Expected output format: Return the indices of all peaks in the array.
- Key requirements and edge cases to consider: 
    - Handle arrays with no peaks.
    - Handle arrays with peaks at the beginning or end.
    - Handle arrays with multiple peaks.
- Example test cases with explanations:
    - `nums = [1, 2, 3, 1]`, output: `[2]`
    - `nums = [1, 2, 1, 3, 5, 6, 4]`, output: `[1, 5]`
    - `nums = [1, 3, 2, 1]`, output: `[1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array and compare each element with its neighbors to determine if it's a peak.
- Step-by-step breakdown of the solution:
    1. Initialize an empty vector `peaks` to store the indices of peaks.
    2. Iterate through the array from the second element to the second last element (inclusive).
    3. For each element, check if it's not smaller than its neighbors. If it's not smaller, add its index to `peaks`.
    4. Handle edge cases for the first and last elements separately.
- Why this approach comes to mind first: It's a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
vector<int> findPeaks(vector<int>& nums) {
    vector<int> peaks;
    int n = nums.size();
    
    // Handle edge case for the first element
    if (n > 1 && nums[0] >= nums[1]) {
        peaks.push_back(0);
    }
    
    // Iterate through the array from the second element to the second last element
    for (int i = 1; i < n - 1; i++) {
        if (nums[i] >= nums[i - 1] && nums[i] >= nums[i + 1]) {
            peaks.push_back(i);
        }
    }
    
    // Handle edge case for the last element
    if (n > 1 && nums[n - 1] >= nums[n - 2]) {
        peaks.push_back(n - 1);
    }
    
    return peaks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're iterating through the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because in the worst case, all elements could be peaks.
> - **Why these complexities occur:** The time complexity occurs because we're iterating through the array once, and the space complexity occurs because we're storing the indices of all peaks.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we need to check each element at least once to determine if it's a peak.
- Detailed breakdown of the approach: The same approach as the brute force solution.
- Proof of optimality: We need to check each element at least once, so the time complexity of $O(n)$ is optimal.
- Why further optimization is impossible: We can't do better than $O(n)$ time complexity because we need to check each element at least once.

```cpp
vector<int> findPeaks(vector<int>& nums) {
    vector<int> peaks;
    int n = nums.size();
    
    // Handle edge case for the first element
    if (n > 1 && nums[0] >= nums[1]) {
        peaks.push_back(0);
    }
    
    // Iterate through the array from the second element to the second last element
    for (int i = 1; i < n - 1; i++) {
        if (nums[i] >= nums[i - 1] && nums[i] >= nums[i + 1]) {
            peaks.push_back(i);
        }
    }
    
    // Handle edge case for the last element
    if (n > 1 && nums[n - 1] >= nums[n - 2]) {
        peaks.push_back(n - 1);
    }
    
    return peaks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're iterating through the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because in the worst case, all elements could be peaks.
> - **Optimality proof:** The time complexity of $O(n)$ is optimal because we need to check each element at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and edge case handling.
- Problem-solving patterns identified: Checking each element at least once to determine if it's a peak.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: Finding valleys in an array, finding local maxima or minima in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not checking each element at least once.
- Edge cases to watch for: The first and last elements, empty array, array with one element.
- Performance pitfalls: Not iterating through the array efficiently.
- Testing considerations: Test the function with different arrays, including edge cases.