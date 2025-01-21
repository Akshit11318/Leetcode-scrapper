## Average Selling Price

**Problem Link:** https://leetcode.com/problems/average-selling-price/description

**Problem Statement:**
- Input format: The `prices` table contains information about the items sold, with columns `sell_date`, `product_id`, `unit_price`, and `quantity`.
- Constraints: The `sell_date` is between '2019-01-01' and '2019-12-31', and the `product_id` is unique within a `sell_date`.
- Expected output format: The average selling price of each product, rounded to two decimal places.
- Key requirements and edge cases to consider: Handling products with no sales, calculating the total revenue for each product, and avoiding division by zero errors.
- Example test cases with explanations:
  - A product with multiple sales on different dates should have its average selling price calculated correctly.
  - A product with no sales should have a NULL average selling price.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total revenue for each product and divide it by the total quantity sold.
- Step-by-step breakdown of the solution:
  1. Initialize a map to store the total revenue and quantity for each product.
  2. Iterate through the `prices` table and update the total revenue and quantity for each product.
  3. Calculate the average selling price for each product by dividing the total revenue by the total quantity.
- Why this approach comes to mind first: It directly addresses the problem statement and is easy to implement.

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <string>

struct ProductInfo {
    double totalRevenue = 0.0;
    int totalQuantity = 0;
};

double calculateAveragePrice(const std::vector<std::string>& sellDate, 
                              const std::vector<int>& productID, 
                              const std::vector<double>& unitPrice, 
                              const std::vector<int>& quantity) {
    std::map<int, ProductInfo> productMap;

    for (int i = 0; i < sellDate.size(); ++i) {
        int product = productID[i];
        double revenue = unitPrice[i] * quantity[i];

        if (productMap.find(product) != productMap.end()) {
            productMap[product].totalRevenue += revenue;
            productMap[product].totalQuantity += quantity[i];
        } else {
            ProductInfo info;
            info.totalRevenue = revenue;
            info.totalQuantity = quantity[i];
            productMap[product] = info;
        }
    }

    for (auto& pair : productMap) {
        if (pair.second.totalQuantity == 0) {
            std::cout << "NULL" << std::endl;
        } else {
            double averagePrice = pair.second.totalRevenue / pair.second.totalQuantity;
            printf("%.2f\n", averagePrice);
        }
    }

    return 0.0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `prices` table. This is because we iterate through the table once to update the product map.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique products. This is because we store the total revenue and quantity for each product in the map.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each row in the table. The space complexity is proportional to the number of unique products because we store information for each product in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use SQL to directly calculate the average selling price for each product.
- Detailed breakdown of the approach:
  1. Use the `SUM` aggregation function to calculate the total revenue for each product.
  2. Use the `SUM` aggregation function to calculate the total quantity for each product.
  3. Divide the total revenue by the total quantity to get the average selling price for each product.
- Proof of optimality: This approach is optimal because it directly addresses the problem statement and minimizes the amount of data that needs to be processed.
- Why further optimization is impossible: This approach is already optimal because it uses a single SQL query to calculate the average selling price for each product.

```sql
SELECT 
    product_id,
    ROUND(SUM(unit_price * quantity) / SUM(quantity), 2) AS average_price
FROM 
    prices
GROUP BY 
    product_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `prices` table. This is because the SQL query iterates through the table once to calculate the average selling price for each product.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique products. This is because the SQL query stores the average selling price for each product in memory.
> - **Optimality proof:** The time complexity is linear because the SQL query performs a constant amount of work for each row in the table. The space complexity is proportional to the number of unique products because the query stores information for each product in memory.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Aggregation functions, grouping, and division.
- Problem-solving patterns identified: Directly addressing the problem statement and minimizing data processing.
- Optimization techniques learned: Using SQL to calculate the average selling price for each product.
- Similar problems to practice: Calculating the average value for each group in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle division by zero errors, incorrectly calculating the total revenue or quantity for each product.
- Edge cases to watch for: Products with no sales, products with zero quantity.
- Performance pitfalls: Using inefficient algorithms or data structures to calculate the average selling price for each product.
- Testing considerations: Verifying that the solution correctly handles edge cases and produces the expected output for different inputs.