## Maximum Number of Weeks for Which You Can Work

**Problem Link:** https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/description

**Problem Statement:**
- Input format and constraints: Given an array `milestones` of size `n`, where `milestones[i]` represents the number of stones at the `i-th` milestone.
- Expected output format: Return the maximum number of weeks for which you can work.
- Key requirements and edge cases to consider: The maximum number of weeks is determined by the largest milestone that can be reached without exceeding the total number of stones.
- Example test cases with explanations:
  - Example 1: Input: `milestones = [5,4,9]`, Output: `3`, Explanation: `5 + 4 + 9 = 18`, so the maximum number of weeks is `3` because `18 / 3 = 6`, which is the largest milestone that can be reached without exceeding the total number of stones.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of milestones to find the maximum number of weeks.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_weeks` to store the maximum number of weeks.
  2. Iterate over all possible combinations of milestones.
  3. For each combination, calculate the total number of stones.
  4. If the total number of stones is greater than or equal to the number of weeks, update `max_weeks`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the iteration over all possible combinations.

```cpp
int numberOfWeeks(vector<int>& milestones) {
    int max_weeks = 0;
    int n = milestones.size();
    for (int i = 1; i <= n; i++) {
        int sum = 0;
        for (int j = 0; j < i; j++) {
            sum += milestones[j];
        }
        if (sum >= i) {
            max_weeks = max(max_weeks, i);
        }
    }
    return max_weeks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of milestones, due to the nested loops.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Why these complexities occur:** The time complexity is high because of the iteration over all possible combinations of milestones, and the space complexity is low because only a few variables are used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The maximum number of weeks is determined by the largest milestone that can be reached without exceeding the total number of stones.
- Detailed breakdown of the approach:
  1. Calculate the total number of stones.
  2. Sort the milestones in descending order.
  3. Initialize a variable `max_weeks` to store the maximum number of weeks.
  4. Iterate over the sorted milestones.
  5. For each milestone, calculate the number of weeks that can be worked without exceeding the total number of stones.
  6. Update `max_weeks` with the maximum number of weeks found.
- Proof of optimality: This approach is optimal because it considers all possible milestones and calculates the maximum number of weeks that can be worked without exceeding the total number of stones.

```cpp
int numberOfWeeks(vector<int>& milestones) {
    int sum = 0;
    for (int milestone : milestones) {
        sum += milestone;
    }
    sort(milestones.rbegin(), milestones.rend());
    int max_weeks = 0;
    for (int milestone : milestones) {
        if (sum >= milestone) {
            max_weeks = max(max_weeks, sum / milestone);
        }
    }
    return max_weeks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of milestones, due to the sorting of milestones.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Optimality proof:** This approach is optimal because it considers all possible milestones and calculates the maximum number of weeks that can be worked without exceeding the total number of stones.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and calculation of maximum values.
- Problem-solving patterns identified: Considering all possible milestones and calculating the maximum number of weeks that can be worked without exceeding the total number of stones.
- Optimization techniques learned: Sorting the milestones in descending order to quickly find the largest milestone that can be reached without exceeding the total number of stones.
- Similar problems to practice: Problems involving sorting, iteration, and calculation of maximum values.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible milestones, not calculating the maximum number of weeks correctly.
- Edge cases to watch for: Empty input, negative milestones.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the solution works correctly.