## All People Report to the Given Manager
**Problem Link:** https://leetcode.com/problems/all-people-report-to-the-given-manager/description

**Problem Statement:**
- Input format and constraints: Given a list of `id`, `name`, `managerId` for each employee, and a given `managerId`.
- Expected output format: A list of `id` for all employees that report to the given manager, either directly or indirectly.
- Key requirements and edge cases to consider: The `id` of the given manager is guaranteed to be in the list of employees.
- Example test cases with explanations:
  - Input: `id = [1,2,3], name = ["John","Alice","Bob"], managerId = [3,3,0], managerId = 3`
  - Output: `[1,2]`
  - Explanation: Employees with `id` 1 and 2 report to the employee with `id` 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each employee, check if they report to the given manager, either directly or indirectly.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the manager of each employee.
  2. Iterate over the employees and check if they report to the given manager.
  3. If an employee reports to the given manager, add them to the result list.
  4. For each employee in the result list, check if they have any direct reports and add them to the result list.
- Why this approach comes to mind first: It's a straightforward solution that checks each employee individually.

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>

vector<int> allPeopleReportToTheGivenManager(vector<int>& id, vector<string>& name, vector<int>& managerId, int managerIdGiven) {
    unordered_map<int, int> managerOf;
    for (int i = 0; i < id.size(); i++) {
        managerOf[id[i]] = managerId[i];
    }
    
    unordered_set<int> result;
    for (int i = 0; i < id.size(); i++) {
        if (managerOf[id[i]] == managerIdGiven) {
            result.insert(id[i]);
        }
    }
    
    // Add indirect reports
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < id.size(); i++) {
            if (managerOf[id[i]] != managerIdGiven && result.find(managerOf[id[i]]) != result.end() && result.find(id[i]) == result.end()) {
                result.insert(id[i]);
                changed = true;
            }
        }
    }
    
    vector<int> resultVector(result.begin(), result.end());
    return resultVector;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of employees. This is because in the worst case, we need to iterate over all employees for each employee.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we need to store the manager of each employee and the result list.
> - **Why these complexities occur:** The brute force approach has high time complexity because it uses a nested loop to check for indirect reports.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) to find all employees that report to the given manager.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the direct reports of each employee.
  2. Perform a DFS from the given manager to find all employees that report to them.
- Proof of optimality: This approach is optimal because it only visits each employee once, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: This approach is already optimal because it only uses a single pass over the employees.

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>

vector<int> allPeopleReportToTheGivenManager(vector<int>& id, vector<string>& name, vector<int>& managerId, int managerIdGiven) {
    unordered_map<int, vector<int>> directReports;
    for (int i = 0; i < id.size(); i++) {
        if (directReports.find(managerId[i]) == directReports.end()) {
            directReports[managerId[i]] = {};
        }
        directReports[managerId[i]].push_back(id[i]);
    }
    
    unordered_set<int> result;
    function<void(int)> dfs = [&](int managerId) {
        if (directReports.find(managerId) != directReports.end()) {
            for (int directReport : directReports[managerId]) {
                result.insert(directReport);
                dfs(directReport);
            }
        }
    };
    
    dfs(managerIdGiven);
    vector<int> resultVector(result.begin(), result.end());
    return resultVector;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because we only visit each employee once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we need to store the direct reports of each employee and the result list.
> - **Optimality proof:** This approach is optimal because it only uses a single pass over the employees, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), dictionary usage.
- Problem-solving patterns identified: Using a dictionary to store relationships between employees.
- Optimization techniques learned: Reducing time complexity by avoiding nested loops.
- Similar problems to practice: Other problems involving graph traversal and employee relationships.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as employees with no direct reports.
- Edge cases to watch for: Employees with no direct reports, employees with multiple direct reports.
- Performance pitfalls: Using nested loops to check for indirect reports, resulting in high time complexity.
- Testing considerations: Testing with different employee relationships and edge cases to ensure correctness.