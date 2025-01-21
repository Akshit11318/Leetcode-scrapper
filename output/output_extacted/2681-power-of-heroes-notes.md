## Power of Heroes

**Problem Link:** https://leetcode.com/problems/power-of-heroes/description

**Problem Statement:**
- Input format and constraints: Given a list of heroes with their respective powers, determine the maximum power that can be achieved by selecting a subset of heroes such that no two heroes have the same power.
- Expected output format: The maximum power that can be achieved.
- Key requirements and edge cases to consider: Handle cases where the input list is empty, contains duplicate powers, or contains powers with different values.
- Example test cases with explanations:
  - Example 1: Input: `[1, 2, 3, 4, 5]`, Output: `15` (Select all heroes to achieve maximum power).
  - Example 2: Input: `[1, 1, 2, 2, 3]`, Output: `6` (Select one hero with power 1, one hero with power 2, and one hero with power 3 to achieve maximum power).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of the given list of heroes and calculate the total power for each subset.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the given list of heroes.
  2. For each subset, calculate the total power by summing up the powers of all heroes in the subset.
  3. Keep track of the maximum power achieved among all subsets.
- Why this approach comes to mind first: It is a straightforward approach to generate all possible subsets and calculate their total power.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int maxPower(std::vector<int>& heroes) {
    int maxPower = 0;
    int n = heroes.size();
    for (int mask = 0; mask < (1 << n); mask++) {
        std::vector<int> subset;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subset.push_back(heroes[i]);
            }
        }
        std::sort(subset.begin(), subset.end());
        int currentPower = 0;
        for (int i = 0; i < subset.size(); i++) {
            if (i == 0 || subset[i] != subset[i - 1]) {
                currentPower += subset[i];
            }
        }
        maxPower = std::max(maxPower, currentPower);
    }
    return maxPower;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot log(n))$ (Generating all subsets and sorting each subset).
> - **Space Complexity:** $O(n)$ (Storing the current subset).
> - **Why these complexities occur:** Generating all subsets has a time complexity of $O(2^n)$, and sorting each subset has a time complexity of $O(n \cdot log(n))$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the maximum power that can be achieved for each subset of powers.
- Detailed breakdown of the approach:
  1. Sort the list of heroes by their powers.
  2. Create a dynamic programming table to store the maximum power that can be achieved for each subset of powers.
  3. Fill the dynamic programming table by iterating through the sorted list of heroes and updating the maximum power for each subset.
- Proof of optimality: This approach has a time complexity of $O(n \cdot log(n))$, which is optimal because we need to sort the list of heroes.

```cpp
#include <vector>
#include <algorithm>

int maxPower(std::vector<int>& heroes) {
    std::sort(heroes.begin(), heroes.end());
    int maxPower = 0;
    int currentPower = 0;
    for (int i = 0; i < heroes.size(); i++) {
        if (i == 0 || heroes[i] != heroes[i - 1]) {
            currentPower += heroes[i];
            maxPower = std::max(maxPower, currentPower);
        }
    }
    return maxPower;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$ (Sorting the list of heroes).
> - **Space Complexity:** $O(1)$ (Not using any extra space).
> - **Optimality proof:** This approach is optimal because we only need to sort the list of heroes and iterate through it once to find the maximum power.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, sorting, and iteration.
- Problem-solving patterns identified: Using dynamic programming to store the maximum power for each subset of powers.
- Optimization techniques learned: Sorting the list of heroes to reduce the time complexity.
- Similar problems to practice: Problems that involve finding the maximum power or value by selecting a subset of elements.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input list.
- Edge cases to watch for: Duplicate powers, powers with different values.
- Performance pitfalls: Using a brute force approach that generates all possible subsets.
- Testing considerations: Testing the function with different input lists, including edge cases.