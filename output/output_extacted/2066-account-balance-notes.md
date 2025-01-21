## Account Balance
**Problem Link:** https://leetcode.com/problems/account-balance/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers representing the account balances.
- Expected output format: The output should be an integer representing the total balance of all accounts.
- Key requirements and edge cases to consider: The input array may be empty, and the balances can be negative or positive.
- Example test cases with explanations: For example, if the input is `[1, 2, 3]`, the output should be `6`. If the input is `[-1, -2, -3]`, the output should be `-6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to find the total balance is to add up all the balances in the array.
- Step-by-step breakdown of the solution: 
  1. Initialize a variable `totalBalance` to 0.
  2. Iterate through each balance in the array.
  3. Add the current balance to `totalBalance`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand.

```cpp
int balance(vector<int>& accounts) {
    int totalBalance = 0;
    for (int balance : accounts) {
        totalBalance += balance;
    }
    return totalBalance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of accounts. This is because we iterate through each account once.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array. This is because we only use a constant amount of space to store the `totalBalance`.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the array once, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we must iterate through each account at least once to find the total balance.
- Detailed breakdown of the approach: 
  1. Initialize a variable `totalBalance` to 0.
  2. Iterate through each balance in the array.
  3. Add the current balance to `totalBalance`.
- Proof of optimality: This solution is optimal because we must iterate through each account at least once, and we use a constant amount of space.
- Why further optimization is impossible: Further optimization is impossible because we must iterate through each account at least once.

```cpp
int balance(vector<int>& accounts) {
    int totalBalance = 0;
    for (int balance : accounts) {
        totalBalance += balance;
    }
    return totalBalance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of accounts.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array.
> - **Optimality proof:** This solution is optimal because we must iterate through each account at least once, and we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration and accumulation.
- Problem-solving patterns identified: The need to iterate through each element in an array to find a total or sum.
- Optimization techniques learned: Using a constant amount of space to reduce the space complexity.
- Similar problems to practice: Other problems that involve iterating through an array to find a total or sum.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `totalBalance` variable or using the wrong data type.
- Edge cases to watch for: An empty input array or an array with negative or positive balances.
- Performance pitfalls: Using a data structure that has a high time complexity for insertion or deletion, such as a `std::list`.
- Testing considerations: Testing the function with different input arrays, including an empty array and arrays with negative or positive balances.