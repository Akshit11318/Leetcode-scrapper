## Calculate Special Bonus
**Problem Link:** https://leetcode.com/problems/calculate-special-bonus/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers representing the `n` employees' scores.
- Expected output format: An array of integers representing the special bonus for each employee.
- Key requirements and edge cases to consider: If an employee's score is better than their neighbors, they receive a special bonus of 1. Employees on the edge (first and last) only have one neighbor to compare with.
- Example test cases with explanations:
  - For scores `[1, 2, 3]`, the output should be `[1, 0, 1]` because the first and last employees' scores are better than their neighbors.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate through the array and compare each score with its neighbors.
- Step-by-step breakdown of the solution:
  1. Initialize an array to store the special bonuses.
  2. Iterate through each score in the input array.
  3. For each score, check if it's better than its neighbors.
  4. If it is, mark the corresponding index in the special bonuses array as 1.
- Why this approach comes to mind first: It directly addresses the problem statement without requiring additional insights.

```cpp
vector<int> specialBonus(vector<int>& scores) {
    int n = scores.size();
    vector<int> bonuses(n, 0); // Initialize all bonuses to 0
    for (int i = 0; i < n; i++) {
        bool isBetter = true;
        if (i > 0 && scores[i] <= scores[i-1]) isBetter = false;
        if (i < n-1 && scores[i] <= scores[i+1]) isBetter = false;
        if (isBetter) bonuses[i] = 1;
    }
    return bonuses;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, because we're doing a constant amount of work for each employee.
> - **Space Complexity:** $O(n)$, because we're creating an additional array of the same size as the input to store the bonuses.
> - **Why these complexities occur:** The linear time complexity is due to the single pass through the input array, and the linear space complexity is due to the additional array needed to store the results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite efficient for this problem, with a linear time complexity. However, we can slightly optimize the code by reducing the number of comparisons for the edge cases.
- Detailed breakdown of the approach:
  1. Initialize the bonuses array as before.
  2. For the first employee, only compare with the next employee if they exist.
  3. For the last employee, only compare with the previous employee.
  4. For all other employees, compare with both neighbors.
- Proof of optimality: This approach still has a linear time complexity but reduces the constant factor by minimizing comparisons.

```cpp
vector<int> specialBonus(vector<int>& scores) {
    int n = scores.size();
    vector<int> bonuses(n, 0);
    for (int i = 0; i < n; i++) {
        if ((i == 0 || scores[i] > scores[i-1]) && 
            (i == n-1 || scores[i] > scores[i+1])) {
            bonuses[i] = 1;
        }
    }
    return bonuses;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we're still doing a constant amount of work for each employee.
> - **Space Complexity:** $O(n)$, because we still need an additional array of the same size as the input.
> - **Optimality proof:** The time complexity is optimal because we must at least look at each employee's score once to determine if they receive a bonus.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning and conditional checks.
- Problem-solving patterns identified: Directly addressing the problem statement and optimizing based on edge cases.
- Optimization techniques learned: Reducing the number of comparisons for edge cases.
- Similar problems to practice: Other problems involving array iterations and conditional checks.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (first and last elements) differently.
- Edge cases to watch for: Employees at the edges of the array.
- Performance pitfalls: Unnecessary comparisons or iterations.
- Testing considerations: Ensure to test with arrays of varying sizes, including edge cases like an array of length 1 or 2.