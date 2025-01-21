## The Two Sneaky Numbers of Digitville
**Problem Link:** https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of integers and an integer `k`, find the two numbers in the array that have the maximum sum and the minimum sum with `k`.
- Expected output format: Return a list of four integers `[min_sum, min_pair, max_sum, max_pair]`, where `min_sum` is the minimum sum of `k` and a number in the array, `min_pair` is the number in the array that achieves `min_sum`, `max_sum` is the maximum sum of `k` and a number in the array, and `max_pair` is the number in the array that achieves `max_sum`.
- Key requirements and edge cases to consider: Handle cases where `k` is not in the array, and where there are multiple pairs that achieve the minimum or maximum sum.
- Example test cases with explanations: For example, given `nums = [1, 2, 3, 4]` and `k = 5`, the output should be `[6, 1, 9, 4]`, because the minimum sum of `5` and a number in the array is `6` (achieved by `5 + 1`), and the maximum sum is `9` (achieved by `5 + 4`).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the minimum and maximum sums of `k` and a number in the array, we can simply iterate over the array and calculate the sum of `k` and each number.
- Step-by-step breakdown of the solution:
  1. Initialize `min_sum` to a large value (e.g., `INT_MAX`) and `max_sum` to a small value (e.g., `INT_MIN`).
  2. Initialize `min_pair` and `max_pair` to any value (e.g., `-1`).
  3. Iterate over the array `nums`.
  4. For each number `num` in the array, calculate the sum `sum = k + num`.
  5. If `sum` is less than `min_sum`, update `min_sum` and `min_pair`.
  6. If `sum` is greater than `max_sum`, update `max_sum` and `max_pair`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
vector<int> twoSneakyNumbers(vector<int>& nums, int k) {
    int min_sum = INT_MAX;
    int max_sum = INT_MIN;
    int min_pair = -1;
    int max_pair = -1;
    
    for (int num : nums) {
        int sum = k + num;
        if (sum < min_sum) {
            min_sum = sum;
            min_pair = num;
        }
        if (sum > max_sum) {
            max_sum = sum;
            max_pair = num;
        }
    }
    
    return {min_sum, min_pair, max_sum, max_pair};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array `nums`, because we iterate over the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum and maximum sums and pairs.
> - **Why these complexities occur:** The time complexity is linear because we iterate over the array once, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, because we must iterate over the array at least once to find the minimum and maximum sums.
- Detailed breakdown of the approach:
  1. Initialize `min_sum` to a large value (e.g., `INT_MAX`) and `max_sum` to a small value (e.g., `INT_MIN`).
  2. Initialize `min_pair` and `max_pair` to any value (e.g., `-1`).
  3. Iterate over the array `nums`.
  4. For each number `num` in the array, calculate the sum `sum = k + num`.
  5. If `sum` is less than `min_sum`, update `min_sum` and `min_pair`.
  6. If `sum` is greater than `max_sum`, update `max_sum` and `max_pair`.
- Proof of optimality: This approach is optimal because we must iterate over the array at least once to find the minimum and maximum sums, and we only iterate over the array once.

```cpp
vector<int> twoSneakyNumbers(vector<int>& nums, int k) {
    int min_sum = INT_MAX;
    int max_sum = INT_MIN;
    int min_pair = -1;
    int max_pair = -1;
    
    for (int num : nums) {
        int sum = k + num;
        if (sum < min_sum) {
            min_sum = sum;
            min_pair = num;
        }
        if (sum > max_sum) {
            max_sum = sum;
            max_pair = num;
        }
    }
    
    return {min_sum, min_pair, max_sum, max_pair};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array `nums`, because we iterate over the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum and maximum sums and pairs.
> - **Optimality proof:** This approach is optimal because we must iterate over the array at least once to find the minimum and maximum sums, and we only iterate over the array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and update.
- Problem-solving patterns identified: Finding minimum and maximum values in an array.
- Optimization techniques learned: None, because the optimal solution is the same as the brute force approach.
- Similar problems to practice: Finding minimum and maximum values in an array, finding the closest pair of numbers to a target value.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing `min_sum` and `max_sum` to the correct values, not updating `min_pair` and `max_pair` correctly.
- Edge cases to watch for: Handling cases where `k` is not in the array, and where there are multiple pairs that achieve the minimum or maximum sum.
- Performance pitfalls: Not iterating over the array only once, using too much space to store the minimum and maximum sums and pairs.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it produces the correct output.