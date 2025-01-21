## Find Latest Salaries
**Problem Link:** https://leetcode.com/problems/find-latest-salaries/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the latest salaries for each employee in a company. The input is a table `Employee` with columns `employee_id`, `salary`, and `from_date`, `to_date`. The constraints are that the table contains at least one record and the dates are in the format `YYYY-MM-DD`.
- Expected output format: The output should be a table with the `employee_id` and the latest `salary` for each employee.
- Key requirements and edge cases to consider: The key requirement is to find the latest salary for each employee based on the `from_date` and `to_date`. An edge case to consider is when an employee has multiple salary records with the same `to_date`, in which case the latest salary should be the one with the latest `from_date`.
- Example test cases with explanations:
  - Example 1: The input table has two records for an employee with `employee_id` = 1, one with `salary` = 10000 and `from_date` = '2020-01-01', `to_date` = '2020-12-31', and another with `salary` = 20000 and `from_date` = '2021-01-01', `to_date` = '2021-12-31'. The output should be the `employee_id` = 1 with the latest `salary` = 20000.
  - Example 2: The input table has one record for an employee with `employee_id` = 2, with `salary` = 30000 and `from_date` = '2020-01-01', `to_date` = '2020-12-31'. The output should be the `employee_id` = 2 with the latest `salary` = 30000.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to iterate over each record in the `Employee` table and find the latest `salary` for each `employee_id`.
- Step-by-step breakdown of the solution:
  1. Iterate over each record in the `Employee` table.
  2. For each record, check if the `employee_id` is already in the result table.
  3. If it is, update the `salary` if the current record's `to_date` is later than the existing `to_date`.
  4. If it is not, add a new record to the result table.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem, but it is not efficient for large tables.

```cpp
SELECT employee_id, MAX(salary) AS latest_salary
FROM Employee
GROUP BY employee_id
```

However, the above query does not guarantee the correct result because it simply selects the maximum salary for each employee, which may not be the latest one. 

A correct brute force approach would involve using a subquery to get the latest `to_date` for each `employee_id` and then joining this result with the `Employee` table to get the corresponding `salary`.

```cpp
SELECT e1.employee_id, e1.salary AS latest_salary
FROM Employee e1
JOIN (
  SELECT employee_id, MAX(to_date) AS latest_to_date
  FROM Employee
  GROUP BY employee_id
) e2
ON e1.employee_id = e2.employee_id AND e1.to_date = e2.latest_to_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of records in the `Employee` table. This is because for each record, we are potentially scanning the entire table to find the latest `to_date`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of records in the `Employee` table. This is because we are storing the result in a new table.
> - **Why these complexities occur:** These complexities occur because the brute force approach involves iterating over each record in the `Employee` table and potentially scanning the entire table for each record.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a subquery to get the latest `to_date` for each `employee_id` and then join this result with the `Employee` table to get the corresponding `salary`.
- Detailed breakdown of the approach:
  1. Use a subquery to get the latest `to_date` for each `employee_id`.
  2. Join this result with the `Employee` table to get the corresponding `salary`.
- Proof of optimality: This approach is optimal because it only requires scanning the `Employee` table twice, once to get the latest `to_date` for each `employee_id` and once to get the corresponding `salary`.
- Why further optimization is impossible: Further optimization is impossible because we must scan the `Employee` table at least once to get the latest `to_date` for each `employee_id` and at least once to get the corresponding `salary`.

```cpp
SELECT e1.employee_id, e1.salary AS latest_salary
FROM Employee e1
JOIN (
  SELECT employee_id, MAX(to_date) AS latest_to_date
  FROM Employee
  GROUP BY employee_id
) e2
ON e1.employee_id = e2.employee_id AND e1.to_date = e2.latest_to_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of records in the `Employee` table. This is because we are scanning the `Employee` table twice, once to get the latest `to_date` for each `employee_id` and once to get the corresponding `salary`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of records in the `Employee` table. This is because we are storing the result in a new table.
> - **Optimality proof:** This approach is optimal because it only requires scanning the `Employee` table twice, which is the minimum number of scans required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated is the use of subqueries to solve complex queries.
- Problem-solving patterns identified: The problem-solving pattern identified is to break down complex queries into simpler subqueries.
- Optimization techniques learned: The optimization technique learned is to minimize the number of scans of the `Employee` table.
- Similar problems to practice: Similar problems to practice include other complex queries that require the use of subqueries.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a brute force approach that scans the `Employee` table multiple times for each record.
- Edge cases to watch for: An edge case to watch for is when an employee has multiple salary records with the same `to_date`, in which case the latest salary should be the one with the latest `from_date`.
- Performance pitfalls: A performance pitfall is to use a query that scans the `Employee` table multiple times, which can be slow for large tables.
- Testing considerations: A testing consideration is to test the query with a large `Employee` table to ensure that it performs well.