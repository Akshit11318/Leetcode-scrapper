## Factor Combinations
**Problem Link:** https://leetcode.com/problems/factor-combinations/description

**Problem Statement:**
- Input format and constraints: The input is a positive integer `n`, and the task is to find all possible combinations of its factors.
- Expected output format: The output should be a list of lists, where each sublist contains a combination of factors that multiply to `n`.
- Key requirements and edge cases to consider: The input `n` is a positive integer, and the output should include all possible combinations of factors, including the number itself and 1.
- Example test cases with explanations: For `n = 12`, the output should be `[[2, 2, 3], [2, 6], [3, 4], [12]]`, which are all possible combinations of factors that multiply to 12.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solving this problem is to generate all possible combinations of factors by iterating through all numbers from 1 to `n` and checking if they are factors of `n`.
- Step-by-step breakdown of the solution: 
  1. Initialize an empty list to store the result.
  2. Iterate through all numbers from 1 to `n`.
  3. For each number, check if it is a factor of `n`.
  4. If it is a factor, recursively generate all combinations of factors for the remaining number.
  5. Add the current factor to each combination and add it to the result.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large inputs due to the recursive nature and the need to check all numbers.

```cpp
class Solution {
public:
    vector<vector<int>> factorCombinations(int n) {
        vector<vector<int>> result;
        vector<int> current;
        dfs(n, 2, current, result);
        return result;
    }
    
    void dfs(int n, int start, vector<int>& current, vector<vector<int>>& result) {
        if (n == 1) {
            if (!current.empty()) {
                result.push_back(current);
            }
            return;
        }
        for (int i = start; i <= n; i++) {
            if (n % i == 0) {
                current.push_back(i);
                dfs(n / i, i, current, result);
                current.pop_back();
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the input number. This is because in the worst case, we need to generate all possible combinations of factors, which can be exponential in the number of factors.
> - **Space Complexity:** $O(n)$, where $n$ is the input number. This is because we need to store the recursive call stack and the current combination of factors.
> - **Why these complexities occur:** The time complexity is high due to the recursive nature of the solution and the need to generate all possible combinations of factors. The space complexity is relatively low because we only need to store the current combination of factors and the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a depth-first search (DFS) approach with backtracking to generate all combinations of factors. This approach is more efficient than the brute force approach because it prunes branches that will not lead to a valid combination of factors.
- Detailed breakdown of the approach: 
  1. Initialize an empty list to store the result.
  2. Start the DFS from the number 2, which is the smallest prime number.
  3. For each number, check if it is a factor of the remaining number.
  4. If it is a factor, recursively generate all combinations of factors for the remaining number.
  5. Add the current factor to each combination and add it to the result.
- Proof of optimality: The DFS approach with backtracking is optimal because it generates all possible combinations of factors without duplicates and without missing any valid combinations.

```cpp
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(n, 2, path, res);
        return res;
    }
    
    void dfs(int n, int start, vector<int>& path, vector<vector<int>>& res) {
        if (n == 1) {
            if (!path.empty()) {
                res.push_back(path);
            }
            return;
        }
        for (int i = start; i * i <= n; i++) {
            if (n % i == 0) {
                path.push_back(i);
                dfs(n / i, i, path, res);
                path.pop_back();
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{\sqrt{n}})$, where $n$ is the input number. This is because in the worst case, we need to generate all possible combinations of factors, which can be exponential in the square root of the number of factors.
> - **Space Complexity:** $O(\sqrt{n})$, where $n$ is the input number. This is because we need to store the recursive call stack and the current combination of factors.
> - **Optimality proof:** The DFS approach with backtracking is optimal because it generates all possible combinations of factors without duplicates and without missing any valid combinations. The time complexity is improved by only iterating up to the square root of the remaining number, which reduces the number of recursive calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) with backtracking, recursive programming.
- Problem-solving patterns identified: Using DFS to generate all combinations of factors, using backtracking to prune branches that will not lead to a valid combination.
- Optimization techniques learned: Pruning branches that will not lead to a valid combination, iterating only up to the square root of the remaining number.
- Similar problems to practice: Generating all combinations of a given set, generating all permutations of a given set.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not pruning branches that will not lead to a valid combination.
- Edge cases to watch for: Handling the case where the input number is 1, handling the case where the input number is a prime number.
- Performance pitfalls: Not using backtracking to prune branches that will not lead to a valid combination, iterating beyond the square root of the remaining number.
- Testing considerations: Testing the function with different input numbers, testing the function with edge cases.