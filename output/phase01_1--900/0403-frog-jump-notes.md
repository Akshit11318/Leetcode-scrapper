## Frog Jump
**Problem Link:** [https://leetcode.com/problems/frog-jump/description](https://leetcode.com/problems/frog-jump/description)

**Problem Statement:**
- Input format and constraints: The function takes an array `stones` of integers representing the positions of stones in a river and an integer `k` representing the maximum jump length of a frog. The function should return a boolean indicating whether the frog can jump to the last stone.
- Expected output format: A boolean value indicating whether the frog can jump to the last stone.
- Key requirements and edge cases to consider:
  - The frog can only jump to the next stone if the distance is less than or equal to `k`.
  - The frog can only jump to a stone if it is not already occupied by another frog.
- Example test cases with explanations:
  - `canCross([0,1,3,5,6,8,12,17], 2)` returns `true` because the frog can jump from stone 0 to stone 1, then to stone 3, then to stone 6, then to stone 8, then to stone 12, and finally to stone 17.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible jump combinations and check if the frog can reach the last stone.
- Step-by-step breakdown of the solution:
  1. Start at the first stone.
  2. Try all possible jumps from the current stone.
  3. If a jump is successful, move to the next stone and repeat step 2.
  4. If no jump is successful, backtrack to the previous stone and try a different jump.
- Why this approach comes to mind first: It is a simple and intuitive approach to try all possible combinations.

```cpp
class Solution {
public:
    bool canCross(vector<int>& stones, int k) {
        int n = stones.size();
        vector<bool> visited(n, false);
        return dfs(stones, 0, k, visited);
    }
    
    bool dfs(vector<int>& stones, int i, int k, vector<bool>& visited) {
        if (i == stones.size() - 1) return true;
        if (visited[i]) return false;
        visited[i] = true;
        for (int j = i + 1; j < stones.size(); j++) {
            if (stones[j] - stones[i] <= k) {
                if (dfs(stones, j, k, visited)) return true;
            }
        }
        visited[i] = false;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because in the worst case, we try all possible combinations of jumps.
> - **Space Complexity:** $O(n)$ because we use a recursive call stack of size $n$.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of jumps, resulting in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use memoization to store the results of subproblems and avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Create a memoization table to store the results of subproblems.
  2. Start at the first stone and try all possible jumps.
  3. If a jump is successful, move to the next stone and repeat step 2.
  4. If no jump is successful, backtrack to the previous stone and try a different jump.
- Proof of optimality: The optimal solution has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: The problem requires trying all possible combinations of jumps, resulting in a time complexity of at least $O(n^2)$.

```cpp
class Solution {
public:
    bool canCross(vector<int>& stones, int k) {
        int n = stones.size();
        unordered_map<int, unordered_set<int>> memo;
        return dfs(stones, 0, k, memo);
    }
    
    bool dfs(vector<int>& stones, int i, int k, unordered_map<int, unordered_set<int>>& memo) {
        if (i == stones.size() - 1) return true;
        if (memo.find(i) != memo.end() && memo[i].find(k) != memo[i].end()) return false;
        for (int j = i + 1; j < stones.size(); j++) {
            if (stones[j] - stones[i] <= k) {
                if (dfs(stones, j, stones[j] - stones[i], memo)) return true;
            }
        }
        if (memo.find(i) == memo.end()) memo[i] = unordered_set<int>();
        memo[i].insert(k);
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we try all possible combinations of jumps and use memoization to store the results of subproblems.
> - **Space Complexity:** $O(n^2)$ because we use a memoization table of size $n^2$.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization, depth-first search.
- Problem-solving patterns identified: Using memoization to store the results of subproblems and avoid redundant calculations.
- Optimization techniques learned: Using memoization to reduce the time complexity of a problem.
- Similar problems to practice: Other problems that involve trying all possible combinations of jumps, such as the "Jump Game" problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the memoization table, or using an incorrect data structure to store the results of subproblems.
- Edge cases to watch for: The case where the input array is empty, or the case where the frog cannot jump to the next stone.
- Performance pitfalls: Using a recursive approach without memoization, resulting in an exponential time complexity.
- Testing considerations: Testing the function with different input arrays and jump lengths to ensure that it works correctly in all cases.