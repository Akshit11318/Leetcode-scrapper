## Count Student Number in Departments
**Problem Link:** https://leetcode.com/problems/count-student-number-in-departments/description

**Problem Statement:**
- Input format: A table `departments` with columns `dept_id` (department ID) and `student_id` (student ID).
- Constraints: `1 <= dept_id <= 10^5` and `1 <= student_id <= 10^5`.
- Expected output format: The number of students in each department.
- Key requirements: Count the number of students in each department.
- Edge cases: Empty table, department with no students, student in multiple departments.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each department and count the number of students.
- Step-by-step breakdown:
  1. Initialize a dictionary to store the count of students in each department.
  2. Iterate through each row in the `departments` table.
  3. For each row, increment the count of students in the corresponding department.
- Why this approach comes to mind first: It's a straightforward way to count the number of students in each department.

```cpp
#include <iostream>
#include <unordered_map>

using namespace std;

int countStudents(unordered_map<int, int>& departmentCounts, vector<vector<int>>& departments) {
    for (const auto& department : departments) {
        int deptId = department[0];
        int studentId = department[1];
        if (departmentCounts.find(deptId) != departmentCounts.end()) {
            departmentCounts[deptId]++;
        } else {
            departmentCounts[deptId] = 1;
        }
    }
    return departmentCounts.size();
}

int main() {
    unordered_map<int, int> departmentCounts;
    vector<vector<int>> departments = {{1, 1}, {1, 2}, {2, 3}};
    int numDepartments = countStudents(departmentCounts, departments);
    for (const auto& department : departmentCounts) {
        cout << "Department " << department.first << ": " << department.second << " students" << endl;
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `departments` table, because we iterate through each row once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique departments, because we store the count of students in each department in a dictionary.
> - **Why these complexities occur:** The time complexity is linear because we only iterate through the table once, and the space complexity is proportional to the number of unique departments because we store a count for each department.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a SQL query to count the number of students in each department.
- Detailed breakdown:
  1. Use a `GROUP BY` clause to group the rows by department ID.
  2. Use a `COUNT` function to count the number of rows in each group.
- Proof of optimality: This approach is optimal because it uses a single SQL query to count the number of students in each department, which is more efficient than iterating through the table multiple times.

```sql
SELECT dept_id, COUNT(student_id) AS student_count
FROM departments
GROUP BY dept_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `departments` table, because the database engine can optimize the query to run in linear time.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique departments, because the database engine stores the count of students in each department in memory.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to count the number of students in each department, which is more efficient than iterating through the table multiple times.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Counting, grouping, and aggregating data.
- Problem-solving patterns: Using SQL queries to optimize data analysis.
- Optimization techniques: Using database engines to optimize queries.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `GROUP BY` clause when counting data.
- Edge cases: Handling empty tables or departments with no students.
- Performance pitfalls: Iterating through the table multiple times instead of using a single SQL query.
- Testing considerations: Testing the query with different inputs and edge cases.