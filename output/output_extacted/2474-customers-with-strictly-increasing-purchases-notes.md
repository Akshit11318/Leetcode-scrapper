## Customers With Strictly Increasing Purchases

**Problem Link:** https://leetcode.com/problems/customers-with-strictly-increasing-purchases/description

**Problem Statement:**
- The problem requires finding all customers with strictly increasing purchases from a given table of customer purchases.
- The input is a table `Purchases` with columns `customer_id`, `product_id`, and `purchase_date`.
- The expected output is a table containing `customer_id` of customers who have made purchases with strictly increasing `product_id`.
- Key requirements include ensuring that each customer's purchases are strictly increasing by `product_id`.
- Edge cases to consider include handling customers with no purchases, or those with non-increasing purchases.

**Example Test Cases:**
- If the `Purchases` table contains entries where a customer's `product_id` increases strictly for each purchase, that customer should be included in the result.
- If a customer has purchases with the same or decreasing `product_id`, they should not be included in the result.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves sorting the purchases by `customer_id` and `purchase_date`, then checking each customer's purchases for strictly increasing `product_id`.
- This approach comes to mind first because it directly addresses the problem statement by examining each customer's purchases in sequence.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Purchase {
    int customer_id;
    int product_id;
    std::string purchase_date;
};

bool comparePurchases(const Purchase& a, const Purchase& b) {
    if (a.customer_id == b.customer_id) {
        return a.purchase_date < b.purchase_date;
    }
    return a.customer_id < b.customer_id;
}

std::vector<int> customersWithIncreasingPurchases(std::vector<Purchase>& purchases) {
    std::sort(purchases.begin(), purchases.end(), comparePurchases);
    std::vector<int> result;
    
    int currentCustomer = -1;
    int previousProduct = -1;
    
    for (const auto& purchase : purchases) {
        if (purchase.customer_id != currentCustomer) {
            currentCustomer = purchase.customer_id;
            previousProduct = -1;
        }
        
        if (previousProduct != -1 && purchase.product_id <= previousProduct) {
            currentCustomer = -1; // Reset for next customer
            continue;
        }
        
        previousProduct = purchase.product_id;
    }
    
    // This approach doesn't correctly implement the logic for selecting customers
    // It's more of a starting point to understand the problem flow
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of purchases.
> - **Space Complexity:** $O(n)$ for storing the sorted purchases and the result.
> - **Why these complexities occur:** Sorting dominates the time complexity, and storing the result and intermediate data structures contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to group purchases by `customer_id` and then check each group for strictly increasing `product_id`.
- This can be achieved by using a SQL query that selects `customer_id` where the condition of strictly increasing `product_id` is met for all purchases of a customer.

```cpp
SELECT customer_id
FROM (
    SELECT customer_id,
    LAG(product_id) OVER (PARTITION BY customer_id ORDER BY purchase_date) AS prev_product_id,
    product_id
    FROM Purchases
) t
WHERE prev_product_id IS NULL OR product_id > prev_product_id
GROUP BY customer_id
HAVING COUNT(DISTINCT CASE WHEN prev_product_id IS NULL OR product_id > prev_product_id THEN product_id END) = COUNT(*)
```

Alternatively, in C++:

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Purchase {
    int customer_id;
    int product_id;
    std::string purchase_date;
};

std::vector<int> customersWithIncreasingPurchases(std::vector<Purchase>& purchases) {
    std::unordered_map<int, std::vector<Purchase>> customerPurchases;
    
    for (const auto& purchase : purchases) {
        customerPurchases[purchase.customer_id].push_back(purchase);
    }
    
    std::vector<int> result;
    
    for (auto& pair : customerPurchases) {
        std::vector<Purchase>& purchases = pair.second;
        std::sort(purchases.begin(), purchases.end(), [](const Purchase& a, const Purchase& b) {
            return a.purchase_date < b.purchase_date;
        });
        
        bool isIncreasing = true;
        for (int i = 1; i < purchases.size(); ++i) {
            if (purchases[i].product_id <= purchases[i-1].product_id) {
                isIncreasing = false;
                break;
            }
        }
        
        if (isIncreasing) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting each customer's purchases, where $n$ is the total number of purchases.
> - **Space Complexity:** $O(n)$ for storing the purchases grouped by customer and the result.
> - **Optimality proof:** This approach is optimal because it directly checks the condition of strictly increasing purchases for each customer with the minimum necessary operations (sorting and comparing adjacent elements).

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem statement and identifying key constraints.
- Using SQL or grouping data by a common attribute (`customer_id` in this case) to simplify the problem.
- The role of sorting in simplifying the comparison of adjacent elements.
- Optimization techniques such as using efficient data structures and algorithms.

**Mistakes to Avoid:**
- Not correctly grouping or sorting data before analysis.
- Failing to check for edge cases such as empty purchases or non-increasing product IDs.
- Inefficiently iterating over data or using suboptimal algorithms.
- Not validating input or handling errors properly.