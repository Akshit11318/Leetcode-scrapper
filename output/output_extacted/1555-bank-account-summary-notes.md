## Bank Account Summary
**Problem Link:** https://leetcode.com/problems/bank-account-summary/description

**Problem Statement:**
- Input format and constraints: The input is a table `Transactions` with columns `name`, `amount`, and `transaction_date`.
- Expected output format: The output should be a table with columns `name` and `balance` where `balance` is the total amount for each `name`.
- Key requirements and edge cases to consider: The `amount` can be positive or negative, and the output should be ordered by `balance` in descending order. If there are multiple `name`s with the same `balance`, the output should be ordered by `name` in ascending order.
- Example test cases with explanations:
  - If the input is `Transactions` table with rows `(John, 100, 2020-01-01)`, `(John, -50, 2020-01-02)`, `(Alice, 200, 2020-01-01)`, the output should be `Alice, 200`, `John, 50`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each row in the `Transactions` table, calculate the total amount for each `name`, and store it in a dictionary or map.
- Step-by-step breakdown of the solution:
  1. Create an empty dictionary to store the total amount for each `name`.
  2. Iterate over each row in the `Transactions` table.
  3. For each row, add the `amount` to the total amount of the corresponding `name` in the dictionary.
  4. After iterating over all rows, create a result table with the `name` and `balance` columns.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

struct Transaction {
    std::string name;
    int amount;
};

std::vector<std::pair<std::string, int>> bankAccountSummary(std::vector<Transaction>& transactions) {
    std::map<std::string, int> balances;
    for (const auto& transaction : transactions) {
        if (balances.find(transaction.name) != balances.end()) {
            balances[transaction.name] += transaction.amount;
        } else {
            balances[transaction.name] = transaction.amount;
        }
    }

    std::vector<std::pair<std::string, int>> result;
    for (const auto& balance : balances) {
        result.push_back(balance);
    }

    std::sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
        if (a.second == b.second) {
            return a.first < b.first;
        }
        return a.second > b.second;
    });

    return result;
}

int main() {
    std::vector<Transaction> transactions = {{"John", 100}, {"John", -50}, {"Alice", 200}};
    std::vector<std::pair<std::string, int>> result = bankAccountSummary(transactions);
    for (const auto& balance : result) {
        std::cout << balance.first << ", " << balance.second << std::endl;
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of unique `name`s. The reason is that we iterate over each row in the `Transactions` table, and then sort the result table.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique `name`s. The reason is that we store the total amount for each `name` in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we sort the result table, and the space complexity occurs because we store the total amount for each `name` in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the `Transactions` table to calculate the total amount for each `name`, and store it in a dictionary or map. Then, we can create a result table with the `name` and `balance` columns, and sort it.
- Detailed breakdown of the approach:
  1. Create an empty dictionary to store the total amount for each `name`.
  2. Iterate over each row in the `Transactions` table, and add the `amount` to the total amount of the corresponding `name` in the dictionary.
  3. Create a result table with the `name` and `balance` columns from the dictionary.
  4. Sort the result table by `balance` in descending order, and then by `name` in ascending order.
- Proof of optimality: This approach is optimal because it only requires a single pass through the `Transactions` table, and the sorting step is necessary to get the correct output.

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

struct Transaction {
    std::string name;
    int amount;
};

std::vector<std::pair<std::string, int>> bankAccountSummary(std::vector<Transaction>& transactions) {
    std::map<std::string, int> balances;
    for (const auto& transaction : transactions) {
        balances[transaction.name] += transaction.amount;
    }

    std::vector<std::pair<std::string, int>> result(balances.begin(), balances.end());
    std::sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
        if (a.second == b.second) {
            return a.first < b.first;
        }
        return a.second > b.second;
    });

    return result;
}

int main() {
    std::vector<Transaction> transactions = {{"John", 100}, {"John", -50}, {"Alice", 200}};
    std::vector<std::pair<std::string, int>> result = bankAccountSummary(transactions);
    for (const auto& balance : result) {
        std::cout << balance.first << ", " << balance.second << std::endl;
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of unique `name`s. The reason is that we iterate over each row in the `Transactions` table, and then sort the result table.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique `name`s. The reason is that we store the total amount for each `name` in a dictionary.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the `Transactions` table, and the sorting step is necessary to get the correct output.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dictionary or map, sorting.
- Problem-solving patterns identified: single pass through the input, sorting the output.
- Optimization techniques learned: using a dictionary or map to store the total amount for each `name`.
- Similar problems to practice: problems that require calculating the total amount for each group, and sorting the output.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the dictionary or map, not sorting the output.
- Edge cases to watch for: empty input, duplicate `name`s.
- Performance pitfalls: using a slow sorting algorithm, not using a dictionary or map to store the total amount for each `name`.
- Testing considerations: testing with different inputs, testing the sorting order.