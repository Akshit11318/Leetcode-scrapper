## Different Ways to Add Parentheses

**Problem Link:** https://leetcode.com/problems/different-ways-to-add-parentheses/description

**Problem Statement:**
- Input: A string `expression` containing digits and operators (+, -, \*).
- Constraints: The string will contain at least one digit and may contain one or more operators.
- Expected output: A list of different possible results after evaluating the expression by adding parentheses in different ways.
- Key requirements: Handle all operators with equal precedence and no associativity (i.e., +, -, \*).
- Example test cases:
  - Input: `"1+2+3"`
  - Output: `[6]`
  - Explanation: `(1+2)+3 = 6`, `1+(2+3) = 6`
  - Input: `"2-1-1"`
  - Output: `[0, 2]`
  - Explanation: `((2-1)-1) = 0`, `(2-(1-1)) = 2`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Enumerate all possible ways to add parentheses to the expression and evaluate each one.
- Step-by-step breakdown:
  1. Generate all possible binary trees that can be formed from the given expression.
  2. Evaluate each binary tree to get the result.
  3. Store unique results.
- Why this approach comes to mind first: It's the most straightforward way to ensure all possible evaluations are considered.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

// Function to evaluate an expression
int eval(const std::string& expression) {
    int result = 0;
    char op = '+';
    int curr = 0;
    for (int i = 0; i < expression.size(); ++i) {
        if (isdigit(expression[i])) {
            curr = curr * 10 + (expression[i] - '0');
        }
        if (!isdigit(expression[i]) || i == expression.size() - 1) {
            if (op == '+') {
                result += curr;
            } else if (op == '-') {
                result -= curr;
            } else if (op == '*') {
                result *= curr;
            }
            op = expression[i];
            curr = 0;
        }
    }
    return result;
}

// Brute force function
void bruteForce(const std::string& expression, std::unordered_set<int>& results) {
    if (expression.find('+') == std::string::npos && expression.find('-') == std::string::npos && expression.find('*') == std::string::npos) {
        results.insert(stoi(expression));
        return;
    }
    for (int i = 0; i < expression.size(); ++i) {
        if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*') {
            std::string left = expression.substr(0, i);
            std::string right = expression.substr(i + 1);
            std::unordered_set<int> leftResults;
            std::unordered_set<int> rightResults;
            bruteForce(left, leftResults);
            bruteForce(right, rightResults);
            for (const auto& l : leftResults) {
                for (const auto& r : rightResults) {
                    if (expression[i] == '+') {
                        results.insert(l + r);
                    } else if (expression[i] == '-') {
                        results.insert(l - r);
                    } else if (expression[i] == '*') {
                        results.insert(l * r);
                    }
                }
            }
        }
    }
}

int main() {
    std::string expression = "2-1-1";
    std::unordered_set<int> results;
    bruteForce(expression, results);
    for (const auto& result : results) {
        std::cout << result << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of operators in the expression. This is because for each operator, we have two choices (include it in the current evaluation or not), leading to exponential time complexity.
> - **Space Complexity:** $O(2^n)$ due to the recursion stack and storing unique results.
> - **Why these complexities occur:** The brute force approach explores all possible combinations of adding parentheses, leading to an exponential number of evaluations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use **dynamic programming** to store and reuse the results of subproblems.
- Detailed breakdown:
  1. Split the expression into two parts at each operator.
  2. Recursively evaluate all possible ways to add parentheses in each part.
  3. Combine the results from both parts based on the operator.
- Proof of optimality: This approach ensures that each subproblem is solved only once, reducing the time complexity significantly.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

// Function to split the expression into numbers and operators
std::vector<std::string> split(const std::string& expression) {
    std::vector<std::string> parts;
    std::string curr = "";
    for (char c : expression) {
        if (c == '+' || c == '-' || c == '*') {
            parts.push_back(curr);
            parts.push_back(std::string(1, c));
            curr = "";
        } else {
            curr += c;
        }
    }
    parts.push_back(curr);
    return parts;
}

// Function to evaluate an expression with dynamic programming
std::vector<int> diffWaysToCompute(const std::string& expression) {
    std::unordered_map<std::string, std::vector<int>> memo;
    std::function<std::vector<int>(const std::string&)> compute = [&](const std::string& expression) {
        if (memo.count(expression)) {
            return memo[expression];
        }
        if (expression.find('+') == std::string::npos && expression.find('-') == std::string::npos && expression.find('*') == std::string::npos) {
            return {std::stoi(expression)};
        }
        std::vector<int> results;
        std::vector<std::string> parts = split(expression);
        for (int i = 1; i < parts.size(); i += 2) {
            std::string left = "";
            for (int j = 0; j < i; ++j) {
                left += parts[j];
            }
            std::string right = "";
            for (int j = i + 1; j < parts.size(); ++j) {
                right += parts[j];
            }
            for (int l : compute(left)) {
                for (int r : compute(right)) {
                    if (parts[i] == "+") {
                        results.push_back(l + r);
                    } else if (parts[i] == "-") {
                        results.push_back(l - r);
                    } else if (parts[i] == "*") {
                        results.push_back(l * r);
                    }
                }
            }
        }
        memo[expression] = results;
        return results;
    };
    return compute(expression);
}

int main() {
    std::string expression = "2-1-1";
    std::vector<int> results = diffWaysToCompute(expression);
    for (int result : results) {
        std::cout << result << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ in the worst case, but significantly reduced in practice due to memoization.
> - **Space Complexity:** $O(2^n)$ for storing the results of subproblems.
> - **Optimality proof:** This approach solves each subproblem only once, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- **Dynamic Programming:** A powerful technique for solving problems with overlapping subproblems.
- **Memoization:** A method to store and reuse the results of expensive function calls.
- **Problem-Solving Patterns:** Identifying the structure of a problem to apply appropriate techniques.

**Mistakes to Avoid:**
- **Not considering all possible cases:** Failing to account for all operators and their positions.
- **Inefficient recursion:** Not using memoization to avoid redundant calculations.
- **Incorrect implementation:** Making errors in the dynamic programming or memoization logic.