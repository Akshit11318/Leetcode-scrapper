## Maximum Strength of a Group
**Problem Link:** https://leetcode.com/problems/maximum-strength-of-a-group/description

**Problem Statement:**
- Input format and constraints: The input is a 2D vector `strength` where each element is a vector of two integers representing the strength of a person in two different groups. The output should be the maximum total strength of a group.
- Expected output format: The function should return an integer representing the maximum total strength.
- Key requirements and edge cases to consider: The function should handle cases where the input is empty or where the number of people is odd. It should also handle cases where the strength of a person in one group is greater than or less than their strength in the other group.
- Example test cases with explanations:
  - Example 1: `strength = [[1,3],[2,2],[3,1]]`, the function should return `4` because the maximum total strength is achieved when the group consists of the first and third persons.
  - Example 2: `strength = [[1,2],[2,3],[3,1]]`, the function should return `4` because the maximum total strength is achieved when the group consists of the first and second persons.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of people and calculating the total strength for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of people.
  2. For each combination, calculate the total strength by summing the strengths of the people in the combination.
  3. Keep track of the maximum total strength found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the number of combinations that need to be generated.

```cpp
#include <vector>
#include <algorithm>

int maxStrength(std::vector<std::vector<int>>& strength) {
    int n = strength.size();
    int maxStrength = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int currentStrength = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                currentStrength += strength[i][0];
            } else {
                currentStrength += strength[i][1];
            }
        }
        maxStrength = std::max(maxStrength, currentStrength);
    }
    return maxStrength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of people. This is because we are generating all possible combinations of people and calculating the total strength for each combination.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum total strength and the current combination.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible combinations of people, and the space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a bitmask to generate all possible combinations of people and calculating the total strength for each combination.
- Detailed breakdown of the approach:
  1. Use a bitmask to generate all possible combinations of people.
  2. For each combination, calculate the total strength by summing the strengths of the people in the combination.
  3. Keep track of the maximum total strength found so far.
- Proof of optimality: This approach is optimal because it generates all possible combinations of people and calculates the total strength for each combination, ensuring that the maximum total strength is found.
- Why further optimization is impossible: This approach is already optimal because it generates all possible combinations of people and calculates the total strength for each combination.

```cpp
#include <vector>
#include <algorithm>

int maxStrength(std::vector<std::vector<int>>& strength) {
    int n = strength.size();
    int maxStrength = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int currentStrength = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                currentStrength += strength[i][0];
            } else {
                currentStrength += strength[i][1];
            }
        }
        maxStrength = std::max(maxStrength, currentStrength);
    }
    return maxStrength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of people. This is because we are generating all possible combinations of people and calculating the total strength for each combination.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum total strength and the current combination.
> - **Optimality proof:** This approach is optimal because it generates all possible combinations of people and calculates the total strength for each combination, ensuring that the maximum total strength is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmasking, combination generation.
- Problem-solving patterns identified: Using a bitmask to generate all possible combinations of people.
- Optimization techniques learned: None, because this approach is already optimal.
- Similar problems to practice: Other problems that involve generating all possible combinations of people and calculating a total value.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input is empty.
- Edge cases to watch for: The case where the number of people is odd.
- Performance pitfalls: Not using a bitmask to generate all possible combinations of people, which can lead to a high time complexity.
- Testing considerations: Testing the function with different inputs, including the case where the input is empty and the case where the number of people is odd.