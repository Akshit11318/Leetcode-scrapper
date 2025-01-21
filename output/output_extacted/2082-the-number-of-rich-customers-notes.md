## The Number of Rich Customers
**Problem Link:** https://leetcode.com/problems/the-number-of-rich-customers/description

**Problem Statement:**
- Input format: An array of integers `accounts` representing the amount of money each customer has, and an integer `minWealth` representing the minimum wealth to be considered rich.
- Constraints: `1 <= accounts.length <= 100`, `1 <= accounts[i] <= 100`, and `1 <= minWealth <= 100`.
- Expected output format: The number of customers who are considered rich.
- Key requirements and edge cases to consider: Customers with wealth greater than or equal to `minWealth` are considered rich.
- Example test cases with explanations:
  - `accounts = [1,2,3], minWealth = 3` returns `1` because only one customer has wealth greater than or equal to `3`.
  - `accounts = [3,3,3], minWealth = 3` returns `3` because all customers have wealth greater than or equal to `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the `accounts` array and count the number of customers with wealth greater than or equal to `minWealth`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable `richCustomers` to 0.
  2. Iterate through the `accounts` array.
  3. For each customer, check if their wealth is greater than or equal to `minWealth`.
  4. If it is, increment the `richCustomers` counter.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
int numberOfRichCustomers(vector<int>& accounts, int minWealth) {
    int richCustomers = 0;
    for (int wealth : accounts) {
        if (wealth >= minWealth) {
            richCustomers++;
        }
    }
    return richCustomers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of customers, because we are iterating through the `accounts` array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the `richCustomers` counter.
> - **Why these complexities occur:** The time complexity is linear because we are iterating through the array, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must iterate through the `accounts` array at least once to count the number of rich customers.
- Detailed breakdown of the approach: The same as the brute force approach.
- Proof of optimality: We cannot do better than $O(n)$ time complexity because we must examine each customer's wealth at least once.
- Why further optimization is impossible: The problem requires us to examine each customer's wealth, so we cannot avoid the linear time complexity.

```cpp
int numberOfRichCustomers(vector<int>& accounts, int minWealth) {
    int richCustomers = 0;
    for (int wealth : accounts) {
        if (wealth >= minWealth) {
            richCustomers++;
        }
    }
    return richCustomers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of customers, because we are iterating through the `accounts` array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the `richCustomers` counter.
> - **Optimality proof:** The time complexity is optimal because we must examine each customer's wealth at least once, and the space complexity is optimal because we are not using any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and counting.
- Problem-solving patterns identified: The problem can be solved using a simple iterative approach.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve iterating through an array and counting or summing elements based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect conditional statements, and forgetting to initialize variables.
- Edge cases to watch for: Empty input arrays, arrays with a single element, and arrays with all elements having the same value.
- Performance pitfalls: Using unnecessary data structures or algorithms that have higher time complexity than necessary.
- Testing considerations: Test the function with different input sizes, edge cases, and expected outputs to ensure correctness.