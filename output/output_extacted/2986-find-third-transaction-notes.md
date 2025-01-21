## Find Third Transaction
**Problem Link:** https://leetcode.com/problems/find-third-transaction/description

**Problem Statement:**
- Input: `transactions` array, `threshold` integer
- Output: Return the names of users who have at least three transactions with a total amount greater than the threshold.
- Key requirements: 
  - Each transaction is represented as an array `[name, country, amount]`.
  - A user is identified by their name.
  - The total amount is the sum of the amounts of the transactions.
  - A transaction is considered valid if the user has at least three transactions with a total amount greater than the threshold.
- Edge cases: 
  - Empty transactions array
  - Threshold is zero or negative
  - Users with less than three transactions
- Example test cases: 
  - `transactions = [["alice","usa",100],["bob","usa",200],["alice","usa",300],["alice","usa",400]]`, `threshold = 900`
  - `transactions = [["alice","usa",100],["bob","usa",200],["alice","usa",300]]`, `threshold = 900`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all transactions and calculate the total amount for each user.
- Step-by-step breakdown: 
  1. Create a dictionary to store the total amount for each user.
  2. Iterate over all transactions and update the total amount for each user.
  3. Check if the total amount for each user is greater than the threshold and if they have at least three transactions.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible transactions.

```cpp
vector<string> invalidTransactions(vector<vector<string>>& transactions, int threshold) {
    unordered_map<string, vector<int>> user_transactions;
    for (int i = 0; i < transactions.size(); i++) {
        string user = transactions[i][0];
        int amount = stoi(transactions[i][2]);
        user_transactions[user].push_back(amount);
    }
    
    vector<string> result;
    for (auto& user : user_transactions) {
        if (user.second.size() >= 3) {
            int total_amount = 0;
            for (int amount : user.second) {
                total_amount += amount;
            }
            if (total_amount > threshold) {
                result.push_back(user.first);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of transactions. This is because we are iterating over all transactions twice: once to update the total amount for each user, and once to check if the total amount is greater than the threshold.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are storing the total amount for each user in a dictionary.
> - **Why these complexities occur:** The time complexity is quadratic because we are iterating over all transactions twice. The space complexity is linear because we are storing the total amount for each user in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a dictionary to store the total amount for each user and update it in a single pass.
- Detailed breakdown: 
  1. Create a dictionary to store the total amount for each user.
  2. Iterate over all transactions and update the total amount for each user.
  3. Check if the total amount for each user is greater than the threshold and if they have at least three transactions.
- Why further optimization is impossible: This approach has a linear time complexity and is therefore optimal.

```cpp
vector<string> invalidTransactions(vector<vector<string>>& transactions, int threshold) {
    unordered_map<string, vector<int>> user_transactions;
    unordered_map<string, int> user_amounts;
    vector<string> result;
    
    for (auto& transaction : transactions) {
        string user = transaction[0];
        int amount = stoi(transaction[2]);
        
        if (user_amounts.find(user) == user_amounts.end()) {
            user_amounts[user] = 0;
            user_transactions[user] = {};
        }
        
        user_amounts[user] += amount;
        user_transactions[user].push_back(amount);
        
        if (user_transactions[user].size() >= 3 && user_amounts[user] > threshold) {
            result.push_back(user);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are iterating over all transactions once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are storing the total amount for each user in a dictionary.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and is therefore the most efficient possible solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
  - Using dictionaries to store and update data.
  - Iterating over all transactions to calculate the total amount for each user.
- Problem-solving patterns identified: 
  - Using a single pass to update the total amount for each user.
  - Checking if the total amount for each user is greater than the threshold and if they have at least three transactions.
- Optimization techniques learned: 
  - Using a dictionary to store the total amount for each user.
  - Iterating over all transactions once to update the total amount for each user.
- Similar problems to practice: 
  - Problems that involve iterating over all transactions to calculate the total amount for each user.

**Mistakes to Avoid:**
- Common implementation errors: 
  - Not checking if the total amount for each user is greater than the threshold.
  - Not checking if the user has at least three transactions.
- Edge cases to watch for: 
  - Empty transactions array.
  - Threshold is zero or negative.
- Performance pitfalls: 
  - Iterating over all transactions twice.
- Testing considerations: 
  - Testing with different inputs to ensure the solution is correct.
  - Testing with edge cases to ensure the solution handles them correctly.