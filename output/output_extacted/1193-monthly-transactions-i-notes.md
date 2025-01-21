## Monthly Transactions I
**Problem Link:** https://leetcode.com/problems/monthly-transactions-i/description

**Problem Statement:**
- Input: A list of transactions where each transaction is represented as a list of three integers: `transaction_id`, `day`, and `amount`.
- Constraints: 
  - `1 <= transaction_id <= 1000`
  - `1 <= day <= 365`
  - `1 <= amount <= 10000`
  - At most `10^5` transactions
- Expected output: A list of `transaction_id`s that have at least one transaction on the day of the month that is the same day of the month as the current date and at least one transaction on a different day of the month.
- Key requirements: Identify transactions that occur on the same day of the month as the current date and also on a different day of the month.
- Example test cases: 
  - Transactions on different days of the month and the same day of the month.
  - No transactions on the same day of the month as the current date.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all transactions and keep track of the days of the month each transaction occurs on.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the days of the month for each transaction.
  2. Iterate over each transaction, updating the dictionary with the day of the month.
  3. For each transaction, check if it has at least one transaction on the same day of the month as the current date and at least one transaction on a different day of the month.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, involving basic iteration and dictionary operations.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

vector<int> findTransactions(vector<vector<int>>& transactions) {
    unordered_map<int, set<int>> transactionDays;
    int currentDay = 15; // Assuming the current date is the 15th

    for (const auto& transaction : transactions) {
        int transactionId = transaction[0];
        int day = transaction[1];

        transactionDays[transactionId].insert(day);
    }

    vector<int> result;
    for (const auto& transaction : transactionDays) {
        if (transaction.second.find(currentDay) != transaction.second.end() && transaction.second.size() > 1) {
            result.push_back(transaction.first);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we iterate over each transaction once to update the dictionary and once to check the conditions.
> - **Space Complexity:** $O(n)$, as we store the days of the month for each transaction in the dictionary.
> - **Why these complexities occur:** The brute force approach involves iterating over all transactions, resulting in linear time complexity. The space complexity is also linear because we store information for each transaction.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in a single pass by maintaining a set of unique days for each transaction and checking the conditions on the fly.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the unique days for each transaction.
  2. Iterate over each transaction, updating the dictionary and checking the conditions.
- Proof of optimality: This approach is optimal because it only requires a single pass over the transactions, resulting in the minimum possible time complexity.
- Why further optimization is impossible: We must examine each transaction at least once to determine if it meets the conditions, so further optimization is not possible.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

vector<int> findTransactions(vector<vector<int>>& transactions) {
    unordered_map<int, set<int>> transactionDays;
    int currentDay = 15; // Assuming the current date is the 15th
    vector<int> result;

    for (const auto& transaction : transactions) {
        int transactionId = transaction[0];
        int day = transaction[1];

        transactionDays[transactionId].insert(day);
        if (transactionDays[transactionId].find(currentDay) != transactionDays[transactionId].end() && transactionDays[transactionId].size() > 1) {
            if (find(result.begin(), result.end(), transactionId) == result.end()) {
                result.push_back(transactionId);
            }
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we iterate over each transaction once to update the dictionary and check the conditions.
> - **Space Complexity:** $O(n)$, as we store the unique days for each transaction in the dictionary.
> - **Optimality proof:** The optimal approach is also $O(n)$, but it only requires a single pass over the transactions, making it more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dictionary operations, set operations, and iteration.
- Problem-solving patterns identified: Single-pass solutions, dictionary usage, and set operations.
- Optimization techniques learned: Reducing the number of passes over the data, using dictionaries for efficient lookups.
- Similar problems to practice: Problems involving dictionary operations, set operations, and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for edge cases, such as empty transactions or transactions with no unique days.
- Edge cases to watch for: Transactions with no unique days, transactions with only one day.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using a list instead of a set for unique days.
- Testing considerations: Testing with different inputs, such as empty transactions, transactions with no unique days, and transactions with only one day.