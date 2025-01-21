## Jump Game

**Problem Link:** https://leetcode.com/problems/jump-game/description

**Problem Statement:**
- Input: An array of non-negative integers `nums`, where `nums[i]` represents the maximum jump length at index `i`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^4`.
- Expected Output: A boolean indicating whether you can reach the last index from the first index.
- Key Requirements:
  - The goal is to determine if there exists a sequence of jumps from the first index to the last index.
  - We can jump at most `nums[i]` steps from index `i`.
- Example Test Cases:
  - `nums = [2,3,1,1,4]`, Output: `true`
  - `nums = [3,2,1,0,4]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible jump sequences from the first index to see if any sequence reaches the last index.
- This approach involves a depth-first search (DFS) strategy, exploring all possible jumps from each index.
- Why this approach comes to mind first: It directly addresses the problem statement by trying all possible solutions.

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        return dfs(nums, 0);
    }
    
    bool dfs(vector<int>& nums, int start) {
        if (start >= nums.size() - 1) return true;
        
        for (int i = 1; i <= nums[start]; i++) {
            if (dfs(nums, start + i)) return true;
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of elements in `nums`. This is because in the worst case, we might have to try all possible jump sequences, and each sequence can branch out into multiple possibilities.
> - **Space Complexity:** $O(n)$, due to the recursion stack in the worst case.
> - **Why these complexities occur:** The exponential time complexity is due to the brute force nature of trying all possible jump sequences without any optimization.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach, keeping track of the maximum reachable position as we iterate through the array.
- We initialize the maximum reachable position to 0 (the first index) and then iterate through the array. For each index, we update the maximum reachable position if the current index plus its jump value exceeds the current maximum reachable position.
- If at any point the current index exceeds the maximum reachable position, we return false because it means we cannot reach this index from any previous index.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best we can achieve since we must at least read the input array once.

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            if (i > maxReach) return false;
            maxReach = max(maxReach, i + nums[i]);
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum reachable position.
> - **Optimality proof:** This is the optimal solution because it achieves a linear time complexity, which is the minimum required to solve the problem since we must examine each element at least once.

---

### Final Notes

**Learning Points:**
- The importance of **greedy algorithms** in solving problems that involve making the locally optimal choice at each step to find a global optimum.
- The concept of **optimality** and how to prove that a solution is optimal.
- The trade-off between **time and space complexity** and how to choose the right approach based on the problem constraints.

**Mistakes to Avoid:**
- Not considering the **base case** in recursive solutions.
- Not validating the **input** to handle edge cases.
- Not optimizing the solution for **performance** when dealing with large inputs.
- Not testing the solution thoroughly with **different test cases** to ensure correctness.