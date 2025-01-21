## Number of Times a Driver Was a Passenger
**Problem Link:** https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/description

**Problem Statement:**
- Input format and constraints: The problem involves two tables, `Rides` and `AcceptedRides`. The `Rides` table has columns `id`, `driver_id`, and `city_id`, while the `AcceptedRides` table has columns `id`, `ride_id`, `driver_id`, and `city_id`. The goal is to find the number of times each driver was a passenger.
- Expected output format: The output should be a table with the driver's ID and the number of times they were a passenger.
- Key requirements and edge cases to consider: We need to join the two tables based on the ride ID and then count the occurrences of each driver as a passenger.
- Example test cases with explanations: For instance, if a driver with ID 1 has driven 5 rides and been a passenger in 2 of those rides, the output should show the driver's ID as 1 and the count as 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each ride in the `Rides` table and check if the driver of that ride exists in the `AcceptedRides` table as a passenger.
- Step-by-step breakdown of the solution:
  1. Iterate through each ride in the `Rides` table.
  2. For each ride, check if the driver exists in the `AcceptedRides` table as a passenger.
  3. If the driver exists as a passenger, increment the count for that driver.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient due to the nested iteration.

```cpp
SELECT 
    a.driver_id, 
    COUNT(*) as count
FROM 
    Rides a
JOIN 
    AcceptedRides b ON a.id = b.ride_id AND a.driver_id = b.driver_id
GROUP BY 
    a.driver_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the number of rides, due to the nested iteration.
> - **Space Complexity:** $O(n)$, where n is the number of unique drivers, for storing the count of each driver.
> - **Why these complexities occur:** The brute force approach involves iterating through each ride and checking if the driver exists in the `AcceptedRides` table, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating through each ride, we can use a SQL query to join the two tables based on the ride ID and then count the occurrences of each driver as a passenger.
- Detailed breakdown of the approach:
  1. Join the `Rides` table with the `AcceptedRides` table based on the ride ID.
  2. Filter the results to only include rows where the driver ID in the `Rides` table matches the driver ID in the `AcceptedRides` table.
  3. Group the results by the driver ID and count the number of occurrences.
- Proof of optimality: This approach is optimal because it uses a single SQL query to perform the join and count operations, resulting in a lower time complexity compared to the brute force approach.

```cpp
SELECT 
    a.driver_id, 
    COUNT(*) as count
FROM 
    Rides a
JOIN 
    AcceptedRides b ON a.id = b.ride_id AND a.driver_id != b.driver_id
GROUP BY 
    a.driver_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where n is the number of rows in the `Rides` table, due to the join operation.
> - **Space Complexity:** $O(n)$, where n is the number of unique drivers, for storing the count of each driver.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to perform the join and count operations, resulting in a lower time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Joining tables based on a common column, filtering results based on conditions, and grouping results to perform aggregate operations.
- Problem-solving patterns identified: Using SQL queries to perform complex operations in a efficient manner.
- Optimization techniques learned: Using joins and aggregate functions to reduce the time complexity of a query.
- Similar problems to practice: Other problems involving table joins and aggregate operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly joining tables or using incorrect conditions in the WHERE clause.
- Edge cases to watch for: Handling cases where a driver has no rides or no accepted rides.
- Performance pitfalls: Using inefficient queries that result in high time complexities.
- Testing considerations: Testing the query with different inputs and edge cases to ensure correctness.