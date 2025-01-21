## Maximum Transaction Each Day

**Problem Link:** https://leetcode.com/problems/maximum-transaction-each-day/description

**Problem Statement:**
- Input: A 2D array `transactions` where each inner array contains two integers, the day and the amount of the transaction.
- Constraints: The number of transactions is at most $10^5$, and each transaction occurs on a day between $1$ and $10^5$.
- Expected Output: The maximum number of transactions that can be performed each day.
- Key Requirements: To maximize the number of transactions each day, the goal is to find the maximum number of days on which a transaction can be performed without violating the rule that no more than one transaction can be performed on the same day.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to sort the transactions based on the day and then iterate through the sorted transactions to find the maximum number of transactions that can be performed each day.
- Step-by-step breakdown of the solution:
  1. Sort the transactions based on the day.
  2. Initialize a set to store the days on which a transaction has been performed.
  3. Iterate through the sorted transactions and for each transaction, check if the day is already in the set. If not, add the day to the set.
  4. The size of the set represents the maximum number of transactions that can be performed each day.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

int maxTransactions(std::vector<std::vector<int>>& transactions) {
    // Sort the transactions based on the day
    std::sort(transactions.begin(), transactions.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });

    // Initialize a set to store the days on which a transaction has been performed
    std::set<int> days;

    // Iterate through the sorted transactions
    for (const auto& transaction : transactions) {
        // Check if the day is already in the set
        if (days.find(transaction[0]) == days.end()) {
            // Add the day to the set
            days.insert(transaction[0]);
        }
    }

    // The size of the set represents the maximum number of transactions that can be performed each day
    return days.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of transactions, where $n$ is the number of transactions.
> - **Space Complexity:** $O(n)$ for storing the days in the set.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to the storage of unique days in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by simply counting the number of unique days in the transactions, as the maximum number of transactions that can be performed each day is equal to the number of unique days.
- Detailed breakdown of the approach:
  1. Use a set to store the unique days.
  2. Iterate through the transactions and add each day to the set.
  3. The size of the set represents the maximum number of transactions that can be performed each day.

```cpp
#include <iostream>
#include <vector>
#include <set>

int maxTransactions(std::vector<std::vector<int>>& transactions) {
    // Initialize a set to store the unique days
    std::set<int> days;

    // Iterate through the transactions
    for (const auto& transaction : transactions) {
        // Add the day to the set
        days.insert(transaction[0]);
    }

    // The size of the set represents the maximum number of transactions that can be performed each day
    return days.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions, as we are iterating through the transactions once.
> - **Space Complexity:** $O(n)$ for storing the unique days in the set.
> - **Optimality proof:** This is the optimal solution as we are only iterating through the transactions once and storing the unique days in a set, which has an average time complexity of $O(1)$ for insertion and search operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to store unique elements and iterating through a collection to count unique elements.
- Problem-solving patterns identified: Finding the maximum number of transactions that can be performed each day by counting the number of unique days.
- Optimization techniques learned: Using a set to store unique days instead of sorting the transactions.

**Mistakes to Avoid:**
- Common implementation errors: Not using a set to store unique days, which can lead to incorrect results.
- Edge cases to watch for: Empty transactions list, transactions list with duplicate days.
- Performance pitfalls: Using a sorting algorithm with a high time complexity, such as bubble sort or insertion sort, which can lead to slow performance for large inputs.
- Testing considerations: Test the function with different inputs, including empty transactions list, transactions list with duplicate days, and transactions list with unique days.