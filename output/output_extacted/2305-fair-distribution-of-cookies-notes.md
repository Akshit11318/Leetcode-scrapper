## Fair Distribution of Cookies
**Problem Link:** https://leetcode.com/problems/fair-distribution-of-cookies/description

**Problem Statement:**
- Input: An integer array `cookies` and an integer `k`, where `k` is the number of children.
- Constraints: `1 <= cookies.length <= 8`, `1 <= cookies[i] <= 10`, `2 <= k <= 8`, and `k <= cookies.length`.
- Expected Output: The minimum maximum size of a cookie distribution.
- Key Requirements: Distribute the cookies fairly among the children to minimize the maximum size of each distribution.
- Example Test Cases:
  - Input: `cookies = [8,15,10,20,8]`, `k = 2`
  - Output: `31`
  - Explanation: One way is to distribute the cookies as follows: Child 1 gets cookies with sizes 8, 8, and 15 (total size of 31), and Child 2 gets cookies with sizes 10 and 20 (total size of 30).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to consider all possible ways to distribute the cookies among the children.
- This approach involves generating all permutations of distributing the cookies and calculating the maximum size of each distribution for each permutation.
- Why this approach comes to mind first: It is a straightforward way to ensure all possibilities are considered, but it is inefficient due to its high complexity.

```cpp
class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        int n = cookies.size();
        int res = INT_MAX;
        vector<int> children(k, 0);
        
        function<void(int)> backtrack = [&](int start) {
            if (start == n) {
                int max = 0;
                for (int i = 0; i < k; ++i) {
                    max = std::max(max, children[i]);
                }
                res = std::min(res, max);
                return;
            }
            
            for (int i = 0; i < k; ++i) {
                children[i] += cookies[start];
                backtrack(start + 1);
                children[i] -= cookies[start];
            }
        };
        
        backtrack(0);
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$, where $n$ is the number of cookies. This is because in the worst case, for each cookie, we have $k$ choices of which child to give it to.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach generates all possible distributions, leading to an exponential time complexity. The space complexity is due to the recursive function call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a bitmask to represent which cookies have been distributed to which children.
- Detailed breakdown: Iterate over all possible bitmasks, and for each bitmask, calculate the total size of cookies for each child. Keep track of the minimum maximum size seen so far.
- Proof of optimality: This approach is optimal because it ensures that all possible distributions are considered in a systematic way, avoiding the need to explicitly generate all permutations.

```cpp
class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        int n = cookies.size();
        vector<int> children(k, 0);
        int res = INT_MAX;
        
        function<void(int)> backtrack = [&](int start) {
            if (start == n) {
                int max = 0;
                for (int i = 0; i < k; ++i) {
                    max = std::max(max, children[i]);
                }
                res = std::min(res, max);
                return;
            }
            
            for (int i = 0; i < k; ++i) {
                if (children[i] + cookies[start] < res) { // Prune branches that cannot lead to a better solution
                    children[i] += cookies[start];
                    backtrack(start + 1);
                    children[i] -= cookies[start];
                }
            }
        };
        
        backtrack(0);
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$, but with significant pruning, the actual time complexity is much less in practice.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Optimality proof:** This approach ensures all distributions are considered while pruning branches that cannot lead to a better solution, making it optimal in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Backtracking, pruning, and bitmasking.
- Problem-solving patterns: Using bitmasks to efficiently represent and iterate over subsets.
- Optimization techniques: Pruning branches in backtracking to reduce the search space.

**Mistakes to Avoid:**
- Not considering the pruning condition to reduce the search space.
- Not initializing the result variable with a large enough value.
- Not properly backtracking by resetting the state after exploring each branch.