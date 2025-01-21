## Friday Purchases II

**Problem Link:** https://leetcode.com/problems/friday-purchases-ii/description

**Problem Statement:**
- Input format and constraints: The problem involves a list of transactions where each transaction is represented by an amount and a day of the week. The goal is to find the maximum amount that can be spent on Fridays, given that the total amount spent on any day cannot exceed the total amount spent on the previous day.
- Expected output format: The maximum amount that can be spent on Fridays.
- Key requirements and edge cases to consider: The problem requires finding the maximum amount that can be spent on Fridays while ensuring that the total amount spent on any day does not exceed the total amount spent on the previous day. This means that the solution must consider the cumulative sum of transactions and ensure that it does not exceed the previous day's total.
- Example test cases with explanations: For example, if the transactions are [(10, "Monday"), (20, "Tuesday"), (30, "Friday")], the maximum amount that can be spent on Fridays is 30, because the total amount spent on Friday (30) does not exceed the total amount spent on the previous day (Tuesday, 20).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of transactions and checking if the total amount spent on any day exceeds the total amount spent on the previous day.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the cumulative sum of transactions for each day.
  2. Iterate over each transaction and add its amount to the corresponding day's cumulative sum.
  3. Check if the total amount spent on any day exceeds the total amount spent on the previous day. If it does, return 0.
  4. Return the maximum amount that can be spent on Fridays.
- Why this approach comes to mind first: The brute force approach is often the first solution that comes to mind because it involves trying all possible combinations of transactions, which seems like a straightforward way to solve the problem.

```cpp
int maxAmount(vector<vector<int>>& transactions) {
    int maxAmount = 0;
    for (int mask = 0; mask < (1 << transactions.size()); mask++) {
        int fridayAmount = 0;
        vector<int> daySums(7, 0);
        bool isValid = true;
        for (int i = 0; i < transactions.size(); i++) {
            if ((mask & (1 << i)) != 0) {
                int day = transactions[i][1];
                daySums[day] += transactions[i][0];
                if (day == 4) { // Friday is the 5th day of the week (0-indexed)
                    fridayAmount += transactions[i][0];
                }
                for (int j = 0; j < 7; j++) {
                    if (j > 0 && daySums[j] > daySums[j - 1]) {
                        isValid = false;
                        break;
                    }
                }
            }
            if (!isValid) break;
        }
        if (isValid) maxAmount = max(maxAmount, fridayAmount);
    }
    return maxAmount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of transactions. This is because we are trying all possible combinations of transactions, which takes $O(2^n)$ time, and for each combination, we are iterating over the transactions, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are storing the cumulative sum of transactions for each day, which takes $O(n)$ space.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of transactions, which is an exponential operation. The space complexity occurs because we are storing the cumulative sum of transactions for each day.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can use dynamic programming to solve this problem. We can create a table where each cell represents the maximum amount that can be spent on Fridays given the transactions up to that point.
- Detailed breakdown of the approach:
  1. Initialize a table to store the maximum amount that can be spent on Fridays given the transactions up to each point.
  2. Iterate over each transaction and update the table accordingly.
  3. Return the maximum amount that can be spent on Fridays.
- Proof of optimality: The dynamic programming approach is optimal because it avoids trying all possible combinations of transactions, which reduces the time complexity from $O(2^n \cdot n)$ to $O(n^2)$.

```cpp
int maxAmount(vector<vector<int>>& transactions) {
    int n = transactions.size();
    vector<vector<int>> dp(n + 1, vector<int>(7, 0));
    for (int i = 1; i <= n; i++) {
        int amount = transactions[i - 1][0];
        int day = transactions[i - 1][1];
        for (int j = 0; j < 7; j++) {
            if (j == day) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][max(0, j - 1)] + amount);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return dp[n][4]; // Friday is the 5th day of the week (0-indexed)
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of transactions. This is because we are iterating over the transactions and updating the table accordingly.
> - **Space Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we are storing the maximum amount that can be spent on Fridays given the transactions up to each point.
> - **Optimality proof:** The dynamic programming approach is optimal because it avoids trying all possible combinations of transactions, which reduces the time complexity from $O(2^n \cdot n)$ to $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit manipulation.
- Problem-solving patterns identified: The problem requires finding the maximum amount that can be spent on Fridays while ensuring that the total amount spent on any day does not exceed the total amount spent on the previous day.
- Optimization techniques learned: Dynamic programming, avoiding unnecessary computations.
- Similar problems to practice: Problems that involve finding the maximum or minimum amount that can be spent or earned given certain constraints.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not initializing variables correctly.
- Edge cases to watch for: The problem requires handling edge cases where the total amount spent on any day exceeds the total amount spent on the previous day.
- Performance pitfalls: The brute force approach can lead to performance pitfalls due to its high time complexity.
- Testing considerations: The solution should be tested with different inputs to ensure that it handles edge cases correctly and produces the correct output.