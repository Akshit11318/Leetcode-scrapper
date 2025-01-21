## Customer Who Visited But Did Not Make Any Transactions
**Problem Link:** https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description

**Problem Statement:**
- Input format: Two tables, `Visits` and `Transactions`, where `Visits` contains the customer ID and the date of visit, and `Transactions` contains the customer ID and the date of transaction.
- Constraints: Find the customer ID of customers who visited the store but did not make any transactions on that date.
- Expected output format: A table with the customer ID.
- Key requirements and edge cases to consider: Handling cases where a customer visits multiple times but makes transactions on some of those visits.

**Example Test Cases:**
- A customer visits on a date and makes no transactions.
- A customer visits on a date and makes a transaction.
- A customer visits multiple times on the same date, with and without transactions.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over each visit and check if there's a corresponding transaction on the same date.
- Step-by-step breakdown:
  1. For each row in the `Visits` table, extract the customer ID and visit date.
  2. For each visit, query the `Transactions` table to check if there's a transaction on the same date for the same customer.
  3. If no transaction is found, add the customer ID to the result set.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

struct Visit {
    int customerId;
    string visitDate;
};

struct Transaction {
    int customerId;
    string transactionDate;
};

vector<int> findCustomersWhoDidNotMakeTransactions(vector<Visit>& visits, vector<Transaction>& transactions) {
    unordered_set<int> result;
    for (const auto& visit : visits) {
        bool transactionFound = false;
        for (const auto& transaction : transactions) {
            if (visit.customerId == transaction.customerId && visit.visitDate == transaction.transactionDate) {
                transactionFound = true;
                break;
            }
        }
        if (!transactionFound) {
            result.insert(visit.customerId);
        }
    }
    vector<int> finalResult(result.begin(), result.end());
    return finalResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of visits and $m$ is the number of transactions, because for each visit, we potentially iterate over all transactions.
> - **Space Complexity:** $O(n + m)$, for storing the visits and transactions.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the visits and transactions, leading to the quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a more efficient data structure, such as a `unordered_map`, to store transactions by customer ID and date, allowing for constant time lookups.
- Detailed breakdown:
  1. Create an `unordered_map` where the key is a pair of customer ID and date, and the value is a boolean indicating whether a transaction occurred.
  2. Populate this map with data from the `Transactions` table.
  3. Then, for each visit, check the map for the presence of a transaction on the same date for the same customer. If not found, add the customer ID to the result set.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Visit {
    int customerId;
    string visitDate;
};

struct Transaction {
    int customerId;
    string transactionDate;
};

using TransactionMap = unordered_map<pair<int, string>, bool>;

vector<int> findCustomersWhoDidNotMakeTransactions(vector<Visit>& visits, vector<Transaction>& transactions) {
    TransactionMap transactionMap;
    for (const auto& transaction : transactions) {
        transactionMap[{transaction.customerId, transaction.transactionDate}] = true;
    }
    
    vector<int> result;
    for (const auto& visit : visits) {
        if (transactionMap.find({visit.customerId, visit.visitDate}) == transactionMap.end()) {
            result.push_back(visit.customerId);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of visits and $m$ is the number of transactions, because we perform a constant amount of work for each visit and transaction.
> - **Space Complexity:** $O(n + m)$, for storing the visits and transactions in the map.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem, leveraging the efficiency of `unordered_map` lookups.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem at hand.
- How to optimize queries by reducing the number of iterations and leveraging constant time lookups.
- The value of breaking down problems into smaller, more manageable parts.

**Mistakes to Avoid:**
- Assuming a brute force approach is the only solution.
- Not considering the trade-offs between time and space complexity.
- Failing to optimize database queries or data structure lookups.