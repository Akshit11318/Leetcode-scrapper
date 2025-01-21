## Products with Three or More Orders in Two Consecutive Years
**Problem Link:** https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/description

**Problem Statement:**
- Input: A table `Orders` with columns `product_id`, `order_id`, `order_year`, `product_name`, `customer_id`.
- Constraints: The table contains information about orders with unique `order_id` for each `customer_id` in a specific `order_year`.
- Expected output: A list of `product_name` and `product_id` that have at least three orders in two consecutive years.
- Key requirements: Identify products with three or more orders in two consecutive years based on the `Orders` table.
- Edge cases: Products with less than three orders in any year, or products with three or more orders but not in consecutive years.

Example test cases:
- If a product has three orders in year 2020 and three orders in year 2021, it should be included in the output.
- If a product has two orders in year 2020 and three orders in year 2021, it should not be included.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Group orders by `product_id` and `order_year`, then count the number of orders for each group.
- Step-by-step breakdown:
  1. Group the `Orders` table by `product_id` and `order_year`.
  2. For each group, count the number of orders.
  3. Check each product to see if it has at least three orders in two consecutive years.
- Why this approach comes to mind first: It directly addresses the problem by counting orders for each product in each year and checking for the condition of having at least three orders in consecutive years.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

struct ProductOrder {
    int product_id;
    int order_year;
    int count;
};

void bruteForceSolution(std::vector<int>& product_ids, std::vector<int>& order_years, std::vector<int>& product_names) {
    std::map<int, std::map<int, int>> orderCounts;
    
    // Count orders for each product in each year
    for (int i = 0; i < product_ids.size(); i++) {
        orderCounts[product_ids[i]][order_years[i]]++;
    }
    
    std::vector<std::pair<int, int>> result;
    
    // Check for products with at least three orders in two consecutive years
    for (auto& product : orderCounts) {
        std::vector<std::pair<int, int>> years;
        for (auto& year : product.second) {
            years.push_back(year);
        }
        std::sort(years.begin(), years.end());
        
        for (int i = 0; i < years.size() - 1; i++) {
            if (years[i].first + 1 == years[i + 1].first && years[i].second >= 3 && years[i + 1].second >= 3) {
                result.push_back(std::make_pair(product.first, years[i].first));
                break;
            }
        }
    }
    
    // Print the result
    for (auto& product : result) {
        std::cout << "Product ID: " << product.first << ", First Year: " << product.second << std::endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rows in the `Orders` table. This is because for each product, we potentially iterate over all orders to count them, and then over all years to check for consecutive years.
> - **Space Complexity:** $O(n)$ for storing the count of orders for each product in each year.
> - **Why these complexities occur:** The brute force approach involves iterating over the data multiple times: once to count orders and again to check for the condition of having at least three orders in consecutive years.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a `std::map` to store the count of orders for each product in each year, and then iterate over the map to find products with at least three orders in two consecutive years.
- Detailed breakdown:
  1. Create a `std::map` where the key is the product ID and the value is another `std::map` with the year as the key and the count of orders as the value.
  2. Iterate over the `Orders` table to populate the map.
  3. Iterate over the map to find products that meet the condition.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data to populate the map and then another pass over the map to find the products, resulting in a linear time complexity.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

struct ProductOrder {
    int product_id;
    int order_year;
    int count;
};

void optimalSolution(std::vector<int>& product_ids, std::vector<int>& order_years) {
    std::map<int, std::map<int, int>> orderCounts;
    
    // Count orders for each product in each year
    for (int i = 0; i < product_ids.size(); i++) {
        orderCounts[product_ids[i]][order_years[i]]++;
    }
    
    std::vector<std::pair<int, int>> result;
    
    // Check for products with at least three orders in two consecutive years
    for (auto& product : orderCounts) {
        std::map<int, int> years = product.second;
        for (auto it = years.begin(); it != years.end(); ++it) {
            if (it->second >= 3 && std::next(it) != years.end() && std::next(it)->first == it->first + 1 && std::next(it)->second >= 3) {
                result.push_back(std::make_pair(product.first, it->first));
            }
        }
    }
    
    // Print the result
    for (auto& product : result) {
        std::cout << "Product ID: " << product.first << ", First Year: " << product.second << std::endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `Orders` table. This is because we make a single pass over the data to populate the map and then another pass over the map to find the products.
> - **Space Complexity:** $O(n)$ for storing the count of orders for each product in each year.
> - **Optimality proof:** This approach is optimal because it minimizes the number of passes over the data and uses a data structure that allows for efficient lookup and insertion.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using maps for efficient lookup and counting, iterating over data structures to find specific conditions.
- Problem-solving patterns identified: Breaking down the problem into smaller steps (counting orders, checking for consecutive years), using data structures to optimize the solution.
- Optimization techniques learned: Minimizing the number of passes over the data, using efficient data structures.
- Similar problems to practice: Problems involving counting and grouping data, finding specific conditions in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases (e.g., empty dataset).
- Edge cases to watch for: Empty dataset, products with no orders, products with orders in non-consecutive years.
- Performance pitfalls: Using inefficient data structures or algorithms, making unnecessary passes over the data.
- Testing considerations: Testing with different datasets, including edge cases, to ensure the solution works correctly in all scenarios.