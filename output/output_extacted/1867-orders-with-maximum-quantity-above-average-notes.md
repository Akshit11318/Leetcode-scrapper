## Orders With Maximum Quantity Above Average
**Problem Link:** https://leetcode.com/problems/orders-with-maximum-quantity-above-average/description

**Problem Statement:**
- Input: A table `orders` with columns `order_id`, `product_id`, and `quantity`.
- Constraints: The table `orders` contains at least one row.
- Expected Output: The `order_id` with the highest `quantity` above the average `quantity` for each `product_id`.
- Key Requirements:
  - For each `product_id`, calculate the average `quantity`.
  - For each `order_id`, calculate the `quantity` above the average for its corresponding `product_id`.
  - Return the `order_id` with the maximum `quantity` above the average for each `product_id`.

**Example Test Cases:**
- Given `orders` table:
  | order_id | product_id | quantity |
  |---------|------------|---------|
  | 1       | 1          | 2       |
  | 2       | 1          | 3       |
  | 3       | 2          | 4       |
  | 4       | 2          | 5       |
- Calculate average `quantity` for each `product_id`:
  - For `product_id` = 1, average `quantity` = (2 + 3) / 2 = 2.5.
  - For `product_id` = 2, average `quantity` = (4 + 5) / 2 = 4.5.
- Calculate `quantity` above average for each `order_id`:
  - For `order_id` = 1, `quantity` above average = 2 - 2.5 = -0.5.
  - For `order_id` = 2, `quantity` above average = 3 - 2.5 = 0.5.
  - For `order_id` = 3, `quantity` above average = 4 - 4.5 = -0.5.
  - For `order_id` = 4, `quantity` above average = 5 - 4.5 = 0.5.
- Return `order_id` with maximum `quantity` above average:
  - Maximum `quantity` above average is 0.5, which corresponds to `order_id` = 2 and `order_id` = 4.

### Brute Force Approach

**Explanation:**
- Calculate the average `quantity` for each `product_id` by iterating over all rows in the `orders` table and summing the `quantity` for each `product_id`.
- Then, for each `order_id`, calculate the `quantity` above the average for its corresponding `product_id`.
- Keep track of the `order_id` with the maximum `quantity` above the average.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Order {
    int order_id;
    int product_id;
    int quantity;
};

vector<int> maxQuantityAboveAverage(vector<Order>& orders) {
    unordered_map<int, int> sumQuantity;
    unordered_map<int, int> countProduct;
    
    // Calculate sum of quantity and count of products for each product_id
    for (const auto& order : orders) {
        sumQuantity[order.product_id] += order.quantity;
        countProduct[order.product_id]++;
    }
    
    unordered_map<int, double> averageQuantity;
    // Calculate average quantity for each product_id
    for (const auto& product : sumQuantity) {
        averageQuantity[product.first] = static_cast<double>(product.second) / countProduct[product.first];
    }
    
    int maxAboveAverage = INT_MIN;
    vector<int> result;
    
    // Calculate quantity above average for each order_id and find the maximum
    for (const auto& order : orders) {
        double aboveAverage = order.quantity - averageQuantity[order.product_id];
        if (aboveAverage > maxAboveAverage) {
            maxAboveAverage = static_cast<int>(aboveAverage);
            result.clear();
            result.push_back(order.order_id);
        } else if (aboveAverage == maxAboveAverage) {
            result.push_back(order.order_id);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `orders` table, because we iterate over the table twice: once to calculate the average quantity for each product, and once to find the order with the maximum quantity above average.
> - **Space Complexity:** $O(n)$ because we use hash maps to store the sum of quantity and count of products for each product_id, and the average quantity for each product_id. In the worst case, the number of unique product_ids could be equal to the number of rows in the table.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each row in the table. The space complexity is also linear because we store information for each unique product_id.

### Optimal Approach (Required)

The provided brute force approach is already optimal with a time complexity of $O(n)$, as we must at least read the input once. However, we can slightly improve the implementation by combining the calculation of the sum of quantities and the count of products into a single pass over the data.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Order {
    int order_id;
    int product_id;
    int quantity;
};

vector<int> maxQuantityAboveAverage(vector<Order>& orders) {
    unordered_map<int, pair<int, int>> productInfo; // <product_id, (sum_quantity, count)>
    
    // Calculate sum of quantity and count of products for each product_id
    for (const auto& order : orders) {
        productInfo[order.product_id].first += order.quantity;
        productInfo[order.product_id].second++;
    }
    
    unordered_map<int, double> averageQuantity;
    // Calculate average quantity for each product_id
    for (const auto& product : productInfo) {
        averageQuantity[product.first] = static_cast<double>(product.second.first) / product.second.second;
    }
    
    int maxAboveAverage = INT_MIN;
    vector<int> result;
    
    // Calculate quantity above average for each order_id and find the maximum
    for (const auto& order : orders) {
        double aboveAverage = order.quantity - averageQuantity[order.product_id];
        if (aboveAverage > maxAboveAverage) {
            maxAboveAverage = static_cast<int>(aboveAverage);
            result.clear();
            result.push_back(order.order_id);
        } else if (aboveAverage == maxAboveAverage) {
            result.push_back(order.order_id);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `orders` table, because we iterate over the table twice: once to calculate the average quantity for each product, and once to find the order with the maximum quantity above average.
> - **Space Complexity:** $O(n)$ because we use hash maps to store the sum of quantity and count of products for each product_id, and the average quantity for each product_id. In the worst case, the number of unique product_ids could be equal to the number of rows in the table.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input data to calculate the necessary information (sum of quantities and count of products for each product_id), and then another pass to find the maximum quantity above average. This results in a linear time complexity, which is the best we can achieve for this problem since we must at least read the input once.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration over data, use of hash maps for efficient lookup and storage, and basic arithmetic operations.
- Problem-solving patterns identified: calculate necessary information in one pass, then use that information to solve the problem in another pass.
- Optimization techniques learned: combining calculations into fewer passes over the data.

**Mistakes to Avoid:**
- Common implementation errors: not initializing variables before use, not checking for division by zero when calculating averages.
- Edge cases to watch for: handling the case where there are no orders for a product_id, or where the quantity is zero.
- Performance pitfalls: using data structures with high lookup times (e.g., linked lists instead of hash maps).
- Testing considerations: test with different inputs, including edge cases, to ensure the solution works correctly in all scenarios.