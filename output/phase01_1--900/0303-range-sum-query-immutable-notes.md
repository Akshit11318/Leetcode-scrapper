## Range Sum Query Immutable

**Problem Link:** https://leetcode.com/problems/range-sum-query-immutable/description

**Problem Statement:**
- Input: A list of integers `nums` representing an array.
- Constraints: The input array will not be empty, and the sum of the elements will not exceed $2^{31} - 1$.
- Expected output: Design a class `NumArray` that supports two methods:
  - `NumArray(int* nums, int numsSize)`: Initializes the object with the given integer array `nums`.
  - `int sumRange(int left, int right)`: Returns the sum of the elements in the range `[left, right]` (inclusive).
- Key requirements: The class should handle multiple queries for the sum of elements in any range.
- Example test cases:
  - `NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);`
  - `numArray.sumRange(0, 2);` returns `-1` because `(-2) + 0 + 3 = 1`.
  - `numArray.sumRange(2, 5);` returns `-1` because `3 + (-5) + 2 + (-1) = -1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves simply iterating over the range specified in each query and summing the elements.
- This approach is straightforward but inefficient for large arrays and multiple queries.
- Step-by-step breakdown:
  1. Initialize the `NumArray` class with the input array.
  2. For each query, iterate from `left` to `right` (inclusive) and sum the elements.
  3. Return the sum for each query.

```cpp
class NumArray {
private:
    int* nums;
    int numsSize;
public:
    NumArray(int* nums, int numsSize) {
        this->nums = nums;
        this->numsSize = numsSize;
    }
    
    int sumRange(int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            sum += nums[i];
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for each query, where $n$ is the size of the range (`right - left + 1`). In the worst case, this could be $O(N)$, where $N$ is the size of the input array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach involves iterating over the array for each query, leading to linear time complexity. The space complexity is constant because we only store the input array and do not allocate additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to precompute the prefix sum (also known as the cumulative sum) of the array during initialization. This allows for constant time complexity for each query.
- Detailed breakdown:
  1. Initialize the `NumArray` class by computing the prefix sum array `prefixSum`, where `prefixSum[i]` is the sum of the first `i + 1` elements of the input array.
  2. For each query, use the prefix sum array to calculate the sum in constant time: `sumRange(left, right) = prefixSum[right] - prefixSum[left - 1]`, adjusting for the case when `left` is 0.
- Proof of optimality: This approach is optimal because it reduces the time complexity of each query to constant time, leveraging the precomputed prefix sum array.

```cpp
class NumArray {
private:
    int* prefixSum;
    int numsSize;
public:
    NumArray(int* nums, int numsSize) {
        this->numsSize = numsSize;
        prefixSum = new int[numsSize + 1];
        prefixSum[0] = 0; // Base case for prefix sum
        for (int i = 0; i < numsSize; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        if (left == 0) {
            return prefixSum[right + 1];
        } else {
            return prefixSum[right + 1] - prefixSum[left];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for each query, as we are simply accessing and subtracting two elements from the prefix sum array.
> - **Space Complexity:** $O(N)$, where $N$ is the size of the input array, because we store the prefix sum array.
> - **Optimality proof:** This approach is optimal because it achieves constant time complexity for each query by leveraging the precomputed prefix sum array, making it the most efficient solution given the constraints of the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept demonstrated: **Prefix Sum** or **Cumulative Sum** technique.
- Problem-solving pattern identified: **Precomputation** to reduce query time complexity.
- Optimization technique learned: Using **auxiliary arrays** to store precomputed values for efficient query processing.

**Mistakes to Avoid:**
- Common implementation error: Not handling edge cases, such as when `left` is 0 or when `right` is the last index of the array.
- Performance pitfall: Not considering the trade-off between precomputation time and query time complexity.
- Testing consideration: Ensure to test the implementation with various input sizes and query ranges to verify its correctness and efficiency.