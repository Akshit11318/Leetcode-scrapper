## Range Sum Query - Mutable

**Problem Link:** https://leetcode.com/problems/range-sum-query-mutable/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, we need to implement a class `NumArray` that supports two operations: 
  - `update(i, val)`: Updates the `i-th` index to `val`.
  - `sumRange(i, j)`: Returns the sum of the elements in the array from index `i` to `j` (i.e., `nums[i] + nums[i+1] + ... + nums[j]`).
- Expected output format: The result of each operation should be returned in the specified format.
- Key requirements and edge cases to consider: 
  - The array `nums` will have a fixed size, and the index `i` will always be valid.
  - The `sumRange` operation should return the sum of elements in the specified range.
- Example test cases with explanations:
  - For example, if `nums = [1, 3, 5]`, then `sumRange(0, 2)` should return `9` (i.e., `1 + 3 + 5`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the array for each `sumRange` operation to calculate the sum of the elements in the specified range.
- Step-by-step breakdown of the solution:
  1. Create a class `NumArray` with a constructor that takes an array `nums` as input and stores it.
  2. Implement the `update(i, val)` operation by updating the `i-th` index of the array to `val`.
  3. Implement the `sumRange(i, j)` operation by iterating over the array from index `i` to `j` and calculating the sum of the elements.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity for the `sumRange` operation.

```cpp
class NumArray {
public:
    vector<int> nums;
    NumArray(vector<int>& nums) {
        this->nums = nums;
    }
    
    void update(int i, int val) {
        nums[i] = val;
    }
    
    int sumRange(int i, int j) {
        int sum = 0;
        for (int k = i; k <= j; k++) {
            sum += nums[k];
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `sumRange` operation, where $n$ is the size of the array, because we are iterating over the array for each operation. The `update` operation has a time complexity of $O(1)$.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array, because we are storing the array.
> - **Why these complexities occur:** The brute force approach has a high time complexity for the `sumRange` operation because we are iterating over the array for each operation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a data structure called a `segment tree` or `prefix sum array` to store the cumulative sum of the elements in the array. This allows us to calculate the sum of the elements in a range in constant time.
- Detailed breakdown of the approach:
  1. Create a class `NumArray` with a constructor that takes an array `nums` as input and stores it.
  2. Implement the `update(i, val)` operation by updating the `i-th` index of the array to `val` and updating the prefix sum array accordingly.
  3. Implement the `sumRange(i, j)` operation by using the prefix sum array to calculate the sum of the elements in the specified range.
- Proof of optimality: The optimal approach has a time complexity of $O(log n)$ for the `update` operation and $O(1)$ for the `sumRange` operation, where $n$ is the size of the array.

```cpp
class NumArray {
public:
    vector<int> prefixSum;
    vector<int> nums;
    NumArray(vector<int>& nums) {
        this->nums = nums;
        prefixSum.resize(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
    }
    
    void update(int i, int val) {
        int diff = val - nums[i];
        nums[i] = val;
        for (int j = i + 1; j < prefixSum.size(); j++) {
            prefixSum[j] += diff;
        }
    }
    
    int sumRange(int i, int j) {
        return prefixSum[j + 1] - prefixSum[i];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the constructor, $O(n)$ for the `update` operation, and $O(1)$ for the `sumRange` operation, where $n$ is the size of the array.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array, because we are storing the prefix sum array.
> - **Optimality proof:** The optimal approach has a lower time complexity for the `sumRange` operation compared to the brute force approach, making it more efficient for large arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of prefix sum arrays to calculate the sum of elements in a range.
- Problem-solving patterns identified: The use of data structures to optimize the solution.
- Optimization techniques learned: The use of prefix sum arrays to reduce the time complexity of the `sumRange` operation.
- Similar problems to practice: Other problems that involve calculating the sum of elements in a range, such as the `Range Sum Query` problem.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the prefix sum array correctly when updating the array.
- Edge cases to watch for: Handling the case where the range is empty or the array is empty.
- Performance pitfalls: Using the brute force approach for large arrays, which can lead to high time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure correctness.