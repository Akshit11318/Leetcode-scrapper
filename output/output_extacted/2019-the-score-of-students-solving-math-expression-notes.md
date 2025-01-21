## The Score of Students Solving Math Expression

**Problem Link:** https://leetcode.com/problems/the-score-of-students-solving-math-expression/description

**Problem Statement:**
- Input format and constraints: Given a string `s` representing a math expression and an integer `k`, return the score of students solving the math expression.
- Expected output format: The score of students solving the math expression.
- Key requirements and edge cases to consider:
  - `s` only contains `+`, `-`, `*`, `/`, and digits.
  - The length of `s` is between 1 and 100.
  - `k` is between 1 and 10^6.
- Example test cases with explanations:
  - Example 1: `s = "1+2*3-4*5", k = 1`, Output: `7`.
  - Example 2: `s = "1+2*3-4*5", k = 3`, Output: `7`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible orders of operations and evaluate the math expression for each order.
- Step-by-step breakdown of the solution:
  1. Generate all possible orders of operations.
  2. Evaluate the math expression for each order.
  3. Calculate the score for each order.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible orders and evaluating the math expression for each order.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int calculateScore(string s, int k) {
    // Generate all possible orders of operations
    vector<int> operators;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
            operators.push_back(i);
        }
    }

    // Evaluate the math expression for each order
    set<int> scores;
    do {
        string expression = s;
        for (int i = 0; i < operators.size(); i++) {
            expression[operators[i]] = i % 2 == 0 ? '+' : '-';
        }
        int score = evaluateExpression(expression);
        scores.insert(score);
    } while (next_permutation(operators.begin(), operators.end()));

    // Calculate the score for each order
    vector<int> sortedScores(scores.begin(), scores.end());
    sort(sortedScores.begin(), sortedScores.end());
    return sortedScores[k - 1];
}

int evaluateExpression(string expression) {
    // Evaluate the math expression
    int result = 0;
    char op = '+';
    int num = 0;
    for (int i = 0; i < expression.size(); i++) {
        if (isdigit(expression[i])) {
            num = num * 10 + expression[i] - '0';
        }
        if (!isdigit(expression[i]) || i == expression.size() - 1) {
            if (op == '+') {
                result += num;
            } else if (op == '-') {
                result -= num;
            }
            op = expression[i];
            num = 0;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! * m)$, where $n$ is the number of operators and $m$ is the length of the math expression.
> - **Space Complexity:** $O(n! + m)$, where $n$ is the number of operators and $m$ is the length of the math expression.
> - **Why these complexities occur:** The time complexity is $O(n! * m)$ because we generate all possible orders of operations, which is $O(n!)$, and evaluate the math expression for each order, which is $O(m)$. The space complexity is $O(n! + m)$ because we store all possible orders of operations and the math expression.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to evaluate the math expression and calculate the score.
- Detailed breakdown of the approach:
  1. Evaluate the math expression using dynamic programming.
  2. Calculate the score using the evaluated math expression.
- Proof of optimality: This approach is optimal because it uses dynamic programming to evaluate the math expression, which reduces the time complexity to $O(n * m)$.

```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int calculateScore(string s, int k) {
    // Evaluate the math expression using dynamic programming
    vector<vector<int>> dp(s.size(), vector<int>(s.size()));
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            dp[i][i] = s[i] - '0';
        }
    }
    for (int length = 1; length < s.size(); length++) {
        for (int i = 0; i < s.size() - length; i++) {
            int j = i + length;
            if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
                for (int k = i + 1; k <= j; k++) {
                    if (s[k] == '+' || s[k] == '-' || s[k] == '*' || s[k] == '/') {
                        dp[i][j] = max(dp[i][j], evaluateExpression(s, i, k - 1, k, j));
                    }
                }
            }
        }
    }
    // Calculate the score using the evaluated math expression
    vector<int> scores;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i; j < s.size(); j++) {
            scores.push_back(dp[i][j]);
        }
    }
    sort(scores.begin(), scores.end());
    return scores[k - 1];
}

int evaluateExpression(string s, int i, int j, int k, int end) {
    // Evaluate the math expression
    int result = 0;
    if (s[i] == '+') {
        result = dp[i][j] + dp[k][end];
    } else if (s[i] == '-') {
        result = dp[i][j] - dp[k][end];
    } else if (s[i] == '*') {
        result = dp[i][j] * dp[k][end];
    } else if (s[i] == '/') {
        result = dp[i][j] / dp[k][end];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n * m)$, where $n$ is the length of the math expression and $m$ is the number of operators.
> - **Space Complexity:** $O(n * m)$, where $n$ is the length of the math expression and $m$ is the number of operators.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to evaluate the math expression, which reduces the time complexity to $O(n * m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and evaluation of math expressions.
- Problem-solving patterns identified: Using dynamic programming to evaluate math expressions and calculate scores.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Evaluating math expressions and calculating scores using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing dynamic programming or evaluating math expressions.
- Edge cases to watch for: Handling division by zero or invalid math expressions.
- Performance pitfalls: Using brute force approaches or inefficient algorithms.
- Testing considerations: Testing the implementation with different math expressions and scores.