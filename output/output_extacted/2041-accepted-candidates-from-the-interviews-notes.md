## Accepted Candidates from the Interviews
**Problem Link:** https://leetcode.com/problems/accepted-candidates-from-the-interviews/description

**Problem Statement:**
- Input format: A table `interviews` with columns `candidate_id`, `interviewer_id`, and `score`.
- Constraints: The table contains at least one row and the `candidate_id` and `interviewer_id` are integers.
- Expected output format: A list of `candidate_id`s that have been accepted.
- Key requirements and edge cases to consider: A candidate is considered accepted if they have received at least one score greater than or equal to 90 from any interviewer.
- Example test cases with explanations:
  - Example 1: 
    - Input: 
      ```sql
+-------------+--------------+-------+
| candidate_id| interviewer_id| score |
+-------------+--------------+-------+
| 1           | 1            | 90    |
| 1           | 2            | 80    |
| 2           | 1            | 80    |
| 3           | 1            | 90    |
+-------------+--------------+-------+
```
    - Output: 
      ```sql
+-------------+
| candidate_id|
+-------------+
| 1           |
| 3           |
+-------------+
```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simply iterate over each row in the table, check if the score is greater than or equal to 90, and keep track of the accepted candidates.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store the accepted candidates.
  2. Iterate over each row in the table.
  3. For each row, check if the score is greater than or equal to 90.
  4. If the score is greater than or equal to 90, add the candidate_id to the set of accepted candidates.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
#include <iostream>
#include <set>
#include <vector>

// Define a struct to represent a row in the table
struct Row {
    int candidate_id;
    int interviewer_id;
    int score;
};

std::vector<int> acceptedCandidates(std::vector<Row>& rows) {
    std::set<int> accepted;
    for (const auto& row : rows) {
        if (row.score >= 90) {
            accepted.insert(row.candidate_id);
        }
    }
    std::vector<int> result(accepted.begin(), accepted.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we iterate over each row once.
> - **Space Complexity:** $O(n)$, because in the worst case, all candidates could be accepted and stored in the set.
> - **Why these complexities occur:** The iteration over the rows causes the time complexity, and the storage of accepted candidates causes the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity because we must examine each row at least once to determine if a candidate is accepted.
- Detailed breakdown of the approach: The same as the brute force approach, but with a focus on optimizing the implementation.
- Proof of optimality: Any algorithm must examine each row at least once, resulting in a time complexity of at least $O(n)$.
- Why further optimization is impossible: The problem requires examining each row, making it impossible to achieve a better time complexity than $O(n)$.

```cpp
#include <iostream>
#include <set>
#include <vector>

// Define a struct to represent a row in the table
struct Row {
    int candidate_id;
    int interviewer_id;
    int score;
};

std::vector<int> acceptedCandidates(std::vector<Row>& rows) {
    std::set<int> accepted;
    for (const auto& row : rows) {
        if (row.score >= 90) {
            accepted.insert(row.candidate_id);
        }
    }
    std::vector<int> result(accepted.begin(), accepted.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table.
> - **Space Complexity:** $O(n)$, because in the worst case, all candidates could be accepted and stored in the set.
> - **Optimality proof:** The algorithm has the optimal time complexity because it only requires a single pass over the data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a dataset, use of a set for efficient storage and lookup.
- Problem-solving patterns identified: Directly addressing the problem statement with a straightforward solution.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems involving iteration over a dataset and filtering based on conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input table.
- Edge cases to watch for: An empty input table, or a table with no accepted candidates.
- Performance pitfalls: Using an inefficient data structure, such as a vector instead of a set, to store the accepted candidates.
- Testing considerations: Thoroughly testing the function with various input scenarios, including edge cases.