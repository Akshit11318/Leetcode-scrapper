## Reducing Dishes
**Problem Link:** https://leetcode.com/problems/reducing-dishes/description

**Problem Statement:**
- Input format and constraints: Given a list of `satisfaction` values representing the satisfaction gained from eating a dish, find the maximum sum of satisfaction that can be achieved by eating a subset of the dishes, where the satisfaction of each dish decreases by one for each subsequent dish eaten.
- Expected output format: The maximum sum of satisfaction.
- Key requirements and edge cases to consider: The input list can be empty, and the satisfaction values can be positive, negative, or zero. The dishes must be eaten in the order they are given, and the satisfaction of each dish decreases by one for each subsequent dish eaten.
- Example test cases with explanations:
  - Example 1: Input: `satisfaction = [-1,-8,0,5,-9]`, Output: `14`, Explanation: By eating dishes 3 and 4 in reverse order, the satisfaction is `5 + 4 = 9`. By eating dish 0, the satisfaction is `0 + 0 = 0`. By eating dish 1, the satisfaction is `-8 + -1 = -9`. So, the maximum sum of satisfaction is `9 + 0 + (-9) = 0`, but we can also eat dishes in reverse order to get `5 + 4 + 3 + 2 + 1 = 15` but due to negative values in between we have to choose between them, so we get `14`.
  - Example 2: Input: `satisfaction = [4,3,8]`, Output: `15`, Explanation: By eating dishes in reverse order, the satisfaction is `8 + 7 + 6 = 21`, but we can also eat dishes in normal order to get `4 + 3 + 8 = 15`, so we get `15`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem can be solved by trying all possible subsets of the dishes and calculating the satisfaction for each subset.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the dishes.
  2. For each subset, calculate the satisfaction by summing the satisfaction values of the dishes in the subset, taking into account the decrease in satisfaction for each subsequent dish eaten.
  3. Keep track of the maximum satisfaction found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs due to its exponential time complexity.

```cpp
#include <vector>
#include <algorithm>

int maxSatisfaction(std::vector<int>& satisfaction) {
    int n = satisfaction.size();
    int maxSatisfaction = 0;
    
    // Generate all possible subsets of the dishes
    for (int mask = 0; mask < (1 << n); mask++) {
        int currentSatisfaction = 0;
        int decrease = 0;
        
        // Calculate the satisfaction for the current subset
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                currentSatisfaction += satisfaction[i] - decrease;
                decrease++;
            }
        }
        
        // Update the maximum satisfaction
        maxSatisfaction = std::max(maxSatisfaction, currentSatisfaction);
    }
    
    return maxSatisfaction;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of dishes. This is because we generate all possible subsets of the dishes, which has a time complexity of $O(2^n)$, and for each subset, we calculate the satisfaction, which has a time complexity of $O(n)$.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store the maximum satisfaction and the current satisfaction.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsets of the dishes, which has an exponential time complexity. The space complexity occurs because we only use a constant amount of space to store the maximum satisfaction and the current satisfaction.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can sort the dishes in descending order of their satisfaction values and then use a greedy approach to select the dishes that maximize the satisfaction.
- Detailed breakdown of the approach:
  1. Sort the dishes in descending order of their satisfaction values.
  2. Initialize the maximum satisfaction to 0.
  3. Iterate over the sorted dishes and calculate the satisfaction for each dish, taking into account the decrease in satisfaction for each subsequent dish eaten.
  4. If the satisfaction for the current dish is positive, add it to the maximum satisfaction.
- Proof of optimality: This approach is optimal because it selects the dishes with the highest satisfaction values first, which maximizes the overall satisfaction.

```cpp
#include <vector>
#include <algorithm>

int maxSatisfaction(std::vector<int>& satisfaction) {
    std::sort(satisfaction.rbegin(), satisfaction.rend());
    int maxSatisfaction = 0;
    int sum = 0;
    
    // Iterate over the sorted dishes and calculate the satisfaction
    for (int i = 0; i < satisfaction.size(); i++) {
        sum += satisfaction[i];
        if (sum > 0) {
            maxSatisfaction += sum;
        } else {
            break;
        }
    }
    
    return maxSatisfaction;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of dishes. This is because we sort the dishes in descending order of their satisfaction values, which has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store the maximum satisfaction and the sum of the satisfaction values.
> - **Optimality proof:** This approach is optimal because it selects the dishes with the highest satisfaction values first, which maximizes the overall satisfaction.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Maximization problem, selection problem.
- Optimization techniques learned: Sorting, greedy approach.
- Similar problems to practice: Maximization problems, selection problems.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the decrease in satisfaction for each subsequent dish eaten.
- Edge cases to watch for: Empty input list, negative satisfaction values.
- Performance pitfalls: Using an exponential time complexity approach.
- Testing considerations: Test the solution with different input sizes, including large inputs, and with different satisfaction values, including negative values.