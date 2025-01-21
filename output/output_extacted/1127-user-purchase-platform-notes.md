## User Purchase Platform

**Problem Link:** https://leetcode.com/problems/user-purchase-platform/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a system that can handle user purchases. The input includes `n` as the number of users, `m` as the number of products, and a list of transactions where each transaction is represented as a triplet `(userId, productId, amount)`.
- Expected output format: The system should be able to report the total amount spent by each user and the total amount earned by each product.
- Key requirements and edge cases to consider: Handling duplicate transactions, ensuring data consistency, and efficiently querying user and product data.
- Example test cases with explanations:
    - A simple test case could involve a single user purchasing a single product.
    - A more complex test case might involve multiple users purchasing multiple products with varying amounts.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each transaction and updating the corresponding user and product amounts.
- Step-by-step breakdown of the solution:
    1. Initialize two maps to store the total amount spent by each user and the total amount earned by each product.
    2. Iterate over each transaction, updating the user's total amount spent and the product's total amount earned.
- Why this approach comes to mind first: It is straightforward and easy to implement, directly addressing the problem's requirements.

```cpp
#include <iostream>
#include <unordered_map>

class UserPurchasePlatform {
public:
    void addTransaction(int userId, int productId, int amount) {
        // Update user's total amount spent
        if (userAmounts.find(userId) == userAmounts.end()) {
            userAmounts[userId] = 0;
        }
        userAmounts[userId] += amount;

        // Update product's total amount earned
        if (productAmounts.find(productId) == productAmounts.end()) {
            productAmounts[productId] = 0;
        }
        productAmounts[productId] += amount;
    }

    int getUserAmount(int userId) {
        // Return user's total amount spent
        if (userAmounts.find(userId) != userAmounts.end()) {
            return userAmounts[userId];
        }
        return 0;
    }

    int getProductAmount(int productId) {
        // Return product's total amount earned
        if (productAmounts.find(productId) != productAmounts.end()) {
            return productAmounts[productId];
        }
        return 0;
    }

private:
    std::unordered_map<int, int> userAmounts;
    std::unordered_map<int, int> productAmounts;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + t)$ where $n$ is the number of users, $m$ is the number of products, and $t$ is the number of transactions. This is because we perform a constant amount of work for each user, product, and transaction.
> - **Space Complexity:** $O(n + m)$ as we need to store the total amount spent by each user and the total amount earned by each product.
> - **Why these complexities occur:** The time complexity is linear with respect to the input size because we perform a constant amount of work for each element in the input. The space complexity is also linear because we need to store information for each unique user and product.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is essentially the same as the brute force approach because the problem requires iterating over each transaction to update the user and product amounts.
- Detailed breakdown of the approach: We use two `unordered_map`s to store the total amount spent by each user and the total amount earned by each product. We iterate over each transaction, updating the corresponding user and product amounts.
- Proof of optimality: This solution is optimal because we must process each transaction at least once to calculate the total amounts. The use of `unordered_map`s allows for efficient lookups and updates, resulting in a time complexity of $O(n + m + t)$.
- Why further optimization is impossible: Further optimization is impossible because we must perform at least one operation for each transaction, resulting in a time complexity of at least $O(t)$.

```cpp
// Same code as the brute force approach
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + t)$
> - **Space Complexity:** $O(n + m)$
> - **Optimality proof:** This solution is optimal because we process each transaction exactly once and use efficient data structures for lookups and updates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of data structures (`unordered_map`) for fast lookups and updates.
- Problem-solving patterns identified: Iterating over each transaction to update user and product amounts.
- Optimization techniques learned: Using efficient data structures to reduce time complexity.
- Similar problems to practice: Problems involving iterating over transactions or updates to calculate totals.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle duplicate transactions or not initializing data structures properly.
- Edge cases to watch for: Handling cases where users or products are not present in the data structures.
- Performance pitfalls: Using inefficient data structures (e.g., `vector` instead of `unordered_map`) that result in higher time complexity.
- Testing considerations: Thoroughly testing the solution with various input scenarios to ensure correctness and efficiency.