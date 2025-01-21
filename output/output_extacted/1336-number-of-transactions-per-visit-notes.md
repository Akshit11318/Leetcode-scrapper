## Number of Transactions Per Visit

**Problem Link:** https://leetcode.com/problems/number-of-transactions-per-visit/description

**Problem Statement:**
- Input format and constraints: The problem takes as input a list of `transactions` where each transaction is a list of three integers: `[transaction_id, customer_id, amount]`, and a list of `visits` where each visit is a list of two integers: `[visit_id, customer_id]`.
- Expected output format: The output should be a list of integers where each integer represents the number of transactions for each visit.
- Key requirements and edge cases to consider:
  - A visit is considered to have a transaction if the customer's visit and transaction occur on the same day.
  - Each transaction should only be counted once for a customer, even if there are multiple transactions for the same customer on the same day.
- Example test cases with explanations:
  - Example 1: 
    - Input: `transactions = [[1,1,10],[2,1,20],[3,2,30]]`, `visits = [[1,1],[2,1],[3,2]]`
    - Output: `[2,1,0]`
    - Explanation: The customer with `customer_id = 1` had two transactions on the day of visit with `visit_id = 1`, and one transaction on the day of visit with `visit_id = 2`. The customer with `customer_id = 2` had one transaction on the day of visit with `visit_id = 3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each visit and check each transaction to see if the customer and visit match, then count the number of transactions for each visit.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the number of transactions for each visit.
  2. Iterate over each visit.
  3. For each visit, iterate over each transaction.
  4. If the customer of the visit and the customer of the transaction match, increment the count of transactions for the visit.
  5. Return the list of transaction counts for each visit.
- Why this approach comes to mind first: It's a straightforward approach that checks each visit against each transaction.

```cpp
vector<int> getTransactionCount(vector<vector<int>>& transactions, vector<vector<int>>& visits) {
    vector<int> result(visits.size(), 0);
    for (int i = 0; i < visits.size(); i++) {
        for (int j = 0; j < transactions.size(); j++) {
            if (visits[i][1] == transactions[j][1]) {
                result[i]++;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of visits and $m$ is the number of transactions.
> - **Space Complexity:** $O(n)$ for the result vector.
> - **Why these complexities occur:** The brute force approach checks each visit against each transaction, resulting in a time complexity of $O(n \times m)$. The space complexity is $O(n)$ because we need to store the result for each visit.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dictionary to store the transactions for each customer, then iterate over the visits and count the number of transactions for each visit.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the transactions for each customer.
  2. Iterate over each transaction and add it to the dictionary.
  3. Create a result vector to store the number of transactions for each visit.
  4. Iterate over each visit and count the number of transactions for the customer.
  5. Return the result vector.
- Proof of optimality: This approach has a time complexity of $O(n + m)$ because we only need to iterate over the transactions and visits once.

```cpp
vector<int> getTransactionCount(vector<vector<int>>& transactions, vector<vector<int>>& visits) {
    unordered_map<int, unordered_set<int>> customerTransactions;
    for (auto& transaction : transactions) {
        customerTransactions[transaction[1]].insert(transaction[0]);
    }
    vector<int> result;
    for (auto& visit : visits) {
        if (customerTransactions.find(visit[1]) != customerTransactions.end()) {
            result.push_back(customerTransactions[visit[1]].size());
        } else {
            result.push_back(0);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of visits and $m$ is the number of transactions.
> - **Space Complexity:** $O(m)$ for the dictionary of transactions.
> - **Optimality proof:** This approach has a time complexity of $O(n + m)$ because we only need to iterate over the transactions and visits once. The space complexity is $O(m)$ because we need to store the transactions for each customer.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using dictionaries to store and count transactions for each customer.
- Problem-solving patterns identified: Iterating over visits and transactions to count the number of transactions for each visit.
- Optimization techniques learned: Using dictionaries to reduce the time complexity from $O(n \times m)$ to $O(n + m)$.
- Similar problems to practice: Problems that involve counting and iterating over data, such as counting the number of occurrences of each word in a text.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when a customer has no transactions.
- Edge cases to watch for: When a customer has no transactions, or when a visit has no matching transactions.
- Performance pitfalls: Using a brute force approach that checks each visit against each transaction, resulting in a time complexity of $O(n \times m)$.
- Testing considerations: Testing the function with different inputs, such as different numbers of visits and transactions, and checking for edge cases.