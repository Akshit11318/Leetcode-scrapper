## Customers Who Bought All Products
**Problem Link:** https://leetcode.com/problems/customers-who-bought-all-products/description

**Problem Statement:**
- Input: Three tables, `Products`, `Orders`, and `Order_Products`, where `Products` lists all available products, `Orders` lists all customer orders, and `Order_Products` is a bridge table connecting orders to the products purchased.
- Expected Output: A list of customer IDs who have bought all products.
- Key Requirements:
  - Identify all unique products.
  - For each customer, determine if they have purchased all unique products.
- Edge Cases:
  - Handling customers with no orders.
  - Handling products that are not ordered by any customer.
- Example Test Cases:
  - A customer who has bought all products.
  - A customer who has not bought all products.

---

### Brute Force Approach

**Explanation:**
- The initial thought is to iterate through each customer's orders, then for each order, iterate through the products in that order.
- For each product, check if the customer has bought it.
- If a customer has bought all products, add them to the result list.

```cpp
#include <vector>
#include <unordered_set>
#include <unordered_map>

struct Product {
    int product_id;
    string product_name;
};

struct Order {
    int order_id;
    int customer_id;
};

struct OrderProduct {
    int order_id;
    int product_id;
};

vector<int> customersWhoBoughtAllProducts(vector<Product>& products, vector<Order>& orders, vector<OrderProduct>& orderProducts) {
    unordered_set<int> allProducts;
    for (auto& p : products) {
        allProducts.insert(p.product_id);
    }

    unordered_map<int, unordered_set<int>> customerProducts;
    for (auto& op : orderProducts) {
        customerProducts[op.order_id].insert(op.product_id);
    }

    unordered_set<int> customersWithAllProducts;
    for (auto& o : orders) {
        unordered_set<int> productsForCustomer;
        for (auto& op : orderProducts) {
            if (op.order_id == o.order_id) {
                productsForCustomer.insert(op.product_id);
            }
        }
        if (productsForCustomer.size() == allProducts.size()) {
            bool hasAllProducts = true;
            for (auto& p : allProducts) {
                if (productsForCustomer.find(p) == productsForCustomer.end()) {
                    hasAllProducts = false;
                    break;
                }
            }
            if (hasAllProducts) {
                customersWithAllProducts.insert(o.customer_id);
            }
        }
    }

    vector<int> result;
    for (auto& c : customersWithAllProducts) {
        result.push_back(c);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot p)$, where $n$ is the number of orders, $m$ is the average number of products per order, and $p$ is the total number of unique products. This is because for each order, we potentially check all products.
> - **Space Complexity:** $O(n + m + p)$, for storing the sets and maps used to keep track of customer products and all products.
> - **Why these complexities occur:** The brute force approach involves multiple nested iterations over the input data, leading to high time complexity. The space complexity is due to the need to store all unique products and the products purchased by each customer.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to first group all products by customer, then check if the count of unique products for a customer matches the total number of unique products.
- Use SQL to efficiently query the database and avoid unnecessary iterations.

```cpp
SELECT customer_id
FROM (
    SELECT o.customer_id, COUNT(DISTINCT op.product_id) as num_products
    FROM Orders o
    JOIN Order_Products op ON o.order_id = op.order_id
    GROUP BY o.customer_id
) AS t
WHERE t.num_products = (SELECT COUNT(*) FROM Products);
```

Or, if you must use C++ and the data is already loaded into memory:

```cpp
#include <vector>
#include <unordered_set>
#include <unordered_map>

struct Product {
    int product_id;
    string product_name;
};

struct Order {
    int order_id;
    int customer_id;
};

struct OrderProduct {
    int order_id;
    int product_id;
};

vector<int> customersWhoBoughtAllProducts(vector<Product>& products, vector<Order>& orders, vector<OrderProduct>& orderProducts) {
    unordered_set<int> allProducts;
    for (auto& p : products) {
        allProducts.insert(p.product_id);
    }

    unordered_map<int, unordered_set<int>> customerProducts;
    for (auto& op : orderProducts) {
        customerProducts[op.order_id].insert(op.product_id);
    }

    unordered_map<int, unordered_set<int>> customerAllProducts;
    for (auto& o : orders) {
        for (auto& op : orderProducts) {
            if (op.order_id == o.order_id) {
                customerAllProducts[o.customer_id].insert(op.product_id);
            }
        }
    }

    vector<int> result;
    for (auto& pair : customerAllProducts) {
        if (pair.second.size() == allProducts.size()) {
            bool hasAllProducts = true;
            for (auto& p : allProducts) {
                if (pair.second.find(p) == pair.second.end()) {
                    hasAllProducts = false;
                    break;
                }
            }
            if (hasAllProducts) {
                result.push_back(pair.first);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + p)$, where $n$ is the number of orders, $m$ is the number of order products, and $p$ is the number of products. This is because we perform a constant amount of work for each order, order product, and product.
> - **Space Complexity:** $O(n + m + p)$, for storing the sets and maps used to keep track of customer products and all products.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through each of the input datasets, and it uses efficient data structures (unordered sets and maps) to minimize the time complexity of lookups and insertions.

---

### Final Notes

**Learning Points:**
- The importance of understanding the data structure and relationships between tables or data sets.
- How to approach problems by first considering a brute force solution and then optimizing.
- The use of efficient data structures like unordered sets and maps for fast lookups and insertions.
- SQL can be very efficient for querying databases directly.

**Mistakes to Avoid:**
- Not considering the relationships between different pieces of data.
- Not optimizing the solution after the initial brute force approach.
- Not using the most efficient data structures for the problem at hand.
- Not testing the solution thoroughly with various edge cases.