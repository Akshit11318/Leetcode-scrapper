## Customers Who Bought Products A and B but Not C

**Problem Link:** https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/description

**Problem Statement:**
- Given a table `Customers` with columns `customer_id` and `product_name`, return the customer IDs of customers who bought products A and B but not C.
- Input format: A table with customer IDs and product names.
- Expected output format: A list of customer IDs.
- Key requirements and edge cases to consider:
  - Handling customers who bought only one of the products A or B.
  - Handling customers who bought product C.
- Example test cases with explanations:
  - If a customer bought A, B, but not C, they should be included in the result.
  - If a customer bought A, B, and C, they should not be included in the result.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each customer and check their purchases.
- Step-by-step breakdown of the solution:
  1. Create a set or map to store the products each customer has bought.
  2. Iterate through each row in the table, adding the product to the customer's set in the map.
  3. Iterate through the map and check each customer's set for products A and B, and the absence of product C.
- Why this approach comes to mind first: It's a straightforward, intuitive method that checks each customer's purchases directly.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> findCustomers(vector<vector<string>>& transactions) {
    unordered_map<int, unordered_set<string>> customerProducts;
    
    // Populate the map with customer products
    for (const auto& transaction : transactions) {
        int customer_id = stoi(transaction[0]);
        string product_name = transaction[1];
        
        if (customerProducts.find(customer_id) == customerProducts.end()) {
            customerProducts[customer_id] = {};
        }
        customerProducts[customer_id].insert(product_name);
    }
    
    vector<int> result;
    
    // Check each customer's products
    for (const auto& pair : customerProducts) {
        const unordered_set<string>& products = pair.second;
        if (products.find("A") != products.end() && products.find("B") != products.end() && products.find("C") == products.end()) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of transactions and $m$ is the number of customers, since we're doing a constant amount of work for each transaction and each customer.
> - **Space Complexity:** $O(n + m)$, for storing the customer products and the result.
> - **Why these complexities occur:** We're iterating through each transaction once to populate the map and then through each customer once to find the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using SQL to filter the results directly, which is more efficient than manually iterating through each transaction.
- Detailed breakdown of the approach: 
  1. Use SQL to select distinct customer IDs.
  2. Filter the results to include only customers who have bought both products A and B.
  3. Exclude customers who have bought product C.
- Proof of optimality: This approach is optimal because it uses the database's built-in filtering capabilities, which are highly optimized for performance.

```sql
SELECT customer_id
FROM Customers
WHERE product_name IN ('A', 'B')
GROUP BY customer_id
HAVING COUNT(DISTINCT product_name) = 2
AND customer_id NOT IN (
    SELECT customer_id
    FROM Customers
    WHERE product_name = 'C'
)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, since we're doing a single pass through the data.
> - **Space Complexity:** $O(n)$, for storing the intermediate results.
> - **Optimality proof:** This is the most efficient approach because it leverages the database's optimized filtering and grouping capabilities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Filtering, grouping, and exclusion.
- Problem-solving patterns identified: Using SQL to optimize data queries.
- Optimization techniques learned: Leveraging database capabilities to reduce computational complexity.
- Similar problems to practice: Other SQL-based problems that involve filtering and grouping.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling NULL values or missing data.
- Edge cases to watch for: Customers with no purchases or customers who have bought only one product.
- Performance pitfalls: Using suboptimal algorithms or data structures that lead to high computational complexity.
- Testing considerations: Thoroughly testing the solution with various input scenarios to ensure correctness.