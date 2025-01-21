## Combinations
**Problem Link:** https://leetcode.com/problems/combinations/description

**Problem Statement:**
- Input format and constraints: Given two integers `n` and `k`, return all possible combinations of `k` numbers out of the range `[1, n]`.
- Expected output format: A list of lists, where each sublist is a combination of `k` numbers.
- Key requirements and edge cases to consider: 
  - `1 <= n <= 20`
  - `1 <= k <= n`
  - The solution should handle cases where `n` and `k` are small as well as cases where `n` and `k` are large.
- Example test cases with explanations: 
  - `n = 4`, `k = 2`: The output should be `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`.
  - `n = 1`, `k = 1`: The output should be `[[1]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible combinations of `k` numbers from the range `[1, n]` and then filter out the invalid combinations.
- Step-by-step breakdown of the solution: 
  1. Generate all possible combinations of `k` numbers from the range `[1, n]`.
  2. Filter out the invalid combinations.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> current;
        for (int i = 1; i <= n; i++) {
            current.push_back(i);
            if (current.size() == k) {
                result.push_back(current);
                current.pop_back();
            } else {
                vector<vector<int>> temp = combine(n, k - current.size());
                for (auto& t : temp) {
                    vector<int> temp2 = current;
                    temp2.insert(temp2.end(), t.begin(), t.end());
                    result.push_back(temp2);
                }
                current.pop_back();
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot \binom{n}{k})$ because in the worst case, we have to generate all possible combinations of `k` numbers from the range `[1, n]`.
> - **Space Complexity:** $O(k \cdot \binom{n}{k})$ because we need to store all possible combinations of `k` numbers from the range `[1, n]`.
> - **Why these complexities occur:** These complexities occur because we are generating all possible combinations of `k` numbers from the range `[1, n]`, which can be very large for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a backtracking approach to generate all possible combinations of `k` numbers from the range `[1, n]`.
- Detailed breakdown of the approach: 
  1. Start with an empty current combination.
  2. Try to add each number from the range `[1, n]` to the current combination.
  3. If the current combination has `k` numbers, add it to the result.
  4. Backtrack and try the next number.
- Proof of optimality: This approach is optimal because it generates all possible combinations of `k` numbers from the range `[1, n]` without generating any duplicate combinations.

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, 1, n, k);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, int start, int n, int k) {
        if (current.size() == k) {
            result.push_back(current);
            return;
        }
        for (int i = start; i <= n; i++) {
            current.push_back(i);
            backtrack(result, current, i + 1, n, k);
            current.pop_back();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\binom{n}{k})$ because we are generating all possible combinations of `k` numbers from the range `[1, n]`.
> - **Space Complexity:** $O(k \cdot \binom{n}{k})$ because we need to store all possible combinations of `k` numbers from the range `[1, n]`.
> - **Optimality proof:** This approach is optimal because it generates all possible combinations of `k` numbers from the range `[1, n]` without generating any duplicate combinations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion.
- Problem-solving patterns identified: Generating all possible combinations of `k` numbers from the range `[1, n]`.
- Optimization techniques learned: Using backtracking to avoid generating duplicate combinations.
- Similar problems to practice: Permutations, subsets.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to backtrack, generating duplicate combinations.
- Edge cases to watch for: `n` and `k` are small, `n` and `k` are large.
- Performance pitfalls: Generating all possible combinations of `k` numbers from the range `[1, n]` without using backtracking.
- Testing considerations: Test the solution with different values of `n` and `k`, including edge cases.