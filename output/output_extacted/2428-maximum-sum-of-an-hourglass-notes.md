## Maximum Sum of an Hourglass

**Problem Link:** https://leetcode.com/problems/maximum-sum-of-an-hourglass/description

**Problem Statement:**
- Input format and constraints: Given a `6 x 6` 2D array, find the maximum sum of an hourglass.
- Expected output format: The maximum sum of an hourglass.
- Key requirements and edge cases to consider: All numbers in the array are positive integers. The array will always be `6 x 6`.
- Example test cases with explanations: 
    - For the input `[[1,2,3],[4,5,6],[7,8,9]]`, the maximum sum is `18` because the hourglass with the maximum sum is `[[5],[4,5,6],[7,8,9]]`.
    - For the input `[[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]`, the maximum sum is `7` because the hourglass with the maximum sum is `[[1,1,1],[1,1,1],[1,1,1]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible hourglass in the array.
- Step-by-step breakdown of the solution:
    1. Iterate over each element in the array.
    2. For each element, calculate the sum of the hourglass centered at that element.
    3. Keep track of the maximum sum found so far.
- Why this approach comes to mind first: It is a straightforward approach that checks every possible solution.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maximumSum(std::vector<std::vector<int>>& arr) {
    int maxSum = -1;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                      arr[i + 1][j + 1] +
                      arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            maxSum = std::max(maxSum, sum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the array is always `6 x 6` and we are checking every possible hourglass.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the maximum sum.
> - **Why these complexities occur:** The time complexity is constant because the size of the input array is constant. The space complexity is constant because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because the array is always `6 x 6` and we are checking every possible hourglass.
- Detailed breakdown of the approach: The approach is the same as the brute force approach.
- Proof of optimality: The approach is optimal because we are checking every possible hourglass and keeping track of the maximum sum found so far.
- Why further optimization is impossible: Further optimization is impossible because we are already checking every possible hourglass and keeping track of the maximum sum found so far.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maximumSum(std::vector<std::vector<int>>& arr) {
    int maxSum = -1;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                      arr[i + 1][j + 1] +
                      arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            maxSum = std::max(maxSum, sum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the array is always `6 x 6` and we are checking every possible hourglass.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the maximum sum.
> - **Optimality proof:** The approach is optimal because we are checking every possible hourglass and keeping track of the maximum sum found so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of checking every possible solution and keeping track of the maximum sum found so far.
- Problem-solving patterns identified: The problem identifies the pattern of checking every possible solution and keeping track of the maximum sum found so far.
- Optimization techniques learned: The problem does not require any optimization techniques because the array is always `6 x 6` and we are checking every possible hourglass.
- Similar problems to practice: Similar problems to practice include finding the maximum sum of a subarray and finding the maximum sum of a submatrix.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to check every possible hourglass.
- Edge cases to watch for: An edge case to watch for is when the array is not `6 x 6`.
- Performance pitfalls: A performance pitfall is to use a recursive approach to check every possible hourglass.
- Testing considerations: A testing consideration is to test the function with different input arrays.