## Suspicious Bank Accounts
**Problem Link:** https://leetcode.com/problems/suspicious-bank-accounts/description

**Problem Statement:**
- Input format and constraints: Given a list of `transactions` where each transaction is a string in the format `transaction_id, account_id, amount, timestamp`, and a list of `account_id` that are considered suspicious. We need to find all `account_id` that are suspicious based on the following rules:
  - If an `account_id` appears in more than one `transaction_id`, it is suspicious.
  - If an `account_id` has transactions with the same `transaction_id` but different `amount` or `timestamp`, it is suspicious.
- Expected output format: Return a list of all `account_id` that are suspicious.
- Key requirements and edge cases to consider:
  - Handling duplicate `transaction_id` and `account_id`.
  - Checking for transactions with the same `transaction_id` but different `amount` or `timestamp`.
- Example test cases with explanations:
  - Test case with multiple `account_id` in a single `transaction_id`.
  - Test case with same `transaction_id` but different `amount` or `timestamp`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all transactions and check for suspicious activity based on the given rules.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the `transaction_id` and corresponding `account_id`.
  2. Create another dictionary to store the `account_id` and its corresponding transactions.
  3. Iterate through all transactions and check for suspicious activity.
- Why this approach comes to mind first: It is a straightforward approach to check all transactions and accounts.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<int> suspiciousBankAccounts(vector<string>& transactions) {
    unordered_map<string, vector<string>> transactionToAccount;
    unordered_map<string, vector<string>> accountToTransactions;
    
    for (const auto& transaction : transactions) {
        size_t comma1 = transaction.find(',');
        size_t comma2 = transaction.find(',', comma1 + 1);
        size_t comma3 = transaction.find(',', comma2 + 1);
        
        string transactionId = transaction.substr(0, comma1);
        string accountId = transaction.substr(comma1 + 1, comma2 - comma1 - 1);
        string amount = transaction.substr(comma2 + 1, comma3 - comma2 - 1);
        string timestamp = transaction.substr(comma3 + 1);
        
        if (transactionToAccount.find(transactionId) != transactionToAccount.end()) {
            // If transactionId already exists, add accountId to its list
            transactionToAccount[transactionId].push_back(accountId);
        } else {
            transactionToAccount[transactionId] = {accountId};
        }
        
        if (accountToTransactions.find(accountId) != accountToTransactions.end()) {
            // If accountId already exists, add transaction to its list
            accountToTransactions[accountId].push_back(transactionId + "," + amount + "," + timestamp);
        } else {
            accountToTransactions[accountId] = {transactionId + "," + amount + "," + timestamp};
        }
    }
    
    vector<int> suspiciousAccounts;
    for (const auto& pair : transactionToAccount) {
        if (pair.second.size() > 1) {
            for (const auto& accountId : pair.second) {
                if (find(suspiciousAccounts.begin(), suspiciousAccounts.end(), stoi(accountId)) == suspiciousAccounts.end()) {
                    suspiciousAccounts.push_back(stoi(accountId));
                }
            }
        }
    }
    
    for (const auto& pair : accountToTransactions) {
        unordered_set<string> transactions;
        for (const auto& transaction : pair.second) {
            transactions.insert(transaction);
        }
        if (transactions.size() != pair.second.size()) {
            if (find(suspiciousAccounts.begin(), suspiciousAccounts.end(), stoi(pair.first)) == suspiciousAccounts.end()) {
                suspiciousAccounts.push_back(stoi(pair.first));
            }
        }
    }
    
    return suspiciousAccounts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of transactions and $m$ is the average number of accounts per transaction.
> - **Space Complexity:** $O(n \cdot m)$ for storing the transaction to account and account to transactions dictionaries.
> - **Why these complexities occur:** The brute force approach requires iterating through all transactions and accounts, resulting in high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the transactions and accounts, and iterate through the transactions only once.
- Detailed breakdown of the approach:
  1. Create a hash map to store the transactions and accounts.
  2. Iterate through the transactions and check for suspicious activity.
- Proof of optimality: The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> suspiciousBankAccounts(vector<string>& transactions) {
    unordered_map<int, unordered_set<string>> accounts;
    unordered_map<string, unordered_set<string>> transactionsMap;
    
    for (const auto& transaction : transactions) {
        size_t comma1 = transaction.find(',');
        size_t comma2 = transaction.find(',', comma1 + 1);
        size_t comma3 = transaction.find(',', comma2 + 1);
        
        string transactionId = transaction.substr(0, comma1);
        int accountId = stoi(transaction.substr(comma1 + 1, comma2 - comma1 - 1));
        string amount = transaction.substr(comma2 + 1, comma3 - comma2 - 1);
        string timestamp = transaction.substr(comma3 + 1);
        
        if (accounts.find(accountId) != accounts.end()) {
            accounts[accountId].insert(transactionId);
        } else {
            accounts[accountId] = {transactionId};
        }
        
        string transactionKey = transactionId + "," + amount + "," + timestamp;
        if (transactionsMap.find(transactionId) != transactionsMap.end()) {
            transactionsMap[transactionId].insert(transactionKey);
        } else {
            transactionsMap[transactionId] = {transactionKey};
        }
    }
    
    vector<int> suspiciousAccounts;
    for (const auto& pair : accounts) {
        if (pair.second.size() > 1) {
            suspiciousAccounts.push_back(pair.first);
        }
    }
    
    for (const auto& pair : transactionsMap) {
        if (pair.second.size() > 1) {
            for (const auto& account : accounts) {
                if (account.second.find(pair.first) != account.second.end() && find(suspiciousAccounts.begin(), suspiciousAccounts.end(), account.first) == suspiciousAccounts.end()) {
                    suspiciousAccounts.push_back(account.first);
                }
            }
        }
    }
    
    return suspiciousAccounts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of transactions.
> - **Space Complexity:** $O(n)$ for storing the transactions and accounts in the hash map.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem, as we need to iterate through all transactions at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, sets, and iteration.
- Problem-solving patterns identified: Using hash maps to store and retrieve data efficiently.
- Optimization techniques learned: Reducing time complexity by using hash maps and iterating through the transactions only once.
- Similar problems to practice: Problems involving hash maps, sets, and iteration, such as finding duplicate elements or checking for suspicious activity.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null or empty values, not handling edge cases, and not using hash maps efficiently.
- Edge cases to watch for: Handling duplicate transactions, checking for suspicious activity, and handling empty or null values.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using arrays instead of hash maps, or iterating through the transactions multiple times.
- Testing considerations: Testing the code with different input values, including edge cases and large inputs, to ensure it works correctly and efficiently.