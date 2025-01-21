## Managers with at Least 5 Direct Reports

**Problem Link:** https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description

**Problem Statement:**
- Input format and constraints: The problem takes a table `Employee` with columns `id`, `name`, and `managerId`. The task is to find the names of managers who have at least 5 direct reports.
- Expected output format: The output should be a list of names of managers who meet the condition.
- Key requirements and edge cases to consider: Handling cases where a manager has fewer than 5 direct reports, and ensuring that only direct reports are counted.
- Example test cases with explanations: For instance, given a table with employees and their managers, identify which managers have at least 5 employees directly reporting to them.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each employee, check their manager, and count the number of employees each manager has.
- Step-by-step breakdown of the solution: 
  1. Create a dictionary or map to store the count of direct reports for each manager.
  2. Iterate through each employee in the table.
  3. For each employee, increment the count of direct reports for their manager in the dictionary.
  4. After counting, iterate through the dictionary and select managers with at least 5 direct reports.
- Why this approach comes to mind first: It's straightforward and involves directly counting the number of reports for each manager.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Employee {
    int id;
    string name;
    int managerId;
};

vector<string> findManagers(vector<Employee>& employees) {
    unordered_map<int, int> managerReports;
    for (const auto& employee : employees) {
        if (employee.managerId != NULL) { // Assuming NULL means no manager
            managerReports[employee.managerId]++;
        }
    }
    
    vector<string> result;
    for (const auto& employee : employees) {
        if (managerReports[employee.id] >= 5) {
            result.push_back(employee.name);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. We iterate through the employees twice: once to count the reports and once to find the managers with at least 5 reports.
> - **Space Complexity:** $O(n)$, as in the worst case, every employee could be a manager, and we store them in the `managerReports` dictionary.
> - **Why these complexities occur:** The iteration through employees for counting and selecting managers causes the time complexity. The space complexity is due to storing the count of reports for each manager.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating through all employees twice, we can combine the steps of counting reports and selecting managers into one pass by storing the employee names with their IDs in a separate data structure for efficient lookup.
- Detailed breakdown of the approach: 
  1. Create a dictionary to store the count of direct reports for each manager and another dictionary to store employee names by their IDs.
  2. Iterate through each employee, incrementing the report count for their manager and storing the employee's name by their ID.
  3. During the iteration, check if a manager has reached 5 direct reports and add their name to the result list if so.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data, minimizing both time and space complexity.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Employee {
    int id;
    string name;
    int managerId;
};

vector<string> findManagers(vector<Employee>& employees) {
    unordered_map<int, int> managerReports;
    unordered_map<int, string> employeeNames;
    vector<string> result;
    
    for (const auto& employee : employees) {
        employeeNames[employee.id] = employee.name;
        if (managerReports.find(employee.managerId) != managerReports.end()) {
            managerReports[employee.managerId]++;
            if (managerReports[employee.managerId] == 5) {
                result.push_back(employeeNames[employee.managerId]);
            }
        } else {
            managerReports[employee.managerId] = 1;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. We make a single pass through the employees.
> - **Space Complexity:** $O(n)$, for storing the count of reports for each manager and the names of employees by their IDs.
> - **Optimality proof:** This is the most efficient approach because it minimizes the number of passes through the data and uses dictionaries for efficient lookup and storage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of dictionaries for counting and lookup, and combining steps to minimize passes through data.
- Problem-solving patterns identified: The importance of storing and efficiently looking up related data (like employee names by ID).
- Optimization techniques learned: Minimizing the number of iterations through data and using appropriate data structures for efficient operations.
- Similar problems to practice: Other SQL or data manipulation problems that require efficient counting and selection based on conditions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (like a manager having fewer than 5 reports), or inefficiently iterating through data.
- Edge cases to watch for: Managers with exactly 5 reports, or cases where there are no managers with at least 5 direct reports.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with the size of the input data.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the solution is robust and correct.