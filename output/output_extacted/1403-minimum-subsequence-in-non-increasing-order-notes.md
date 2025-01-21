## Minimum Subsequence in Non-Increasing Order
**Problem Link:** https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 1000`, `0 <= nums[i] <= 1000`.
- Expected output format: The minimum subsequence in non-increasing order that represents the sum of all elements in the input array.
- Key requirements and edge cases to consider: The subsequence must be in non-increasing order and its sum should be equal to the sum of all elements in the input array.
- Example test cases with explanations:
  - For `nums = [4, 3, 10, 9, 8]`, the minimum subsequence is `[10, 9, 8]`.
  - For `nums = [4, 3, 10, 9, 8, 4]`, the minimum subsequence is `[10, 9, 8, 4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the input array, calculate their sums, and check if they are in non-increasing order.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array.
  2. Calculate the sum of each subsequence.
  3. Check if the subsequence is in non-increasing order.
  4. If the sum of the subsequence is equal to the sum of the input array, return the subsequence.
- Why this approach comes to mind first: It is a straightforward approach that tries to find the minimum subsequence by checking all possible subsequences.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> minSubsequence(std::vector<int>& nums) {
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }
    std::sort(nums.rbegin(), nums.rend());
    int currSum = 0;
    std::vector<int> result;
    for (int num : nums) {
        currSum += num;
        result.push_back(num);
        if (currSum >= sum) {
            break;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(n)$ for storing the result subsequence.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to storing the result subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the input array in descending order and then iterate over the sorted array, adding elements to the result subsequence until the sum of the result subsequence is greater than or equal to the sum of the input array.
- Detailed breakdown of the approach:
  1. Sort the input array in descending order.
  2. Initialize the sum of the input array and the result subsequence.
  3. Iterate over the sorted array, adding elements to the result subsequence until the sum of the result subsequence is greater than or equal to the sum of the input array.
- Proof of optimality: This approach is optimal because it uses a greedy strategy to find the minimum subsequence in non-increasing order.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> minSubsequence(std::vector<int>& nums) {
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }
    std::sort(nums.rbegin(), nums.rend());
    int currSum = 0;
    std::vector<int> result;
    for (int num : nums) {
        currSum += num;
        result.push_back(num);
        if (currSum >= sum / 2) {
            break;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(n)$ for storing the result subsequence.
> - **Optimality proof:** This approach is optimal because it uses a greedy strategy to find the minimum subsequence in non-increasing order, which is guaranteed to find the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm, and iterative approach.
- Problem-solving patterns identified: Using a greedy strategy to find the minimum subsequence in non-increasing order.
- Optimization techniques learned: Using sorting to reduce the number of comparisons and iterations.
- Similar problems to practice: Finding the minimum subsequence in non-decreasing order, finding the maximum subsequence in non-increasing order, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for overflow, etc.
- Edge cases to watch for: Empty input array, input array with a single element, etc.
- Performance pitfalls: Using an inefficient sorting algorithm, not using a greedy strategy, etc.
- Testing considerations: Testing with different input sizes, testing with different input patterns, etc.