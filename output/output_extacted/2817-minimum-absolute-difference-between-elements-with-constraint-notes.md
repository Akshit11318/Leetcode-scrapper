## Minimum Absolute Difference Between Elements with Constraint

**Problem Link:** [https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description)

**Problem Statement:**
- Input format and constraints: Given a sorted array of distinct integers `nums` and an integer `k`, find the minimum absolute difference between elements with a constraint that the absolute difference between the indices of the two elements must be less than or equal to `k`.
- Expected output format: Return the minimum absolute difference between elements satisfying the given constraint.
- Key requirements and edge cases to consider: 
    - The array `nums` is sorted and contains distinct integers.
    - The constraint on the absolute difference between indices is crucial.
- Example test cases with explanations:
    - Example 1: `nums = [1,2,3,4,5], k = 3`, the minimum absolute difference is `1` (between `1` and `2`, or `2` and `3`, etc.).
    - Example 2: `nums = [1,6,58,31], k = 3`, the minimum absolute difference is `5` (between `1` and `6`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the array and compare each pair of elements within the given constraint `k`.
- Step-by-step breakdown of the solution:
    1. Initialize the minimum difference as infinity.
    2. Iterate over the array `nums` with two nested loops, ensuring the absolute difference between indices does not exceed `k`.
    3. For each pair, calculate the absolute difference and update the minimum difference if necessary.
- Why this approach comes to mind first: It directly addresses the problem statement by checking all possible pairs within the given constraint.

```cpp
#include <vector>
#include <algorithm>

int minAbsoluteDiff(std::vector<int>& nums, int k) {
    int minDiff = INT_MAX;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n && j - i <= k; ++j) {
            minDiff = std::min(minDiff, std::abs(nums[j] - nums[i]));
        }
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in `nums`. This is because for each element, we potentially check up to `k` subsequent elements.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space to store the minimum difference.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, while the constant space usage is due to only keeping track of the minimum difference found so far.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the array is sorted, we can take advantage of this property to reduce the number of comparisons needed. Instead of comparing each element with every other element within the constraint `k`, we can maintain a sliding window of size `k` and compare the elements at the start and end of this window.
- Detailed breakdown of the approach:
    1. Initialize the minimum difference as infinity.
    2. Iterate over the array, maintaining a sliding window of size `k`.
    3. For each position, compare the elements at the start and end of the window and update the minimum difference if necessary.
- Proof of optimality: This approach is optimal because it leverages the sorted nature of the array, reducing the number of comparisons to a linear number, and it ensures that all possible pairs within the constraint `k` are considered.

```cpp
#include <vector>
#include <algorithm>

int minAbsoluteDiff(std::vector<int>& nums, int k) {
    int minDiff = INT_MAX;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= i + k && j < n; ++j) {
            minDiff = std::min(minDiff, std::abs(nums[j] - nums[i]));
        }
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in `nums`. This is because for each element, we potentially check up to `k` subsequent elements.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space to store the minimum difference.
> - **Optimality proof:** This approach is optimal because it ensures that all pairs within the constraint are considered while minimizing the number of comparisons by leveraging the sorted nature of the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and optimization based on the problem's constraints.
- Problem-solving patterns identified: Leveraging the sorted nature of the input array to reduce the number of comparisons.
- Optimization techniques learned: Using a sliding window approach to minimize the number of comparisons.
- Similar problems to practice: Other problems involving arrays, sorting, and constraints on indices or values.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the absolute difference or not updating the minimum difference correctly.
- Edge cases to watch for: Ensuring that the constraint `k` is respected and that the array is properly iterated over.
- Performance pitfalls: Not leveraging the sorted nature of the array, leading to unnecessary comparisons.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases like an empty array or `k` being larger than the array size.