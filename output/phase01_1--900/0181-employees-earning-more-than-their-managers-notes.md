## Employees Earning More Than Their Managers
**Problem Link:** https://leetcode.com/problems/employees-earning-more-than-their-managers/description

**Problem Statement:**
- Input format: You are given a table `Employee` with columns `id`, `name`, `salary`, and `managerId`.
- Constraints: The table has at least one row, and the `id` and `managerId` are integers.
- Expected output format: A table with the names of employees who earn more than their managers.
- Key requirements and edge cases to consider: 
  - Each employee has a unique `id`.
  - `managerId` is the `id` of the employee's manager.
  - The `id` of the top manager is `NULL`.
- Example test cases with explanations:
  - For the table `Employee` with rows `(1, 'John', 100, NULL)`, `(2, 'Anna', 200, 1)`, `(3, 'Peter', 90, 1)`, the output should be `Anna` because she earns more than her manager `John`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each employee and compare their salary with their manager's salary.
- Step-by-step breakdown of the solution:
  1. Iterate over each employee in the table.
  2. For each employee, find their manager's salary by iterating over the table again.
  3. Compare the employee's salary with their manager's salary. If the employee earns more, add their name to the result.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
#include <vector>
#include <string>

using namespace std;

struct Employee {
    int id;
    string name;
    int salary;
    int managerId;
};

vector<string> employeesEarningMoreThanTheirManagers(vector<Employee>& employees) {
    vector<string> result;
    for (const auto& employee : employees) {
        for (const auto& manager : employees) {
            if (employee.managerId == manager.id && employee.salary > manager.salary) {
                result.push_back(employee.name);
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of employees. This is because we are iterating over the table for each employee.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees who earn more than their managers. This is because we are storing the names of these employees in the result vector.
> - **Why these complexities occur:** The time complexity is high because of the nested iteration, and the space complexity is moderate because we are storing the result in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over the table for each employee, we can create a map that maps each manager's `id` to their `salary`. This way, we can find a manager's salary in constant time.
- Detailed breakdown of the approach:
  1. Create a map `managerSalaries` that maps each manager's `id` to their `salary`.
  2. Iterate over the employees. For each employee, check if their manager's salary is in the `managerSalaries` map.
  3. If the employee earns more than their manager, add their name to the result.
- Proof of optimality: This solution has a linear time complexity because we are iterating over the table only twice: once to create the `managerSalaries` map and once to find the employees who earn more than their managers.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

struct Employee {
    int id;
    string name;
    int salary;
    int managerId;
};

vector<string> employeesEarningMoreThanTheirManagers(vector<Employee>& employees) {
    unordered_map<int, int> managerSalaries;
    for (const auto& employee : employees) {
        managerSalaries[employee.id] = employee.salary;
    }

    vector<string> result;
    for (const auto& employee : employees) {
        if (managerSalaries.find(employee.managerId) != managerSalaries.end() && employee.salary > managerSalaries[employee.managerId]) {
            result.push_back(employee.name);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because we are iterating over the table twice: once to create the `managerSalaries` map and once to find the employees who earn more than their managers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we are storing the `managerSalaries` map and the result vector.
> - **Optimality proof:** The time complexity is optimal because we are iterating over the table only twice, and the space complexity is moderate because we are storing the `managerSalaries` map and the result vector.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, mapping, and comparison.
- Problem-solving patterns identified: Using a map to store and retrieve data efficiently.
- Optimization techniques learned: Reducing the time complexity by avoiding nested iteration.
- Similar problems to practice: Problems that involve iteration, mapping, and comparison, such as finding the maximum or minimum value in a table.

**Mistakes to Avoid:**
- Common implementation errors: Nested iteration, incorrect use of maps or vectors.
- Edge cases to watch for: Employees with no manager, employees with the same salary as their manager.
- Performance pitfalls: High time complexity due to nested iteration.
- Testing considerations: Test cases with different table sizes, employee salaries, and manager relationships.