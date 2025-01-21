## Combination Sum II
**Problem Link:** https://leetcode.com/problems/combination-sum-ii/description

**Problem Statement:**
- Input: A `candidate` array of distinct integers and a `target` integer.
- Constraints: Each number in `candidates` may only be used once in the combination.
- Expected Output: All unique combinations in `candidates` where the candidate numbers sum to `target`.
- Key Requirements and Edge Cases:
  - The same number may not be used more than once in a combination.
  - All numbers (including `target`) are positive integers.
  - Example Test Cases:
    - Input: `candidates = [10,1,2,7,6,1,5], target = 8`
      Output: `[1,1,6], [1,2,5], [1,7], [2,6]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible combinations of numbers from the `candidates` array and checking which combinations sum up to the `target`.
- Step-by-step breakdown:
  1. Generate all possible subsets of the `candidates` array.
  2. For each subset, calculate the sum of its elements.
  3. If the sum equals the `target`, add the subset to the result list.
- Why this approach comes to mind first: It's a straightforward method to ensure all combinations are considered, but it's inefficient due to the large number of subsets.

```cpp
#include <vector>
#include <iostream>

void backtrack(std::vector<int>& candidates, int start, int target, std::vector<int>& path, std::vector<std::vector<int>>& result) {
    if (target < 0) return;
    if (target == 0) {
        result.push_back(path);
        return;
    }
    for (int i = start; i < candidates.size(); ++i) {
        // Skip duplicates
        if (i > start && candidates[i] == candidates[i-1]) continue;
        path.push_back(candidates[i]);
        backtrack(candidates, i + 1, target - candidates[i], path, result);
        path.pop_back();
    }
}

std::vector<std::vector<int>> combinationSum2(std::vector<int>& candidates, int target) {
    std::sort(candidates.begin(), candidates.end());
    std::vector<std::vector<int>> result;
    std::vector<int> path;
    backtrack(candidates, 0, target, path, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of candidates, due to generating all subsets.
> - **Space Complexity:** $O(n)$ for storing the current path and the result.
> - **Why these complexities occur:** The brute force approach generates an exponential number of subsets, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves using a **backtracking** approach with **pruning** to reduce unnecessary branches.
- Key Insight: Sort the `candidates` array and use a `start` index to track the current position in the array. This allows for skipping duplicates and pruning branches that exceed the `target`.
- Detailed Breakdown:
  1. Sort the `candidates` array.
  2. Initialize an empty result list and an empty path.
  3. Call the `backtrack` function with the initial parameters.
  4. In the `backtrack` function:
    - If the `target` becomes negative, return immediately (pruning).
    - If the `target` becomes zero, add the current path to the result list.
    - Iterate through the `candidates` array starting from the `start` index.
    - For each candidate, skip duplicates by checking if the current candidate is the same as the previous one.
    - Add the candidate to the current path and recursively call the `backtrack` function with the updated `target` and `start` index.
    - After the recursive call, remove the last added candidate from the path (backtracking).
- Proof of Optimality: This approach ensures that all unique combinations are found while minimizing the number of recursive calls.

```cpp
#include <vector>
#include <iostream>

void backtrack(std::vector<int>& candidates, int start, int target, std::vector<int>& path, std::vector<std::vector<int>>& result) {
    if (target < 0) return;
    if (target == 0) {
        result.push_back(path);
        return;
    }
    for (int i = start; i < candidates.size(); ++i) {
        // Skip duplicates
        if (i > start && candidates[i] == candidates[i-1]) continue;
        path.push_back(candidates[i]);
        backtrack(candidates, i + 1, target - candidates[i], path, result);
        path.pop_back();
    }
}

std::vector<std::vector<int>> combinationSum2(std::vector<int>& candidates, int target) {
    std::sort(candidates.begin(), candidates.end());
    std::vector<std::vector<int>> result;
    std::vector<int> path;
    backtrack(candidates, 0, target, path, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ in the worst case, but significantly reduced due to pruning.
> - **Space Complexity:** $O(n)$ for storing the current path and the result.
> - **Optimality proof:** The approach ensures that all unique combinations are found while minimizing the number of recursive calls.

---

### Final Notes

**Learning Points:**
- The importance of **pruning** in reducing unnecessary branches in backtracking algorithms.
- The use of **sorting** to facilitate skipping duplicates and pruning.
- The **backtracking** technique for solving combinatorial problems.

**Mistakes to Avoid:**
- Not skipping duplicates, leading to incorrect results.
- Not pruning branches that exceed the target, leading to inefficient computation.
- Not using sorting to facilitate the backtracking process.