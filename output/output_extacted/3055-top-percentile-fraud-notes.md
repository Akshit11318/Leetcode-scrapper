## Top Percentile Fraud
**Problem Link:** https://leetcode.com/problems/top-percentile-fraud/description

**Problem Statement:**
- Input format: `transactions` table with `id`, `name`, `day`, `amount`, and `type` columns.
- Constraints: `1 <= id <= 10^5`, `1 <= day <= 100`, `1 <= amount <= 20000`, and `type` is either `0` or `1`.
- Expected output format: Return the `id` of the top percentile fraud transactions.
- Key requirements and edge cases to consider:
  - A transaction is considered fraudulent if its `type` is `0` and its `amount` is greater than the 90th percentile of all transactions of the same `type`.
  - If there are multiple transactions with the same `id`, return the maximum `id`.
- Example test cases with explanations:
  - For a single transaction with `id = 1`, `name = 'John'`, `day = 1`, `amount = 1000`, and `type = 0`, if the 90th percentile of all transactions of the same `type` is `500`, the transaction is considered fraudulent.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the 90th percentile of all transactions of the same `type` and compare it with each transaction's `amount`.
- Step-by-step breakdown of the solution:
  1. Group all transactions by their `type`.
  2. For each group, calculate the 90th percentile of the `amount` column.
  3. For each transaction, check if its `type` is `0` and its `amount` is greater than the 90th percentile of the corresponding group.
  4. If a transaction is considered fraudulent, add its `id` to the result list.
- Why this approach comes to mind first: It directly addresses the problem statement by calculating the 90th percentile and comparing it with each transaction's `amount`.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

struct Transaction {
    int id;
    string name;
    int day;
    int amount;
    int type;
};

vector<int> findTopPercentileFraud(vector<Transaction>& transactions) {
    // Group all transactions by their type
    vector<vector<Transaction>> groups(2);
    for (const auto& transaction : transactions) {
        groups[transaction.type].push_back(transaction);
    }

    // Calculate the 90th percentile of each group
    vector<int> percentiles(2, 0);
    for (int i = 0; i < 2; ++i) {
        if (!groups[i].empty()) {
            vector<int> amounts;
            for (const auto& transaction : groups[i]) {
                amounts.push_back(transaction.amount);
            }
            sort(amounts.begin(), amounts.end());
            int index = amounts.size() * 9 / 10;
            percentiles[i] = amounts[index];
        }
    }

    // Find fraudulent transactions
    vector<int> result;
    for (const auto& transaction : transactions) {
        if (transaction.type == 0 && transaction.amount > percentiles[0]) {
            result.push_back(transaction.id);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of transactions. This is because we sort the `amount` column for each group.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we store all transactions in the `groups` vector.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is determined by the storage of all transactions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a single pass to calculate the 90th percentile and compare it with each transaction's `amount`.
- Detailed breakdown of the approach:
  1. Initialize two vectors to store the `amount` values for each `type`.
  2. Iterate over all transactions and append their `amount` values to the corresponding vector.
  3. For each vector, calculate the 90th percentile using a single pass.
  4. Iterate over all transactions again and check if each transaction's `amount` is greater than the 90th percentile of the corresponding vector.
  5. If a transaction is considered fraudulent, add its `id` to the result list.
- Why further optimization is impossible: We must iterate over all transactions at least twice to calculate the 90th percentile and compare it with each transaction's `amount`.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>

using namespace std;

struct Transaction {
    int id;
    string name;
    int day;
    int amount;
    int type;
};

vector<int> findTopPercentileFraud(vector<Transaction>& transactions) {
    // Initialize vectors to store amount values for each type
    vector<int> amounts0, amounts1;

    // Calculate the 90th percentile of each type
    for (const auto& transaction : transactions) {
        if (transaction.type == 0) {
            amounts0.push_back(transaction.amount);
        } else {
            amounts1.push_back(transaction.amount);
        }
    }

    // Calculate the 90th percentile
    int percentile0 = 0, percentile1 = 0;
    if (!amounts0.empty()) {
        sort(amounts0.begin(), amounts0.end());
        int index = amounts0.size() * 9 / 10;
        percentile0 = amounts0[index];
    }
    if (!amounts1.empty()) {
        sort(amounts1.begin(), amounts1.end());
        int index = amounts1.size() * 9 / 10;
        percentile1 = amounts1[index];
    }

    // Find fraudulent transactions
    vector<int> result;
    for (const auto& transaction : transactions) {
        if (transaction.type == 0 && transaction.amount > percentile0) {
            result.push_back(transaction.id);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of transactions. This is because we sort the `amount` values for each `type`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we store all `amount` values for each `type`.
> - **Optimality proof:** We must iterate over all transactions at least twice to calculate the 90th percentile and compare it with each transaction's `amount`. The single-pass approach minimizes the number of iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Calculating the 90th percentile, iterating over all transactions, and comparing each transaction's `amount` with the 90th percentile.
- Problem-solving patterns identified: Using a single pass to calculate the 90th percentile and compare it with each transaction's `amount`.
- Optimization techniques learned: Minimizing the number of iterations by using a single pass.
- Similar problems to practice: Calculating other percentiles, such as the 25th or 75th percentile.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty vectors or invalid input.
- Edge cases to watch for: Empty vectors, invalid input, or transactions with invalid `type` values.
- Performance pitfalls: Using unnecessary iterations or sorting operations.
- Testing considerations: Test the solution with various input scenarios, including empty vectors, invalid input, and transactions with different `type` values.