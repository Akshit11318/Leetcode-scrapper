## Visit Array Positions to Maximize Score
**Problem Link:** https://leetcode.com/problems/visit-array-positions-to-maximize-score/description

**Problem Statement:**
- Input: A non-empty array of integers `arr` and an integer `k`.
- Output: The maximum score that can be achieved.
- Key requirements: Visit each position in `arr` exactly once, and for each position `i`, the score is `arr[i] * min(i, k)`.
- Edge cases: `arr` can have any length, and `k` can be any positive integer.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of the array and calculate the score for each permutation.
- Step-by-step breakdown:
  1. Generate all permutations of the array.
  2. For each permutation, calculate the score by iterating over each position `i` and multiplying the value at that position by `min(i, k)`.
  3. Keep track of the maximum score found.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& arr, int k) {
    int n = arr.size();
    int maxScore = 0;
    std::vector<int> perm(n);
    for (int i = 0; i < n; i++) perm[i] = i;

    do {
        int score = 0;
        for (int i = 0; i < n; i++) {
            score += arr[perm[i]] * std::min(i, k);
        }
        maxScore = std::max(maxScore, score);
    } while (std::next_permutation(perm.begin(), perm.end()));

    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the array, because we generate all permutations of the array.
> - **Space Complexity:** $O(n)$, because we need to store the current permutation.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the array, which results in a time complexity of $O(n!)$.

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to maximize the score. We want to place the largest numbers in the positions that will give us the highest score.
- Detailed breakdown:
  1. Sort the array in descending order.
  2. Initialize the score to 0.
  3. Iterate over the sorted array, and for each number, multiply it by `min(i, k)` and add it to the score.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& arr, int k) {
    int n = arr.size();
    std::sort(arr.rbegin(), arr.rend());
    int score = 0;
    for (int i = 0; i < n; i++) {
        score += arr[i] * std::min(i + 1, k);
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the array, because we sort the array.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the score.
> - **Optimality proof:** This approach is optimal because we are placing the largest numbers in the positions that will give us the highest score.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, sorting.
- Problem-solving patterns identified: Maximization problems, permutation problems.
- Optimization techniques learned: Avoiding unnecessary computations, using greedy approaches.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables.
- Edge cases to watch for: Empty arrays, arrays with a single element.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Test with small and large inputs, test with edge cases.