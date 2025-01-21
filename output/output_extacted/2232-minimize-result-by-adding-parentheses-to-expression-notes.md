## Minimize Result by Adding Parentheses to Expression

**Problem Link:** https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/description

**Problem Statement:**
- Input: A string `expression` containing digits and '+' operators.
- Constraints: The length of `expression` is between 3 and 10.
- Expected output: The minimum possible result after adding parentheses to `expression`.
- Key requirements: The input string will only contain digits and '+' operators, and will have at least one '+' operator.
- Example test cases:
  - Input: "247+42"
  - Output: 4
  - Explanation: Evaluate "247+42" as (2*4*7)+(4*2) = 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of adding parentheses to the expression and evaluating each combination to find the minimum result.
- Step-by-step breakdown:
  1. Generate all possible combinations of adding parentheses to the expression.
  2. Evaluate each combination to find the result.
  3. Keep track of the minimum result found.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int calculate(const std::string& expression) {
    int result = 0;
    int num = 0;
    for (char c : expression) {
        if (c == '+') {
            result += num;
            num = 0;
        } else {
            num = num * 10 + (c - '0');
        }
    }
    result += num;
    return result;
}

int minResult(const std::string& expression) {
    int minVal = INT_MAX;
    for (int mask = 1; mask < (1 << (expression.size() - 1)); mask++) {
        std::string temp = expression;
        for (int i = 0; i < expression.size() - 1; i++) {
            if ((mask & (1 << i)) != 0) {
                temp.insert(i + 1, ")");
                temp.insert(0, "(");
            }
        }
        int val = calculate(temp);
        minVal = std::min(minVal, val);
    }
    return minVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate $2^{n-1}$ combinations of adding parentheses and evaluate each combination in $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the temporary expression with added parentheses.
> - **Why these complexities occur:** The brute force approach has high time complexity due to generating all possible combinations of adding parentheses, and space complexity due to storing the temporary expressions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of trying all possible combinations of adding parentheses, we can use dynamic programming to find the minimum result.
- Detailed breakdown:
  1. Initialize a 2D array `dp` to store the minimum result for each subexpression.
  2. Fill the `dp` array in a bottom-up manner by considering all possible splits of the subexpression.
  3. The minimum result for the entire expression is stored in `dp[0][expression.size() - 1]`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int minResult(const std::string& expression) {
    int n = expression.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, INT_MAX));
    for (int i = 0; i < n; i++) {
        dp[i][i] = expression[i] - '0';
    }
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            for (int k = i + 1; k <= j; k += 2) {
                dp[i][j] = std::min(dp[i][j], dp[i][k - 1] + dp[k + 1][j]);
            }
        }
    }
    return dp[0][n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we fill the `dp` array in a bottom-up manner with three nested loops.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we need to store the `dp` array.
> - **Optimality proof:** This approach is optimal because it considers all possible splits of the subexpressions and finds the minimum result using dynamic programming.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, bottom-up approach.
- Problem-solving patterns identified: breaking down the problem into smaller subproblems and solving them using dynamic programming.
- Optimization techniques learned: using dynamic programming to avoid redundant calculations.
- Similar problems to practice: other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the `dp` array, incorrect calculation of the minimum result.
- Edge cases to watch for: empty input string, input string with only one digit.
- Performance pitfalls: using a brute force approach instead of dynamic programming.
- Testing considerations: testing the function with different input strings, including edge cases.