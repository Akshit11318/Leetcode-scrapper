## The Most Frequently Ordered Products for Each Customer

**Problem Link:** https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/description

**Problem Statement:**
- Input format: The problem takes in a table `Orders` with columns `order_id`, `customer_id`, `order_date`, and `product_id`.
- Constraints: The table has no constraints provided, but we can assume that all columns are non-null and that `order_id` is unique.
- Expected output format: The output should be a table with columns `customer_id` and `product_id`, where each row represents the most frequently ordered product for each customer.
- Key requirements and edge cases to consider:
  - If a customer has multiple products with the same highest frequency, return any one of them.
  - If a customer has no orders, they should not appear in the output.

**Example Test Cases:**

| order_id | customer_id | order_date | product_id |
| --- | --- | --- | --- |
| 1 | 1 | 2020-01-01 | A |
| 2 | 1 | 2020-01-02 | A |
| 3 | 1 | 2020-01-03 | B |
| 4 | 2 | 2020-01-01 | C |
| 5 | 2 | 2020-01-02 | C |

Expected Output:

| customer_id | product_id |
| --- | --- |
| 1 | A |
| 2 | C |

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to count the frequency of each product for each customer and then find the product with the highest frequency for each customer.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the frequency of each product for each customer.
  2. Iterate over the orders table and update the frequency dictionary.
  3. For each customer, find the product with the highest frequency.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Order {
    int order_id;
    int customer_id;
    std::string order_date;
    char product_id;
};

std::vector<std::pair<int, char>> mostFrequentlyOrderedProducts(std::vector<Order>& orders) {
    std::unordered_map<int, std::unordered_map<char, int>> frequency;
    for (const auto& order : orders) {
        frequency[order.customer_id][order.product_id]++;
    }

    std::vector<std::pair<int, char>> result;
    for (const auto& customer : frequency) {
        char maxProduct = ' ';
        int maxCount = 0;
        for (const auto& product : customer.second) {
            if (product.second > maxCount) {
                maxCount = product.second;
                maxProduct = product.first;
            }
        }
        result.push_back({customer.first, maxProduct});
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of orders and $m$ is the average number of products per customer.
> - **Space Complexity:** $O(n \cdot m)$, for storing the frequency dictionary.
> - **Why these complexities occur:** The brute force approach requires iterating over all orders and storing the frequency of each product for each customer.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a SQL query to solve this problem efficiently.
- Detailed breakdown of the approach:
  1. Use a `GROUP BY` clause to group the orders by customer and product.
  2. Use the `COUNT` function to count the frequency of each product for each customer.
  3. Use a subquery to find the product with the highest frequency for each customer.

```sql
SELECT customer_id, product_id
FROM (
  SELECT customer_id, product_id, COUNT(order_id) AS count,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY COUNT(order_id) DESC) AS row_num
  FROM Orders
  GROUP BY customer_id, product_id
) t
WHERE row_num = 1;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of orders, due to the sorting in the subquery.
> - **Space Complexity:** $O(n)$, for storing the intermediate results.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to solve the problem, which is more efficient than iterating over the orders in code.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency counting, grouping, and sorting.
- Problem-solving patterns identified: using a dictionary to store frequency counts and using a subquery to find the maximum value.
- Optimization techniques learned: using SQL queries to solve problems efficiently.
- Similar problems to practice: problems involving frequency counting and grouping.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as customers with no orders.
- Edge cases to watch for: customers with multiple products with the same highest frequency.
- Performance pitfalls: using inefficient algorithms, such as iterating over the orders in code.
- Testing considerations: testing the solution with different inputs, including edge cases.