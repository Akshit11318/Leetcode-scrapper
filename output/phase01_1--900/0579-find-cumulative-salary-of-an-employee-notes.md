## Find Cumulative Salary of an Employee

**Problem Link:** https://leetcode.com/problems/find-cumulative-salary-of-an-employee/description

**Problem Statement:**
- Given an employee's `id`, `month`, and `salary`, calculate the cumulative salary for the employee.
- Input format and constraints: 
  - `id` is an integer representing the employee's ID.
  - `month` is an integer representing the month.
  - `salary` is an integer representing the salary for the month.
- Expected output format: The cumulative salary for the employee.
- Key requirements and edge cases to consider:
  - Handle cases where the employee has no previous salary records.
  - Handle cases where the employee has multiple salary records for the same month.

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the cumulative salary by summing up all the salaries for the employee.
- This approach involves iterating over all the salary records for the employee and summing up the salaries.

```cpp
struct Employee {
    int id;
    int month;
    int salary;
};

int getCumulativeSalary(vector<Employee>& employees, int id) {
    int cumulativeSalary = 0;
    for (const auto& employee : employees) {
        if (employee.id == id) {
            cumulativeSalary += employee.salary;
        }
    }
    return cumulativeSalary;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, because in the worst case, we need to iterate over all the employees.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the cumulative salary.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over all the employees to calculate the cumulative salary. The space complexity is constant because we only use a fixed amount of space to store the cumulative salary.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to use a `map` to store the cumulative salary for each employee.
- We can then iterate over the employees and update the cumulative salary for each employee.

```cpp
int getCumulativeSalary(vector<Employee>& employees, int id) {
    unordered_map<int, int> cumulativeSalaries;
    for (const auto& employee : employees) {
        cumulativeSalaries[employee.id] += employee.salary;
    }
    return cumulativeSalaries[id];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, because in the worst case, we need to iterate over all the employees.
> - **Space Complexity:** $O(n)$, because we use a `map` to store the cumulative salaries for all the employees.
> - **Optimality proof:** This is the optimal solution because we only need to iterate over the employees once to calculate the cumulative salaries. Using a `map` allows us to store and retrieve the cumulative salaries in constant time.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `map` to store and retrieve data in constant time.
- Problem-solving patterns identified: Iterating over a list of data and updating a running total.
- Optimization techniques learned: Using a `map` to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve calculating a running total or using a `map` to store and retrieve data.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the cumulative salary to 0 before iterating over the employees.
- Edge cases to watch for: Handling cases where the employee has no previous salary records.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it works correctly.