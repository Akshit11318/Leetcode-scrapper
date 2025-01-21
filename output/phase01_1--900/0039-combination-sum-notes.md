## Combination Sum
**Problem Link:** [https://leetcode.com/problems/combination-sum/description](https://leetcode.com/problems/combination-sum/description)

**Problem Statement:**
- Input format and constraints: The problem takes an array of distinct integers `candidates` and a target integer `target` as input, where `1 <= candidates.length <= 30`, `1 <= candidates[i] <= 200`, and `1 <= target <= 500`. The task is to find all unique combinations in `candidates` where the candidate numbers sum up to `target`. The same number may be used an unlimited number of times.
- Expected output format: A list of lists, where each sublist contains a combination of numbers that sum up to `target`.
- Key requirements and edge cases to consider:
  - All numbers (including `target`) will be positive integers.
  - The solution set must not contain duplicate combinations.
  - The input array `candidates` is not sorted.
- Example test cases with explanations:
  - Input: `candidates = [2,3,6,7], target = 7`
    Output: `[[2,2,3],[7]]`
  - Input: `candidates = [2,3,5], target = 8`
    Output: `[[2,2,2,2],[2,3,3],[3,5]]`
  - Input: `candidates = [2], target = 1`
    Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach to solving this problem is to generate all possible combinations of numbers from the `candidates` array and check if their sum equals the `target`.
- Step-by-step breakdown of the solution:
  1. Start with an empty combination.
  2. For each number in `candidates`, add it to the current combination and recursively generate all combinations including this number.
  3. If the sum of the current combination equals `target`, add it to the result list.
  4. If the sum exceeds `target`, stop exploring this branch as adding more numbers will only increase the sum.
- Why this approach comes to mind first: It's a simple, intuitive way to explore all possibilities.

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, candidates, target, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int remain, int start) {
        if (remain == 0) {
            result.push_back(current);
        } else if (remain < 0) {
            return;
        } else {
            for (int i = start; i < candidates.size(); i++) {
                current.push_back(candidates[i]);
                backtrack(result, current, candidates, remain - candidates[i], i); // Note: i, not i + 1, to allow unlimited use of each number
                current.pop_back();
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N^{\frac{target}{min(candidates)}})$, where $N$ is the number of candidates. This is because in the worst case, we might have to explore a very deep tree if `target` is large and the smallest candidate is 1.
> - **Space Complexity:** $O(target/min(candidates))$, as this is the maximum depth of the recursion tree, which translates to the space needed on the call stack.
> - **Why these complexities occur:** The recursive nature of the solution and the need to explore all possible combinations lead to these complexities.

---

### Optimal Approach (Required)

The provided brute force solution is actually quite efficient for this problem, given the constraints. It uses a form of backtracking to efficiently explore all combinations without unnecessary repetition. However, it's worth noting that this problem doesn't have a significantly more efficient algorithm due to its nature, which requires exploring all possible combinations that sum up to the target. The given solution is optimal in the sense that it avoids redundant calculations by allowing the use of each number starting from the current index `i`, not `i+1`, thus enabling the combination of the same number multiple times.

The **time complexity** remains $O(N^{\frac{target}{min(candidates)}})$ and the **space complexity** remains $O(target/min(candidates))$ due to the recursive call stack. This is because the problem inherently requires exploring all possible combinations, and the given solution does so in a manner that minimizes unnecessary explorations.

### Final Notes

**Learning Points:**
- The importance of backtracking in solving combinatorial problems.
- How to efficiently explore all combinations without repetition.
- Understanding the trade-offs between time and space complexity in recursive solutions.

**Mistakes to Avoid:**
- Incorrectly implementing the recursive function, leading to infinite loops or missing combinations.
- Not considering the possibility of using each number more than once.
- Failing to optimize the solution by stopping the exploration when the sum exceeds the target.

This problem is a classic example of a combinatorial problem that can be solved using backtracking, and understanding the solution to this problem can help in solving similar problems involving combinations and permutations.