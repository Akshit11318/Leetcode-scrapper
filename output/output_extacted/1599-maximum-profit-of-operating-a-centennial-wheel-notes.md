## Maximum Profit of Operating a Centennial Wheel
**Problem Link:** https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers representing the `customers` and an integer `finalCustomers` as input. The customers array represents the number of customers that will arrive at each hour. The finalCustomers integer represents the final hour when the centennial wheel will stop operating.
- Expected output format: The expected output is the maximum profit that can be obtained by operating the centennial wheel.
- Key requirements and edge cases to consider: The centennial wheel can only operate for a certain number of hours, and the profit is calculated based on the number of customers that arrive at each hour.
- Example test cases with explanations:
  - Example 1: Input: `customers = [8,3], finalCustomers = 10`, Output: `5`. Explanation: The centennial wheel can operate for 10 hours. At the first hour, 8 customers arrive, and at the second hour, 3 customers arrive. The maximum profit that can be obtained is 5 (by operating the wheel for 5 hours with 1 customer per hour).
  - Example 2: Input: `customers = [10,9,6], finalCustomers = 7`, Output: `7`. Explanation: The centennial wheel can operate for 7 hours. At the first hour, 10 customers arrive, at the second hour, 9 customers arrive, and at the third hour, 6 customers arrive. The maximum profit that can be obtained is 7 (by operating the wheel for 7 hours with 1 customer per hour).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of operating hours and calculating the profit for each combination.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum profit to 0.
  2. Iterate over all possible operating hours (from 1 to `finalCustomers`).
  3. For each operating hour, calculate the profit by summing up the minimum of the current hour's customers and the operating hour.
  4. Update the maximum profit if the current profit is greater than the maximum profit.
- Why this approach comes to mind first: The brute force approach is often the first approach that comes to mind because it involves trying all possible combinations, which guarantees finding the optimal solution.

```cpp
int minOperationsMaxProfit(vector<int>& customers, int finalCustomers) {
    int maxProfit = 0;
    int minOperations = 0;
    for (int i = 1; i <= finalCustomers; i++) {
        int profit = 0;
        int remainingCustomers = 0;
        for (int j = 0; j < customers.size(); j++) {
            remainingCustomers += customers[j];
            int currentProfit = min(remainingCustomers, i);
            profit += currentProfit;
            remainingCustomers -= currentProfit;
        }
        if (profit > maxProfit) {
            maxProfit = profit;
            minOperations = i;
        }
    }
    return minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of customers and $m$ is the final number of customers. The reason for this complexity is that we are iterating over all possible operating hours and calculating the profit for each hour.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum profit and the minimum number of operations.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of operating hours, which results in a nested loop structure. The space complexity is constant because we are only using a fixed amount of space to store the maximum profit and the minimum number of operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can calculate the profit for each hour in a single pass, without trying all possible combinations of operating hours.
- Detailed breakdown of the approach:
  1. Initialize the maximum profit to 0 and the minimum number of operations to 0.
  2. Initialize the current profit to 0 and the remaining customers to 0.
  3. Iterate over the customers array, calculating the profit for each hour and updating the maximum profit and the minimum number of operations as needed.
- Proof of optimality: The optimal approach is optimal because it calculates the profit for each hour in a single pass, without trying all possible combinations of operating hours. This results in a significant reduction in time complexity.
- Why further optimization is impossible: Further optimization is impossible because we must iterate over the customers array at least once to calculate the profit for each hour.

```cpp
int minOperationsMaxProfit(vector<int>& customers, int finalCustomers) {
    int maxProfit = 0;
    int minOperations = 0;
    int currentProfit = 0;
    int remainingCustomers = 0;
    for (int i = 0; i < finalCustomers; i++) {
        if (i < customers.size()) {
            remainingCustomers += customers[i];
        }
        int currentHourProfit = min(remainingCustomers, 1);
        currentProfit += currentHourProfit;
        remainingCustomers -= currentHourProfit;
        if (currentProfit > maxProfit) {
            maxProfit = currentProfit;
            minOperations = i + 1;
        }
    }
    return minOperations == 0 ? -1 : minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the final number of customers. The reason for this complexity is that we are iterating over the customers array only once.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum profit and the minimum number of operations.
> - **Optimality proof:** The optimal approach is optimal because it calculates the profit for each hour in a single pass, without trying all possible combinations of operating hours. This results in a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of dynamic programming and the importance of optimizing algorithms to reduce time complexity.
- Problem-solving patterns identified: The problem identifies the pattern of calculating the profit for each hour in a single pass, without trying all possible combinations of operating hours.
- Optimization techniques learned: The problem teaches the technique of optimizing algorithms by reducing the number of iterations and using dynamic programming.
- Similar problems to practice: Similar problems to practice include other dynamic programming problems, such as the `Coin Change` problem and the `Knapsack` problem.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include using a brute force approach instead of an optimal approach, and not handling edge cases correctly.
- Edge cases to watch for: Edge cases to watch for include the case where the final number of customers is 0, and the case where the customers array is empty.
- Performance pitfalls: Performance pitfalls include using a brute force approach, which can result in a significant increase in time complexity.
- Testing considerations: Testing considerations include testing the algorithm with different inputs, including edge cases, to ensure that it produces the correct output.