## 24 Game
**Problem Link:** https://leetcode.com/problems/24-game/description

**Problem Statement:**
- Input: An array of four integers `nums` containing the numbers 1-9.
- Constraints: All numbers are distinct, and there are no zeros.
- Expected Output: Return `true` if you can get exactly 24 from the four numbers, and `false` otherwise.
- Key Requirements: Use basic arithmetic operations `+`, `-`, `*`, `/` and consider the order of operations.
- Edge Cases: Watch for division by zero and ensure distinct results.
- Example Test Cases:
  - Input: `nums = [4,1,8,7]`
  - Output: `true`
  - Explanation: `(8*4)-(7-1) = 24`

---

### Brute Force Approach
**Explanation:**
- Generate all possible combinations of the four numbers using the four basic arithmetic operations.
- Evaluate each expression and check if the result equals 24.
- This approach comes to mind first because it exhaustively checks all possibilities.

```cpp
#include <vector>
#include <cmath>

bool judgePoint24(std::vector<int>& nums) {
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            for (char op1 : {'+', '-', '*', '/'}) {
                for (int k = j + 1; k < 4; k++) {
                    for (char op2 : {'+', '-', '*', '/'}) {
                        for (int l = k + 1; l < 4; l++) {
                            for (char op3 : {'+', '-', '*', '/'}) {
                                double a = nums[i], b = nums[j], c = nums[k], d = nums[l];
                                double result1 = eval(a, b, op1);
                                double result2 = eval(result1, c, op2);
                                double result3 = eval(result2, d, op3);
                                if (std::abs(result3 - 24) < 0.001) return true;
                                result1 = eval(a, b, op1);
                                result2 = eval(c, d, op2);
                                result3 = eval(result1, result2, op3);
                                if (std::abs(result3 - 24) < 0.001) return true;
                                result1 = eval(a, b, op1);
                                result2 = eval(d, c, op2);
                                result3 = eval(result1, result2, op3);
                                if (std::abs(result3 - 24) < 0.001) return true;
                                result1 = eval(b, a, op1);
                                result2 = eval(c, d, op2);
                                result3 = eval(result1, result2, op3);
                                if (std::abs(result3 - 24) < 0.001) return true;
                                result1 = eval(b, a, op1);
                                result2 = eval(d, c, op2);
                                result3 = eval(result1, result2, op3);
                                if (std::abs(result3 - 24) < 0.001) return true;
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

double eval(double a, double b, char op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b == 0) return INFINITY;
            return a / b;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because there are a constant number of operations, although the number of permutations and combinations is large, it's still bounded by a constant.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the numbers and the results of the operations.
> - **Why these complexities occur:** The brute force approach checks all possible combinations of numbers and operations, resulting in a constant number of operations.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is similar to the brute force approach, but it uses a more efficient algorithm to generate all possible combinations of numbers and operations.
- This approach uses recursion to generate all possible combinations of numbers and operations.
- The base case is when there is only one number left, in which case we return the number itself.
- The recursive case is when there are more than one numbers left, in which case we try all possible combinations of numbers and operations.

```cpp
#include <vector>
#include <cmath>

bool judgePoint24(std::vector<int>& nums) {
    return dfs(nums, 4);
}

bool dfs(std::vector<int>& nums, int k) {
    if (k == 1) {
        return std::abs(nums[0] - 24) < 0.001;
    }
    for (int i = 0; i < k; i++) {
        for (int j = i + 1; j < k; j++) {
            for (char op : {'+', '-', '*', '/'}) {
                double a = nums[i], b = nums[j];
                double result = eval(a, b, op);
                std::vector<int> next;
                for (int x = 0; x < k; x++) {
                    if (x != i && x != j) {
                        next.push_back(nums[x]);
                    }
                }
                next.push_back(int(result));
                if (dfs(next, k - 1)) return true;
            }
        }
    }
    return false;
}

double eval(double a, double b, char op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b == 0) return INFINITY;
            return a / b;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because there are a constant number of operations, although the number of permutations and combinations is large, it's still bounded by a constant.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the numbers and the results of the operations.
> - **Optimality proof:** The optimal approach uses recursion to generate all possible combinations of numbers and operations, which is more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursion, permutation, combination.
- Problem-solving patterns identified: using recursion to generate all possible combinations of numbers and operations.
- Optimization techniques learned: using recursion to reduce the number of operations.
- Similar problems to practice: problems that involve generating all possible combinations of numbers and operations.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle the case where the denominator is zero.
- Edge cases to watch for: the case where the input numbers are not distinct.
- Performance pitfalls: using a brute force approach that checks all possible combinations of numbers and operations.
- Testing considerations: testing the function with different input numbers and checking that it returns the correct result.