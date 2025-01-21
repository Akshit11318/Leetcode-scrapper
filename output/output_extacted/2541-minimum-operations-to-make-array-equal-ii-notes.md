## Minimum Operations to Make Array Equal II

**Problem Link:** https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/description

**Problem Statement:**
- Given an integer array `nums`, return the minimum number of operations to make all array elements equal.
- The operations allowed are incrementing or decrementing an element by 1.
- The input array `nums` contains `n` integers where `1 <= n <= 10^5`.
- The expected output is the minimum number of operations required.

**Key Requirements and Edge Cases:**
- The input array can be empty or contain a single element.
- All elements in the array are integers.
- The operations can only be applied to individual elements, not to the entire array at once.

**Example Test Cases:**
- For `nums = [1, 2, 3]`, the output should be `2` because we can make all elements equal to `2` by applying one increment operation to the first element and one decrement operation to the third element.
- For `nums = [1, 10, 2, 9]`, the output should be `16` because we need to apply multiple increment and decrement operations to make all elements equal.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible target values that the array elements could be made equal to.
- For each target value, calculate the total number of operations required to make all elements equal to that target.
- The target value with the minimum number of operations is the answer.

```cpp
int minOperations(vector<int>& nums) {
    int n = nums.size();
    int minOps = INT_MAX;
    for (int target = *min_element(nums.begin(), nums.end()); target <= *max_element(nums.begin(), nums.end()); target++) {
        int ops = 0;
        for (int num : nums) {
            ops += abs(num - target);
        }
        minOps = min(minOps, ops);
    }
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the size of the input array and $m$ is the range of possible target values. This is because for each target value, we iterate over the entire array to calculate the number of operations.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the minimum number of operations and the current target value.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible target values, and for each target, we are iterating over the entire array. The space complexity is low because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the optimal target value is the median of the array. This is because the median is the value that minimizes the sum of absolute differences with all other values in the array.
- We can find the median by sorting the array and then selecting the middle value (or the average of the two middle values if the array has an even number of elements).
- Once we have the median, we can calculate the minimum number of operations by summing the absolute differences between each element and the median.

```cpp
int minOperations(vector<int>& nums) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int median;
    if (n % 2 == 1) {
        median = nums[n / 2];
    } else {
        median = (nums[n / 2 - 1] + nums[n / 2]) / 2;
    }
    int ops = 0;
    for (int num : nums) {
        ops += abs(num - median);
    }
    return ops;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(1)$ if we sort in-place, or $O(n)$ if we use a sorting algorithm that requires additional space.
> - **Optimality proof:** The median is the value that minimizes the sum of absolute differences with all other values in the array. This is because the median is the value that has the minimum sum of distances to all other points in the array. Therefore, making all elements equal to the median requires the minimum number of operations.

---

### Final Notes

**Learning Points:**
- The importance of understanding the properties of the median and its relation to minimizing the sum of absolute differences.
- How to apply this understanding to solve problems involving minimizing operations to make all elements equal.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the properties of the median and trying all possible target values.
- Not optimizing the sorting operation to reduce time complexity.
- Not handling edge cases such as an empty or single-element array.