## CEO Subordinate Hierarchy
**Problem Link:** https://leetcode.com/problems/ceo-subordinate-hierarchy/description

**Problem Statement:**
- Input format: A table `Employees` with columns `employee_id` and `manager_id`.
- Constraints: `1 <= employee_id <= 10^5`, `1 <= manager_id <= 10^5`, and `employee_id` is unique.
- Expected output format: A hierarchical structure showing the CEO (the employee with no manager) at the top and their direct and indirect subordinates below them.
- Key requirements and edge cases to consider: The CEO has no manager, and every other employee has a manager. The hierarchy should be constructed based on the manager-employee relationships.
- Example test cases with explanations:
  - Test case 1: A simple hierarchy with a CEO and two direct subordinates.
  - Test case 2: A more complex hierarchy with multiple levels of subordinates.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by identifying the CEO, then recursively find their direct and indirect subordinates.
- Step-by-step breakdown of the solution:
  1. Find the CEO by selecting the employee with no manager.
  2. Use a recursive function to find the CEO's direct and indirect subordinates.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Employee {
    int employee_id;
    int manager_id;
};

std::unordered_map<int, std::vector<int>> build_hierarchy(std::vector<Employee>& employees) {
    std::unordered_map<int, std::vector<int>> hierarchy;
    for (const auto& employee : employees) {
        if (hierarchy.find(employee.manager_id) == hierarchy.end()) {
            hierarchy[employee.manager_id] = {};
        }
        hierarchy[employee.manager_id].push_back(employee.employee_id);
    }
    return hierarchy;
}

void print_hierarchy(const std::unordered_map<int, std::vector<int>>& hierarchy, int manager_id, int level = 0) {
    std::cout << std::string(level * 2, ' ') << manager_id << std::endl;
    if (hierarchy.find(manager_id) != hierarchy.end()) {
        for (const auto& employee_id : hierarchy.at(manager_id)) {
            print_hierarchy(hierarchy, employee_id, level + 1);
        }
    }
}

int main() {
    std::vector<Employee> employees = {{1, 0}, {2, 1}, {3, 1}, {4, 2}, {5, 2}};
    std::unordered_map<int, std::vector<int>> hierarchy = build_hierarchy(employees);
    print_hierarchy(hierarchy, 1);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, since we're doing a constant amount of work for each employee.
> - **Space Complexity:** $O(n)$, since in the worst case, we might store every employee in the hierarchy.
> - **Why these complexities occur:** The brute force approach has a linear time complexity because it involves a single pass through the list of employees to build the hierarchy. The space complexity is also linear because we're storing the hierarchy in a data structure that can potentially hold every employee.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a single SQL query that selects the CEO and their direct and indirect subordinates.
- Detailed breakdown of the approach:
  1. Select the CEO by finding the employee with no manager.
  2. Use a recursive common table expression (CTE) to find the CEO's direct and indirect subordinates.
- Proof of optimality: This approach is optimal because it uses a single SQL query to solve the problem, which is more efficient than any approach that involves multiple queries or manual recursion.
- Why further optimization is impossible: This approach is already optimal because it uses a single query to solve the problem, which is the most efficient way to solve it.

```sql
WITH RECURSIVE hierarchy AS (
    SELECT employee_id, manager_id, 0 AS level
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.manager_id, level + 1
    FROM Employees e
    JOIN hierarchy m ON e.manager_id = m.employee_id
)
SELECT * FROM hierarchy;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, since the database is doing a constant amount of work for each employee.
> - **Space Complexity:** $O(n)$, since in the worst case, the database might store every employee in the hierarchy.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to solve the problem, which is more efficient than any approach that involves multiple queries or manual recursion.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive common table expressions, hierarchical queries.
- Problem-solving patterns identified: Using a single query to solve a problem, using recursion to traverse a hierarchy.
- Optimization techniques learned: Using a single query instead of multiple queries, using recursion instead of manual iteration.
- Similar problems to practice: Other problems that involve hierarchical data, such as finding the ancestors of a node in a tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of the recursion, using an incorrect join condition.
- Edge cases to watch for: Employees with no manager, employees with multiple managers.
- Performance pitfalls: Using multiple queries instead of a single query, using manual iteration instead of recursion.
- Testing considerations: Testing the query with different inputs, testing the query with a large number of employees.