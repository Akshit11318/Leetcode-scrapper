## Number of Employees Who Met the Target

**Problem Link:** https://leetcode.com/problems/number-of-employees-who-met-the-target/description

**Problem Statement:**
- Input format: The function takes a list of integers `employees` representing the number of employees in each department, a list of integers `targets` representing the target number for each department, and an integer `maxEmployees` representing the maximum number of employees that can be chosen.
- Constraints: 
    - `1 <= employees.length == targets.length <= 15`
    - `1 <= employees[i] <= 10^5`
    - `1 <= targets[i] <= 10^5`
    - `1 <= maxEmployees <= 10^5`
- Expected output format: The function should return the maximum number of employees that can be chosen such that the sum of the target numbers for the chosen employees does not exceed `maxEmployees`.
- Key requirements and edge cases to consider:
    - Each department can either be included or excluded.
    - The sum of the target numbers for the chosen departments should not exceed `maxEmployees`.
- Example test cases with explanations:
    - `employees = [1, 2, 3], targets = [1, 2, 3], maxEmployees = 5` should return `3` because we can choose all departments.
    - `employees = [1, 2, 3], targets = [1, 2, 3], maxEmployees = 2` should return `1` because we can only choose one department.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsets of departments and calculate the sum of the target numbers for each subset.
- The step-by-step breakdown of the solution is as follows:
    1. Generate all possible subsets of departments using bit manipulation.
    2. For each subset, calculate the sum of the target numbers.
    3. Check if the sum does not exceed `maxEmployees`.
    4. If it does not exceed, update the maximum number of employees that can be chosen.
- This approach comes to mind first because it is a straightforward way to solve the problem by considering all possible cases.

```cpp
class Solution {
public:
    int maxNumberOfEmployees(vector<int>& employees, vector<int>& targets, int maxEmployees) {
        int n = employees.size();
        int maxNum = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int sum = 0;
            int num = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    sum += targets[i];
                    num++;
                }
            }
            if (sum <= maxEmployees) {
                maxNum = max(maxNum, num);
            }
        }
        return maxNum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of departments. This is because we generate all possible subsets of departments, and for each subset, we calculate the sum of the target numbers.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input. This is because we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity occurs because we use a loop to generate all possible subsets of departments, and for each subset, we use another loop to calculate the sum of the target numbers. The space complexity occurs because we only use a constant amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a recursive approach with memoization to store the results of subproblems.
- The detailed breakdown of the approach is as follows:
    1. Define a recursive function that takes the current index and the remaining number of employees as arguments.
    2. Use memoization to store the results of subproblems.
    3. For each department, consider two cases: include the department or exclude the department.
    4. Update the maximum number of employees that can be chosen.
- This approach is optimal because it avoids redundant calculations by storing the results of subproblems.

```cpp
class Solution {
public:
    int maxNumberOfEmployees(vector<int>& employees, vector<int>& targets, int maxEmployees) {
        int n = employees.size();
        vector<vector<int>> memo(n, vector<int>(maxEmployees + 1, -1));
        function<int(int, int)> dfs = [&](int i, int remaining) {
            if (i == n) {
                return 0;
            }
            if (memo[i][remaining] != -1) {
                return memo[i][remaining];
            }
            int exclude = dfs(i + 1, remaining);
            int include = 0;
            if (remaining >= targets[i]) {
                include = 1 + dfs(i + 1, remaining - targets[i]);
            }
            memo[i][remaining] = max(exclude, include);
            return memo[i][remaining];
        };
        return dfs(0, maxEmployees);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot maxEmployees)$, where $n$ is the number of departments. This is because we use a recursive approach with memoization to store the results of subproblems.
> - **Space Complexity:** $O(n \cdot maxEmployees)$, which means the space required changes with the size of the input. This is because we use memoization to store the results of subproblems.
> - **Optimality proof:** This approach is optimal because it avoids redundant calculations by storing the results of subproblems, and it considers all possible cases by using a recursive approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive approach, memoization, and bit manipulation.
- Problem-solving patterns identified: using a recursive approach with memoization to solve problems with overlapping subproblems.
- Optimization techniques learned: using memoization to avoid redundant calculations.
- Similar problems to practice: problems that involve recursive approaches and memoization, such as the `0/1 Knapsack Problem`.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to initialize the memoization table, or using incorrect indices to access the memoization table.
- Edge cases to watch for: handling the base case of the recursive function, or considering the case where the remaining number of employees is 0.
- Performance pitfalls: using a naive recursive approach without memoization, or using a recursive approach with a large number of recursive calls.
- Testing considerations: testing the function with different inputs, including edge cases and large inputs.