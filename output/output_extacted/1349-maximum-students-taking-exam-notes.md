## Maximum Students Taking Exam
**Problem Link:** https://leetcode.com/problems/maximum-students-taking-exam/description

**Problem Statement:**
- Input format: A 2D `vector<vector<int>>` `seats` representing the seats in the exam room.
- Constraints: `1 <= seats.size() <= 10`, `seats[i].length == seats[0].length`, `seats[i][j]` is either `0` or `1`.
- Expected output format: The maximum number of students that can take the exam.
- Key requirements and edge cases to consider: No two students can sit in adjacent seats, and no two students can sit in the same row or column.
- Example test cases with explanations: 
    - Input: `seats = [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1]]`
      Output: `10`
      Explanation: We can put 2 students in each of the first 5 rows.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of students in the seats.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of students in the seats.
  2. For each combination, check if any two students are in adjacent seats, the same row, or the same column.
  3. If not, count the number of students in the combination.
- Why this approach comes to mind first: It's a straightforward and intuitive way to solve the problem.

```cpp
class Solution {
public:
    int maxStudents(vector<vector<int>>& seats) {
        int m = seats.size();
        int n = seats[0].size();
        vector<vector<int>> combinations(1 << m, vector<int>(n));
        for (int mask = 0; mask < (1 << m); mask++) {
            for (int i = 0; i < m; i++) {
                if ((mask >> i) & 1) {
                    combinations[mask][i] = 1;
                }
            }
        }
        int max_students = 0;
        for (int mask = 0; mask < (1 << m); mask++) {
            bool valid = true;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (seats[i][j] == 0) {
                        continue;
                    }
                    if (combinations[mask][i] == 1) {
                        if (j > 0 && combinations[mask][i] == 1) {
                            valid = false;
                            break;
                        }
                        if (j < n - 1 && combinations[mask][i] == 1) {
                            valid = false;
                            break;
                        }
                    }
                }
                if (!valid) {
                    break;
                }
            }
            if (valid) {
                int count = 0;
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        if (combinations[mask][i] == 1) {
                            count++;
                        }
                    }
                }
                max_students = max(max_students, count);
            }
        }
        return max_students;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns.
> - **Space Complexity:** $O(2^m \cdot m)$, for storing the combinations.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of students in the seats, resulting in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the maximum number of students that can be seated in each row, considering the previous rows.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` to store the maximum number of students that can be seated in each row.
  2. For each row, try all possible combinations of students in the row.
  3. For each combination, check if any two students are in adjacent seats.
  4. If not, update the maximum number of students that can be seated in the current row.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of students in the rows, while avoiding redundant calculations.

```cpp
class Solution {
public:
    int maxStudents(vector<vector<int>>& seats) {
        int m = seats.size();
        int n = seats[0].size();
        int max_mask = (1 << n);
        vector<int> dp(max_mask, 0);
        for (int i = 0; i < m; i++) {
            vector<int> next_dp(max_mask, 0);
            for (int mask = 0; mask < max_mask; mask++) {
                bool valid = true;
                for (int j = 0; j < n; j++) {
                    if ((mask >> j) & 1) {
                        if (j > 0 && (mask >> (j - 1)) & 1) {
                            valid = false;
                            break;
                        }
                        if (seats[i][j] == 0) {
                            valid = false;
                            break;
                        }
                    }
                }
                if (!valid) {
                    continue;
                }
                int count = 0;
                for (int j = 0; j < n; j++) {
                    if ((mask >> j) & 1) {
                        count++;
                    }
                }
                for (int prev_mask = 0; prev_mask < max_mask; prev_mask++) {
                    bool valid_prev = true;
                    for (int j = 0; j < n; j++) {
                        if ((prev_mask >> j) & 1 && (mask >> j) & 1) {
                            valid_prev = false;
                            break;
                        }
                    }
                    if (valid_prev) {
                        next_dp[mask] = max(next_dp[mask], dp[prev_mask] + count);
                    }
                }
            }
            dp = next_dp;
        }
        int max_students = 0;
        for (int mask = 0; mask < max_mask; mask++) {
            max_students = max(max_students, dp[mask]);
        }
        return max_students;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot 2^{2n})$, where $m$ is the number of rows and $n$ is the number of columns.
> - **Space Complexity:** $O(2^n)$, for storing the dynamic programming table.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of students in the rows, while avoiding redundant calculations, resulting in an optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit manipulation.
- Problem-solving patterns identified: Using dynamic programming to store intermediate results, avoiding redundant calculations.
- Optimization techniques learned: Using bit manipulation to represent combinations of students in the rows.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid combinations of students in the rows, not updating the maximum number of students correctly.
- Edge cases to watch for: Empty input, rows with no seats, columns with no seats.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to store intermediate results.
- Testing considerations: Test the solution with different input sizes, test the solution with different combinations of students in the rows.