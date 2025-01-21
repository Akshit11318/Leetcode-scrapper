## Running Sum of 1d Array

**Problem Link:** [https://leetcode.com/problems/running-sum-of-1d-array/description](https://leetcode.com/problems/running-sum-of-1d-array/description)

**Problem Statement:**
- Input format and constraints: The input is a 1D array of integers `nums`, and the constraints include the number of elements in the array.
- Expected output format: The output is a modified version of the input array where each element at index `i` is the sum of all elements up to `i` in the input array.
- Key requirements and edge cases to consider: The array can be empty, or it can contain a single element. The array can also contain negative numbers or zero.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,2,3,4]`, Output: `[1,3,6,10]`. Explanation: Running sum from left to right: `[1, 1+2, 1+2+3, 1+2+3+4]`.
  - Example 2: Input: `nums = [1,1,1,1,1]`, Output: `[1,2,3,4,5]`. Explanation: Running sum from left to right: `[1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]`.
  - Example 3: Input: `nums = [3,1,2,10]`, Output: `[3,4,6,16]`. Explanation: Running sum from left to right: `[3, 3+1, 3+1+2, 3+1+2+10]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through the array and calculating the sum of all elements up to each index.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array to store the running sum.
  2. Iterate through each element in the input array.
  3. For each element, calculate the sum of all elements up to the current index.
  4. Append the calculated sum to the running sum array.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first choice.

```cpp
#include <vector>

std::vector<int> runningSum(std::vector<int>& nums) {
    std::vector<int> runningSumArray;
    int currentSum = 0;
    for (int num : nums) {
        currentSum += num;
        runningSumArray.push_back(currentSum);
    }
    return runningSumArray;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we are storing the running sum in a separate array.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through the array once, and the space complexity occurs because we are storing the running sum in a separate array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the running sum in-place, without the need for an additional array.
- Detailed breakdown of the approach:
  1. Initialize the first element of the input array as the running sum.
  2. Iterate through the rest of the elements in the input array.
  3. For each element, add the previous element's value to the current element's value.
- Proof of optimality: This approach has a time complexity of $O(n)$ and a space complexity of $O(1)$, making it the most efficient solution.

```cpp
#include <vector>

std::vector<int> runningSum(std::vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        nums[i] += nums[i-1];
    }
    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in the input array. This is because we are modifying the input array in-place.
> - **Optimality proof:** This approach is optimal because we are only iterating through the array once, and we are not using any additional space that scales with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, running sum calculation.
- Problem-solving patterns identified: Iterating through an array, modifying elements in-place.
- Optimization techniques learned: Reducing space complexity by modifying the input array in-place.
- Similar problems to practice: Other problems that involve calculating running sums or modifying arrays in-place.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the first element of the running sum array, using an incorrect index to access the previous element's value.
- Edge cases to watch for: Empty input array, input array with a single element.
- Performance pitfalls: Using a separate array to store the running sum, which can increase the space complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases and large inputs.