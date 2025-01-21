## Minimum Cost to Change the Final Value of Expression

**Problem Link:** https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/description

**Problem Statement:**
- Input: `expression` (string), `target` (integer)
- Constraints: `expression` consists of digits, `+`, and `-` operators.
- Expected Output: Minimum cost to change the final value of `expression` to `target`.
- Key Requirements: 
    - The cost of changing a digit is the absolute difference between the original and new digit.
    - The final value must be equal to `target`.
- Example Test Cases:
    - `expression = "1+2-3", target = -7` 
    - `expression = "1+2+3", target = 6`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of digit changes.
- Step-by-step breakdown:
    1. Parse the `expression` into a list of operators and digits.
    2. Generate all possible combinations of digit changes.
    3. For each combination, calculate the new expression value.
    4. Calculate the cost of changing the digits for each combination.
    5. Keep track of the minimum cost that results in a final value equal to `target`.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int minCost(string expression, int target) {
    // Parse expression into digits and operators
    vector<int> digits;
    vector<char> operators;
    int currDigit = 0;
    for (char c : expression) {
        if (c == '+' || c == '-') {
            digits.push_back(currDigit);
            operators.push_back(c);
            currDigit = 0;
        } else {
            currDigit = currDigit * 10 + (c - '0');
        }
    }
    digits.push_back(currDigit);

    int minCost = INT_MAX;
    // Try all possible digit changes
    for (int mask = 0; mask < (1 << digits.size()); mask++) {
        vector<int> newDigits = digits;
        for (int i = 0; i < digits.size(); i++) {
            if (mask & (1 << i)) {
                // Change the digit
                for (int j = 0; j <= 9; j++) {
                    newDigits[i] = j;
                    int newExprValue = newDigits[0];
                    for (int k = 1; k < newDigits.size(); k++) {
                        if (operators[k - 1] == '+') {
                            newExprValue += newDigits[k];
                        } else {
                            newExprValue -= newDigits[k];
                        }
                    }
                    if (newExprValue == target) {
                        int cost = 0;
                        for (int l = 0; l < digits.size(); l++) {
                            cost += abs(digits[l] - newDigits[l]);
                        }
                        minCost = min(minCost, cost);
                    }
                }
                newDigits[i] = digits[i]; // Reset for next iteration
            }
        }
    }
    return minCost == INT_MAX ? -1 : minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot 10^n \cdot n)$ where $n$ is the number of digits in the expression, due to the exhaustive search and digit change iterations.
> - **Space Complexity:** $O(n)$ for storing the parsed digits and operators.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of digit changes, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store and reuse intermediate results, reducing the search space.
- Detailed breakdown:
    1. Initialize a DP table to store the minimum cost for each possible expression value.
    2. Iterate through each digit and operator, updating the DP table with the minimum cost for each possible new expression value.
    3. Use the DP table to find the minimum cost for the target expression value.
- Proof of optimality: This approach ensures that each possible expression value is considered only once, minimizing the search space.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <climits>
using namespace std;

int minCost(string expression, int target) {
    vector<int> digits;
    vector<char> operators;
    int currDigit = 0;
    for (char c : expression) {
        if (c == '+' || c == '-') {
            digits.push_back(currDigit);
            operators.push_back(c);
            currDigit = 0;
        } else {
            currDigit = currDigit * 10 + (c - '0');
        }
    }
    digits.push_back(currDigit);

    const int MAX_VAL = 1000; // Assuming the maximum possible expression value
    vector<vector<int>> dp(digits.size() + 1, vector<int>(2 * MAX_VAL + 1, INT_MAX));
    dp[0][MAX_VAL] = 0; // Initialize the DP table

    for (int i = 1; i <= digits.size(); i++) {
        for (int j = 0; j <= 2 * MAX_VAL; j++) {
            if (dp[i - 1][j] != INT_MAX) {
                for (int k = 0; k <= 9; k++) {
                    int newExprValue = j - MAX_VAL;
                    if (i == 1) {
                        newExprValue = k;
                    } else if (operators[i - 2] == '+') {
                        newExprValue += k;
                    } else {
                        newExprValue -= k;
                    }
                    int newCost = dp[i - 1][j] + abs(k - digits[i - 1]);
                    int newIndex = newExprValue + MAX_VAL;
                    dp[i][newIndex] = min(dp[i][newIndex], newCost);
                }
            }
        }
    }

    int targetIndex = target + MAX_VAL;
    return dp[digits.size()][targetIndex] == INT_MAX ? -1 : dp[digits.size()][targetIndex];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10 \cdot MAX\_VAL)$ where $n$ is the number of digits in the expression, due to the dynamic programming iterations.
> - **Space Complexity:** $O(n \cdot MAX\_VAL)$ for the DP table.
> - **Optimality proof:** This approach ensures that each possible expression value is considered only once, minimizing the search space and reducing the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, exhaustive search.
- Problem-solving patterns identified: Using DP to reduce the search space.
- Optimization techniques learned: Minimizing the search space by reusing intermediate results.
- Similar problems to practice: Other dynamic programming problems, such as the **0/1 Knapsack Problem** or the **Longest Common Subsequence** problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the DP table correctly, not handling edge cases.
- Edge cases to watch for: Empty expression, invalid characters in the expression.
- Performance pitfalls: Using an exhaustive search approach, not optimizing the search space.
- Testing considerations: Test with different expressions, targets, and edge cases to ensure the solution is robust.