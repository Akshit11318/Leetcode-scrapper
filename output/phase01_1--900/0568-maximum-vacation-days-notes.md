## Maximum Vacation Days

**Problem Link:** https://leetcode.com/problems/maximum-vacation-days/description

**Problem Statement:**
- Input format and constraints: 
  - `flights`: a 2D array of size `n x n`, where `flights[i][j]` is `1` if there is a flight from city `i` to city `j`, and `0` otherwise.
  - `days`: a 2D array of size `n x k`, where `days[i][j]` is the number of vacation days spent in city `i` in the `j-th` week.
  - `n`: the number of cities.
  - `k`: the number of weeks.
- Expected output format: 
  - The maximum number of vacation days that can be spent over `k` weeks.
- Key requirements and edge cases to consider: 
  - The number of cities `n` and the number of weeks `k` are positive integers.
  - The input arrays are not empty and have the correct dimensions.
  - The input values are valid and within the specified ranges.
- Example test cases with explanations:
  - For example, given `flights = [[0,1,1],[1,0,1],[1,1,0]]` and `days = [[1,3,1],[6,0,3],[3,3,3]]`, the output should be `12`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible sequences of cities for each week and calculating the total number of vacation days for each sequence.
- Step-by-step breakdown of the solution: 
  1. Generate all possible sequences of cities for each week.
  2. For each sequence, calculate the total number of vacation days by summing up the vacation days spent in each city.
  3. Keep track of the maximum total number of vacation days found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has an exponential time complexity due to the generation of all possible sequences.

```cpp
#include <vector>
#include <algorithm>

int maxVacationDays(std::vector<std::vector<int>>& flights, std::vector<std::vector<int>>& days) {
    int n = flights.size();
    int k = days[0].size();
    int maxDays = 0;

    // Generate all possible sequences of cities for each week
    std::vector<int> sequence(k);
    for (int i = 0; i < k; i++) {
        sequence[i] = 0;
    }

    std::function<void(int)> generateSequence = [&](int week) {
        if (week == k) {
            int totalDays = 0;
            for (int i = 0; i < k; i++) {
                totalDays += days[sequence[i]][i];
            }
            maxDays = std::max(maxDays, totalDays);
        } else {
            for (int city = 0; city < n; city++) {
                if (week == 0 || flights[sequence[week - 1]][city] == 1) {
                    sequence[week] = city;
                    generateSequence(week + 1);
                }
            }
        }
    };

    generateSequence(0);
    return maxDays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^k)$, where $n$ is the number of cities and $k$ is the number of weeks. This is because we generate all possible sequences of cities for each week.
> - **Space Complexity:** $O(k)$, where $k$ is the number of weeks. This is because we use a recursive function to generate the sequences, and the maximum depth of the recursion tree is $k$.
> - **Why these complexities occur:** The time complexity is exponential because we try all possible sequences of cities, and the space complexity is linear because we use a recursive function with a maximum depth of $k$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to maintain a 2D array `dp` where `dp[i][j]` represents the maximum number of vacation days that can be spent from city `i` to the end of the `j-th` week.
- Detailed breakdown of the approach: 
  1. Initialize the `dp` array with zeros.
  2. For each week `j` from `0` to `k-1`, for each city `i` from `0` to `n-1`, update `dp[i][j]` to be the maximum number of vacation days that can be spent from city `i` to the end of the `j-th` week.
  3. The maximum number of vacation days that can be spent over `k` weeks is stored in `dp[i][k-1]` for any city `i`.
- Proof of optimality: The dynamic programming approach is optimal because it avoids the exponential time complexity of the brute force approach by storing and reusing the results of subproblems.

```cpp
int maxVacationDays(std::vector<std::vector<int>>& flights, std::vector<std::vector<int>>& days) {
    int n = flights.size();
    int k = days[0].size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(k, 0));

    // Initialize the dp array for the first week
    for (int i = 0; i < n; i++) {
        dp[i][0] = days[i][0];
    }

    // Update the dp array for each week
    for (int j = 1; j < k; j++) {
        for (int i = 0; i < n; i++) {
            int maxDays = 0;
            for (int city = 0; city < n; city++) {
                if (flights[city][i] == 1) {
                    maxDays = std::max(maxDays, dp[city][j - 1]);
                }
            }
            dp[i][j] = maxDays + days[i][j];
        }
    }

    // Find the maximum number of vacation days that can be spent over k weeks
    int maxDays = 0;
    for (int i = 0; i < n; i++) {
        maxDays = std::max(maxDays, dp[i][k - 1]);
    }
    return maxDays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2k)$, where $n$ is the number of cities and $k$ is the number of weeks. This is because we update the `dp` array for each week and each city.
> - **Space Complexity:** $O(nk)$, where $n` is the number of cities and `k` is the number of weeks. This is because we use a 2D array `dp` to store the maximum number of vacation days for each city and each week.
> - **Optimality proof:** The dynamic programming approach is optimal because it avoids the exponential time complexity of the brute force approach by storing and reusing the results of subproblems.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive functions.
- Problem-solving patterns identified: Using dynamic programming to avoid exponential time complexity.
- Optimization techniques learned: Storing and reusing the results of subproblems to avoid redundant calculations.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: The number of cities `n` and the number of weeks `k` are positive integers, the input arrays are not empty and have the correct dimensions.
- Performance pitfalls: Using a brute force approach with an exponential time complexity, not storing and reusing the results of subproblems.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it works correctly and efficiently.