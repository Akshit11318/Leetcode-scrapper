## Minimum Amount of Time to Fill Cups

**Problem Link:** https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description

**Problem Statement:**
- Input format and constraints: Given an integer array `amount` of size `n`, representing the amount of water in each cup, and an integer `numExchange`, representing the number of times we can exchange a cup of water with the `amount` array.
- Expected output format: The minimum amount of time to fill all cups.
- Key requirements and edge cases to consider: The amount of water in each cup is non-negative, and the number of exchanges is non-negative.
- Example test cases with explanations: 
  - For `amount = [1,2,3]` and `numExchange = 1`, the minimum amount of time to fill all cups is `3`.
  - For `amount = [1,2,3,4]` and `numExchange = 3`, the minimum amount of time to fill all cups is `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of exchanges to find the minimum time.
- Step-by-step breakdown of the solution: 
  1. Generate all possible combinations of exchanges.
  2. For each combination, calculate the time to fill all cups.
  3. Keep track of the minimum time found.
- Why this approach comes to mind first: It is a straightforward way to solve the problem, but it is inefficient due to the large number of combinations.

```cpp
#include <vector>
#include <algorithm>

int minTimeToFillCups(std::vector<int>& amount, int numExchange) {
    // Sort the amount array in descending order
    std::sort(amount.rbegin(), amount.rend());
    
    int time = 0;
    for (int i = 0; i < amount.size(); i++) {
        // If we have exchanges left, exchange the current cup with the smallest cup
        if (numExchange > 0 && i > 0) {
            numExchange--;
            time += amount[i - 1];
        } else {
            time += amount[i];
        }
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the `amount` array, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and we only use a constant amount of space to store the time and exchange variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can always exchange the cup with the largest amount of water with the cup that has the smallest amount of water.
- Detailed breakdown of the approach: 
  1. Sort the `amount` array in descending order.
  2. Initialize the time to fill all cups to the sum of the `amount` array.
  3. For each exchange, subtract the difference between the largest and smallest cups from the time.
- Proof of optimality: This approach is optimal because it always exchanges the cup with the largest amount of water with the cup that has the smallest amount of water, which minimizes the time to fill all cups.
- Why further optimization is impossible: We have already minimized the time to fill all cups by always exchanging the cup with the largest amount of water with the cup that has the smallest amount of water.

```cpp
#include <vector>
#include <algorithm>

int minTimeToFillCups(std::vector<int>& amount, int numExchange) {
    // Sort the amount array in descending order
    std::sort(amount.rbegin(), amount.rend());
    
    int time = 0;
    for (int i = 0; i < amount.size(); i++) {
        time += amount[i];
    }
    
    for (int i = 0; i < numExchange; i++) {
        // If we have exchanges left, exchange the current cup with the smallest cup
        if (i < amount.size() - 1) {
            time -= (amount[0] - amount[amount.size() - 1]);
            // Update the amount array
            amount[0] = amount[amount.size() - 1];
            std::sort(amount.rbegin(), amount.rend());
        } else {
            break;
        }
    }
    return time;
}
```

However, the above code can be optimized further by realizing that we don't need to actually sort and update the array after each exchange. We can simply calculate the minimum time by subtracting the difference between the largest and smallest cups from the total time for each exchange.

```cpp
#include <vector>
#include <algorithm>

int minTimeToFillCups(std::vector<int>& amount, int numExchange) {
    // Sort the amount array in descending order
    std::sort(amount.rbegin(), amount.rend());
    
    int time = 0;
    for (int i = 0; i < amount.size(); i++) {
        time += amount[i];
    }
    
    for (int i = 0; i < numExchange && i < amount.size() - 1; i++) {
        // If we have exchanges left, exchange the current cup with the smallest cup
        time -= (amount[0] - amount[amount.size() - 1]);
        // Update the amount array
        // amount[0] = amount[amount.size() - 1];
        // std::sort(amount.rbegin(), amount.rend());
        // We can simply consider the next largest cup for the next exchange
        amount[0] = amount[1];
    }
    return time;
}
```

But even the above code can be optimized further. 

```cpp
#include <vector>
#include <algorithm>

int minTimeToFillCups(std::vector<int>& amount, int numExchange) {
    // Sort the amount array in descending order
    std::sort(amount.rbegin(), amount.rend());
    
    int time = 0;
    for (int i = 0; i < amount.size(); i++) {
        time += amount[i];
    }
    
    for (int i = 0; i < numExchange && i < amount.size() - 1; i++) {
        // If we have exchanges left, exchange the current cup with the smallest cup
        time -= (amount[0] - amount[amount.size() - 1]);
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the `amount` array, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it always exchanges the cup with the largest amount of water with the cup that has the smallest amount of water, which minimizes the time to fill all cups.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithms.
- Problem-solving patterns identified: Always try to find the optimal solution by considering the best possible exchange at each step.
- Optimization techniques learned: Avoid unnecessary operations by only updating the time variable.
- Similar problems to practice: Other problems that involve finding the minimum or maximum value by exchanging or modifying elements in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the `amount` array in descending order.
- Edge cases to watch for: When the number of exchanges is greater than or equal to the size of the `amount` array.
- Performance pitfalls: Using unnecessary operations or not optimizing the solution.
- Testing considerations: Test the solution with different inputs, including edge cases.