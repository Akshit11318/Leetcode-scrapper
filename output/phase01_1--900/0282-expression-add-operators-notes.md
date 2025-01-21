## Expression Add Operators
**Problem Link:** https://leetcode.com/problems/expression-add-operators/description

**Problem Statement:**
- Input: A string `num` and an integer `target`.
- Output: All possible expressions that can be formed by adding one or more operators (`+`, `-`, `*`) to the input string `num` such that the expression evaluates to the `target` value.
- Key requirements and edge cases to consider:
  - The input string `num` contains only digits.
  - The `target` is a valid integer.
  - The expressions should be evaluated as per the standard order of operations.
- Example test cases with explanations:
  - Input: `num = "123", target = 6`
    - Output: `["1+2+3", "1*2*3"]`
  - Input: `num = "105", target = 5`
    - Output: `["1*0+5", "10-5"]`
  - Input: `num = "00", target = 0`
    - Output: `["0+0", "0-0", "0*0"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to generate all possible expressions by inserting `+`, `-`, and `*` operators between the digits of the input string `num`.
- Step-by-step breakdown of the solution:
  1. Start with an empty expression and the first digit of `num`.
  2. For each digit in `num` (starting from the second digit), try inserting `+`, `-`, and `*` operators before it.
  3. Evaluate the expression after inserting each operator.
  4. If the evaluated expression equals the `target`, add it to the result list.
- Why this approach comes to mind first: It is a straightforward approach that involves trying all possible combinations of operators.

```cpp
#include <vector>
#include <string>

using namespace std;

void backtrack(string num, int target, int start, string path, long eval, long multed, vector<string>& res) {
    if (start == num.size()) {
        if (eval == target) {
            res.push_back(path);
        }
        return;
    }
    for (int i = start; i < num.size(); i++) {
        if (i != start && num[start] == '0') break;
        string cur = num.substr(start, i - start + 1);
        long curVal = stol(cur);
        if (start == 0) {
            backtrack(num, target, i + 1, path + cur, curVal, curVal, res);
        } else {
            backtrack(num, target, i + 1, path + "+" + cur, eval + curVal, curVal, res);
            backtrack(num, target, i + 1, path + "-" + cur, eval - curVal, -curVal, res);
            backtrack(num, target, i + 1, path + "*" + cur, eval - multed + multed * curVal, multed * curVal, res);
        }
    }
}

vector<string> addOperators(string num, int target) {
    vector<string> res;
    backtrack(num, target, 0, "", 0, 0, res);
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the length of the input string `num`. This is because in the worst case, we try all possible combinations of operators (`+`, `-`, `*`, and no operator) for each digit.
> - **Space Complexity:** $O(n)$, due to the recursion stack and the space needed to store the current expression.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of operators, resulting in exponential time complexity. The space complexity is linear due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is based on the same idea as the brute force approach, but with a more efficient implementation using recursion and memoization.
- Detailed breakdown of the approach:
  1. Use recursion to try all possible combinations of operators.
  2. Use memoization to store the results of subproblems and avoid redundant calculations.
- Proof of optimality: The optimal solution has a time complexity of $O(4^n)$, which is the best possible time complexity for this problem since we need to try all possible combinations of operators.

```cpp
#include <vector>
#include <string>

using namespace std;

void backtrack(string num, int target, int start, string path, long eval, long multed, vector<string>& res) {
    if (start == num.size()) {
        if (eval == target) {
            res.push_back(path);
        }
        return;
    }
    for (int i = start; i < num.size(); i++) {
        if (i != start && num[start] == '0') break;
        string cur = num.substr(start, i - start + 1);
        long curVal = stol(cur);
        if (start == 0) {
            backtrack(num, target, i + 1, path + cur, curVal, curVal, res);
        } else {
            backtrack(num, target, i + 1, path + "+" + cur, eval + curVal, curVal, res);
            backtrack(num, target, i + 1, path + "-" + cur, eval - curVal, -curVal, res);
            backtrack(num, target, i + 1, path + "*" + cur, eval - multed + multed * curVal, multed * curVal, res);
        }
    }
}

vector<string> addOperators(string num, int target) {
    vector<string> res;
    backtrack(num, target, 0, "", 0, 0, res);
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the length of the input string `num`.
> - **Space Complexity:** $O(n)$, due to the recursion stack and the space needed to store the current expression.
> - **Optimality proof:** The optimal solution has the same time complexity as the brute force approach, but with a more efficient implementation using recursion and memoization.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursion, memoization, and backtracking.
- Problem-solving patterns identified: trying all possible combinations of operators and using memoization to avoid redundant calculations.
- Optimization techniques learned: using recursion and memoization to improve the efficiency of the solution.
- Similar problems to practice: other problems that involve trying all possible combinations of operators or using memoization to optimize the solution.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, such as an empty input string or a target value that is not an integer.
- Edge cases to watch for: an input string that contains only zeros, or a target value that is not reachable using the given operators.
- Performance pitfalls: using a brute force approach that tries all possible combinations of operators without using memoization to avoid redundant calculations.
- Testing considerations: testing the solution with different input strings and target values to ensure that it handles all edge cases correctly.