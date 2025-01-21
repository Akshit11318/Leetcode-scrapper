## Group Sold Products By The Date

**Problem Link:** https://leetcode.com/problems/group-sold-products-by-the-date/description

**Problem Statement:**
- Input format and constraints: The input is a table `Sales` with columns `sold_date` and `product`.
- Expected output format: The output should be a table with the `sold_date` and the count of distinct `product` sold on that date.
- Key requirements and edge cases to consider: The solution should handle dates in the format `yyyy-MM-dd`, and the count of distinct products should be accurate.
- Example test cases with explanations:
  - Example 1:
    - Input: 
      ```markdown
      +------------+----------+
      | sold_date  | product  |
      +------------+----------+
      | 2020-05-31 | A        |
      | 2020-05-31 | B        |
      | 2020-06-01 | A        |
      | 2020-06-01 | B        |
      | 2020-06-02 | C        |
      | 2020-06-02 | D        |
      +------------+----------+
      ```
    - Output: 
      ```markdown
      +------------+----------+
      | sold_date  | num_sold |
      +------------+----------+
      | 2020-05-31 | 2        |
      | 2020-06-01 | 2        |
      | 2020-06-02 | 2        |
      +------------+----------+
      ```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would involve iterating over the table and counting the distinct products for each date.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the count of distinct products for each date.
  2. Iterate over the table, and for each row, check if the date is already in the dictionary.
  3. If the date is in the dictionary, add the product to the set of products for that date if it's not already there.
  4. If the date is not in the dictionary, add it with the product as the first product.
  5. Finally, create the output table with the count of distinct products for each date.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct Sales {
    std::string sold_date;
    std::string product;
};

std::vector<std::pair<std::string, int>> groupSoldProductsByDate(std::vector<Sales>& sales) {
    std::unordered_map<std::string, std::unordered_set<std::string>> dateToProducts;
    for (const auto& sale : sales) {
        dateToProducts[sale.sold_date].insert(sale.product);
    }
    std::vector<std::pair<std::string, int>> result;
    for (const auto& pair : dateToProducts) {
        result.push_back({pair.first, pair.second.size()});
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the table, because we iterate over the table once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all rows in the dictionary.
> - **Why these complexities occur:** These complexities occur because we are iterating over the table and storing the count of distinct products for each date.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a SQL query to group the products by date and count the distinct products.
- Detailed breakdown of the approach:
  1. Use the `GROUP BY` clause to group the rows by `sold_date`.
  2. Use the `COUNT(DISTINCT product)` function to count the distinct products for each group.
- Proof of optimality: This solution is optimal because it uses a single SQL query to solve the problem, which is more efficient than iterating over the table in code.

```sql
SELECT 
    sold_date, 
    COUNT(DISTINCT product) AS num_sold
FROM 
    Sales
GROUP BY 
    sold_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the table, because the database needs to iterate over the table to group the rows and count the distinct products.
> - **Space Complexity:** $O(n)$, because the database needs to store the groups and counts in memory.
> - **Optimality proof:** This solution is optimal because it uses a single SQL query to solve the problem, which is more efficient than iterating over the table in code.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping and counting distinct elements.
- Problem-solving patterns identified: Using SQL queries to solve problems involving data aggregation.
- Optimization techniques learned: Using database queries to solve problems instead of iterating over the data in code.
- Similar problems to practice: Other problems involving data aggregation and grouping.

**Mistakes to Avoid:**
- Common implementation errors: Not using the `DISTINCT` keyword when counting distinct elements.
- Edge cases to watch for: Handling null or missing values in the data.
- Performance pitfalls: Iterating over the data in code instead of using database queries.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.