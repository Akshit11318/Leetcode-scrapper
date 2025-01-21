## Find All K-Distant Indices in an Array
**Problem Link:** https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description

**Problem Statement:**
- Input format: You are given a `0-indexed` integer array `nums` and an integer `k`.
- Constraints: The length of `nums` will be in the range `[1, 1000]`, and `k` will be in the range `[1, 1000]`.
- Expected output format: Return an array of all indices `i` such that `nums[i] - nums[i - k] <= 1`.
- Key requirements and edge cases to consider: The array is `0-indexed`, so for the first `k` elements, there is no `i - k`. We should handle this edge case carefully.
- Example test cases with explanations:
  - For `nums = [1,2,3,4,5]` and `k = 3`, the output should be `[3]` because `nums[3] - nums[3 - 3] = 4 - 1 = 3` which is less than or equal to `1`.
  - For `nums = [1,2,3,4,5]` and `k = 2`, the output should be `[2, 3]` because `nums[2] - nums[2 - 2] = 3 - 1 = 2` and `nums[3] - nums[3 - 2] = 4 - 2 = 2`, both of which are less than or equal to `1` after re-checking the condition.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the array and for each element, check if the difference between the current element and the element `k` positions before it is less than or equal to `1`.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store the indices that satisfy the condition.
  2. Iterate through the array starting from the `k-th` index (since for the first `k` elements, we cannot find `i - k`).
  3. For each index `i`, calculate `nums[i] - nums[i - k]`.
  4. If the result is less than or equal to `1`, add `i` to the result vector.
- Why this approach comes to mind first: It's a straightforward approach that directly checks every element against the condition given in the problem.

```cpp
#include <vector>

std::vector<int> kDistantIndices(std::vector<int>& nums, int k) {
    std::vector<int> result;
    for (int i = k; i < nums.size(); ++i) {
        if (nums[i] - nums[i - k] <= 1) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we are doing a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every index in the result vector.
> - **Why these complexities occur:** The time complexity is linear because we visit each element once. The space complexity is also linear because we store the indices that satisfy the condition, and in the worst case, this could be every index.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity because we must at least look at each element once to determine if it satisfies the condition. However, we can slightly optimize the code by using a more efficient way to add elements to the result vector.
- Detailed breakdown of the approach: The approach remains the same as the brute force. We iterate through the array and check each element against the condition. If it satisfies the condition, we add its index to the result vector.
- Proof of optimality: Since we must look at each element at least once, the optimal time complexity is $O(n)$. The brute force approach already achieves this, making it optimal in terms of time complexity.
- Why further optimization is impossible: Further optimization in terms of time complexity is impossible because we must examine each element. However, minor optimizations in the implementation can be made, such as reserving space for the result vector if we have an upper bound on the number of elements that will satisfy the condition.

```cpp
#include <vector>

std::vector<int> kDistantIndices(std::vector<int>& nums, int k) {
    std::vector<int> result;
    result.reserve(nums.size() - k); // Minor optimization
    for (int i = k; i < nums.size(); ++i) {
        if (nums[i] - nums[i - k] <= 1) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every index in the result vector.
> - **Optimality proof:** The time complexity is optimal because we must look at each element at least once. The space complexity is also necessary because we need to store the indices that satisfy the condition.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks.
- Problem-solving patterns identified: The need to examine each element at least once to determine if it satisfies a given condition.
- Optimization techniques learned: Minor optimizations such as reserving space for vectors.
- Similar problems to practice: Other problems that involve iterating through arrays or vectors and checking conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as the first `k` elements.
- Edge cases to watch for: The first `k` elements, where `i - k` would be out of bounds.
- Performance pitfalls: Not optimizing the implementation, such as not reserving space for vectors when possible.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the solution works correctly.