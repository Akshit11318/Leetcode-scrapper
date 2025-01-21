## Maximum Score of Non-Overlapping Intervals
**Problem Link:** https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/description

**Problem Statement:**
- Input format: A list of intervals where each interval is a pair of integers `[start, end]` and a list of integers `scores` representing the score of each interval.
- Constraints: The input list of intervals and scores are of the same length. The start and end of each interval are distinct.
- Expected output format: The maximum score that can be achieved by selecting non-overlapping intervals.
- Key requirements and edge cases to consider: Intervals may overlap, and we need to select non-overlapping intervals to maximize the score. If there are no intervals, the maximum score is 0.
- Example test cases with explanations:
  - Example 1: Given `intervals = [[1,3],[2,4],[3,5],[6,7]]` and `scores = [2,3,1,4]`, the maximum score is 7 (by selecting intervals `[1,3]` and `[6,7]`).
  - Example 2: Given `intervals = [[1,3],[2,4],[4,6],[8,9]]` and `scores = [2,3,1,4]`, the maximum score is 7 (by selecting intervals `[1,3]` and `[8,9]` or `[2,4]` and `[8,9]`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of intervals and select the combination that yields the highest score without overlapping intervals.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of intervals.
  2. For each combination, check if the intervals are non-overlapping.
  3. If they are non-overlapping, calculate the total score for this combination.
  4. Keep track of the maximum score seen so far.
- Why this approach comes to mind first: It is a straightforward method to consider all possibilities, but it is inefficient due to the exponential number of combinations.

```cpp
#include <vector>
#include <algorithm>

int maxScore(std::vector<std::vector<int>>& intervals, std::vector<int>& scores) {
    int n = intervals.size();
    int maxScore = 0;
    
    for (int mask = 0; mask < (1 << n); ++mask) {
        int currentScore = 0;
        bool isNonOverlapping = true;
        std::vector<int> lastEnd;
        
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                if (!lastEnd.empty() && intervals[i][0] < lastEnd.back()) {
                    isNonOverlapping = false;
                    break;
                }
                currentScore += scores[i];
                lastEnd.push_back(intervals[i][1]);
            }
        }
        
        if (isNonOverlapping) {
            maxScore = std::max(maxScore, currentScore);
        }
    }
    
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of intervals. This is because we generate all possible combinations of intervals (which is $2^n$) and for each combination, we check if the intervals are non-overlapping (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, for storing the last end of the selected intervals.
> - **Why these complexities occur:** The brute force approach is inefficient because it considers all possible combinations of intervals, leading to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to sort the intervals by their end points and then use a dynamic programming array `dp` where `dp[i]` represents the maximum score that can be achieved by considering the first `i` intervals.
- Detailed breakdown of the approach:
  1. Sort the intervals by their end points.
  2. Initialize a dynamic programming array `dp` of size `n`, where `n` is the number of intervals.
  3. For each interval, find the previous interval that does not overlap with it and update `dp[i]` accordingly.
- Proof of optimality: This approach is optimal because it considers all possible non-overlapping intervals and selects the ones that yield the maximum score.

```cpp
#include <vector>
#include <algorithm>

int maxScore(std::vector<std::vector<int>>& intervals, std::vector<int>& scores) {
    int n = intervals.size();
    std::vector<std::pair<int, int>> intervalScores;
    
    for (int i = 0; i < n; ++i) {
        intervalScores.emplace_back(intervals[i][1], scores[i]);
    }
    
    std::sort(intervalScores.begin(), intervalScores.end());
    
    std::vector<int> dp(n);
    dp[0] = intervalScores[0].second;
    
    for (int i = 1; i < n; ++i) {
        int maxVal = 0;
        for (int j = 0; j < i; ++j) {
            if (intervalScores[j].first <= intervalScores[i].first) {
                maxVal = std::max(maxVal, dp[j]);
            }
        }
        dp[i] = std::max(maxVal + intervalScores[i].second, dp[i-1]);
    }
    
    return dp.back();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of intervals. This is because we sort the intervals and then use a nested loop to fill up the dynamic programming array.
> - **Space Complexity:** $O(n)$, for storing the dynamic programming array.
> - **Optimality proof:** This approach is optimal because it considers all possible non-overlapping intervals and selects the ones that yield the maximum score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, sorting, and greedy algorithms.
- Problem-solving patterns identified: The problem can be solved by breaking it down into smaller sub-problems and solving each sub-problem only once.
- Optimization techniques learned: We can optimize the brute force approach by using dynamic programming to avoid redundant calculations.
- Similar problems to practice: Other problems that involve selecting non-overlapping intervals, such as the "Non-Overlapping Intervals" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input list.
- Edge cases to watch for: The input list may be empty, or the intervals may not overlap.
- Performance pitfalls: The brute force approach can be very slow for large inputs.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure that it works correctly.