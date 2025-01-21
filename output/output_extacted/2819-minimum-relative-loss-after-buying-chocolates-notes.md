## Minimum Relative Loss After Buying Chocolates
**Problem Link:** https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/description

**Problem Statement:**
- Input format: `int initialBuy, int finalBuy, vector<int>& chocolates`
- Constraints: $1 \leq \text{initialBuy}, \text{finalBuy} \leq 10^6$, $1 \leq \text{chocolates.size}() \leq 10^5$, $1 \leq \text{chocolates[i]} \leq 10^6$
- Expected output format: Return the minimum relative loss after buying all the chocolates.
- Key requirements and edge cases to consider: The relative loss is calculated as $\frac{\text{initialBuy} - \text{finalBuy}}{\text{initialBuy}}$ after buying all the chocolates. We need to find the minimum relative loss.
- Example test cases with explanations:
  - `initialBuy = 1000, finalBuy = 100, chocolates = [1, 2, 3]`, the relative loss is $\frac{1000 - 100}{1000} = 0.9$ after buying all the chocolates.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total cost of buying all the chocolates with the initial buy price, then calculate the total cost with the final buy price.
- Step-by-step breakdown of the solution:
  1. Calculate the total cost of buying all the chocolates with the initial buy price.
  2. Calculate the total cost of buying all the chocolates with the final buy price.
  3. Calculate the relative loss as $\frac{\text{initialBuy} - \text{finalBuy}}{\text{initialBuy}}$.
- Why this approach comes to mind first: It is the most straightforward way to calculate the relative loss.

```cpp
int calculateRelativeLoss(int initialBuy, int finalBuy, vector<int>& chocolates) {
    int initialTotalCost = 0;
    int finalTotalCost = 0;
    
    for (int chocolate : chocolates) {
        initialTotalCost += initialBuy * chocolate;
        finalTotalCost += finalBuy * chocolate;
    }
    
    return (initialTotalCost - finalTotalCost) / (double) initialTotalCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of chocolates. This is because we iterate over the chocolates once to calculate the total cost with the initial and final buy prices.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the total costs and the relative loss.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the chocolates, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can simplify the calculation of the relative loss by canceling out the common terms.
- Detailed breakdown of the approach:
  1. Calculate the total number of chocolates.
  2. Calculate the relative loss as $\frac{\text{initialBuy} - \text{finalBuy}}{\text{initialBuy}}$.
- Proof of optimality: This approach is optimal because it has the same time complexity as the brute force approach but uses less calculations.
- Why further optimization is impossible: This approach is already optimal because it uses the minimum number of calculations required to calculate the relative loss.

```cpp
int calculateRelativeLoss(int initialBuy, int finalBuy, vector<int>& chocolates) {
    int totalChocolates = 0;
    
    for (int chocolate : chocolates) {
        totalChocolates += chocolate;
    }
    
    return (initialBuy - finalBuy) / (double) initialBuy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of chocolates. This is because we iterate over the chocolates once to calculate the total number of chocolates.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the total number of chocolates and the relative loss.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of calculations required to calculate the relative loss.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simplification of calculations, canceling out common terms.
- Problem-solving patterns identified: Looking for ways to simplify calculations, using mathematical insights to optimize solutions.
- Optimization techniques learned: Canceling out common terms, using mathematical insights to reduce calculations.
- Similar problems to practice: Other problems that involve simplifying calculations, using mathematical insights to optimize solutions.

**Mistakes to Avoid:**
- Common implementation errors: Not canceling out common terms, using unnecessary calculations.
- Edge cases to watch for: Handling cases where the initial buy price is zero, handling cases where the final buy price is zero.
- Performance pitfalls: Using unnecessary calculations, not optimizing solutions.
- Testing considerations: Testing cases where the initial buy price is zero, testing cases where the final buy price is zero, testing cases where the number of chocolates is large.