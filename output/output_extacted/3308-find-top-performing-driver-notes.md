## Find Top Performing Driver
**Problem Link:** https://leetcode.com/problems/find-top-performing-driver/description

**Problem Statement:**
- Input format and constraints: The problem provides two tables, `Rides` and `AcceptedRides`. The `Rides` table contains columns for `ride_id`, `user_id`, `requested_at`. The `AcceptedRides` table contains columns for `ride_id`, `driver_id`, `ride_distance`, `ride_duration`. We need to find the top-performing driver based on the acceptance rate of rides.
- Expected output format: The output should be a table with one row containing the `driver_id` and their acceptance rate.
- Key requirements and edge cases to consider: We need to calculate the acceptance rate for each driver and return the top-performing driver.
- Example test cases with explanations: 
    - Test case 1: 
        - Input: 
            - `Rides` table: 
                | ride_id | user_id | requested_at |
                | --- | --- | --- |
                | 1 | 1 | 2022-01-01 12:00:00 |
                | 2 | 2 | 2022-01-01 13:00:00 |
            - `AcceptedRides` table: 
                | ride_id | driver_id | ride_distance | ride_duration |
                | --- | --- | --- | --- |
                | 1 | 1 | 10 | 30 |
        - Output: 
            | driver_id | acceptance_rate |
            | --- | --- |
            | 1 | 1.00 |

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can calculate the acceptance rate for each driver by dividing the number of accepted rides by the total number of rides requested.
- Step-by-step breakdown of the solution:
    1. Join the `Rides` and `AcceptedRides` tables on the `ride_id` column.
    2. Calculate the total number of rides requested for each driver.
    3. Calculate the number of accepted rides for each driver.
    4. Calculate the acceptance rate for each driver.
    5. Return the driver with the highest acceptance rate.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. However, it may not be efficient for large datasets.

```cpp
SELECT 
    a.driver_id,
    COUNT(DISTINCT b.ride_id) / 
    (SELECT COUNT(*) FROM Rides WHERE requested_at BETWEEN '2022-01-01' AND '2022-01-31') AS acceptance_rate
FROM 
    AcceptedRides a
JOIN 
    Rides b ON a.ride_id = b.ride_id
WHERE 
    b.requested_at BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY 
    a.driver_id
ORDER BY 
    acceptance_rate DESC
LIMIT 1;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the intermediate results.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to storing the intermediate results.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a single SQL query to calculate the acceptance rate for each driver and return the top-performing driver.
- Detailed breakdown of the approach:
    1. Calculate the total number of rides requested for each driver.
    2. Calculate the number of accepted rides for each driver.
    3. Calculate the acceptance rate for each driver.
    4. Return the driver with the highest acceptance rate.
- Proof of optimality: This approach is optimal because it uses a single SQL query to calculate the acceptance rate for each driver and return the top-performing driver.

```cpp
SELECT 
    a.driver_id,
    COUNT(CASE WHEN b.ride_id IS NOT NULL THEN 1 ELSE NULL END) / COUNT(a.ride_id) AS acceptance_rate
FROM 
    Rides a
LEFT JOIN 
    AcceptedRides b ON a.ride_id = b.ride_id
WHERE 
    a.requested_at BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY 
    a.driver_id
ORDER BY 
    acceptance_rate DESC
LIMIT 1;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the intermediate results.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to calculate the acceptance rate for each driver and return the top-performing driver.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: SQL queries, aggregation, and sorting.
- Problem-solving patterns identified: Using a single SQL query to calculate the acceptance rate for each driver and return the top-performing driver.
- Optimization techniques learned: Using a single SQL query to reduce the complexity of the solution.
- Similar problems to practice: Other SQL-based problems that require aggregation and sorting.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly joining tables, incorrectly calculating the acceptance rate.
- Edge cases to watch for: Handling cases where the total number of rides requested is zero.
- Performance pitfalls: Using inefficient SQL queries that result in high time and space complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.