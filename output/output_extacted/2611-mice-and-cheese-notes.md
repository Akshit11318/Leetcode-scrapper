## Mice and Cheese
**Problem Link:** https://leetcode.com/problems/mice-and-cheese/description

**Problem Statement:**
- Input format and constraints: The problem takes two arrays of integers, `reward1` and `reward2`, representing the reward for each mouse to eat a piece of cheese from the first and second type of cheese, respectively. The goal is to maximize the total reward by selecting the optimal combination of cheese pieces for each mouse.
- Expected output format: The function should return the maximum total reward that can be achieved.
- Key requirements and edge cases to consider: The number of mice is equal to the number of cheese pieces of each type. Each mouse can eat one piece of cheese from either type.
- Example test cases with explanations: For example, given `reward1 = [1, 1, 3, 4]` and `reward2 = [4, 4, 1, 1]`, the maximum total reward is `10`, achieved by selecting the first two pieces from the second type of cheese and the last two pieces from the first type.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of cheese pieces for each mouse and calculating the total reward for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of cheese pieces for each mouse.
  2. For each combination, calculate the total reward by summing up the rewards for each mouse.
  3. Keep track of the maximum total reward found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that ensures all possibilities are considered.

```cpp
#include <vector>
#include <algorithm>

int miceAndCheese(std::vector<int>& reward1, std::vector<int>& reward2) {
    int n = reward1.size();
    int maxReward = 0;
    
    // Generate all possible combinations
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalReward = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                totalReward += reward1[i];
            } else {
                totalReward += reward2[i];
            }
        }
        maxReward = std::max(maxReward, totalReward);
    }
    
    return maxReward;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of mice, because we generate all possible combinations of cheese pieces for each mouse.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum total reward and the current combination.
> - **Why these complexities occur:** The time complexity is exponential because we try all possible combinations, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a greedy approach by sorting the differences between the rewards for each mouse and then selecting the cheese pieces with the highest differences.
- Detailed breakdown of the approach:
  1. Calculate the differences between the rewards for each mouse.
  2. Sort the differences in descending order.
  3. Select the cheese pieces with the highest differences.
- Proof of optimality: The greedy approach is optimal because it ensures that the maximum total reward is achieved by selecting the cheese pieces with the highest rewards.

```cpp
#include <vector>
#include <algorithm>

int miceAndCheese(std::vector<int>& reward1, std::vector<int>& reward2) {
    int n = reward1.size();
    std::vector<int> diff(n);
    
    // Calculate the differences between the rewards
    for (int i = 0; i < n; i++) {
        diff[i] = reward1[i] - reward2[i];
    }
    
    // Sort the differences in descending order
    std::sort(diff.rbegin(), diff.rend());
    
    int totalReward = 0;
    for (int i = 0; i < n; i++) {
        if (diff[i] > 0) {
            totalReward += reward1[i];
        } else {
            totalReward += reward2[i];
        }
    }
    
    return totalReward;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of mice, because we sort the differences between the rewards.
> - **Space Complexity:** $O(n)$, because we use a vector to store the differences between the rewards.
> - **Optimality proof:** The greedy approach is optimal because it ensures that the maximum total reward is achieved by selecting the cheese pieces with the highest rewards.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Finding the maximum total reward by selecting the optimal combination of cheese pieces.
- Optimization techniques learned: Using a greedy approach to solve the problem efficiently.
- Similar problems to practice: Other problems that involve finding the maximum total reward or selecting the optimal combination of items.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the differences between the rewards correctly.
- Edge cases to watch for: Handling cases where the number of mice is equal to the number of cheese pieces of each type.
- Performance pitfalls: Using an exponential time complexity algorithm instead of a greedy approach.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it produces the correct output.