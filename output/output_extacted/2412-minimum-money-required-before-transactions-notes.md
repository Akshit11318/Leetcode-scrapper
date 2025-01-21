## Minimum Money Required Before Transactions
**Problem Link:** https://leetcode.com/problems/minimum-money-required-before-transactions/description

**Problem Statement:**
- Input format and constraints: You are given a 2D integer array `transactions`, where `transactions[i] = [cost_i, cashback_i]`, and an integer `totalCash`. The task is to find the minimum amount of money required to complete all transactions.
- Expected output format: The function should return the minimum money required before transactions.
- Key requirements and edge cases to consider:
  - All transactions must be completed.
  - The cashback from one transaction can be used for subsequent transactions.
- Example test cases with explanations:
  - For `transactions = [[2,1],[5,0],[4,0]]` and `totalCash = 5`, the output is `10`.
  - For `transactions = [[0,0]]` and `totalCash = 1`, the output is `1`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of transactions and calculate the minimum money required.
- Step-by-step breakdown of the solution:
  1. Sort the transactions based on the cashback.
  2. Initialize a variable to store the minimum money required.
  3. Iterate over all possible combinations of transactions.
  4. For each combination, calculate the total cost and cashback.
  5. Update the minimum money required if the current combination requires less money.
- Why this approach comes to mind first: It is a straightforward approach that tries all possibilities.

```cpp
class Solution {
public:
    long long minimumMoney(vector<vector<int>>& transactions, int totalCash) {
        long long minMoney = LLONG_MAX;
        int n = transactions.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            long long money = totalCash;
            long long cost = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    cost += transactions[i][0];
                    money += transactions[i][1];
                }
            }
            minMoney = min(minMoney, max(0LL, cost - money));
        }
        return minMoney;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of transactions. This is because we are trying all possible combinations of transactions.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over all possible combinations of transactions, and for each combination, we are calculating the total cost and cashback.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can always choose to do the transactions with the most cashback first.
- Detailed breakdown of the approach:
  1. Sort the transactions based on the cashback in descending order.
  2. Initialize a variable to store the minimum money required.
  3. Initialize a variable to store the current cash.
  4. Iterate over the sorted transactions.
  5. For each transaction, subtract the cost from the current cash and add the cashback to the current cash.
  6. Update the minimum money required if the current cash is less than 0.
- Proof of optimality: This approach is optimal because we are always choosing the transactions with the most cashback first, which maximizes the amount of cash we have at any given time.

```cpp
class Solution {
public:
    long long minimumMoney(vector<vector<int>>& transactions, int totalCash) {
        long long minMoney = 0;
        long long cash = totalCash;
        sort(transactions.begin(), transactions.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] > b[1];
        });
        for (auto& transaction : transactions) {
            cash -= transaction[0];
            cash += transaction[1];
            minMoney = max(minMoney, -cash);
        }
        return minMoney;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of transactions. This is because we are sorting the transactions based on the cashback.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Optimality proof:** This approach is optimal because we are always choosing the transactions with the most cashback first, which maximizes the amount of cash we have at any given time.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Choosing the best option at each step.
- Optimization techniques learned: Sorting the transactions based on the cashback.
- Similar problems to practice: Other problems that involve choosing the best option at each step.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the transactions correctly.
- Edge cases to watch for: Transactions with zero cost or cashback.
- Performance pitfalls: Not using the optimal approach.
- Testing considerations: Test the solution with different inputs, including edge cases.