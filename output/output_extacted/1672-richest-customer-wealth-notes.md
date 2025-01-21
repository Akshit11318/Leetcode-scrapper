## Richest Customer Wealth
**Problem Link:** https://leetcode.com/problems/richest-customer-wealth/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `accounts` where `accounts[i]` is a list of integers representing the wealth of the `i-th` customer. The constraint is that `1 <= accounts.length <= 10^5` and `1 <= accounts[i].length <= 10^5`.
- Expected output format: The output should be an integer representing the maximum wealth of the customers.
- Key requirements and edge cases to consider: The function should handle empty input, single customer, and multiple customers with different wealth.
- Example test cases with explanations:
  - `accounts = [[1,2,3],[3,2,1]]`: The output should be `6` because the first customer has a total wealth of `1+2+3 = 6`, which is the maximum.
  - `accounts = [[1,5],[7,3],[3,5]]`: The output should be `10` because the customer with the maximum wealth is the first one with a total wealth of `1+5 = 6`, but the second customer has a total wealth of `7+3 = 10`, which is the maximum.
  - `accounts = [[2,8,7],[7,1,3],[1,9,5]]`: The output should be `17` because the customer with the maximum wealth is the third one with a total wealth of `1+9+5 = 15`, but the first customer has a total wealth of `2+8+7 = 17`, which is the maximum.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each customer's accounts and calculating their total wealth.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `maxWealth` to store the maximum wealth found so far.
  2. Iterate over each customer's accounts.
  3. For each customer, calculate their total wealth by summing up all their accounts.
  4. Update `maxWealth` if the current customer's wealth is greater than the maximum wealth found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first thought.

```cpp
int maximumWealth(vector<vector<int>>& accounts) {
    int maxWealth = 0;
    for (int i = 0; i < accounts.size(); i++) {
        int customerWealth = 0;
        for (int j = 0; j < accounts[i].size(); j++) {
            customerWealth += accounts[i][j];
        }
        maxWealth = max(maxWealth, customerWealth);
    }
    return maxWealth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m*n)$, where $m$ is the number of customers and $n$ is the average number of accounts per customer. This is because we are iterating over each customer's accounts.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input. We are only using a constant amount of space to store the maximum wealth.
> - **Why these complexities occur:** The time complexity is $O(m*n)$ because we are iterating over each customer's accounts, and the space complexity is $O(1)$ because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we need to iterate over each customer's accounts to calculate their total wealth.
- Detailed breakdown of the approach:
  1. Initialize a variable `maxWealth` to store the maximum wealth found so far.
  2. Iterate over each customer's accounts.
  3. For each customer, calculate their total wealth by summing up all their accounts using the `accumulate` function.
  4. Update `maxWealth` if the current customer's wealth is greater than the maximum wealth found so far.
- Proof of optimality: This solution is optimal because we need to iterate over each customer's accounts to calculate their total wealth, and we are doing this in a single pass.

```cpp
int maximumWealth(vector<vector<int>>& accounts) {
    int maxWealth = 0;
    for (auto& customer : accounts) {
        int customerWealth = accumulate(customer.begin(), customer.end(), 0);
        maxWealth = max(maxWealth, customerWealth);
    }
    return maxWealth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m*n)$, where $m$ is the number of customers and $n$ is the average number of accounts per customer. This is because we are iterating over each customer's accounts.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input. We are only using a constant amount of space to store the maximum wealth.
> - **Optimality proof:** This solution is optimal because we need to iterate over each customer's accounts to calculate their total wealth, and we are doing this in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, accumulation, and comparison.
- Problem-solving patterns identified: The need to iterate over each customer's accounts to calculate their total wealth.
- Optimization techniques learned: Using the `accumulate` function to calculate the sum of a customer's accounts.
- Similar problems to practice: Problems that involve iterating over a 2D array and calculating a sum or maximum value.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `maxWealth` variable, or using the wrong data type for the `maxWealth` variable.
- Edge cases to watch for: Empty input, single customer, and multiple customers with different wealth.
- Performance pitfalls: Using a nested loop to calculate the sum of a customer's accounts, which can lead to a time complexity of $O(m*n^2)$.
- Testing considerations: Testing the function with different inputs, including empty input, single customer, and multiple customers with different wealth.