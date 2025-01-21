## Primary Department for Each Employee

**Problem Link:** https://leetcode.com/problems/primary-department-for-each-employee/description

**Problem Statement:**
- Given the `Employees` table with columns `employee_id`, `name`, and `department_id`, and the `Department` table with columns `department_id` and `department_name`, find the primary department for each employee.
- Expected output format: A table with columns `employee_id`, `name`, and `primary_department`.
- Key requirements and edge cases to consider: Each employee has a primary department, and there are no duplicate employee IDs.
- Example test cases with explanations:
  - If an employee is in only one department, that is their primary department.
  - If an employee is in multiple departments, the department with the smallest ID is their primary department.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each employee, find all departments they belong to, and then determine the primary department.
- Step-by-step breakdown of the solution:
  1. Iterate over each employee in the `Employees` table.
  2. For each employee, find all departments they belong to by iterating over the `Department` table.
  3. Determine the primary department for each employee by finding the department with the smallest ID.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Employee {
    int employee_id;
    std::string name;
    int department_id;
};

struct Department {
    int department_id;
    std::string department_name;
};

std::vector<std::tuple<int, std::string, std::string>> primaryDepartmentForEachEmployee(std::vector<Employee>& employees, std::vector<Department>& departments) {
    std::vector<std::tuple<int, std::string, std::string>> result;
    for (const auto& employee : employees) {
        int minDepartmentId = INT_MAX;
        std::string primaryDepartment;
        for (const auto& department : departments) {
            if (department.department_id == employee.department_id) {
                if (department.department_id < minDepartmentId) {
                    minDepartmentId = department.department_id;
                    primaryDepartment = department.department_name;
                }
            }
        }
        result.push_back(std::make_tuple(employee.employee_id, employee.name, primaryDepartment));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of employees and $m$ is the number of departments, because we are iterating over each employee and then over each department for each employee.
> - **Space Complexity:** $O(n)$, because we are storing the result for each employee.
> - **Why these complexities occur:** The time complexity occurs because of the nested iteration over employees and departments, and the space complexity occurs because of the storage of the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the departments for each employee, and then find the primary department for each employee.
- Detailed breakdown of the approach:
  1. Create a hash map to store the departments for each employee.
  2. Iterate over the `Employees` table and populate the hash map.
  3. Iterate over the hash map and find the primary department for each employee by finding the department with the smallest ID.
- Proof of optimality: This approach is optimal because it reduces the time complexity to $O(n + m)$, where $n$ is the number of employees and $m$ is the number of departments.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Employee {
    int employee_id;
    std::string name;
    int department_id;
};

struct Department {
    int department_id;
    std::string department_name;
};

std::vector<std::tuple<int, std::string, std::string>> primaryDepartmentForEachEmployee(std::vector<Employee>& employees, std::vector<Department>& departments) {
    std::unordered_map<int, std::vector<int>> employeeDepartments;
    for (const auto& employee : employees) {
        employeeDepartments[employee.employee_id].push_back(employee.department_id);
    }
    
    std::vector<std::tuple<int, std::string, std::string>> result;
    for (const auto& employee : employees) {
        int minDepartmentId = INT_MAX;
        std::string primaryDepartment;
        for (const auto& departmentId : employeeDepartments[employee.employee_id]) {
            for (const auto& department : departments) {
                if (department.department_id == departmentId) {
                    if (department.department_id < minDepartmentId) {
                        minDepartmentId = department.department_id;
                        primaryDepartment = department.department_name;
                    }
                }
            }
        }
        result.push_back(std::make_tuple(employee.employee_id, employee.name, primaryDepartment));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of employees and $m$ is the number of departments, because we are iterating over each employee and each department once.
> - **Space Complexity:** $O(n + m)$, because we are storing the departments for each employee and the result.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to $O(n + m)$, which is the minimum possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, iteration, and optimization.
- Problem-solving patterns identified: Using hash maps to reduce time complexity.
- Optimization techniques learned: Reducing nested iteration by using hash maps.
- Similar problems to practice: Problems involving hash maps and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly populating the hash map or iterating over the result.
- Edge cases to watch for: Employees with no departments or departments with no employees.
- Performance pitfalls: Using nested iteration without optimization.
- Testing considerations: Testing with different input sizes and edge cases.