## Paint House III
**Problem Link:** https://leetcode.com/problems/paint-house-iii/description

**Problem Statement:**
- Input format and constraints: The problem requires painting `n` houses with `m` colors, each house having a specific cost to paint with a certain color. The goal is to find the minimum cost to paint all houses with the given constraints.
- Expected output format: The minimum cost to paint all houses.
- Key requirements and edge cases to consider: The houses must be painted such that no two adjacent houses have the same color, and each house must be painted with one of the `m` colors.
- Example test cases with explanations: 
    - For example, given `n = 3`, `m = 3`, `street = [0,1,0]`, `cost = [[1,5,3],[2,9,1],[3,1,2],[4,2,5],[5,3,3]]`, `len = 3`, the minimum cost to paint all houses is `9`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of colors for each house and calculating the total cost for each combination.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of colors for each house.
    2. Calculate the total cost for each combination.
    3. Keep track of the minimum cost found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs due to its exponential time complexity.

```cpp
int minCost(vector<vector<int>>& cost, vector<int>& street, int m, int n, int len) {
    int min_cost = INT_MAX;
    vector<vector<int>> combinations;
    generateCombinations(combinations, m, n);
    for (auto combination : combinations) {
        int total_cost = 0;
        for (int i = 0; i < n; i++) {
            total_cost += cost[street[i]][combination[i]];
        }
        min_cost = min(min_cost, total_cost);
    }
    return min_cost;
}

void generateCombinations(vector<vector<int>>& combinations, int m, int n) {
    vector<int> current_combination(n, 0);
    generateCombinationsRecursive(combinations, current_combination, m, n, 0);
}

void generateCombinationsRecursive(vector<vector<int>>& combinations, vector<int>& current_combination, int m, int n, int index) {
    if (index == n) {
        combinations.push_back(current_combination);
        return;
    }
    for (int i = 0; i < m; i++) {
        current_combination[index] = i;
        generateCombinationsRecursive(combinations, current_combination, m, n, index + 1);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^n)$, where `m` is the number of colors and `n` is the number of houses. This is because we generate all possible combinations of colors for each house.
> - **Space Complexity:** $O(m^n)$, where `m` is the number of colors and `n` is the number of houses. This is because we store all possible combinations of colors for each house.
> - **Why these complexities occur:** The brute force approach has exponential time and space complexities because it tries all possible combinations of colors for each house, resulting in a large number of possibilities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming. We can use a 2D array `dp` where `dp[i][j]` represents the minimum cost to paint the first `i` houses with the `i-th` house painted with color `j`.
- Detailed breakdown of the approach: 
    1. Initialize the `dp` array with the costs of painting the first house with each color.
    2. For each subsequent house, calculate the minimum cost to paint the house with each color by considering the minimum cost to paint the previous house with a different color.
    3. Keep track of the minimum cost to paint all houses.
- Proof of optimality: The dynamic programming approach is optimal because it considers all possible combinations of colors for each house and calculates the minimum cost to paint all houses.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n \cdot m^2)$, which is the best possible time complexity for this problem.

```cpp
int minCost(vector<vector<int>>& cost, vector<int>& street, int m, int n, int len) {
    vector<vector<int>> dp(n, vector<int>(m, INT_MAX));
    // Initialize the dp array with the costs of painting the first house with each color
    for (int j = 0; j < m; j++) {
        dp[0][j] = cost[street[0]][j];
    }
    // Calculate the minimum cost to paint each house with each color
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < m; k++) {
                if (j != k) {
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + cost[street[i]][j]);
                }
            }
        }
    }
    // Find the minimum cost to paint all houses
    int min_cost = INT_MAX;
    for (int j = 0; j < m; j++) {
        min_cost = min(min_cost, dp[n - 1][j]);
    }
    return min_cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where `n` is the number of houses and `m` is the number of colors. This is because we use a 2D array `dp` to store the minimum cost to paint each house with each color.
> - **Space Complexity:** $O(n \cdot m)$, where `n` is the number of houses and `m` is the number of colors. This is because we use a 2D array `dp` to store the minimum cost to paint each house with each color.
> - **Optimality proof:** The dynamic programming approach is optimal because it considers all possible combinations of colors for each house and calculates the minimum cost to paint all houses.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the solutions to these sub-problems in a 2D array.
- Optimization techniques learned: Memoization, dynamic programming.
- Similar problems to practice: Paint House, Paint House II.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not considering all possible combinations of colors for each house.
- Edge cases to watch for: The number of houses or colors is zero, the costs of painting the houses are negative.
- Performance pitfalls: Not using memoization or dynamic programming, resulting in exponential time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure it works correctly.