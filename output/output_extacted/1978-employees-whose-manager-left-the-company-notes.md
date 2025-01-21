## Employees Whose Manager Left the Company

**Problem Link:** https://leetcode.com/problems/employees-whose-manager-left-the-company/description

**Problem Statement:**
- Input format and constraints: The problem takes two tables as input, `Employees` and `Managers`, with columns `id`, `name`, `department`, `managerId` for `Employees`, and `id`, `name`, `department` for `Managers`. 
- Expected output format: The output should be a table with `id` and `name` of employees whose managers have left the company.
- Key requirements and edge cases to consider: 
    - An employee's manager is defined by the `managerId` in the `Employees` table matching the `id` in the `Managers` table.
    - If a manager is not present in the `Managers` table, it implies the manager has left the company.
- Example test cases with explanations: 
    - Test cases should cover scenarios where employees have managers who are present or absent in the `Managers` table.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over each employee in the `Employees` table and check if their manager exists in the `Managers` table.
- Step-by-step breakdown of the solution:
    1. Iterate over each row in the `Employees` table.
    2. For each employee, check if there is a matching `id` in the `Managers` table for their `managerId`.
    3. If no match is found, it means the manager has left, so include the employee's `id` and `name` in the result.
- Why this approach comes to mind first: It's a straightforward, intuitive method based on the problem's requirements.

```cpp
SELECT E.id, E.name
FROM Employees E
WHERE E.managerId NOT IN (SELECT M.id FROM Managers M);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n*m)$ where $n$ is the number of employees and $m$ is the number of managers, because for each employee, we potentially scan all managers.
> - **Space Complexity:** $O(1)$, as we're not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves nested scans of the `Employees` and `Managers` tables, leading to the $O(n*m)$ time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize SQL's built-in `LEFT JOIN` or `NOT EXISTS` to efficiently find employees whose managers are not present in the `Managers` table.
- Detailed breakdown of the approach: 
    - Perform a `LEFT JOIN` of `Employees` with `Managers` on the condition that `Employees.managerId = Managers.id`.
    - Select the `id` and `name` of employees where the `Managers.id` is `NULL`, indicating the manager is not found in the `Managers` table.
- Proof of optimality: This approach is optimal because it leverages the database's ability to perform joins efficiently, reducing the time complexity compared to the brute force approach.
- Why further optimization is impossible: The optimal approach already minimizes the number of operations needed to find the desired employees.

```cpp
SELECT E.id, E.name
FROM Employees E
LEFT JOIN Managers M ON E.managerId = M.id
WHERE M.id IS NULL;
```

Alternatively, using `NOT EXISTS`:

```cpp
SELECT E.id, E.name
FROM Employees E
WHERE NOT EXISTS (
    SELECT 1
    FROM Managers M
    WHERE M.id = E.managerId
);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of employees and $m$ is the number of managers, because the database can perform the join and filtering in linear time.
> - **Space Complexity:** $O(n + m)$, for storing the results of the join.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least read the input tables once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of SQL joins and filtering.
- Problem-solving patterns identified: Leveraging database capabilities for efficient data manipulation.
- Optimization techniques learned: Using `LEFT JOIN` or `NOT EXISTS` instead of nested queries for better performance.
- Similar problems to practice: Other SQL problems involving joins, subqueries, and data filtering.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect join conditions or forgetting to handle `NULL` values.
- Edge cases to watch for: Employees without managers or managers without employees.
- Performance pitfalls: Using inefficient query structures like nested scans.
- Testing considerations: Ensure test cases cover various scenarios, including empty tables and tables with no matching managers.