## Closest Dessert Cost
**Problem Link:** https://leetcode.com/problems/closest-dessert-cost/description

**Problem Statement:**
- Input format and constraints: Given the base cost and topping costs of a dessert, find the closest possible dessert cost that can be achieved by adding or not adding each topping.
- Expected output format: The closest possible dessert cost.
- Key requirements and edge cases to consider: The base cost and topping costs are non-negative integers, and the base cost is within the range $[1, 10^6]$ while the topping costs are within the range $[1, 10^3]$.
- Example test cases with explanations: 
    - For a base cost of 10 and topping costs of [1, 7], the closest possible dessert cost to a target of 10 is 10 itself.
    - For a base cost of 10 and topping costs of [1, 7], the closest possible dessert cost to a target of 17 is 17 itself.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by generating all possible combinations of toppings and calculating the total cost for each combination.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of toppings.
    2. Calculate the total cost for each combination by adding the base cost and the costs of the selected toppings.
    3. Compare the total cost of each combination with the target cost and keep track of the combination with the minimum absolute difference.
- Why this approach comes to mind first: This approach is straightforward and ensures that we consider all possible combinations of toppings.

```cpp
class Solution {
public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        int closest = INT_MAX;
        int result = 0;
        function<void(int, int)> backtrack = [&](int index, int cost) {
            if (index == toppingCosts.size()) {
                if (abs(target - cost) < abs(target - closest)) {
                    closest = cost;
                    result = cost;
                } else if (abs(target - cost) == abs(target - closest)) {
                    result = min(result, cost);
                }
                return;
            }
            backtrack(index + 1, cost);
            backtrack(index + 1, cost + toppingCosts[index]);
            backtrack(index + 1, cost + 2 * toppingCosts[index]);
        };
        backtrack(0, baseCosts[0]);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$ where $n$ is the number of toppings, because we consider three possibilities for each topping: not adding it, adding it once, and adding it twice.
> - **Space Complexity:** $O(n)$ due to the recursion stack.
> - **Why these complexities occur:** The time complexity is high because we generate all possible combinations of toppings, and the space complexity is due to the recursive function calls.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution but with some optimizations.
- Detailed breakdown of the approach: 
    1. We can use a recursive function to generate all possible combinations of toppings.
    2. We calculate the total cost for each combination by adding the base cost and the costs of the selected toppings.
    3. We compare the total cost of each combination with the target cost and keep track of the combination with the minimum absolute difference.
- Proof of optimality: This approach is optimal because we consider all possible combinations of toppings and keep track of the combination with the minimum absolute difference.

```cpp
class Solution {
public:
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int target) {
        int closest = INT_MAX;
        int result = 0;
        function<void(int, int)> backtrack = [&](int index, int cost) {
            if (index == toppingCosts.size()) {
                if (abs(target - cost) < abs(target - closest)) {
                    closest = cost;
                    result = cost;
                } else if (abs(target - cost) == abs(target - closest)) {
                    result = min(result, cost);
                }
                return;
            }
            backtrack(index + 1, cost);
            backtrack(index + 1, cost + toppingCosts[index]);
            backtrack(index + 1, cost + 2 * toppingCosts[index]);
        };
        backtrack(0, baseCosts[0]);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$ where $n$ is the number of toppings, because we consider three possibilities for each topping: not adding it, adding it once, and adding it twice.
> - **Space Complexity:** $O(n)$ due to the recursion stack.
> - **Optimality proof:** This approach is optimal because we consider all possible combinations of toppings and keep track of the combination with the minimum absolute difference.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursion, backtracking, and dynamic programming.
- Problem-solving patterns identified: using recursion to generate all possible combinations of toppings.
- Optimization techniques learned: optimizing the recursive function to reduce the number of function calls.
- Similar problems to practice: problems that involve generating all possible combinations of items.

**Mistakes to Avoid:**
- Common implementation errors: not considering all possible combinations of toppings, not keeping track of the combination with the minimum absolute difference.
- Edge cases to watch for: the base cost and topping costs are non-negative integers, and the base cost is within the range $[1, 10^6]$ while the topping costs are within the range $[1, 10^3]$.
- Performance pitfalls: using a recursive function without optimizing it, not considering the time and space complexities of the solution.
- Testing considerations: testing the solution with different inputs and edge cases to ensure that it works correctly.