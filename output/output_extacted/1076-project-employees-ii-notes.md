## Project Employees II

**Problem Link:** https://leetcode.com/problems/project-employees-ii/description

**Problem Statement:**
- Input format and constraints: The problem provides a table `Project` with columns `project_id` and `employee_id`. The goal is to find the `project_id` that has the most employees and return all such `project_id`s.
- Expected output format: A list of `project_id`s with the maximum number of employees.
- Key requirements and edge cases to consider:
  - There can be multiple `project_id`s with the same maximum number of employees.
  - The `project_id` should be returned even if there is only one employee.
- Example test cases with explanations:
  - If the table contains [(1, 1), (1, 2), (2, 1)], the output should be [1] because project 1 has the most employees.
  - If the table contains [(1, 1), (1, 2), (2, 1), (3, 1)], the output should be [1] because project 1 still has the most employees.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the number of employees for each project and compare them to find the maximum.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the count of employees for each project.
  2. Iterate through the table and update the count in the dictionary for each project.
  3. Find the maximum count.
  4. Return all project_ids that have the maximum count.
- Why this approach comes to mind first: It is a straightforward way to solve the problem by counting and comparing.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> projectEmployeesII(vector<vector<int>>& projects) {
    unordered_map<int, int> projectCount;
    int maxCount = 0;
    
    // Count employees for each project
    for (auto& project : projects) {
        projectCount[project[0]]++;
        maxCount = max(maxCount, projectCount[project[0]]);
    }
    
    vector<int> result;
    // Find projects with the maximum count
    for (auto& pair : projectCount) {
        if (pair.second == maxCount) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we make two passes through the data: one to count the employees and another to find the projects with the maximum count.
> - **Space Complexity:** $O(n)$, because in the worst case, every project could have a unique `project_id`, requiring space to store each count.
> - **Why these complexities occur:** The brute force approach requires iterating through all the data to count employees and then again to find the maximum, leading to linear time complexity. The space complexity is also linear because we need to store the count for each project.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can still use a dictionary to count the employees for each project but optimize the process by keeping track of the maximum count as we iterate through the table, thus avoiding the need for a second pass.
- Detailed breakdown of the approach:
  1. Initialize a dictionary to store the count of employees for each project and a variable to keep track of the maximum count.
  2. Iterate through the table, updating the count in the dictionary for each project and updating the maximum count if necessary.
  3. During the iteration, also keep track of the projects that have the current maximum count.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data, minimizing both time and space complexity.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> projectEmployeesII(vector<vector<int>>& projects) {
    unordered_map<int, int> projectCount;
    int maxCount = 0;
    vector<int> maxProjects;
    
    for (auto& project : projects) {
        projectCount