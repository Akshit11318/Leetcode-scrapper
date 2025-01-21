## Maximum Ice Cream Bars
**Problem Link:** https://leetcode.com/problems/maximum-ice-cream-bars/description

**Problem Statement:**
- Input: An array of integers `costs` representing the costs of ice cream bars and an integer `coins` representing the total amount of money.
- Constraints: `1 <= costs.length <= 1000`, `1 <= costs[i] <= 10^5`, `1 <= coins <= 10^5`.
- Expected Output: The maximum number of ice cream bars that can be bought with the given amount of money.
- Key Requirements: The solution should find the optimal way to spend the money to buy the maximum number of ice cream bars.
- Example Test Cases:
  - `costs = [1,3,2,4,1]`, `coins = 7`, Output: `4` (Buy ice cream bars with costs 1, 1, 2, and 3).
  - `costs = [10,6,8,7,7,8]`, `coins = 50`, Output: `0` (No ice cream bars can be bought with the given amount of money).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of buying ice cream bars and check which combination gives the maximum number of bars.
- This approach involves using recursion or bit manipulation to generate all possible combinations.
- However, this approach is not efficient for large inputs due to its exponential time complexity.

```cpp
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int maxBars = 0;
        int n = costs.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            int currentBars = 0;
            int currentCost = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    currentBars++;
                    currentCost += costs[i];
                }
            }
            if (currentCost <= coins) {
                maxBars = max(maxBars, currentBars);
            }
        }
        return maxBars;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of ice cream bars. This is because we are generating all possible combinations of buying ice cream bars.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum number of bars and the current combination.
> - **Why these complexities occur:** The exponential time complexity occurs because we are using a brute force approach to try all possible combinations.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to sort the costs of ice cream bars in ascending order and then buy the bars with the lowest costs first.
- This approach ensures that we are always buying the maximum number of bars with the given amount of money.
- We can use a greedy algorithm to implement this approach.

```cpp
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(), costs.end());
        int maxBars = 0;
        for (int cost : costs) {
            if (coins >= cost) {
                maxBars++;
                coins -= cost;
            } else {
                break;
            }
        }
        return maxBars;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of ice cream bars. This is because we are sorting the costs of ice cream bars.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum number of bars and the current cost.
> - **Optimality proof:** This approach is optimal because it ensures that we are always buying the maximum number of bars with the given amount of money. By sorting the costs in ascending order, we are guaranteed to buy the bars with the lowest costs first, which maximizes the number of bars we can buy.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of a greedy algorithm to solve an optimization problem.
- The problem-solving pattern identified is to sort the input data in ascending order and then use a greedy approach to find the optimal solution.
- The optimization technique learned is to use a greedy algorithm to solve problems that have the optimal substructure property.

**Mistakes to Avoid:**
- A common implementation error is to forget to sort the costs of ice cream bars in ascending order.
- An edge case to watch for is when the input array is empty or when the total amount of money is 0.
- A performance pitfall is to use a brute force approach to solve the problem, which can lead to exponential time complexity.