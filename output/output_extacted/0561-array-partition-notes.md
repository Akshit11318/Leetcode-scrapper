## Array Partition
**Problem Link:** [https://leetcode.com/problems/array-partition/description](https://leetcode.com/problems/array-partition/description)

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums` with a length of `n`, where `n` is even. Each integer in `nums` is between 1 and `10^4`.
- Expected output format: The function should return the maximum sum of the minimum of each pair.
- Key requirements and edge cases to consider: The input array must be partitioned into `n/2` pairs, and the sum of the minimum of each pair should be maximized.
- Example test cases with explanations:
  - For `nums = [1,4,3,2]`, the output should be `4` because we can pair `1` with `2` and `3` with `4`, resulting in a sum of `min(1,2) + min(3,4) = 1 + 3 = 4`.
  - For `nums = [6,2,6,5,1,2]`, the output should be `9` because we can pair `1` with `2` and `5` with `6`, and another `6` with `2`, resulting in a sum of `min(1,2) + min(5,6) + min(6,2) = 1 + 5 + 2 = 8` which is not the optimal solution. The optimal solution is `min(2,1) + min(6,2) + min(6,5) = 1 + 2 + 5 = 8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To maximize the sum of the minimum of each pair, we need to try all possible pairings and calculate the sum for each pairing.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairings of the input array.
  2. For each pairing, calculate the sum of the minimum of each pair.
  3. Keep track of the maximum sum found.
- Why this approach comes to mind first: This approach is intuitive because it considers all possible pairings, ensuring that we don't miss the optimal solution.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int arrayPairSum(std::vector<int>& nums) {
    int n = nums.size();
    int maxSum = 0;
    // Generate all permutations of the input array
    std::sort(nums.begin(), nums.end());
    for (int i = 0; i < n; i += 2) {
        maxSum += std::min(nums[i], nums[i + 1]);
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(1)$ for the input array.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which has a time complexity of $O(n \log n)$. The space complexity is $O(1)$ because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the input array is sorted, we can directly pair adjacent elements to maximize the sum of the minimum of each pair.
- Detailed breakdown of the approach:
  1. Sort the input array in ascending order.
  2. Iterate through the sorted array and pair adjacent elements.
  3. Calculate the sum of the minimum of each pair.
- Proof of optimality: This approach is optimal because it ensures that the smallest numbers are paired with the next smallest numbers, maximizing the sum of the minimum of each pair.

```cpp
int arrayPairSum(std::vector<int>& nums) {
    int n = nums.size();
    int maxSum = 0;
    std::sort(nums.begin(), nums.end());
    for (int i = 0; i < n; i += 2) {
        maxSum += nums[i];
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(1)$ for the input array.
> - **Optimality proof:** This approach is optimal because it ensures that the smallest numbers are paired with the next smallest numbers, maximizing the sum of the minimum of each pair.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and greedy algorithms.
- Problem-solving patterns identified: Maximizing the sum of the minimum of each pair by pairing adjacent elements in a sorted array.
- Optimization techniques learned: Using sorting to simplify the problem and reduce the search space.
- Similar problems to practice: Other problems involving pairing or matching elements in an array or graph.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to sort the input array or incorrectly calculating the sum of the minimum of each pair.
- Edge cases to watch for: Empty input arrays or arrays with an odd number of elements.
- Performance pitfalls: Using an inefficient sorting algorithm or not taking advantage of the fact that the input array can be sorted to simplify the problem.
- Testing considerations: Testing the function with different input arrays, including edge cases and large inputs, to ensure that it works correctly and efficiently.