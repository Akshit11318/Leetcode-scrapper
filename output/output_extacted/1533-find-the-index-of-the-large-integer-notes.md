## Find the Index of the Large Integer

**Problem Link:** https://leetcode.com/problems/find-the-index-of-the-large-integer/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an array of integers `index`, we need to find the index of the large integer in `nums` corresponding to each index in `index`.
- Expected output format: An array of integers where each integer is the index of the large integer in `nums` corresponding to the index in `index`.
- Key requirements and edge cases to consider: 
  - Each index in `index` corresponds to a subarray in `nums`.
  - The subarray in `nums` starts at the index specified in `index` and ends at the next index in `index` (or the end of the array if it's the last index).
  - If there are multiple maximum integers in a subarray, the index of the first occurrence should be returned.
- Example test cases with explanations:
  - Example 1: 
    - Input: `nums = [1, 2, 3, 4, 5], index = [0, 1, 2]`
    - Output: `[0, 1, 2]`
    - Explanation: The subarrays are `[1]`, `[2, 3]`, and `[4, 5]`. The maximum integer in each subarray is `1`, `3`, and `5`, respectively. The indices of these maximum integers are `0`, `1`, and `2`, respectively.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each index in `index`, find the corresponding subarray in `nums`, and then find the index of the maximum integer in that subarray.
- Step-by-step breakdown of the solution:
  1. Iterate over each index in `index`.
  2. For each index, find the corresponding subarray in `nums`.
  3. Find the maximum integer in the subarray.
  4. Find the index of the maximum integer in the subarray.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

```cpp
vector<int> findIndex(vector<int>& nums, vector<int>& index) {
    vector<int> result;
    for (int i = 0; i < index.size(); i++) {
        int maxVal = INT_MIN;
        int maxIndex = -1;
        for (int j = index[i]; j < (i == index.size() - 1 ? nums.size() : index[i + 1]); j++) {
            if (nums[j] > maxVal) {
                maxVal = nums[j];
                maxIndex = j;
            }
        }
        result.push_back(maxIndex);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `index` and $m$ is the average size of the subarrays in `nums`.
> - **Space Complexity:** $O(n)$, where $n$ is the size of `index`.
> - **Why these complexities occur:** The time complexity occurs because we're iterating over each index in `index` and then iterating over the corresponding subarray in `nums`. The space complexity occurs because we're storing the result for each index in `index`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through `nums` to find the maximum integer in each subarray and its index.
- Detailed breakdown of the approach:
  1. Initialize an empty result vector.
  2. Iterate over each index in `index`.
  3. For each index, find the corresponding subarray in `nums`.
  4. Find the maximum integer in the subarray and its index.
  5. Append the index of the maximum integer to the result vector.
- Proof of optimality: This approach is optimal because it only requires a single pass through `nums` and `index`.

```cpp
vector<int> findIndex(vector<int>& nums, vector<int>& index) {
    vector<int> result;
    for (int i = 0; i < index.size(); i++) {
        int maxVal = INT_MIN;
        int maxIndex = -1;
        for (int j = index[i]; j < (i == index.size() - 1 ? nums.size() : index[i + 1]); j++) {
            if (nums[j] > maxVal) {
                maxVal = nums[j];
                maxIndex = j;
            }
        }
        result.push_back(maxIndex);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `index` and $m$ is the average size of the subarrays in `nums`.
> - **Space Complexity:** $O(n)$, where $n$ is the size of `index`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `nums` and `index`, and it finds the maximum integer in each subarray in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and array manipulation.
- Problem-solving patterns identified: Finding the maximum integer in a subarray and its index.
- Optimization techniques learned: Using a single pass through the input arrays to find the maximum integer in each subarray.
- Similar problems to practice: Finding the minimum integer in a subarray, finding the sum of integers in a subarray, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not initializing variables properly, and not handling errors correctly.
- Edge cases to watch for: Empty input arrays, arrays with a single element, and arrays with duplicate maximum integers.
- Performance pitfalls: Using nested loops with high time complexity, not optimizing the algorithm for large input sizes.
- Testing considerations: Testing the algorithm with different input sizes, testing with edge cases, and testing with different types of input data.