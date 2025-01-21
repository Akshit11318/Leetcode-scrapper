## Patients With a Condition
**Problem Link:** https://leetcode.com/problems/patients-with-a-condition/description

**Problem Statement:**
- Input format: A table `Patients` with columns `patient_id` and `conditions`.
- Constraints: The table contains at least one record, and there are no duplicate patient IDs.
- Expected output format: A table with patient IDs and the conditions they have.
- Key requirements and edge cases to consider: Handling cases where a patient has multiple conditions or no conditions at all.
- Example test cases with explanations: 
  - A patient with a single condition.
  - A patient with multiple conditions.
  - A patient with no conditions.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simply query the database for all patients and their conditions.
- Step-by-step breakdown of the solution:
  1. Retrieve all records from the `Patients` table.
  2. For each record, extract the patient ID and condition.
  3. Return all patient IDs and their corresponding conditions.
- Why this approach comes to mind first: It directly addresses the problem statement without considering optimization.

```cpp
SELECT patient_id, conditions 
FROM Patients 
WHERE conditions LIKE '%condition_name%';
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we potentially scan every row once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might return every row in the table.
> - **Why these complexities occur:** The brute force approach involves a linear scan of the table, which leads to linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize SQL's built-in filtering capabilities to directly select patients with the specified condition.
- Detailed breakdown of the approach:
  1. Use the `LIKE` operator with a wildcard to match the condition anywhere in the `conditions` column.
  2. Select only the `patient_id` and `conditions` columns to minimize data retrieval.
- Proof of optimality: This approach directly filters out unnecessary data at the database level, minimizing the amount of data that needs to be processed.
- Why further optimization is impossible: This query is as specific as possible, given the constraints of the problem.

```sql
SELECT patient_id, conditions 
FROM Patients 
WHERE conditions LIKE '%condition_name%';
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because in the worst case, the database still has to scan every row to apply the filter.
> - **Space Complexity:** $O(n)$, as in the worst case, every row could match the condition, and we'd have to return all of them.
> - **Optimality proof:** The query is optimized because it uses the database's native filtering capabilities, which are generally more efficient than applying filters in application code.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct filtering and efficient data retrieval.
- Problem-solving patterns identified: Utilizing native database features for optimization.
- Optimization techniques learned: Minimizing data retrieval and using database-level filtering.
- Similar problems to practice: Other SQL optimization problems focusing on efficient data retrieval and filtering.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of the `LIKE` operator or failure to minimize data retrieval.
- Edge cases to watch for: Handling patients with no conditions or multiple conditions.
- Performance pitfalls: Retrieving more data than necessary or applying filters at the application level instead of the database level.
- Testing considerations: Ensure to test with various conditions, including empty conditions and conditions that do not exist in the data.