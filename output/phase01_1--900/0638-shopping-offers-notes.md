## Shopping Offers
**Problem Link:** https://leetcode.com/problems/shopping-offers/description

**Problem Statement:**
- Input format and constraints: Given a list of `prices` of items and a list of `specials` where each special is a list of items and a price for the special offer, find the minimum cost to buy all items.
- Expected output format: The minimum cost.
- Key requirements and edge cases to consider: The list of prices and specials, handling cases where items are not in any special offer, and ensuring all items are bought.
- Example test cases with explanations:
  - Example 1: prices = [2,5], specials = [[3,0,5],[1,2,10]], return 14.
  - Example 2: prices = [0,0,0], specials = [[1,1,1,0]], return 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of buying items at their individual prices or using special offers.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of buying items.
  2. For each combination, calculate the total cost.
  3. Keep track of the minimum cost found.
- Why this approach comes to mind first: It's a straightforward method to consider all possibilities.

```cpp
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int n = price.size();
        int res = INT_MAX;
        dfs(price, special, needs, 0, res);
        return res;
    }
    
    void dfs(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, int cost, int& res) {
        res = min(res, cost + getCost(price, needs));
        for (auto& s : special) {
            vector<int> clone = needs;
            bool canUse = true;
            for (int i = 0; i < s.size() - 1; ++i) {
                clone[i] -= s[i];
                if (clone[i] < 0) canUse = false;
            }
            if (canUse) dfs(price, special, clone, cost + s.back(), res);
        }
    }
    
    int getCost(vector<int>& price, vector<int>& needs) {
        int cost = 0;
        for (int i = 0; i < needs.size(); ++i) {
            cost += needs[i] * price[i];
        }
        return cost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$ where $n$ is the number of items and $m$ is the number of special offers. This is because in the worst case, we might end up exploring all possible combinations of buying items and using special offers.
> - **Space Complexity:** $O(n)$ for the recursive call stack and cloning the needs vector.
> - **Why these complexities occur:** The brute force approach considers all possible scenarios, leading to exponential time complexity. The space complexity is due to the recursive call stack and temporary vectors created during the DFS.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use memoization to store the results of subproblems to avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Implement a recursive DFS function similar to the brute force approach.
  2. Use a hashmap to store the minimum cost for each subproblem (represented by the current needs vector).
  3. Before calculating the cost for a subproblem, check if it's already in the hashmap. If it is, return the stored result.
- Proof of optimality: This approach ensures that each subproblem is solved only once, reducing the time complexity significantly.

```cpp
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int n = price.size();
        unordered_map<string, int> memo;
        return dfs(price, special, needs, memo);
    }
    
    int dfs(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, unordered_map<string, int>& memo) {
        string key;
        for (int need : needs) key += to_string(need) + ",";
        if (memo.count(key)) return memo[key];
        
        int res = getCost(price, needs);
        for (auto& s : special) {
            vector<int> clone = needs;
            bool canUse = true;
            for (int i = 0; i < s.size() - 1; ++i) {
                clone[i] -= s[i];
                if (clone[i] < 0) canUse = false;
            }
            if (canUse) res = min(res, dfs(price, special, clone, memo) + s.back());
        }
        memo[key] = res;
        return res;
    }
    
    int getCost(vector<int>& price, vector<int>& needs) {
        int cost = 0;
        for (int i = 0; i < needs.size(); ++i) {
            cost += needs[i] * price[i];
        }
        return cost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot 2^n)$ where $m$ is the number of special offers and $n$ is the number of items. This is because we explore each special offer for each subproblem, but we avoid redundant calculations through memoization.
> - **Space Complexity:** $O(n \cdot 2^n)$ for the memoization hashmap and the recursive call stack.
> - **Optimality proof:** This approach is optimal because it ensures that each subproblem is solved only once, minimizing the number of calculations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **Dynamic Programming** (memoization) and **Depth-First Search**.
- Problem-solving patterns identified: Breaking down problems into smaller subproblems and using memoization to avoid redundant calculations.
- Optimization techniques learned: Using memoization to store the results of subproblems.
- Similar problems to practice: Other problems that involve breaking down into subproblems and using dynamic programming, such as **Coin Change** or **Partition Equal Subset Sum**.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for negative values in the needs vector when applying special offers.
- Edge cases to watch for: Handling cases where the input vectors are empty or where the special offers are not valid (e.g., a special offer with a negative price).
- Performance pitfalls: Not using memoization, leading to exponential time complexity.
- Testing considerations: Test the solution with various input cases, including edge cases and large inputs to ensure the memoization is working correctly.