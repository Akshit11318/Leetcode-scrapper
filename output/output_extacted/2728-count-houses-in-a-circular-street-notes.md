## Count Houses in a Circular Street

**Problem Link:** https://leetcode.com/problems/count-houses-in-a-circular-street/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the number of houses in a circular street, and an array `street` of length `n`, where `street[i]` is either `0` (no house) or `1` (house).
- Expected output format: The function should return the number of houses in the circular street.
- Key requirements and edge cases to consider: The street is circular, meaning the first house is adjacent to the last house. A house can be built if and only if the adjacent house is not built.
- Example test cases with explanations: For example, given `n = 3` and `street = [1, 0, 1]`, the function should return `2`, because the houses are built in a way that no two adjacent houses are built.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of building houses and count the valid ones.
- Step-by-step breakdown of the solution: 
  1. Initialize a counter for the number of houses.
  2. Iterate over all possible combinations of building houses (using a bit mask or recursion).
  3. For each combination, check if it is valid (i.e., no two adjacent houses are built).
  4. If the combination is valid, increment the counter.

```cpp
int countHouses(int n, vector<int>& street) {
    int count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        bool valid = true;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) && ((mask & (1 << ((i + 1) % n))) || (mask & (1 << ((i + n - 1) % n))))) {
                valid = false;
                break;
            }
        }
        if (valid) {
            int houses = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    houses++;
                }
            }
            count = max(count, houses);
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of houses. This is because we are trying all possible combinations of building houses.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is exponential because we are trying all possible combinations, and the space complexity is constant because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem efficiently. The idea is to keep track of the maximum number of houses that can be built up to each position.
- Detailed breakdown of the approach: 
  1. Initialize two arrays, `dp` and `dp1`, to store the maximum number of houses that can be built up to each position.
  2. For each position, calculate the maximum number of houses that can be built by considering the previous position and the position before that.
  3. Return the maximum number of houses that can be built up to the last position.

```cpp
int countHouses(int n, vector<int>& street) {
    vector<int> dp(n, 0);
    dp[0] = 1;
    vector<int> dp1(n, 0);
    dp1[0] = 1;
    for (int i = 1; i < n; i++) {
        if (street[i] == 0) {
            dp[i] = dp1[i - 1];
            dp1[i] = max(dp[i - 1], dp1[i - 1]);
        } else {
            dp[i] = dp[i - 1];
            dp1[i] = max(dp[i - 1], dp1[i - 1]);
        }
    }
    int maxHouses = max(dp[n - 1], dp1[n - 1]);
    if (n > 1 && street[0] == 0 && street[n - 1] == 0) {
        maxHouses = max(maxHouses, dp1[n - 2] + 1);
    }
    return maxHouses;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of houses. This is because we are iterating over the positions once.
> - **Space Complexity:** $O(n)$, because we are using two arrays to store the maximum number of houses that can be built up to each position.
> - **Optimality proof:** This solution is optimal because we are considering all possible combinations of building houses and keeping track of the maximum number of houses that can be built up to each position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit masking, and recursion.
- Problem-solving patterns identified: Using dynamic programming to solve problems that have overlapping subproblems.
- Optimization techniques learned: Using bit masking to try all possible combinations efficiently.
- Similar problems to practice: Counting the number of ways to build houses in a grid, counting the number of ways to color a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not initializing variables correctly.
- Edge cases to watch for: Handling the case where the input array is empty, handling the case where the input array has only one element.
- Performance pitfalls: Using a brute force approach that has an exponential time complexity.
- Testing considerations: Testing the function with different input arrays, testing the function with edge cases.