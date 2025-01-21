## Bank Account Summary II
**Problem Link:** https://leetcode.com/problems/bank-account-summary-ii/description

**Problem Statement:**
- Input format and constraints: The problem involves processing a list of transactions to determine the summary of a bank account. The input includes the account number, customer name, and a list of transactions. The transactions are represented by a transaction ID, account number, transaction type (deposit or withdrawal), and the transaction amount.
- Expected output format: The output should include the account number, customer name, and the total amount in the account.
- Key requirements and edge cases to consider: The solution should handle multiple transactions for the same account, calculate the total amount correctly, and ignore transactions for other accounts.
- Example test cases with explanations: 
    - Test case 1: A single account with multiple deposits and withdrawals.
    - Test case 2: Multiple accounts with different transactions.
    - Test case 3: An empty list of transactions.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each transaction and checking if it belongs to the given account. If it does, update the total amount accordingly.
- Step-by-step breakdown of the solution:
    1. Initialize a dictionary to store the account information (account number and customer name).
    2. Initialize a variable to store the total amount for each account.
    3. Iterate over each transaction in the list of transactions.
    4. Check if the transaction belongs to the given account.
    5. If it does, update the total amount based on the transaction type (deposit or withdrawal).
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a natural starting point.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

struct Transaction {
    int id;
    int accountId;
    string type;
    int amount;
};

struct Account {
    int id;
    string customerName;
};

void bankAccountSummary(vector<Transaction>& transactions, vector<Account>& accounts) {
    unordered_map<int, int> accountAmounts;
    for (const auto& account : accounts) {
        accountAmounts[account.id] = 0;
    }
    
    for (const auto& transaction : transactions) {
        if (accountAmounts.find(transaction.accountId) != accountAmounts.end()) {
            if (transaction.type == "deposit") {
                accountAmounts[transaction.accountId] += transaction.amount;
            } else if (transaction.type == "withdrawal") {
                accountAmounts[transaction.accountId] -= transaction.amount;
            }
        }
    }
    
    for (const auto& account : accounts) {
        cout << "Account Number: " << account.id << ", Customer Name: " << account.customerName << ", Total Amount: " << accountAmounts[account.id] << endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where n is the number of accounts and m is the number of transactions. This is because we iterate over each account and each transaction once.
> - **Space Complexity:** $O(n)$, where n is the number of accounts. This is because we store the account information in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we perform a constant amount of work for each account and transaction. The space complexity occurs because we store the account information in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a dictionary to store the account information and updating the total amount for each account in a single pass.
- Detailed breakdown of the approach:
    1. Initialize a dictionary to store the account information (account number, customer name, and total amount).
    2. Iterate over each account and initialize the total amount to 0.
    3. Iterate over each transaction and update the total amount for the corresponding account.
    4. Print the account information and total amount for each account.
- Proof of optimality: The optimal solution has a time complexity of $O(n + m)$, which is the best possible time complexity because we must process each account and transaction at least once.
- Why further optimization is impossible: Further optimization is impossible because we must perform a constant amount of work for each account and transaction.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

struct Transaction {
    int id;
    int accountId;
    string type;
    int amount;
};

struct Account {
    int id;
    string customerName;
};

void bankAccountSummary(vector<Transaction>& transactions, vector<Account>& accounts) {
    unordered_map<int, pair<string, int>> accountInfo;
    
    for (const auto& account : accounts) {
        accountInfo[account.id] = {account.customerName, 0};
    }
    
    for (const auto& transaction : transactions) {
        if (accountInfo.find(transaction.accountId) != accountInfo.end()) {
            if (transaction.type == "deposit") {
                accountInfo[transaction.accountId].second += transaction.amount;
            } else if (transaction.type == "withdrawal") {
                accountInfo[transaction.accountId].second -= transaction.amount;
            }
        }
    }
    
    for (const auto& account : accountInfo) {
        cout << "Account Number: " << account.first << ", Customer Name: " << account.second.first << ", Total Amount: " << account.second.second << endl;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where n is the number of accounts and m is the number of transactions. This is because we iterate over each account and each transaction once.
> - **Space Complexity:** $O(n)$, where n is the number of accounts. This is because we store the account information in a dictionary.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n + m)$, which is the best possible time complexity because we must process each account and transaction at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dictionary usage, iteration, and conditional statements.
- Problem-solving patterns identified: Using a dictionary to store information and updating it in a single pass.
- Optimization techniques learned: Reducing the number of iterations and using a dictionary to store information.
- Similar problems to practice: Problems involving dictionary usage and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dictionary correctly, not updating the total amount correctly, and not handling edge cases.
- Edge cases to watch for: Empty list of transactions, empty list of accounts, and transactions for other accounts.
- Performance pitfalls: Using nested loops and not using a dictionary to store information.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure it works correctly.