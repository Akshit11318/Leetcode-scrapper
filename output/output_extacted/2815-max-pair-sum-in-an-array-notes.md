## Max Pair Sum in an Array

**Problem Link:** https://leetcode.com/problems/max-pair-sum-in-an-array/description

**Problem Statement:**
- Given an array of integers, find the maximum sum of a pair of numbers in the array.
- Input: An integer array `nums` of length `n`.
- Expected output: The maximum sum of a pair of numbers in the array.
- Key requirements: The pair must consist of two distinct elements in the array.
- Edge cases: Handle arrays with less than two elements, arrays with duplicate elements, and arrays with negative numbers.

**Example Test Cases:**
- Example 1: Input `nums = [3,5,2,6]`, Output `11` (pair: `(5, 6)`).
- Example 2: Input `nums = [1,3,5,7]`, Output `12` (pair: `(5, 7)`).
- Example 3: Input `nums = [1,1,1,1]`, Output `2` (pair: `(1, 1)`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible pair of numbers in the array to find the maximum sum.
- This approach comes to mind first because it directly addresses the problem statement by considering all possible pairs.

```cpp
int maxPairSum(vector<int>& nums) {
    int maxSum = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            maxSum = max(maxSum, nums[i] + nums[j]);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, because we are using two nested loops to check all pairs of numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, while the space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to find the two largest numbers in the array, as their sum will be the maximum pair sum.
- This can be done in a single pass through the array, keeping track of the maximum and second maximum numbers encountered so far.
- This approach is optimal because it only requires a single pass through the array, resulting in a significant improvement over the brute force approach for large inputs.

```cpp
int maxPairSum(vector<int>& nums) {
    if (nums.size() < 2) {
        throw runtime_error("Array must contain at least two elements");
    }
    
    int max1 = INT_MIN, max2 = INT_MIN;
    for (int num : nums) {
        if (num > max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }
    }
    return max1 + max2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum and second maximum numbers.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best possible for this problem since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- The importance of identifying the key insight that leads to an optimal solution.
- The technique of keeping track of the maximum and second maximum (or minimum) values in a single pass through an array.
- Optimization techniques, such as reducing the number of operations and avoiding unnecessary comparisons.

**Mistakes to Avoid:**
- Not considering edge cases, such as arrays with less than two elements.
- Not optimizing the solution for large inputs, leading to inefficient algorithms.
- Failing to validate inputs and handle potential errors, such as empty arrays or arrays with a single element.