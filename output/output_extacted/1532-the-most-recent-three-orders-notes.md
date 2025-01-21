## The Most Recent Three Orders
**Problem Link:** https://leetcode.com/problems/the-most-recent-three-orders/description

**Problem Statement:**
- Input format and constraints: The problem provides a list of orders, where each order contains a customer ID, an order ID, and an order date. The task is to find the most recent three orders for each customer.
- Expected output format: A list of the most recent three orders for each customer.
- Key requirements and edge cases to consider: Handling cases where a customer has less than three orders, and ensuring that the orders are sorted by date in descending order.
- Example test cases with explanations: For example, given a list of orders `[[1, 1, "2020-01-01"], [1, 2, "2020-01-02"], [1, 3, "2020-01-03"], [2, 4, "2020-01-04"], [2, 5, "2020-01-05"], [2, 6, "2020-01-06"]]`, the output should be `[[1, 3, "2020-01-03"], [1, 2, "2020-01-02"], [1, 1, "2020-01-01"], [2, 6, "2020-01-06"], [2, 5, "2020-01-05"], [2, 4, "2020-01-04"]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to sort the orders by date in descending order, and then iterate through the sorted list to find the most recent three orders for each customer.
- Step-by-step breakdown of the solution:
  1. Sort the orders by date in descending order.
  2. Iterate through the sorted list and keep track of the most recent three orders for each customer.
  3. If a customer has less than three orders, include all of their orders in the output.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Order {
    int customerId;
    int orderId;
    std::string date;
};

bool compareOrders(const Order& a, const Order& b) {
    return a.date > b.date;
}

std::vector<Order> mostRecentThreeOrders(std::vector<Order>& orders) {
    std::sort(orders.begin(), orders.end(), compareOrders);
    std::vector<Order> result;
    std::unordered_map<int, int> customerOrderCount;

    for (const auto& order : orders) {
        if (customerOrderCount[order.customerId] < 3) {
            result.push_back(order);
            customerOrderCount[order.customerId]++;
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of orders.
> - **Space Complexity:** $O(n)$ for storing the sorted orders and the customer order count map.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to the additional data structures used to store the sorted orders and customer order count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `std::unordered_map` to store the most recent three orders for each customer, and iterating through the orders in a single pass.
- Detailed breakdown of the approach:
  1. Create a `std::unordered_map` to store the most recent three orders for each customer.
  2. Iterate through the orders and update the map for each customer.
  3. If a customer has more than three orders, remove the oldest order from the map.
- Proof of optimality: This approach has a linear time complexity and uses a constant amount of space for each customer, making it optimal.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <deque>

struct Order {
    int customerId;
    int orderId;
    std::string date;
};

std::vector<Order> mostRecentThreeOrders(std::vector<Order>& orders) {
    std::unordered_map<int, std::deque<Order>> customerOrders;

    for (const auto& order : orders) {
        if (customerOrders[order.customerId].size() < 3) {
            customerOrders[order.customerId].push_back(order);
        } else {
            if (order.date > customerOrders[order.customerId].front().date) {
                customerOrders[order.customerId].pop_front();
                customerOrders[order.customerId].push_back(order);
            }
        }
    }

    std::vector<Order> result;
    for (const auto& pair : customerOrders) {
        for (const auto& order : pair.second) {
            result.push_back(order);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of orders.
> - **Space Complexity:** $O(n)$ for storing the customer orders map.
> - **Optimality proof:** The approach has a linear time complexity and uses a constant amount of space for each customer, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `std::unordered_map` to store customer orders, and iterating through the orders in a single pass.
- Problem-solving patterns identified: Using a map to store customer data and iterating through the orders to update the map.
- Optimization techniques learned: Using a `std::deque` to store the most recent three orders for each customer and removing the oldest order when a customer has more than three orders.
- Similar problems to practice: Finding the most recent $k$ orders for each customer, or finding the most recent orders for each customer within a certain time range.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as customers with less than three orders.
- Edge cases to watch for: Handling cases where a customer has more than three orders, and ensuring that the orders are sorted by date in descending order.
- Performance pitfalls: Using a sorting operation with a high time complexity, such as $O(n^2)$.
- Testing considerations: Testing the implementation with different input scenarios, including edge cases and large input sizes.