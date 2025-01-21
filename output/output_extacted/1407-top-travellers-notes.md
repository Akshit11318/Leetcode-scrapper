## Top Travellers
**Problem Link:** https://leetcode.com/problems/top-travellers/description

**Problem Statement:**
- Input format and constraints: The problem provides three tables: `Users`, `Rides`, and `Locations`. The goal is to find the top 3 users with the longest total travel distance.
- Expected output format: The result should be a list of user IDs with their corresponding total travel distances.
- Key requirements and edge cases to consider: The solution must handle cases where users have the same total travel distance and must return only the top 3 users.
- Example test cases with explanations: 
    - A test case where one user has a significantly longer total travel distance than the others.
    - A test case where multiple users have the same total travel distance.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total travel distance for each user by summing up the distances of all their rides.
- Step-by-step breakdown of the solution:
    1. Join the `Users`, `Rides`, and `Locations` tables based on the user ID and ride ID.
    2. Calculate the distance of each ride by finding the difference between the end and start locations.
    3. Sum up the distances of all rides for each user.
    4. Sort the users by their total travel distances in descending order.
    5. Return the top 3 users with the longest total travel distances.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
SELECT u.id, SUM(l2.latitude - l1.latitude + l2.longitude - l1.longitude) AS travel_distance
FROM Users u
JOIN Rides r ON u.id = r.user_id
JOIN Locations l1 ON r.start_location_id = l1.id
JOIN Locations l2 ON r.end_location_id = l2.id
GROUP BY u.id
ORDER BY travel_distance DESC
LIMIT 3;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rides, due to the sorting operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rides, for storing the intermediate results.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to the storage of intermediate results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a SQL query with window functions to calculate the total travel distance for each user and then rank them.
- Detailed breakdown of the approach:
    1. Calculate the distance of each ride by finding the difference between the end and start locations.
    2. Use a window function to calculate the total travel distance for each user.
    3. Rank the users by their total travel distances in descending order.
    4. Return the top 3 users with the longest total travel distances.
- Proof of optimality: This approach is optimal because it uses a single SQL query to calculate the total travel distances and rank the users, minimizing the number of operations required.

```cpp
WITH distances AS (
    SELECT u.id, SUM(l2.latitude - l1.latitude + l2.longitude - l1.longitude) AS travel_distance
    FROM Users u
    JOIN Rides r ON u.id = r.user_id
    JOIN Locations l1 ON r.start_location_id = l1.id
    JOIN Locations l2 ON r.end_location_id = l2.id
    GROUP BY u.id
),
ranked_users AS (
    SELECT id, travel_distance,
    DENSE_RANK() OVER (ORDER BY travel_distance DESC) AS rank
    FROM distances
)
SELECT id, travel_distance
FROM ranked_users
WHERE rank <= 3;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rides, due to the sorting operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rides, for storing the intermediate results.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to calculate the total travel distances and rank the users, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Window functions, ranking, and aggregation.
- Problem-solving patterns identified: Using SQL queries to solve data analysis problems.
- Optimization techniques learned: Minimizing the number of operations required to solve the problem.
- Similar problems to practice: Data analysis problems involving aggregation, ranking, and window functions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the total travel distance or ranking the users.
- Edge cases to watch for: Users with the same total travel distance or missing data.
- Performance pitfalls: Using inefficient SQL queries or algorithms.
- Testing considerations: Thoroughly testing the solution with different input data and edge cases.