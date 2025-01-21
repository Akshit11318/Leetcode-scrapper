## The Number of Employees Which Report to Each Employee

**Problem Link:** https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description

**Problem Statement:**
- Input: A list of `Employee` objects, where each `Employee` has an `id`, a `name`, and a `managerId`.
- Constraints: 
  - The input list is not empty.
  - The `id` of each employee is unique.
  - The `managerId` of each employee is the `id` of another employee in the list, except for the top-level manager whose `managerId` is `NULL`.
- Expected output: A list of strings, where each string contains the `name` of an employee and the number of employees who report to them.
- Key requirements and edge cases to consider: 
  - The output list should be ordered by the `id` of the employees.
  - The number of employees who report to each employee should include both direct and indirect reports.

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a dictionary to store the employees who report to each manager.
- Step-by-step breakdown of the solution:
  1. Create a dictionary `reports` where the keys are the `id` of each employee and the values are lists of employees who report to them.
  2. Iterate through the list of employees and populate the `reports` dictionary.
  3. Create a dictionary `count` to store the number of employees who report to each employee.
  4. Iterate through the `reports` dictionary and calculate the number of employees who report to each employee, including both direct and indirect reports.
  5. Create a list of strings where each string contains the `name` of an employee and the number of employees who report to them.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

struct Employee {
    int id;
    std::string name;
    int managerId;
};

std::vector<std::string> countReports(std::vector<Employee>& employees) {
    // Create a dictionary to store the employees who report to each manager
    std::unordered_map<int, std::vector<int>> reports;
    for (const auto& employee : employees) {
        if (reports.find(employee.managerId) == reports.end()) {
            reports[employee.managerId] = {};
        }
        reports[employee.managerId].push_back(employee.id);
    }

    // Create a dictionary to store the number of employees who report to each employee
    std::unordered_map<int, int> count;
    for (const auto& employee : employees) {
        count[employee.id] = 0;
    }

    // Calculate the number of employees who report to each employee
    for (const auto& pair : reports) {
        int managerId = pair.first;
        std::vector<int> reportIds = pair.second;
        for (int reportId : reportIds) {
            count[managerId]++;
            if (reports.find(reportId) != reports.end()) {
                count[managerId] += count[reportId];
            }
        }
    }

    // Create a list of strings where each string contains the name of an employee and the number of employees who report to them
    std::vector<std::string> result;
    for (const auto& employee : employees) {
        result.push_back(employee.name + " " + std::to_string(count[employee.id]));
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of employees. This is because we are iterating through the list of employees and the `reports` dictionary in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we are storing the `reports` dictionary and the `count` dictionary.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to calculate the number of employees who report to each employee. The space complexity occurs because we are storing the `reports` dictionary and the `count` dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a depth-first search (DFS) to calculate the number of employees who report to each employee.
- Detailed breakdown of the approach:
  1. Create a dictionary `reports` where the keys are the `id` of each employee and the values are lists of employees who report to them.
  2. Create a dictionary `count` to store the number of employees who report to each employee.
  3. Define a DFS function to calculate the number of employees who report to each employee.
  4. Iterate through the list of employees and call the DFS function for each employee.
  5. Create a list of strings where each string contains the `name` of an employee and the number of employees who report to them.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

struct Employee {
    int id;
    std::string name;
    int managerId;
};

std::vector<std::string> countReports(std::vector<Employee>& employees) {
    // Create a dictionary to store the employees who report to each manager
    std::unordered_map<int, std::vector<int>> reports;
    for (const auto& employee : employees) {
        if (reports.find(employee.managerId) == reports.end()) {
            reports[employee.managerId] = {};
        }
        reports[employee.managerId].push_back(employee.id);
    }

    // Create a dictionary to store the number of employees who report to each employee
    std::unordered_map<int, int> count;
    for (const auto& employee : employees) {
        count[employee.id] = 0;
    }

    // Define a DFS function to calculate the number of employees who report to each employee
    std::function<int(int)> dfs = [&](int id) {
        if (reports.find(id) == reports.end()) {
            return 0;
        }
        int sum = 0;
        for (int reportId : reports[id]) {
            sum += 1 + dfs(reportId);
        }
        return sum;
    };

    // Calculate the number of employees who report to each employee
    for (const auto& employee : employees) {
        count[employee.id] = dfs(employee.id);
    }

    // Create a list of strings where each string contains the name of an employee and the number of employees who report to them
    std::vector<std::string> result;
    for (const auto& employee : employees) {
        result.push_back(employee.name + " " + std::to_string(count[employee.id]));
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because we are using a DFS to calculate the number of employees who report to each employee.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we are storing the `reports` dictionary and the `count` dictionary.
> - **Optimality proof:** The time complexity is optimal because we are only visiting each employee once during the DFS. The space complexity is optimal because we are only storing the necessary information in the `reports` dictionary and the `count` dictionary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, dictionary usage.
- Problem-solving patterns identified: Using a DFS to calculate the number of employees who report to each employee.
- Optimization techniques learned: Using a DFS to reduce the time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: Other problems involving hierarchical structures and DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly in the DFS function.
- Edge cases to watch for: Employees with no reports, employees with multiple reports.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.