## Minimum Difference Between Highest and Lowest of K Scores
**Problem Link:** https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description

**Problem Statement:**
- Input: A list of integers `scores` and an integer `k`.
- Constraints: `1 <= k <= scores.length <= 10^5`, `1 <= scores[i] <= 10^8`.
- Expected Output: The minimum possible difference between the highest and lowest of `k` scores.
- Key Requirements: Find the smallest possible difference by selecting any `k` scores from the given list.
- Example Test Cases:
  - `scores = [10, 20, 30, 40, 50, 60, 70], k = 3`
  - `scores = [10], k = 1`

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of `k` scores from the given list.
- Step-by-step breakdown:
  1. Generate all combinations of `k` scores from the list.
  2. For each combination, find the highest and lowest score.
  3. Calculate the difference between the highest and lowest score.
  4. Keep track of the minimum difference found.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int minimumDifference(std::vector<int>& scores, int k) {
    std::sort(scores.begin(), scores.end());
    int minDiff = INT_MAX;
    for (int i = 0; i <= scores.size() - k; ++i) {
        int diff = scores[i + k - 1] - scores[i];
        minDiff = std::min(minDiff, diff);
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of scores. The subsequent loop has a complexity of $O(n - k + 1)$, but since $k$ can be $1$, this simplifies to $O(n)$, making the overall time complexity $O(n \log n)$.
> - **Space Complexity:** $O(1)$ if we consider the input list as part of the space complexity, otherwise $O(n)$ for sorting in the worst case.
> - **Why these complexities occur:** The sorting step dominates the time complexity, and the space complexity is dependent on the sorting algorithm used.

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the minimum difference between the highest and lowest of `k` scores will be found in a contiguous subarray of `k` scores because the list is sorted.
- Detailed breakdown:
  1. Sort the list of scores in ascending order.
  2. Initialize the minimum difference with the difference between the last and first element of the first `k` scores.
  3. Slide a window of size `k` over the sorted list to find the minimum difference.

```cpp
int minimumDifference(std::vector<int>& scores, int k) {
    std::sort(scores.begin(), scores.end());
    int minDiff = scores[k - 1] - scores[0];
    for (int i = 1; i <= scores.size() - k; ++i) {
        int diff = scores[i + k - 1] - scores[i];
        minDiff = std::min(minDiff, diff);
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of scores. The subsequent loop has a complexity of $O(n - k + 1)$, which simplifies to $O(n)$.
> - **Space Complexity:** $O(1)$ if we consider the input list as part of the space complexity, otherwise $O(n)$ for sorting in the worst case.
> - **Optimality proof:** This approach is optimal because it takes advantage of the fact that the minimum difference will be found in a contiguous subarray of `k` scores after sorting, reducing the search space significantly.

### Final Notes

**Learning Points:**
- The importance of sorting in reducing the search space for finding minimum or maximum differences.
- The concept of sliding windows to efficiently find the minimum or maximum of a certain size of subarray.

**Mistakes to Avoid:**
- Not considering the impact of sorting on the overall time complexity.
- Failing to recognize that the minimum difference will be in a contiguous subarray of `k` scores after sorting.

This problem demonstrates the power of sorting and sliding window techniques in solving problems related to finding minimum or maximum differences within a certain window size.