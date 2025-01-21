## Immediate Food Delivery I

**Problem Link:** https://leetcode.com/problems/immediate-food-delivery-i/description

**Problem Statement:**
- Input format and constraints: We are given a 2D array `orders` where each order is a list of three integers `[customer_id, order_id, delivery_time]`. The goal is to find the number of immediate food delivery orders for each customer.
- Expected output format: The function should return a list of integers representing the number of immediate food delivery orders for each customer.
- Key requirements and edge cases to consider: 
  - Immediate food delivery orders are those where the delivery time is less than or equal to the order time.
  - We need to consider the case where a customer has multiple orders with the same order time but different delivery times.
- Example test cases with explanations:
  - For example, if the input is `orders = [[1, 1, 10], [1, 2, 5], [2, 1, 7]]`, the output should be `[1, 1]` because customer 1 has one immediate food delivery order and customer 2 has one immediate food delivery order.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate through each order and check if the delivery time is less than or equal to the order time. 
- Step-by-step breakdown of the solution:
  1. Initialize an empty dictionary `customer_orders` to store the number of immediate food delivery orders for each customer.
  2. Iterate through each order in the `orders` list.
  3. For each order, check if the customer is already in the `customer_orders` dictionary. If not, add them with a count of 0.
  4. If the delivery time is less than or equal to the order time, increment the count for the customer in the `customer_orders` dictionary.
  5. Finally, return a list of the counts for each customer in the `customer_orders` dictionary.
- Why this approach comes to mind first: This approach is the most straightforward because it involves simply iterating through each order and checking the delivery time.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> deliveryOrders(std::vector<std::vector<int>>& orders) {
    std::unordered_map<int, int> customer_orders;
    for (auto& order : orders) {
        int customer_id = order[0];
        int order_id = order[1];
        int delivery_time = order[2];
        if (customer_orders.find(customer_id) == customer_orders.end()) {
            customer_orders[customer_id] = 0;
        }
        if (delivery_time <= order_id) {
            customer_orders[customer_id]++;
        }
    }
    std::vector<int> result;
    for (auto& pair : customer_orders) {
        result.push_back(pair.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of orders, because we are iterating through each order once.
> - **Space Complexity:** $O(n)$ because in the worst case, we might have to store every customer in the `customer_orders` dictionary.
> - **Why these complexities occur:** These complexities occur because we are using a dictionary to store the counts for each customer, which allows for constant time lookups and insertions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we need to check every order to determine if it is an immediate food delivery order.
- Detailed breakdown of the approach:
  1. Initialize an empty dictionary `customer_orders` to store the number of immediate food delivery orders for each customer.
  2. Iterate through each order in the `orders` list.
  3. For each order, check if the customer is already in the `customer_orders` dictionary. If not, add them with a count of 0.
  4. If the delivery time is less than or equal to the order time, increment the count for the customer in the `customer_orders` dictionary.
  5. Finally, return a list of the counts for each customer in the `customer_orders` dictionary.
- Proof of optimality: This approach is optimal because we need to check every order to determine if it is an immediate food delivery order.
- Why further optimization is impossible: Further optimization is impossible because we need to check every order.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> deliveryOrders(std::vector<std::vector<int>>& orders) {
    std::unordered_map<int, int> customer_orders;
    for (auto& order : orders) {
        int customer_id = order[0];
        int order_id = order[1];
        int delivery_time = order[2];
        if (customer_orders.find(customer_id) == customer_orders.end()) {
            customer_orders[customer_id] = 0;
        }
        if (delivery_time <= order_id) {
            customer_orders[customer_id]++;
        }
    }
    std::vector<int> result;
    for (auto& pair : customer_orders) {
        result.push_back(pair.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of orders, because we are iterating through each order once.
> - **Space Complexity:** $O(n)$ because in the worst case, we might have to store every customer in the `customer_orders` dictionary.
> - **Optimality proof:** This approach is optimal because we need to check every order to determine if it is an immediate food delivery order.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of dictionaries to store and retrieve data efficiently.
- Problem-solving patterns identified: The need to check every order to determine if it is an immediate food delivery order.
- Optimization techniques learned: The use of dictionaries to reduce the time complexity of the solution.
- Similar problems to practice: Problems that involve checking every element in a list or array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a customer is already in the `customer_orders` dictionary before trying to increment their count.
- Edge cases to watch for: The case where a customer has multiple orders with the same order time but different delivery times.
- Performance pitfalls: Using a data structure that has a high time complexity for lookups or insertions, such as a list.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it is working correctly.