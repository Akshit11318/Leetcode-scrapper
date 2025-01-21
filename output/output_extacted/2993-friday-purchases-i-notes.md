## Friday Purchases I
**Problem Link:** https://leetcode.com/problems/friday-purchases-i/description

**Problem Statement:**
- Input format and constraints: Given a list of transactions where each transaction is a list of integers, the first integer is the day of the week (1 = Monday, 2 = Tuesday, ..., 7 = Sunday) and the second integer is the amount spent.
- Expected output format: Return the amount spent on Fridays (5) in total.
- Key requirements and edge cases to consider: The list of transactions can be empty, and the day of the week can be outside the range of 1-7.
- Example test cases with explanations:
  - transactions = [[1, 10], [2, 20], [5, 30]]: The amount spent on Fridays is 30.
  - transactions = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70]]: The amount spent on Fridays is 50.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each transaction in the list and check if the day of the week is Friday (5). If it is, add the amount spent to a running total.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `total_spent` to 0.
  2. Iterate over each transaction in the list.
  3. Check if the day of the week is Friday (5). If it is, add the amount spent to `total_spent`.
  4. Return `total_spent` after iterating over all transactions.
- Why this approach comes to mind first: It is a simple and straightforward solution that directly addresses the problem.

```cpp
int totalSpend(vector<vector<int>>& transactions) {
    int total_spent = 0;
    for (const auto& transaction : transactions) {
        if (transaction[0] == 5) {
            total_spent += transaction[1];
        }
    }
    return total_spent;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we iterate over each transaction once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the running total.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each transaction. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must examine each transaction at least once to determine if it occurred on a Friday.
- Detailed breakdown of the approach: The same as the brute force approach.
- Proof of optimality: We cannot do better than $O(n)$ time complexity because we must examine each transaction at least once. The space complexity of $O(1)$ is also optimal because we only need to store a single variable to keep track of the running total.
- Why further optimization is impossible: We have already achieved the best possible time and space complexity for this problem.

```cpp
int totalSpend(vector<vector<int>>& transactions) {
    int total_spent = 0;
    for (const auto& transaction : transactions) {
        if (transaction[0] == 5) {
            total_spent += transaction[1];
        }
    }
    return total_spent;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the running total.
> - **Optimality proof:** The time complexity is optimal because we must examine each transaction at least once. The space complexity is optimal because we only need to store a single variable.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and accumulation.
- Problem-solving patterns identified: Directly addressing the problem by iterating over the input and accumulating the desired values.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve iterating over a list and accumulating values based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the running total, using the wrong index to access the day of the week or amount spent, and not checking for the correct day of the week.
- Edge cases to watch for: An empty list of transactions, transactions with invalid days of the week, and transactions with negative amounts spent.
- Performance pitfalls: Using a data structure with a higher time complexity than necessary, such as a list or map, to store the running total.
- Testing considerations: Test the function with an empty list of transactions, a list with a single transaction, and a list with multiple transactions, including some that occur on Fridays and some that do not.