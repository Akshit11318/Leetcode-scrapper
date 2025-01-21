## Unique Orders and Customers Per Month
**Problem Link:** [https://leetcode.com/problems/unique-orders-and-customers-per-month/description](https://leetcode.com/problems/unique-orders-and-customers-per-month/description)

**Problem Statement:**
- Input format and constraints: The problem involves two tables, `Orders` and `Customers`, where each order is associated with a customer. The `Orders` table has columns `order_id`, `customer_id`, and `order_date`, while the `Customers` table has columns `customer_id` and `name`. The goal is to find the number of unique orders and customers for each month.
- Expected output format: The output should include the month and year of the order date, the number of unique orders, and the number of unique customers.
- Key requirements and edge cases to consider: The solution should handle cases where there are no orders or customers for a particular month, and it should also account for the fact that a customer can place multiple orders in the same month.
- Example test cases with explanations: For example, if there are two orders in January 2022 from the same customer, the output should show one unique customer and two unique orders for that month.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each order and customer, and then manually counting the number of unique orders and customers for each month.
- Step-by-step breakdown of the solution:
  1. Initialize variables to store the count of unique orders and customers for each month.
  2. Iterate over each order in the `Orders` table.
  3. For each order, extract the month and year from the `order_date`.
  4. Check if the customer has already been counted for this month. If not, increment the count of unique customers.
  5. Increment the count of unique orders for this month.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient for large datasets.

```cpp
using namespace std;

// Define the structure for an order
struct Order {
    int order_id;
    int customer_id;
    string order_date;
};

// Define the structure for a customer
struct Customer {
    int customer_id;
    string name;
};

// Function to count unique orders and customers per month
void count_unique_orders_and_customers(vector<Order>& orders, vector<Customer>& customers) {
    // Initialize a map to store the count of unique orders and customers for each month
    map<string, pair<int, set<int>>> month_counts;

    // Iterate over each order
    for (const auto& order : orders) {
        // Extract the month and year from the order date
        string month = order.order_date.substr(0, 7);

        // Check if the month is already in the map
        if (month_counts.find(month) == month_counts.end()) {
            // If not, initialize the count of unique orders and customers for this month
            month_counts[month] = {0, {}};
        }

        // Increment the count of unique orders for this month
        month_counts[month].first++;

        // Add the customer to the set of unique customers for this month
        month_counts[month].second.insert(order.customer_id);
    }

    // Print the count of unique orders and customers for each month
    for (const auto& month : month_counts) {
        cout << "Month: " << month.first << ", Unique Orders: " << month.second.first << ", Unique Customers: " << month.second.second.size() << endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of orders, because we iterate over each order once.
> - **Space Complexity:** $O(n)$, because we store the count of unique orders and customers for each month in a map.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over each order once, and the space complexity is also linear because we store a constant amount of information for each month.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a SQL query to count the number of unique orders and customers for each month.
- Detailed breakdown of the approach:
  1. Use the `DATE_FORMAT` function to extract the month and year from the `order_date`.
  2. Use the `COUNT(DISTINCT order_id)` function to count the number of unique orders for each month.
  3. Use the `COUNT(DISTINCT customer_id)` function to count the number of unique customers for each month.
- Proof of optimality: This approach is optimal because it uses the database's built-in functions to count the number of unique orders and customers, which is more efficient than iterating over each order and customer manually.
- Why further optimization is impossible: This approach is already optimal because it uses the most efficient way to count the number of unique orders and customers for each month.

```sql
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(DISTINCT order_id) AS unique_orders,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM 
    Orders
GROUP BY 
    DATE_FORMAT(order_date, '%Y-%m')
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of orders, because the database has to iterate over each order to count the number of unique orders and customers.
> - **Space Complexity:** $O(n)$, because the database has to store the count of unique orders and customers for each month.
> - **Optimality proof:** This approach is optimal because it uses the database's built-in functions to count the number of unique orders and customers, which is more efficient than iterating over each order and customer manually.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of using efficient data structures and algorithms to count the number of unique orders and customers for each month.
- Problem-solving patterns identified: The problem identifies the pattern of using a map to store the count of unique orders and customers for each month.
- Optimization techniques learned: The problem teaches the technique of using a SQL query to count the number of unique orders and customers for each month.
- Similar problems to practice: Similar problems to practice include counting the number of unique orders and customers for each quarter or year.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to iterate over each order and customer manually, which can be inefficient for large datasets.
- Edge cases to watch for: An edge case to watch for is when there are no orders or customers for a particular month.
- Performance pitfalls: A performance pitfall is to use a brute force approach to count the number of unique orders and customers for each month.
- Testing considerations: A testing consideration is to test the solution with a large dataset to ensure that it is efficient and accurate.