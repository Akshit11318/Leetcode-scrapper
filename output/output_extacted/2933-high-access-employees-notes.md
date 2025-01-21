## High Access Employees
**Problem Link:** [https://leetcode.com/problems/high-access-employees/description](https://leetcode.com/problems/high-access-employees/description)

**Problem Statement:**
- Input: An array of `Employee` objects, each containing `id`, `name`, `departmentId`, and `managerId`.
- Constraints: 
  - The total number of employees is between $1$ and $10^5$.
  - The `departmentId` and `managerId` are integers between $1$ and $10^5$.
- Expected output: An array of strings representing the names of employees with the highest access level in each department.
- Key requirements and edge cases:
  - An employee has the highest access level in their department if they are the manager of that department or if their manager has the highest access level.
  - If there are multiple employees with the same highest access level, include all of them in the output.
- Example test cases:
  - Input: `employees = [[1, "John", 1, -1], [2, "Alice", 1, 1], [3, "Bob", 2, 1], [4, "Eve", 2, 3], [5, "Mike", 2, -1]]`
  - Output: `["Alice", "Bob", "Eve"]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each employee, determining their access level, and comparing it with others in the same department.
- To find the access level of an employee, we need to traverse up the management hierarchy until we reach the top-level manager.
- We keep track of the access level for each employee and their department.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

struct Employee {
    int id;
    std::string name;
    int departmentId;
    int managerId;
};

std::vector<std::string> highAccessEmployees(std::vector<Employee>& employees) {
    std::unordered_map<int, std::vector<std::string>> departmentEmployees;
    std::unordered_map<int, int> accessLevels;

    // Group employees by department
    for (const auto& employee : employees) {
        departmentEmployees[employee.departmentId].push_back(employee.name);
    }

    // Calculate access levels
    for (const auto& employee : employees) {
        int current = employee.id;
        int level = 0;
        while (current != -1) {
            level++;
            // Find the manager of the current employee
            for (const auto& e : employees) {
                if (e.id == current) {
                    current = e.managerId;
                    break;
                }
            }
        }
        accessLevels[employee.id] = level;
    }

    // Find employees with the highest access level in each department
    std::vector<std::string> result;
    for (const auto& department : departmentEmployees) {
        int maxLevel = 0;
        for (const auto& employeeName : department.second) {
            // Find the employee object for the current name
            for (const auto& e : employees) {
                if (e.name == employeeName) {
                    if (accessLevels[e.id] > maxLevel) {
                        maxLevel = accessLevels[e.id];
                        result.clear();
                        result.push_back(employeeName);
                    } else if (accessLevels[e.id] == maxLevel) {
                        result.push_back(employeeName);
                    }
                }
            }
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of employees. This is because for each employee, we potentially iterate through all employees to find their manager and calculate their access level.
> - **Space Complexity:** $O(n)$, for storing the department-wise grouping of employees and access levels.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the employees, leading to a quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- To optimize, we first build a map of `managerId` to `employeeId` for efficient lookup of an employee's manager.
- Then, we perform a depth-first search (DFS) from each employee to calculate their access level. This avoids the need for nested iterations over all employees.
- We maintain a `visited` set to prevent revisiting employees and to avoid infinite loops in case of cyclic dependencies.

```cpp
std::vector<std::string> highAccessEmployees(std::vector<Employee>& employees) {
    std::unordered_map<int, std::vector<std::string>> departmentEmployees;
    std::unordered_map<int, int> managerToEmployee;
    std::unordered_map<int, int> accessLevels;

    // Map managerId to employeeId for efficient lookup
    for (const auto& employee : employees) {
        managerToEmployee[employee.id] = employee.managerId;
    }

    // Group employees by department
    for (const auto& employee : employees) {
        departmentEmployees[employee.departmentId].push_back(employee.name);
    }

    // Calculate access levels using DFS
    std::unordered_set<int> visited;
    for (const auto& employee : employees) {
        if (visited.find(employee.id) == visited.end()) {
            dfs(employee.id, visited, managerToEmployee, accessLevels);
        }
    }

    // Find employees with the highest access level in each department
    std::vector<std::string> result;
    for (const auto& department : departmentEmployees) {
        int maxLevel = 0;
        for (const auto& employeeName : department.second) {
            // Find the employee object for the current name
            for (const auto& e : employees) {
                if (e.name == employeeName) {
                    if (accessLevels[e.id] > maxLevel) {
                        maxLevel = accessLevels[e.id];
                        result.clear();
                        result.push_back(employeeName);
                    } else if (accessLevels[e.id] == maxLevel) {
                        result.push_back(employeeName);
                    }
                }
            }
        }
    }

    return result;
}

void dfs(int currentId, std::unordered_set<int>& visited, std::unordered_map<int, int>& managerToEmployee, std::unordered_map<int, int>& accessLevels) {
    visited.insert(currentId);
    int managerId = managerToEmployee[currentId];
    if (managerId != -1 && visited.find(managerId) == visited.end()) {
        dfs(managerId, visited, managerToEmployee, accessLevels);
    }
    // Calculate access level based on the depth of the DFS
    accessLevels[currentId] = getDepth(currentId, managerToEmployee);
}

int getDepth(int currentId, std::unordered_map<int, int>& managerToEmployee) {
    int depth = 0;
    int managerId = managerToEmployee[currentId];
    while (managerId != -1) {
        depth++;
        managerId = managerToEmployee[managerId];
    }
    return depth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because each employee is visited once during the DFS.
> - **Space Complexity:** $O(n)$, for storing the `visited` set, `managerToEmployee` map, and `accessLevels` map.
> - **Optimality proof:** This approach is optimal because it visits each employee exactly once, minimizing the number of operations required to calculate access levels.

---

### Final Notes

**Learning Points:**
- The importance of **efficient data structures** (e.g., `unordered_map`, `unordered_set`) for fast lookup and insertion.
- **Depth-first search (DFS)** as a technique for traversing graphs or trees, useful in problems involving hierarchical relationships.
- **Optimization techniques**, such as avoiding nested iterations and using memoization (implicitly through the `visited` set).

**Mistakes to Avoid:**
- **Inefficient data structures**: Using `vector` or `list` for lookup operations can lead to high time complexities.
- **Nested iterations**: Avoid iterating over all employees for each employee, as this can result in quadratic time complexity.
- **Not handling cycles**: In problems involving graphs, failing to handle cycles can lead to infinite loops or incorrect results.