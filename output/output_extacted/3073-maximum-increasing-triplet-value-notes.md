## Maximum Increasing Triplet Value
**Problem Link:** https://leetcode.com/problems/maximum-increasing-triplet-value/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 5 * 10^4`, `1 <= nums[i] <= 10^5`.
- Expected output format: The maximum triplet value.
- Key requirements and edge cases to consider: The array may not contain three increasing numbers, in which case the function should return 0.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible triplets in the array to see if they are increasing.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum triplet value to 0.
  2. Iterate over the array with three nested loops to generate all possible triplets.
  3. For each triplet, check if the numbers are in increasing order.
  4. If they are, update the maximum triplet value if the current triplet value is larger.
- Why this approach comes to mind first: It is a straightforward solution that checks all possibilities, but it is inefficient due to its cubic time complexity.

```cpp
int maximumTripletValue(vector<int>& nums) {
    int maxTriplet = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                if (nums[i] < nums[j] && nums[j] < nums[k]) {
                    maxTriplet = max(maxTriplet, nums[k]);
                }
            }
        }
    }
    return maxTriplet;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array, because we have three nested loops.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum triplet value.
> - **Why these complexities occur:** The time complexity is cubic because we generate all possible triplets, and the space complexity is constant because we only store a single variable.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use two variables to keep track of the smallest and second smallest numbers we have seen so far that are in increasing order.
- Detailed breakdown of the approach:
  1. Initialize `first` and `second` to infinity, and `maxTriplet` to 0.
  2. Iterate over the array. For each number, check if it is smaller than `first`. If it is, update `first`.
  3. If the current number is larger than `first` but smaller than `second`, update `second`.
  4. If the current number is larger than `second`, update `maxTriplet` if the current number is larger.
- Proof of optimality: This solution has a linear time complexity because we only iterate over the array once, and we use a constant amount of space to store the variables.

```cpp
int maximumTripletValue(vector<int>& nums) {
    int first = INT_MAX;
    int second = INT_MAX;
    int maxTriplet = 0;
    for (int num : nums) {
        if (num <= first) {
            first = num;
        } else if (num <= second) {
            second = num;
        } else {
            maxTriplet = max(maxTriplet, num);
        }
    }
    return maxTriplet;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we only iterate over the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the variables.
> - **Optimality proof:** This solution is optimal because we only need to iterate over the array once to find the maximum triplet value, and we use a constant amount of space.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and variable updates.
- Problem-solving patterns identified: Using variables to keep track of the smallest and second smallest numbers in increasing order.
- Optimization techniques learned: Reducing the time complexity from cubic to linear by using a single pass over the array.
- Similar problems to practice: Other problems that involve finding maximum or minimum values in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, or not updating variables correctly.
- Edge cases to watch for: Empty arrays, or arrays with less than three elements.
- Performance pitfalls: Using nested loops, which can lead to high time complexities.
- Testing considerations: Testing the function with different input arrays, including edge cases.