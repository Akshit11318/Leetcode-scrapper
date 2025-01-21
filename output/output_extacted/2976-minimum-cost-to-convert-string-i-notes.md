## Minimum Cost to Convert String
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-convert-string-i/description

**Problem Statement:**
- Input: A string `s` and an array of integers `cost`.
- Constraints: `s` has length `n`, and `cost` has length `n`, where `1 <= n <= 1000`.
- Expected Output: The minimum cost to convert `s` into a string of the same length, where each character can be converted to any other character.
- Key Requirements: The cost of converting a character at position `i` is `cost[i]`.
- Edge Cases: If `s` is empty, return `0`.

### Brute Force Approach
**Explanation:**
- The initial thought process is to consider all possible conversions of each character and calculate the total cost for each conversion.
- Step-by-step breakdown:
  1. Initialize a variable `minCost` to infinity.
  2. Generate all possible strings of the same length as `s` by converting each character to all other characters.
  3. For each generated string, calculate the total cost by summing the costs of converting each character.
  4. Update `minCost` if the total cost of the current string is less than `minCost`.
- Why this approach comes to mind first: It's a straightforward approach that considers all possibilities.

```cpp
int minCost(string s, vector<int>& cost) {
    int n = s.size();
    int minCost = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalCost = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                totalCost += cost[i];
            }
        }
        minCost = min(minCost, totalCost);
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `s`. This is because we generate all possible subsets of characters to convert, and for each subset, we calculate the total cost.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and the current mask.
> - **Why these complexities occur:** The time complexity is exponential because we consider all possible subsets of characters to convert. The space complexity is constant because we only use a fixed amount of space to store the minimum cost and the current mask.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use dynamic programming to solve this problem more efficiently.
- Detailed breakdown:
  1. Initialize a variable `minCost` to `0`.
  2. Iterate over the string `s` and the cost array `cost`.
  3. For each character, we have two options: convert it or not.
  4. If we convert the character, we add the cost of conversion to `minCost`.
  5. If we don't convert the character, we don't add any cost to `minCost`.
- Proof of optimality: This approach is optimal because we consider all possible conversions of each character and choose the one that results in the minimum cost.

```cpp
int minCost(string s, vector<int>& cost) {
    int n = s.size();
    int minCost = 0;
    for (int i = 0; i < n; i++) {
        minCost += min(cost[i], 0);
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we only iterate over the string and the cost array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost.
> - **Optimality proof:** This approach is optimal because we consider all possible conversions of each character and choose the one that results in the minimum cost.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming and greedy algorithms.
- Problem-solving patterns identified: considering all possible conversions of each character and choosing the one that results in the minimum cost.
- Optimization techniques learned: using dynamic programming to reduce the time complexity from exponential to linear.

**Mistakes to Avoid:**
- Common implementation errors: not considering all possible conversions of each character.
- Edge cases to watch for: an empty string.
- Performance pitfalls: using an exponential-time algorithm when a linear-time algorithm is available.
- Testing considerations: test the function with different inputs, including an empty string and a string with a single character.