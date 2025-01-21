## Transformed Array
**Problem Link:** https://leetcode.com/problems/transformed-array/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, we need to transform it into a new array `transformed` such that each element `transformed[i]` is equal to `nums[i]` if `nums[i]` is odd, otherwise `transformed[i]` is equal to `nums[i] + 1`. Then, we need to return the maximum value in the `transformed` array.
- Expected output format: The maximum value in the `transformed` array.
- Key requirements and edge cases to consider:
  - The input array `nums` can be empty.
  - The input array `nums` can contain duplicate elements.
  - The input array `nums` can contain negative numbers.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 4, 5]`: The `transformed` array would be `[1, 3, 3, 5, 5]`, and the maximum value would be `5`.
  - `nums = [2, 4, 6, 8]`: The `transformed` array would be `[3, 5, 7, 9]`, and the maximum value would be `9`.
  - `nums = [1, 3, 5]`: The `transformed` array would be `[1, 3, 5]`, and the maximum value would be `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simply iterate over the input array `nums`, transform each element according to the given rules, and keep track of the maximum value.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `transformed` to store the transformed elements.
  2. Initialize a variable `max_val` to store the maximum value in the `transformed` array.
  3. Iterate over the input array `nums`.
  4. For each element `nums[i]`, check if it is odd or even.
  5. If `nums[i]` is odd, add it to the `transformed` array as is.
  6. If `nums[i]` is even, add `nums[i] + 1` to the `transformed` array.
  7. Update `max_val` if the current element in the `transformed` array is greater than `max_val`.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that directly implements the problem statement.

```cpp
vector<int> transformArray(vector<int>& nums) {
    vector<int> transformed;
    int max_val = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] % 2 == 0) {
            transformed.push_back(nums[i] + 1);
        } else {
            transformed.push_back(nums[i]);
        }
        max_val = max(max_val, transformed.back());
    }
    return transformed;
}

int findMax(vector<int>& nums) {
    vector<int> transformed = transformArray(nums);
    int max_val = INT_MIN;
    for (int i = 0; i < transformed.size(); i++) {
        max_val = max(max_val, transformed[i]);
    }
    return max_val;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because we are iterating over the input array twice: once to transform the elements and once to find the maximum value.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because we are storing the transformed elements in a new array.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the input array twice, and the space complexity occurs because we are storing the transformed elements in a new array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the maximum value in the `transformed` array in a single pass, without storing the transformed elements in a new array.
- Detailed breakdown of the approach:
  1. Initialize a variable `max_val` to store the maximum value in the `transformed` array.
  2. Iterate over the input array `nums`.
  3. For each element `nums[i]`, check if it is odd or even.
  4. If `nums[i]` is odd, update `max_val` if `nums[i]` is greater than `max_val`.
  5. If `nums[i]` is even, update `max_val` if `nums[i] + 1` is greater than `max_val`.
- Proof of optimality: This approach is optimal because we are only iterating over the input array once, and we are not storing any additional data.
- Why further optimization is impossible: We must iterate over the input array at least once to find the maximum value, so further optimization is impossible.

```cpp
int findMax(vector<int>& nums) {
    int max_val = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] % 2 == 0) {
            max_val = max(max_val, nums[i] + 1);
        } else {
            max_val = max(max_val, nums[i]);
        }
    }
    return max_val;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because we are iterating over the input array once.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the input array `nums`. This is because we are not storing any additional data.
> - **Optimality proof:** This approach is optimal because we are only iterating over the input array once, and we are not storing any additional data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and optimization techniques.
- Problem-solving patterns identified: The problem can be solved by iterating over the input array and keeping track of the maximum value.
- Optimization techniques learned: We can optimize the solution by finding the maximum value in a single pass, without storing the transformed elements in a new array.
- Similar problems to practice: Other problems that involve iterating over an array and finding the maximum or minimum value.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables before using them, not checking for edge cases, and not optimizing the solution.
- Edge cases to watch for: The input array can be empty, and the input array can contain duplicate elements.
- Performance pitfalls: Storing the transformed elements in a new array can increase the space complexity, and iterating over the input array multiple times can increase the time complexity.
- Testing considerations: We should test the solution with different input arrays, including empty arrays and arrays with duplicate elements.