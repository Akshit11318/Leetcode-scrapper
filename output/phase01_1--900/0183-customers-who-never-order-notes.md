## Customers Who Never Order

**Problem Link:** https://leetcode.com/problems/customers-who-never-order/description

**Problem Statement:**
- Input: Two tables, `Customers` and `Orders`, where `Customers` contains information about each customer and `Orders` contains information about each order.
- Constraints: 
    - `Customers` table has columns `id` (primary key) and `name`.
    - `Orders` table has columns `id` (primary key), `customerId` (foreign key referencing `Customers.id`), and `orderDate`.
- Expected Output: A list of customers who have never placed an order.
- Key Requirements and Edge Cases:
    - Handle cases where there are no orders for a customer.
    - Consider customers with no orders as those who have never placed an order.
- Example Test Cases:
    - If `Customers` table contains customers with `id` 1, 2, and 3, and `Orders` table contains an order for customer with `id` 1, then the expected output should include customers with `id` 2 and 3.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each customer and check if they have any orders.
- For each customer, query the `Orders` table to see if there are any orders associated with their `id`.
- If no orders are found for a customer, add them to the result list.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

struct Customer {
    int id;
    std::string name;
};

struct Order {
    int id;
    int customerId;
    std::string orderDate;
};

std::vector<Customer> findCustomersWhoNeverOrder(std::vector<Customer>& customers, std::vector<Order>& orders) {
    std::vector<Customer> result;
    for (const auto& customer : customers) {
        bool hasOrder = false;
        for (const auto& order : orders) {
            if (order.customerId == customer.id) {
                hasOrder = true;
                break;
            }
        }
        if (!hasOrder) {
            result.push_back(customer);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of customers and $m$ is the number of orders. This is because for each customer, we potentially iterate over all orders.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity. The space complexity is due to storing the customers who never ordered.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `HashSet` to store the customer `id`s that have orders.
- Iterate over the `Orders` table once to populate the `HashSet`.
- Then, iterate over the `Customers` table. If a customer's `id` is not in the `HashSet`, they have never ordered.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<Customer> findCustomersWhoNeverOrderOptimal(std::vector<Customer>& customers, std::vector<Order>& orders) {
    std::unordered_set<int> customersWithOrders;
    for (const auto& order : orders) {
        customersWithOrders.insert(order.customerId);
    }
    
    std::vector<Customer> result;
    for (const auto& customer : customers) {
        if (customersWithOrders.find(customer.id) == customersWithOrders.end()) {
            result.push_back(customer);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of customers and $m$ is the number of orders. This is because we make one pass over the orders and one pass over the customers.
> - **Space Complexity:** $O(m)$ for the `HashSet` of customer `id`s with orders.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations by avoiding unnecessary comparisons and using a data structure that allows for constant time lookup.

---

### Final Notes

**Learning Points:**
- Using a `HashSet` for fast lookup can significantly improve performance.
- Avoiding nested loops when possible can reduce time complexity.
- Understanding the problem constraints and identifying the key operations (in this case, checking if a customer has an order) is crucial for finding an optimal solution.

**Mistakes to Avoid:**
- Not considering the use of more efficient data structures like `HashSet` for lookup operations.
- Failing to recognize the potential for reducing time complexity by minimizing the number of iterations.
- Not testing edge cases, such as an empty `Orders` table or a `Customers` table with no matching orders.