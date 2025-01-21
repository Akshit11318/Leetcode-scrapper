## Find Bursty Behavior
**Problem Link:** https://leetcode.com/problems/find-bursty-behavior/description

**Problem Statement:**
- Given a table `transactions` with columns `id`, `account_id`, and `day`, find the accounts that exhibit **bursty behavior**, defined as having at least two transactions in a 3-day period and no more than 1 transaction in any other 3-day period.
- Input constraints: The table contains at least 1 and at most 20 rows.
- Expected output format: Return the `account_id` of the accounts that exhibit bursty behavior.

**Key Requirements and Edge Cases:**
- Handle cases where an account has only one transaction.
- Consider cases where an account has multiple transactions within a 3-day period but does not exhibit bursty behavior.

**Example Test Cases:**
- Suppose we have the following transactions:
  | id | account_id | day |
  |----|------------|-----|
  | 1  | 1          | 1   |
  | 2  | 1          | 2   |
  | 3  | 1          | 3   |
  | 4  | 2          | 1   |
  | 5  | 2          | 4   |
- The account with `account_id` = 1 exhibits bursty behavior because it has at least two transactions in a 3-day period (days 1-3) and no more than 1 transaction in any other 3-day period.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each account and check for bursty behavior by examining all possible 3-day periods.
- For each account, we will count the number of transactions in each 3-day period and check if the conditions for bursty behavior are met.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Transaction {
    int id;
    int account_id;
    int day;
};

std::vector<int> find_bursty_accounts(std::vector<Transaction>& transactions) {
    std::unordered_map<int, std::vector<int>> account_transactions;
    for (const auto& transaction : transactions) {
        account_transactions[transaction.account_id].push_back(transaction.day);
    }

    std::vector<int> bursty_accounts;
    for (const auto& account : account_transactions) {
        bool is_bursty = false;
        std::vector<int> days = account.second;
        std::sort(days.begin(), days.end());

        for (int i = 0; i < days.size() - 1; ++i) {
            if (days[i + 1] - days[i] <= 2) {
                is_bursty = true;
                break;
            }
        }

        if (is_bursty) {
            bool has_more_than_one_burst = false;
            for (int i = 0; i < days.size() - 2; ++i) {
                if (days[i + 2] - days[i] <= 2) {
                    has_more_than_one_burst = true;
                    break;
                }
            }

            if (!has_more_than_one_burst) {
                bursty_accounts.push_back(account.first);
            }
        }
    }

    return bursty_accounts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log m)$, where $n$ is the number of accounts and $m$ is the maximum number of transactions per account. The sorting operation dominates the time complexity.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of accounts and $m$ is the maximum number of transactions per account. We store all transactions for each account.
> - **Why these complexities occur:** The brute force approach involves iterating over all transactions for each account, sorting the transactions by day, and checking for bursty behavior. The sorting operation is the most time-consuming part.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to efficiently count the number of transactions in each 3-day period.
- We will iterate over each account's transactions and use a sliding window of size 3 to check for bursty behavior.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Transaction {
    int id;
    int account_id;
    int day;
};

std::vector<int> find_bursty_accounts(std::vector<Transaction>& transactions) {
    std::unordered_map<int, std::vector<int>> account_transactions;
    for (const auto& transaction : transactions) {
        account_transactions[transaction.account_id].push_back(transaction.day);
    }

    std::vector<int> bursty_accounts;
    for (const auto& account : account_transactions) {
        std::vector<int> days = account.second;
        std::sort(days.begin(), days.end());

        int max_count = 0;
        int current_count = 0;
        for (int i = 0; i < days.size(); ++i) {
            if (i == 0 || days[i] - days[i - 1] > 2) {
                current_count = 1;
            } else {
                current_count++;
            }

            max_count = std::max(max_count, current_count);
        }

        if (max_count >= 2) {
            bool has_more_than_one_burst = false;
            for (int i = 0; i < days.size() - 2; ++i) {
                if (days[i + 2] - days[i] <= 2) {
                    has_more_than_one_burst = true;
                    break;
                }
            }

            if (!has_more_than_one_burst) {
                bursty_accounts.push_back(account.first);
            }
        }
    }

    return bursty_accounts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log m)$, where $n$ is the number of accounts and $m$ is the maximum number of transactions per account. The sorting operation dominates the time complexity.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of accounts and $m$ is the maximum number of transactions per account. We store all transactions for each account.
> - **Optimality proof:** The optimal approach still requires sorting the transactions by day, which dominates the time complexity. However, the sliding window approach reduces the number of iterations and improves the overall efficiency of the algorithm.

---

### Final Notes

**Learning Points:**
- The importance of **sliding window techniques** in solving problems involving intervals or periods.
- The need to **optimize sorting operations** when dealing with large datasets.
- The use of **unordered maps** to efficiently store and retrieve data.

**Mistakes to Avoid:**
- Failing to **handle edge cases**, such as accounts with only one transaction.
- Not **optimizing the sorting operation**, which can significantly impact performance.
- Not **using efficient data structures**, such as unordered maps, to store and retrieve data.