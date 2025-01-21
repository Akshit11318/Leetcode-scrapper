## Calculate Money in LeetCode Bank
**Problem Link:** https://leetcode.com/problems/calculate-money-in-leetcode-bank/description

**Problem Statement:**
- Input format: `initialMoney`, `initialCoins`, `bills` array, `coins` array
- Constraints: `1 <= bills.length, coins.length <= 10^5`, `0 <= bills[i], coins[i] <= 10^5`
- Expected output format: The total amount of money after all transactions
- Key requirements and edge cases to consider: Handle cases where `initialMoney` and `initialCoins` are 0, and where the length of `bills` and `coins` arrays are different
- Example test cases with explanations:
  - Example 1: `initialMoney = 100, initialCoins = 100, bills = [5, 10, 20], coins = [1, 2, 3]`
  - Example 2: `initialMoney = 0, initialCoins = 0, bills = [1], coins = [1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each bill and coin, calculate the total money after each transaction
- Step-by-step breakdown of the solution:
  1. Initialize `totalMoney` with `initialMoney`
  2. Iterate through each bill in `bills` array, add the bill amount to `totalMoney`
  3. Iterate through each coin in `coins` array, add the coin amount to `totalMoney`
- Why this approach comes to mind first: Simple and straightforward, but may not be efficient for large inputs

```cpp
int calculateMoney(int initialMoney, int initialCoins, vector<int>& bills, vector<int>& coins) {
    int totalMoney = initialMoney;
    for (int bill : bills) {
        totalMoney += bill;
    }
    for (int coin : coins) {
        totalMoney += coin;
    }
    return totalMoney;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `bills` and `coins` arrays respectively
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `totalMoney` variable
> - **Why these complexities occur:** The time complexity is linear because we iterate through each bill and coin once, and the space complexity is constant because we only use a fixed amount of space to store the result

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the total money by summing up all the bills and coins in a single pass
- Detailed breakdown of the approach:
  1. Initialize `totalMoney` with `initialMoney`
  2. Use a single loop to iterate through both `bills` and `coins` arrays, adding each element to `totalMoney`
- Proof of optimality: This approach has the same time complexity as the brute force approach, but is more efficient in practice because it uses a single loop instead of two separate loops
- Why further optimization is impossible: This approach has the minimum possible time complexity because we must iterate through each bill and coin at least once to calculate the total money

```cpp
int calculateMoney(int initialMoney, int initialCoins, vector<int>& bills, vector<int>& coins) {
    int totalMoney = initialMoney;
    for (int i = 0; i < max(bills.size(), coins.size()); i++) {
        if (i < bills.size()) {
            totalMoney += bills[i];
        }
        if (i < coins.size()) {
            totalMoney += coins[i];
        }
    }
    return totalMoney;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `bills` and `coins` arrays respectively
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `totalMoney` variable
> - **Optimality proof:** This approach is optimal because it has the minimum possible time complexity and uses a single loop to iterate through both arrays

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, summation
- Problem-solving patterns identified: Using a single loop to iterate through multiple arrays
- Optimization techniques learned: Reducing the number of loops to improve efficiency
- Similar problems to practice: Other problems that involve iterating through arrays and calculating sums or products

**Mistakes to Avoid:**
- Common implementation errors: Using separate loops for each array, forgetting to initialize the `totalMoney` variable
- Edge cases to watch for: Handling cases where `initialMoney` and `initialCoins` are 0, and where the length of `bills` and `coins` arrays are different
- Performance pitfalls: Using inefficient algorithms or data structures that have high time or space complexities
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly