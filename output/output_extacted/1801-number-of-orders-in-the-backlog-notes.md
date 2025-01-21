## Number of Orders in the Backlog
**Problem Link:** https://leetcode.com/problems/number-of-orders-in-the-backlog/description

**Problem Statement:**
- Input format and constraints: Given a list of `orderType` (0 for sell, 1 for buy) and `orderPrice`, find the number of orders in the backlog after processing all orders.
- Expected output format: Return the number of sell orders and buy orders that are still in the backlog.
- Key requirements and edge cases to consider:
  - Orders are processed in the order they appear in the input list.
  - Sell orders are matched with buy orders if the sell price is less than or equal to the buy price.
  - If an order is not matched, it is added to the backlog.
- Example test cases with explanations:
  - Input: `orderType = [0,1,0,1], orderPrice = [10,20,5,8]`, Output: `[1,1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use two lists to keep track of sell and buy orders in the backlog. Iterate through the input list and match orders based on their prices.
- Step-by-step breakdown of the solution:
  1. Initialize two empty lists to store sell and buy orders.
  2. Iterate through the input list. For each order, check if it is a sell or buy order.
  3. If it is a sell order, check if there are any buy orders in the backlog with a price greater than or equal to the sell price. If so, match the orders and remove them from the backlog.
  4. If it is a buy order, check if there are any sell orders in the backlog with a price less than or equal to the buy price. If so, match the orders and remove them from the backlog.
  5. If an order is not matched, add it to the backlog.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly implements the problem's requirements.

```cpp
vector<int> getNumberOfBacklogOrders(vector<vector<int>>& orders) {
    vector<int> result(2, 0);
    vector<vector<int>> sell, buy;
    
    for (auto& order : orders) {
        int type = order[0], price = order[1];
        
        if (type == 0) {
            while (!buy.empty() && buy.back()[0] >= price) {
                if (buy.back()[1] == 1) {
                    buy.pop_back();
                    break;
                } else {
                    buy.back()[1]--;
                    if (buy.back()[1] == 0) buy.pop_back();
                }
            }
            if (!buy.empty() || !sell.empty()) {
                sell.push_back({price, 1});
            }
        } else {
            while (!sell.empty() && sell.back()[0] <= price) {
                if (sell.back()[1] == 1) {
                    sell.pop_back();
                    break;
                } else {
                    sell.back()[1]--;
                    if (sell.back()[1] == 0) sell.pop_back();
                }
            }
            if (!buy.empty() || !sell.empty()) {
                buy.push_back({price, 1});
            }
        }
    }
    
    for (auto& s : sell) result[0] += s[1];
    for (auto& b : buy) result[1] += b[1];
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of orders. This is because in the worst-case scenario, we might need to iterate through the backlog for each order.
> - **Space Complexity:** $O(n)$, where $n$ is the number of orders. This is because we need to store the backlog of orders.
> - **Why these complexities occur:** The time complexity is high because of the nested loops used to match orders. The space complexity is linear because we need to store all orders in the backlog.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to store sell and buy orders. This allows us to efficiently find the best match for each order.
- Detailed breakdown of the approach:
  1. Initialize two priority queues to store sell and buy orders.
  2. Iterate through the input list. For each order, check if it is a sell or buy order.
  3. If it is a sell order, check if there are any buy orders in the priority queue with a price greater than or equal to the sell price. If so, match the orders and remove them from the priority queue.
  4. If it is a buy order, check if there are any sell orders in the priority queue with a price less than or equal to the buy price. If so, match the orders and remove them from the priority queue.
  5. If an order is not matched, add it to the priority queue.
- Why further optimization is impossible: This solution has the optimal time complexity because we are using a priority queue to efficiently find the best match for each order.

```cpp
vector<int> getNumberOfBacklogOrders(vector<vector<int>>& orders) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> sell;
    priority_queue<pair<int, int>> buy;
    
    for (auto& order : orders) {
        int type = order[0], price = order[1], amount = 1;
        
        if (type == 0) {
            while (!buy.empty() && buy.top().first >= price) {
                if (buy.top().second == 1) {
                    buy.pop();
                    break;
                } else {
                    buy.top().second--;
                    if (buy.top().second == 0) buy.pop();
                }
            }
            if (!buy.empty() || !sell.empty()) {
                sell.push({price, amount});
            }
        } else {
            while (!sell.empty() && sell.top().first <= price) {
                if (sell.top().second == 1) {
                    sell.pop();
                    break;
                } else {
                    sell.top().second--;
                    if (sell.top().second == 0) sell.pop();
                }
            }
            if (!buy.empty() || !sell.empty()) {
                buy.push({price, amount});
            }
        }
    }
    
    vector<int> result(2, 0);
    while (!sell.empty()) {
        result[0] += sell.top().second;
        sell.pop();
    }
    while (!buy.empty()) {
        result[1] += buy.top().second;
        buy.pop();
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of orders. This is because we are using a priority queue to efficiently find the best match for each order.
> - **Space Complexity:** $O(n)$, where $n$ is the number of orders. This is because we need to store the backlog of orders in the priority queue.
> - **Optimality proof:** This solution is optimal because we are using a priority queue to efficiently find the best match for each order, resulting in the lowest possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, greedy algorithms.
- Problem-solving patterns identified: Using data structures to efficiently solve problems.
- Optimization techniques learned: Using priority queues to reduce time complexity.
- Similar problems to practice: Other problems that involve matching orders or finding the best match.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not using priority queues efficiently.
- Edge cases to watch for: Orders with the same price, orders with a quantity of 0.
- Performance pitfalls: Using nested loops to match orders, not using priority queues to reduce time complexity.
- Testing considerations: Testing with different input sizes, testing with different types of orders.