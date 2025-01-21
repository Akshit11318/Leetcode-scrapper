## Invalid Transactions
**Problem Link:** https://leetcode.com/problems/invalid-transactions/description

**Problem Statement:**
- Input format: A list of strings `transactions` where each string represents a transaction in the format "city,name,time,amount".
- Constraints: 
  - $1 \leq \text{number of transactions} \leq 10^5$
  - Each transaction is a string of length at most $100$
- Expected output format: A list of invalid transactions
- Key requirements and edge cases to consider:
  - A transaction is invalid if the city of the transaction is different from the city of another transaction on the same day by the same person and the amount exceeds $1000.
  - A transaction is also invalid if there are two transactions on the same day by the same person in different cities.
- Example test cases with explanations:
  - For example, if we have transactions "NewYork,John,10,100" and "NewYork,John,20,1000", the second transaction is invalid because the amount exceeds $1000.
  - If we have transactions "NewYork,John,10,100" and "LosAngeles,John,10,1000", both transactions are invalid because they are on the same day by the same person in different cities.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate through each transaction and compare it with every other transaction to check for invalid conditions.
- Step-by-step breakdown of the solution:
  1. Parse each transaction to extract the city, name, time, and amount.
  2. Compare each transaction with every other transaction.
  3. Check if the cities are different and the names are the same and the time is the same and the amount exceeds $1000, or if the cities are different and the names are the same and the time is the same.
  4. If an invalid condition is found, mark the transaction as invalid.
- Why this approach comes to mind first: This approach is the most intuitive because it directly addresses the problem statement by comparing each transaction with every other transaction.

```cpp
vector<string> invalidTransactions(vector<string>& transactions) {
    vector<string> invalid;
    for (int i = 0; i < transactions.size(); i++) {
        string city1, name1, time1, amount1;
        stringstream ss1(transactions[i]);
        string token;
        getline(ss1, city1, ',');
        getline(ss1, name1, ',');
        getline(ss1, time1, ',');
        getline(ss1, amount1, ',');
        bool isValid = true;
        for (int j = 0; j < transactions.size(); j++) {
            if (i == j) continue;
            string city2, name2, time2, amount2;
            stringstream ss2(transactions[j]);
            getline(ss2, city2, ',');
            getline(ss2, name2, ',');
            getline(ss2, time2, ',');
            getline(ss2, amount2, ',');
            if (city1 != city2 && name1 == name2 && abs(stoi(time1) - stoi(time2)) <= 60 && (stoi(amount1) > 1000 || stoi(amount2) > 1000)) {
                isValid = false;
                break;
            }
            if (city1 != city2 && name1 == name2 && abs(stoi(time1) - stoi(time2)) <= 60) {
                isValid = false;
                break;
            }
        }
        if (!isValid) {
            invalid.push_back(transactions[i]);
        }
    }
    return invalid;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of transactions, because we are comparing each transaction with every other transaction.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions, because we are storing the invalid transactions in a separate vector.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to compare each transaction with every other transaction. The space complexity occurs because we are storing the invalid transactions in a separate vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each transaction with every other transaction, we can use a hashmap to store the transactions by name and time.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the transactions by name and time.
  2. Iterate through each transaction and add it to the hashmap.
  3. For each transaction, check if there are any other transactions in the hashmap with the same name and time but different city.
  4. If such a transaction is found, mark both transactions as invalid.
- Why further optimization is impossible: This approach is optimal because it reduces the time complexity from $O(n^2)$ to $O(n)$ by using a hashmap to store the transactions.

```cpp
vector<string> invalidTransactions(vector<string>& transactions) {
    vector<string> invalid;
    unordered_map<string, vector<string>> map;
    for (string transaction : transactions) {
        string city, name, time, amount;
        stringstream ss(transaction);
        string token;
        getline(ss, city, ',');
        getline(ss, name, ',');
        getline(ss, time, ',');
        getline(ss, amount, ',');
        map[name + "," + time].push_back(transaction);
    }
    for (auto& pair : map) {
        vector<string> transactions = pair.second;
        unordered_set<string> cities;
        for (string transaction : transactions) {
            string city, name, time, amount;
            stringstream ss(transaction);
            string token;
            getline(ss, city, ',');
            getline(ss, name, ',');
            getline(ss, time, ',');
            getline(ss, amount, ',');
            cities.insert(city);
            if (stoi(amount) > 1000) {
                invalid.push_back(transaction);
            }
        }
        if (cities.size() > 1) {
            for (string transaction : transactions) {
                invalid.push_back(transaction);
            }
        }
    }
    return invalid;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions, because we are iterating through each transaction once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions, because we are storing the transactions in a hashmap.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^2)$ to $O(n)$ by using a hashmap to store the transactions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to reduce time complexity.
- Problem-solving patterns identified: Using a hashmap to store transactions by name and time.
- Optimization techniques learned: Reducing time complexity by using a hashmap.
- Similar problems to practice: Problems that involve reducing time complexity by using a hashmap.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly.
- Edge cases to watch for: Transactions with the same name and time but different city.
- Performance pitfalls: Not using a hashmap to reduce time complexity.
- Testing considerations: Testing the solution with different inputs to ensure correctness.