## Maximum Number that Sum of the Prices is Less than or Equal to K
**Problem Link:** https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/description

**Problem Statement:**
- Input format: `prices` is an array of integers representing the prices of items, and `k` is an integer representing the maximum sum of prices.
- Constraints: $1 \leq prices.length \leq 100$, $1 \leq prices[i] \leq 100$, $1 \leq k \leq 1000$.
- Expected output format: The maximum number of items that can be bought such that the sum of their prices is less than or equal to `k`.
- Key requirements and edge cases to consider:
  - Handling cases where `k` is less than the minimum price in `prices`.
  - Handling cases where `k` is greater than or equal to the sum of all prices in `prices`.
- Example test cases with explanations:
  - `prices = [1,2,3], k = 4` should return `3` because we can buy all items with a total price of $1+2+3=6$, but we can only spend up to $4$, so we cannot buy all items. However, we can buy the first two items with a total price of $1+2=3$, which is less than $4$. This leaves us with the option to buy one more item of price $1$, thus achieving a total of $3$ items.
  - `prices = [1,2,3], k = 2` should return `2` because we can buy the first two items with a total price of $1+1=2$, which is exactly equal to $2$.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of items and checking if their sum is less than or equal to `k`.
- Step-by-step breakdown:
  1. Generate all possible subsets of the `prices` array.
  2. For each subset, calculate the sum of its prices.
  3. If the sum is less than or equal to `k`, update the maximum count of items if necessary.
- Why this approach comes to mind first: It's a straightforward way to ensure we don't miss any possible combination of items.

```cpp
class Solution {
public:
    int maxNumber(vector<int>& prices, int k) {
        int maxCount = 0;
        int n = prices.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            int count = 0;
            int sum = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    count++;
                    sum += prices[i];
                }
            }
            if (sum <= k) {
                maxCount = max(maxCount, count);
            }
        }
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of items. This is because we generate all possible subsets (which is $2^n$) and for each subset, we calculate the sum of its prices (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `maxCount`, `n`, `mask`, `count`, and `sum` variables.
> - **Why these complexities occur:** The time complexity is high because we are considering all possible subsets, and for each subset, we perform a linear scan to calculate the sum of its prices. The space complexity is low because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to select the items with the lowest prices first, as this maximizes the number of items we can buy.
- Detailed breakdown of the approach:
  1. Sort the `prices` array in ascending order.
  2. Initialize a variable `count` to keep track of the number of items bought.
  3. Initialize a variable `sum` to keep track of the total price of the items bought.
  4. Iterate through the sorted `prices` array, and for each price, check if buying the item would exceed the budget `k`.
  5. If buying the item would not exceed the budget, increment `count` and update `sum`.
- Proof of optimality: This approach is optimal because it ensures that we are always buying the item with the lowest price that fits within our remaining budget, thus maximizing the number of items we can buy.

```cpp
class Solution {
public:
    int maxNumber(vector<int>& prices, int k) {
        sort(prices.begin(), prices.end());
        int count = 0;
        int sum = 0;
        for (int price : prices) {
            if (sum + price <= k) {
                count++;
                sum += price;
            } else {
                break;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of items. This is because we sort the `prices` array (which takes $O(n \log n)$ time) and then iterate through it once (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `count` and `sum` variables.
> - **Optimality proof:** This approach is optimal because it ensures that we are always buying the item with the lowest price that fits within our remaining budget, thus maximizing the number of items we can buy.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, sorting.
- Problem-solving patterns identified: Maximization problems, budget constraints.
- Optimization techniques learned: Greedy selection, sorting for efficient iteration.
- Similar problems to practice: Other maximization problems with budget constraints.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for budget exceedance before buying an item.
- Edge cases to watch for: Handling cases where `k` is less than the minimum price in `prices`.
- Performance pitfalls: Using inefficient algorithms (e.g., brute force) for large inputs.
- Testing considerations: Test cases with varying `k` values and `prices` arrays to ensure correctness.