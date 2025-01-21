## Maximize Amount After Two Days of Conversions
**Problem Link:** https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/description

**Problem Statement:**
- Input: An array of integers `transactions` representing the transactions of the first day and a float `fee` representing the fee per transaction.
- Expected Output: The maximum amount after two days of conversions.
- Key Requirements: 
    1. Each day, we can either sell all of the items in our inventory or buy all the items from the `transactions` array.
    2. If we decide to sell all items in our inventory, we get the sum of all items in our inventory minus the fee.
    3. If we decide to buy all items from the `transactions` array, we add all the items to our inventory.
- Edge Cases: 
    1. If the `transactions` array is empty, return 0.
    2. If the `fee` is 0, we can simply buy all items on the first day and sell them on the second day.

---

### Brute Force Approach
**Explanation:**
- The brute force approach involves simulating all possible scenarios: buying all items on the first day and selling them on the second day, selling all items on the first day and buying them on the second day, buying all items on both days, and selling all items on both days.
- We calculate the total amount after two days for each scenario and return the maximum amount.

```cpp
int maxAmount(vector<int>& transactions, float fee) {
    int n = transactions.size();
    int maxAmount = 0;
    
    // Calculate the sum of all transactions
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += transactions[i];
    }
    
    // Scenario 1: Buy all items on the first day and sell them on the second day
    maxAmount = max(maxAmount, sum - fee);
    
    // Scenario 2: Sell all items on the first day and buy them on the second day
    maxAmount = max(maxAmount, -sum + fee);
    
    // Scenario 3: Buy all items on both days
    maxAmount = max(maxAmount, sum - fee + sum - fee);
    
    // Scenario 4: Sell all items on both days
    maxAmount = max(maxAmount, -sum + fee - sum + fee);
    
    return maxAmount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. We need to calculate the sum of all transactions.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum amount and the sum of transactions.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over all transactions to calculate the sum. The space complexity is constant because we only use a fixed amount of space to store the maximum amount and the sum of transactions.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using dynamic programming to calculate the maximum amount after two days.
- We use two variables: `buy` and `sell`, to represent the maximum amount after buying and selling all items on the first day, respectively.
- We update `buy` and `sell` based on the maximum amount we can get after buying and selling all items on the second day.

```cpp
int maxAmount(vector<int>& transactions, float fee) {
    int n = transactions.size();
    int buy = 0, sell = 0;
    
    for (int i = 0; i < n; i++) {
        int newBuy = max(buy, sell - transactions[i] - fee);
        int newSell = max(sell, buy + transactions[i] - fee);
        buy = newBuy;
        sell = newSell;
    }
    
    return sell;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. We need to iterate over all transactions to update `buy` and `sell`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store `buy` and `sell`.
> - **Optimality proof:** This approach is optimal because we consider all possible scenarios and update `buy` and `sell` based on the maximum amount we can get after buying and selling all items on the second day.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, greedy algorithm.
- Problem-solving patterns identified: using variables to represent the maximum amount after buying and selling all items.
- Optimization techniques learned: using dynamic programming to avoid redundant calculations.

**Mistakes to Avoid:**
- Common implementation errors: not updating `buy` and `sell` correctly.
- Edge cases to watch for: when the `transactions` array is empty or the `fee` is 0.
- Performance pitfalls: using a brute force approach that has a high time complexity.
- Testing considerations: testing the function with different inputs to ensure it returns the correct result.