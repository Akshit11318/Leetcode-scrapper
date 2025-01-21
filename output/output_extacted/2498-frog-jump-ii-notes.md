## Frog Jump II
**Problem Link:** https://leetcode.com/problems/frog-jump-ii/description

**Problem Statement:**
- Given an array of integers `stones` representing stones along a river, and an integer `k` representing the maximum number of steps the frog can jump, determine if the frog can reach the last stone.
- Input format: `stones` array and `k` integer.
- Constraints: `1 <= stones.length <= 1000`, `0 <= stones[i] <= 10^9`, `0 <= k <= 1000`.
- Expected output: `true` if the frog can reach the last stone, `false` otherwise.
- Key requirements: The frog can jump to a stone if the difference between the current stone and the previous stone is within `k` steps.
- Edge cases: The frog starts at the first stone, and there are no stones before the first stone.

**Example Test Cases:**
- `stones = [0,2], k = 2` returns `true` because the frog can jump from the first stone to the second stone.
- `stones = [0,3,5,6,8,12,17], k = 2` returns `false` because the frog cannot jump from the first stone to the second stone.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible jump combinations and see if the frog can reach the last stone.
- The brute force approach involves using a recursive function to try all possible jumps from each stone.
- This approach comes to mind first because it is a straightforward way to solve the problem, but it is not efficient due to its high time complexity.

```cpp
class Solution {
public:
    bool canCross(vector<int>& stones, int k) {
        unordered_set<int> stoneSet(stones.begin(), stones.end());
        return canJump(stoneSet, stones.back(), k);
    }
    
    bool canJump(unordered_set<int>& stoneSet, int target, int k) {
        if (target == 0) return true;
        for (int i = max(1, target - k); i <= min(target - 1, target + k); i++) {
            if (stoneSet.find(i) != stoneSet.end() && canJump(stoneSet, i, k)) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n \cdot k})$ where $n$ is the number of stones and $k$ is the maximum number of steps the frog can jump. This is because in the worst case, the frog can try all possible jumps from each stone.
> - **Space Complexity:** $O(n)$ where $n$ is the number of stones. This is because we need to store all the stones in a set for efficient lookup.
> - **Why these complexities occur:** The high time complexity occurs because we are trying all possible jump combinations, which leads to exponential time complexity. The space complexity occurs because we need to store all the stones in a set.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use memoization to store the results of subproblems.
- We can use a recursive function with memoization to try all possible jumps from each stone, but store the results of subproblems to avoid redundant computation.
- This approach is optimal because it reduces the time complexity from exponential to polynomial.

```cpp
class Solution {
public:
    bool canCross(vector<int>& stones, int k) {
        unordered_set<int> stoneSet(stones.begin(), stones.end());
        unordered_map<int, unordered_map<int, bool>> memo;
        return canJump(stoneSet, memo, stones.back(), k);
    }
    
    bool canJump(unordered_set<int>& stoneSet, unordered_map<int, unordered_map<int, bool>>& memo, int target, int k) {
        if (target == 0) return true;
        if (memo.find(target) != memo.end() && memo[target].find(k) != memo[target].end()) {
            return memo[target][k];
        }
        for (int i = max(1, target - k); i <= min(target - 1, target + k); i++) {
            if (stoneSet.find(i) != stoneSet.end() && canJump(stoneSet, memo, i, k)) {
                memo[target][k] = true;
                return true;
            }
        }
        memo[target][k] = false;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ where $n$ is the number of stones and $k$ is the maximum number of steps the frog can jump. This is because we are trying all possible jumps from each stone, but storing the results of subproblems to avoid redundant computation.
> - **Space Complexity:** $O(n \cdot k)$ where $n$ is the number of stones and $k$ is the maximum number of steps the frog can jump. This is because we need to store the results of subproblems in a memoization table.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from exponential to polynomial, and it is not possible to further reduce the time complexity without using a different algorithm.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: memoization, recursive functions, and dynamic programming.
- Problem-solving patterns identified: using memoization to store the results of subproblems to avoid redundant computation.
- Optimization techniques learned: using memoization to reduce the time complexity of a recursive function.
- Similar problems to practice: other problems that involve using memoization to store the results of subproblems.

**Mistakes to Avoid:**
- Common implementation errors: not using memoization to store the results of subproblems, which can lead to exponential time complexity.
- Edge cases to watch for: the frog starts at the first stone, and there are no stones before the first stone.
- Performance pitfalls: not using memoization to store the results of subproblems, which can lead to exponential time complexity.
- Testing considerations: testing the function with different inputs to ensure it works correctly.