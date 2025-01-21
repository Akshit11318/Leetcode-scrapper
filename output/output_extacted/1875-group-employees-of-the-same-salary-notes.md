## Group Employees of the Same Salary

**Problem Link:** https://leetcode.com/problems/group-employees-of-the-same-salary/description

**Problem Statement:**
- Input format: A list of employees with their IDs and salaries.
- Constraints: Each employee has a unique ID and a salary.
- Expected output format: A list of lists where each sublist contains the IDs of employees with the same salary.
- Key requirements and edge cases to consider:
  - Handling employees with unique salaries.
  - Handling employees with duplicate salaries.
- Example test cases with explanations:
  - Test case 1: Employees with unique salaries.
  - Test case 2: Employees with duplicate salaries.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the list of employees and compare each employee's salary with every other employee's salary.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. Iterate through the list of employees.
  3. For each employee, iterate through the list of employees again to find employees with the same salary.
  4. If an employee with the same salary is found, add their ID to a sublist.
  5. Add the sublist to the result list.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
vector<vector<int>> groupEmployees(vector<int>& employee_id, vector<int>& employee_salary) {
    vector<vector<int>> result;
    for (int i = 0; i < employee_id.size(); i++) {
        vector<int> sublist;
        for (int j = 0; j < employee_id.size(); j++) {
            if (employee_salary[i] == employee_salary[j]) {
                sublist.push_back(employee_id[j]);
            }
        }
        // Remove duplicates from sublist
        sort(sublist.begin(), sublist.end());
        sublist.erase(unique(sublist.begin(), sublist.end()), sublist.end());
        if (!sublist.empty()) {
            result.push_back(sublist);
        }
    }
    // Remove duplicates from result
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of employees. This is because we have a nested loop structure, where each employee is compared with every other employee.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we need to store the result list, which can contain up to $n$ sublists.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it involves comparing each employee with every other employee. The space complexity is relatively low because we only need to store the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the employee IDs for each salary.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store the employee IDs for each salary.
  2. Iterate through the list of employees and add each employee's ID to the corresponding salary in the hash map.
  3. Convert the hash map values to a list of lists and return the result.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because it avoids the nested loop structure.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the minimum required to iterate through the list of employees.

```cpp
vector<vector<int>> groupEmployees(vector<int>& employee_id, vector<int>& employee_salary) {
    unordered_map<int, vector<int>> salary_map;
    for (int i = 0; i < employee_id.size(); i++) {
        salary_map[employee_salary[i]].push_back(employee_id[i]);
    }
    vector<vector<int>> result;
    for (auto& pair : salary_map) {
        result.push_back(pair.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees. This is because we only need to iterate through the list of employees once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees. This is because we need to store the hash map, which can contain up to $n$ employee IDs.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the minimum required to iterate through the list of employees.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps and iteration.
- Problem-solving patterns identified: Using hash maps to store and retrieve data efficiently.
- Optimization techniques learned: Avoiding nested loop structures and using hash maps to reduce time complexity.
- Similar problems to practice: Problems involving hash maps and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the hash map or not checking for duplicates in the result list.
- Edge cases to watch for: Handling employees with unique salaries or duplicate salaries.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the function with different input scenarios and edge cases.