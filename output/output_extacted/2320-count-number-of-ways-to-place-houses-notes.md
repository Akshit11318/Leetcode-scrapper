## Count Number of Ways to Place Houses
**Problem Link:** https://leetcode.com/problems/count-number-of-ways-to-place-houses/description

**Problem Statement:**
- Input: Two integers `totalPlots` and `numHouses`.
- Constraints: $1 \leq totalPlots \leq 100$ and $0 \leq numHouses \leq totalPlots$.
- Expected Output: The number of ways to place `numHouses` houses on `totalPlots` plots such that no two houses are adjacent.
- Key Requirements:
  - Each house can be placed on any plot, but no two houses can be adjacent.
  - A plot can either have a house or not have a house.
- Edge Cases:
  - If `numHouses` is 0, there is only one way to place houses (i.e., not placing any houses).
  - If `totalPlots` equals `numHouses`, there are no valid ways to place houses since they cannot be adjacent.
- Example Test Cases:
  - For `totalPlots = 4` and `numHouses = 2`, there are 3 ways: [H _ H _], [H _ _ H], and [_ H _ H].
  - For `totalPlots = 6` and `numHouses = 3`, there are 5 ways: [H _ H _ H _], [H _ H _ _ H], [H _ _ H _ H], [_ H _ H _ H], and [_ H _ H _ H].

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of placing houses on plots.
- We use a recursive function to place houses one by one, ensuring that no two houses are adjacent.
- We start by placing a house on the first plot and then recursively try to place the remaining houses on the subsequent plots, skipping one plot after each house.

```cpp
#include <vector>
#include <iostream>

int countWays(int totalPlots, int numHouses) {
    if (numHouses == 0) return 1; // Base case: no houses to place
    if (totalPlots < numHouses || totalPlots < 2 * numHouses - 1) return 0; // Not enough plots to place houses without being adjacent
    
    std::vector<int> plots(totalPlots, 0); // Initialize plots as empty
    
    return countWaysHelper(plots, numHouses, 0);
}

int countWaysHelper(std::vector<int>& plots, int numHouses, int index) {
    if (numHouses == 0) return 1; // Base case: all houses placed
    if (index >= plots.size()) return 0; // Not enough plots left
    
    int ways = 0;
    
    // Try placing a house at the current index
    if (index == 0 || plots[index - 1] == 0) {
        plots[index] = 1; // Place a house
        ways += countWaysHelper(plots, numHouses - 1, index + 2); // Recursively place the next house
        plots[index] = 0; // Backtrack
    }
    
    // Try not placing a house at the current index
    ways += countWaysHelper(plots, numHouses, index + 1);
    
    return ways;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{totalPlots})$ in the worst case, as we potentially explore all possible configurations of plots.
> - **Space Complexity:** $O(totalPlots)$ for the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible configurations, leading to exponential time complexity, and uses recursive calls, which consume stack space.

---

### Optimal Approach (Required)

**Explanation:**
- We recognize that this problem is similar to the Fibonacci sequence, where each number is the sum of the two preceding ones.
- The key insight is that the number of ways to place `numHouses` houses on `totalPlots` plots without any two houses being adjacent is equivalent to choosing `numHouses` positions out of `totalPlots - numHouses + 1` positions (since we need to leave at least one plot empty between houses).
- This can be solved using dynamic programming or combinatorial methods.

```cpp
int countWays(int totalPlots, int numHouses) {
    if (numHouses == 0) return 1; // Base case: no houses to place
    if (totalPlots < numHouses || totalPlots < 2 * numHouses - 1) return 0; // Not enough plots to place houses without being adjacent
    
    std::vector<int> dp(totalPlots + 1, 0);
    dp[0] = 1; // Base case for dynamic programming
    
    for (int i = 1; i <= totalPlots; i++) {
        dp[i] = dp[i - 1]; // Not placing a house
        if (i >= 2) {
            dp[i] += dp[i - 2]; // Placing a house
        }
    }
    
    return dp[totalPlots];
}
```

Alternatively, recognizing the problem as a combinatorial one, we can use the formula for combinations to directly calculate the result without needing to iterate through all possibilities.

```cpp
int countWays(int totalPlots, int numHouses) {
    if (numHouses == 0) return 1; // Base case: no houses to place
    if (totalPlots < numHouses || totalPlots < 2 * numHouses - 1) return 0; // Not enough plots to place houses without being adjacent
    
    int n = totalPlots - numHouses + 1;
    int k = numHouses;
    
    // Calculate combination using the formula n! / (k! * (n-k)!)
    long long result = 1;
    for (int i = 1; i <= k; i++) {
        result = result * (n - i + 1) / i;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(totalPlots)$ for the dynamic programming approach and $O(numHouses)$ for the combinatorial approach.
> - **Space Complexity:** $O(totalPlots)$ for the dynamic programming approach and $O(1)$ for the combinatorial approach.
> - **Optimality proof:** The dynamic programming approach avoids redundant calculations by storing intermediate results, and the combinatorial approach directly calculates the result, making them both optimal.

---

### Final Notes

**Learning Points:**
- Recognizing patterns similar to known sequences (like Fibonacci) can lead to more efficient solutions.
- Dynamic programming can significantly reduce computational complexity by avoiding redundant calculations.
- Combinatorial problems can often be solved using direct formulas, which can be more efficient than iterative or recursive approaches.

**Mistakes to Avoid:**
- Not considering the adjacency constraint properly, leading to overcounting.
- Not optimizing the solution for larger inputs, resulting in performance issues.
- Not validating the inputs to handle edge cases correctly.