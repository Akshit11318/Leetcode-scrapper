## Sellers with No Sales

**Problem Link:** https://leetcode.com/problems/sellers-with-no-sales/description

**Problem Statement:**
- Input format and constraints: The problem provides two tables, `Orders` and `Sellers`, with their respective columns. The goal is to find the names of sellers who have not made any sales.
- Expected output format: A list of seller names with no sales.
- Key requirements and edge cases to consider: Handling cases where a seller may not have any orders, or where an order may not be associated with a seller.
- Example test cases with explanations:
  - Example 1: If a seller has no orders, they should be included in the result.
  - Example 2: If an order does not have a seller associated with it, it should not affect the result.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by iterating through all sellers and checking if they have any orders.
- Step-by-step breakdown of the solution:
  1. Select all seller names from the `Sellers` table.
  2. For each seller, query the `Orders` table to see if there are any orders associated with the seller.
  3. If no orders are found for a seller, include the seller's name in the result.
- Why this approach comes to mind first: It's a straightforward method that checks each seller individually.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

struct Seller {
    int seller_id;
    std::string name;
};

struct Order {
    int order_id;
    int seller_id;
};

std::vector<std::string> sellersWithNoSales(const std::vector<Seller>& sellers, const std::vector<Order>& orders) {
    std::vector<std::string> result;
    std::unordered_set<int> sellersWithSales;

    // Populate set of sellers with sales
    for (const auto& order : orders) {
        sellersWithSales.insert(order.seller_id);
    }

    // Find sellers without sales
    for (const auto& seller : sellers) {
        if (sellersWithSales.find(seller.seller_id) == sellersWithSales.end()) {
            result.push_back(seller.name);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of sellers and $m$ is the number of orders, because we iterate through all sellers and orders once.
> - **Space Complexity:** $O(n + m)$ because in the worst case, all sellers and orders could be stored in the set and result vector.
> - **Why these complexities occur:** The iteration through all data points and the storage of unique sellers with sales cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize SQL to directly query for sellers without orders, leveraging database indexing for efficiency.
- Detailed breakdown of the approach:
  1. Use a `LEFT JOIN` to combine the `Sellers` and `Orders` tables based on the seller ID.
  2. Select the seller names where the order ID is `NULL`, indicating no orders for the seller.
- Proof of optimality: This approach directly queries the database for the required information without needing to iterate through all data points in the application code, making it more efficient for large datasets.
- Why further optimization is impossible: This solution leverages the database's ability to efficiently handle joins and filtering, making it the most direct and efficient approach.

```sql
SELECT s.name
FROM Sellers s
LEFT JOIN Orders o ON s.seller_id = o.seller_id
WHERE o.order_id IS NULL;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of rows in the `Sellers` table and $m$ is the number of rows in the `Orders` table, because the database must perform the join and filter operation.
> - **Space Complexity:** $O(n + m)$ for storing the intermediate results of the join operation.
> - **Optimality proof:** This solution is optimal because it uses the database's built-in capabilities to perform the join and filter in the most efficient manner possible, without requiring additional application-level processing.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, set operations, and database querying.
- Problem-solving patterns identified: Checking for the absence of data (in this case, orders for a seller).
- Optimization techniques learned: Leveraging database capabilities for efficient data processing.
- Similar problems to practice: Other database query optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly assuming all sellers have orders, or not handling `NULL` values properly.
- Edge cases to watch for: Sellers with no orders, or orders without associated sellers.
- Performance pitfalls: Performing unnecessary iterations or not utilizing database indexing.
- Testing considerations: Ensure to test with various dataset sizes and scenarios to validate performance and correctness.