## Solve the Equation

**Problem Link:** https://leetcode.com/problems/solve-the-equation/description

**Problem Statement:**
- Input format: A string `equation` representing a linear equation in the form `x + b = c` or `x - b = c`, where `x` is the variable and `b` and `c` are constants.
- Constraints: The input equation is always valid and does not contain any spaces.
- Expected output format: A string representing the solution to the equation in the form `x = x` or "No solution" if the equation has no solution, or "Infinite solutions" if the equation has infinite solutions.
- Key requirements and edge cases to consider:
  - Handling cases where the equation has no solution (e.g., `x + 1 = x - 1`).
  - Handling cases where the equation has infinite solutions (e.g., `x = x`).
  - Handling cases where the equation has a unique solution (e.g., `x + 1 = 2`).

Example test cases with explanations:

- Input: `equation = "x+5-3+2=x+4"`
  Output: `"x=x"`
  Explanation: The equation simplifies to `x = x`, which means it has infinite solutions.

- Input: `equation = "x=4"`
  Output: `"x=4"`
  Explanation: The equation simplifies to `x = 4`, which means it has a unique solution.

- Input: `equation = "2x=x"`
  Output: `"x=0"`
  Explanation: The equation simplifies to `x = 0`, which means it has a unique solution.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The equation can be solved by comparing the coefficients of `x` on both sides and the constant terms.
- Step-by-step breakdown of the solution:
  1. Parse the equation to extract the coefficients of `x` and the constant terms on both sides.
  2. Compare the coefficients of `x` on both sides to determine if the equation has a unique solution, no solution, or infinite solutions.
  3. If the equation has a unique solution, calculate the value of `x` by equating the constant terms on both sides.

```cpp
class Solution {
public:
    string solveEquation(string equation) {
        int lhsX = 0, lhsNum = 0, rhsX = 0, rhsNum = 0;
        bool lhsFlag = true;
        int num = 0;
        
        for (int i = 0; i < equation.length(); i++) {
            if (equation[i] == '=') {
                lhsFlag = false;
                continue;
            }
            if (equation[i] == 'x') {
                if (i > 0 && equation[i - 1] == '+') {
                    if (lhsFlag) {
                        lhsX += 1;
                    } else {
                        rhsX += 1;
                    }
                } else if (i > 0 && equation[i - 1] == '-') {
                    if (lhsFlag) {
                        lhsX -= 1;
                    } else {
                        rhsX -= 1;
                    }
                } else {
                    if (lhsFlag) {
                        lhsX += 1;
                    } else {
                        rhsX += 1;
                    }
                }
            } else if (equation[i] == '+') {
                if (lhsFlag) {
                    lhsNum += num;
                } else {
                    rhsNum += num;
                }
                num = 0;
            } else if (equation[i] == '-') {
                if (lhsFlag) {
                    lhsNum += num;
                } else {
                    rhsNum += num;
                }
                num = 0;
            } else {
                num = num * 10 + equation[i] - '0';
            }
        }
        
        if (lhsFlag) {
            lhsNum += num;
        } else {
            rhsNum += num;
        }
        
        int x = lhsX - rhsX;
        int numDiff = rhsNum - lhsNum;
        
        if (x == 0) {
            if (numDiff == 0) {
                return "Infinite solutions";
            } else {
                return "No solution";
            }
        }
        
        return "x=" + to_string(numDiff / x);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `equation`. This is because we are parsing the equation once to extract the coefficients and constant terms.
> - **Space Complexity:** $O(1)$, which means the space used does not grow with the size of the input. This is because we are using a constant amount of space to store the coefficients and constant terms.
> - **Why these complexities occur:** The time complexity is linear because we are parsing the input string once, and the space complexity is constant because we are using a fixed amount of space to store the coefficients and constant terms.

---

### Optimal Approach (Required)

The provided brute force approach is already optimal for this problem, as we need to parse the input string at least once to extract the coefficients and constant terms. Therefore, we cannot improve upon the time complexity of $O(n)$.

However, we can slightly optimize the code to make it more concise and efficient.

```cpp
class Solution {
public:
    string solveEquation(string equation) {
        int x = 0, num = 0;
        bool isNumPositive = true;
        
        for (int i = 0; i < equation.length(); i++) {
            if (equation[i] == 'x') {
                x += isNumPositive ? (num == 0 ? 1 : num) : (num == 0 ? -1 : -num);
                num = 0;
                isNumPositive = true;
            } else if (equation[i] == '=') {
                num = 0;
                isNumPositive = true;
            } else if (equation[i] == '+') {
                num = 0;
                isNumPositive = true;
            } else if (equation[i] == '-') {
                num = 0;
                isNumPositive = false;
            } else if (equation[i] == '0' + 1) {
                num = num * 10 + equation[i] - '0';
            }
        }
        
        if (equation[equation.length() - 1] != 'x') {
            num = isNumPositive ? (num == 0 ? 0 : num) : (num == 0 ? 0 : -num);
        }
        
        x -= num;
        
        if (x == 0) {
            return "No solution";
        }
        
        return "x=" + to_string(x);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `equation`.
> - **Space Complexity:** $O(1)$, which means the space used does not grow with the size of the input.
> - **Optimality proof:** The time complexity is optimal because we need to parse the input string at least once to extract the coefficients and constant terms. The space complexity is optimal because we are using a constant amount of space to store the coefficients and constant terms.

---

### Final Notes

**Learning Points:**

* Key algorithmic concepts demonstrated: parsing input strings, extracting coefficients and constant terms, and solving linear equations.
* Problem-solving patterns identified: breaking down complex problems into simpler sub-problems and using mathematical insights to optimize solutions.
* Optimization techniques learned: using constant space to store coefficients and constant terms, and parsing input strings only once to minimize time complexity.

**Mistakes to Avoid:**

* Common implementation errors: not handling edge cases correctly, such as when the equation has no solution or infinite solutions.
* Edge cases to watch for: equations with no `x` term, equations with only constant terms, and equations with infinite solutions.
* Performance pitfalls: using excessive space or time complexity, such as parsing the input string multiple times or using recursive functions.
* Testing considerations: testing the solution with a variety of input cases, including edge cases and boundary cases.