## Customers With Maximum Number of Transactions On Consecutive Days

**Problem Link:** https://leetcode.com/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/description

**Problem Statement:**
- Input format and constraints: The input is a table `Transactions` with columns `id`, `name`, `day`, `amount`, and `type`. The task is to find all customers who have the maximum number of transactions on consecutive days.
- Expected output format: The output should be a table with the `name` of the customers who have the maximum number of transactions on consecutive days.
- Key requirements and edge cases to consider: 
    - A customer can have multiple transactions on the same day, which counts as one day of transactions.
    - The number of consecutive days with transactions should be maximized.
- Example test cases with explanations:
    - Example 1:
        - Input: `Transactions` table with data.
        - Output: The `name` of the customers with the maximum number of transactions on consecutive days.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through each customer's transactions, sorting them by day, and then counting the number of consecutive days with transactions.
- Step-by-step breakdown of the solution:
    1. Group the transactions by customer `name`.
    2. For each customer, sort the transactions by `day`.
    3. Iterate through the sorted transactions and count the number of consecutive days with transactions.
    4. Keep track of the maximum number of consecutive days with transactions for each customer.
- Why this approach comes to mind first: The brute force approach is straightforward and involves iterating through each customer's transactions, which makes it easy to understand and implement.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

struct Transaction {
    int id;
    std::string name;
    int day;
    int amount;
    std::string type;
};

std::vector<std::string> customersWithMaximumNumberOfTransactionsOnConsecutiveDays(std::vector<Transaction>& transactions) {
    std::map<std::string, std::vector<int>> customerTransactions;
    
    // Group transactions by customer
    for (const auto& transaction : transactions) {
        customerTransactions[transaction.name].push_back(transaction.day);
    }
    
    std::map<std::string, int> maxConsecutiveDays;
    
    // Count consecutive days for each customer
    for (const auto& pair : customerTransactions) {
        std::vector<int> days = pair.second;
        std::sort(days.begin(), days.end());
        
        int maxDays = 0;
        int currentDays = 1;
        
        for (int i = 1; i < days.size(); ++i) {
            if (days[i] - days[i - 1] == 1) {
                currentDays++;
            } else {
                maxDays = std::max(maxDays, currentDays);
                currentDays = 1;
            }
        }
        
        maxDays = std::max(maxDays, currentDays);
        maxConsecutiveDays[pair.first] = maxDays;
    }
    
    int maxConsecutiveDaysOverall = 0;
    for (const auto& pair : maxConsecutiveDays) {
        maxConsecutiveDaysOverall = std::max(maxConsecutiveDaysOverall, pair.second);
    }
    
    std::vector<std::string> result;
    for (const auto& pair : maxConsecutiveDays) {
        if (pair.second == maxConsecutiveDaysOverall) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of transactions. This is because we are sorting the transactions for each customer.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are storing the transactions in a map.
> - **Why these complexities occur:** The time complexity occurs because we are sorting the transactions for each customer, and the space complexity occurs because we are storing the transactions in a map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `map` to store the transactions for each customer and a `set` to store the days with transactions. This allows us to efficiently count the number of consecutive days with transactions.
- Detailed breakdown of the approach:
    1. Create a `map` to store the transactions for each customer.
    2. Create a `set` to store the days with transactions for each customer.
    3. Iterate through the transactions and update the `map` and `set`.
    4. For each customer, count the number of consecutive days with transactions by iterating through the `set`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the transactions and uses efficient data structures to store and count the transactions.
- Why further optimization is impossible: This approach is already optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

struct Transaction {
    int id;
    std::string name;
    int day;
    int amount;
    std::string type;
};

std::vector<std::string> customersWithMaximumNumberOfTransactionsOnConsecutiveDays(std::vector<Transaction>& transactions) {
    std::map<std::string, std::set<int>> customerTransactions;
    
    // Group transactions by customer and count consecutive days
    for (const auto& transaction : transactions) {
        customerTransactions[transaction.name].insert(transaction.day);
    }
    
    std::map<std::string, int> maxConsecutiveDays;
    
    for (const auto& pair : customerTransactions) {
        std::set<int> days = pair.second;
        
        int maxDays = 0;
        int currentDays = 1;
        
        std::set<int>::iterator it = days.begin();
        std::set<int>::iterator nextIt = ++days.begin();
        
        for (; nextIt != days.end(); ++it, ++nextIt) {
            if (*nextIt - *it == 1) {
                currentDays++;
            } else {
                maxDays = std::max(maxDays, currentDays);
                currentDays = 1;
            }
        }
        
        maxDays = std::max(maxDays, currentDays);
        maxConsecutiveDays[pair.first] = maxDays;
    }
    
    int maxConsecutiveDaysOverall = 0;
    for (const auto& pair : maxConsecutiveDays) {
        maxConsecutiveDaysOverall = std::max(maxConsecutiveDaysOverall, pair.second);
    }
    
    std::vector<std::string> result;
    for (const auto& pair : maxConsecutiveDays) {
        if (pair.second == maxConsecutiveDaysOverall) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of transactions. This is because we are using a `set` to store the days with transactions.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are storing the transactions in a `map`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the transactions and uses efficient data structures to store and count the transactions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - Using a `map` to group transactions by customer.
    - Using a `set` to store the days with transactions.
    - Counting the number of consecutive days with transactions.
- Problem-solving patterns identified: 
    - Grouping data by a key (customer name).
    - Counting consecutive occurrences of a value (days with transactions).
- Optimization techniques learned: 
    - Using efficient data structures (maps and sets) to store and count transactions.
    - Minimizing the number of passes through the data.

**Mistakes to Avoid:**
- Common implementation errors: 
    - Not checking for edge cases (e.g., empty input).
    - Not using efficient data structures.
- Edge cases to watch for: 
    - Empty input.
    - Duplicate transactions.
- Performance pitfalls: 
    - Using inefficient data structures (e.g., vectors instead of sets).
    - Making unnecessary passes through the data.
- Testing considerations: 
    - Testing with different input sizes and edge cases.
    - Verifying the correctness of the output.