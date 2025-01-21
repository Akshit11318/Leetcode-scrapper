## Maximum Energy Boost From Two Drinks

**Problem Link:** https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers representing the energy values of different drinks. The goal is to find the maximum energy boost that can be achieved by drinking two different drinks.
- Expected output format: The function should return the maximum energy boost as an integer.
- Key requirements and edge cases to consider: The input array will have at least 3 elements, and the energy values are non-negative integers. The maximum energy boost is achieved by finding the maximum sum of two different energy values.
- Example test cases with explanations:
  - Example 1: Input: `energy = [4, 6, 1, 2]`, Output: `10`. Explanation: Drinking the drinks with energy values 4 and 6 gives a total energy of 10.
  - Example 2: Input: `energy = [1, 3, 5]`, Output: `8`. Explanation: Drinking the drinks with energy values 3 and 5 gives a total energy of 8.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to try all possible pairs of drinks and find the maximum energy boost.
- Step-by-step breakdown of the solution:
  1. Iterate over the array of energy values.
  2. For each energy value, iterate over the remaining energy values to form pairs.
  3. Calculate the sum of each pair and keep track of the maximum sum found.
- Why this approach comes to mind first: This approach is intuitive because it exhaustively checks all possible combinations of drinks.

```cpp
int maximumEnergy(vector<int>& energy) {
    int maxEnergy = 0;
    for (int i = 0; i < energy.size(); i++) {
        for (int j = i + 1; j < energy.size(); j++) {
            maxEnergy = max(maxEnergy, energy[i] + energy[j]);
        }
    }
    return maxEnergy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of energy values. This is because we have two nested loops that iterate over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum energy.
> - **Why these complexities occur:** The time complexity is quadratic because we are checking all pairs of energy values, resulting in $n \times (n-1)$ comparisons. The space complexity is constant because we only need to store the maximum energy found so far.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all pairs of energy values, we can find the two maximum energy values in a single pass through the array.
- Detailed breakdown of the approach:
  1. Initialize variables to store the maximum and second maximum energy values.
  2. Iterate over the array of energy values.
  3. Update the maximum and second maximum energy values as we iterate.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, resulting in a linear time complexity.

```cpp
int maximumEnergy(vector<int>& energy) {
    int maxEnergy = INT_MIN;
    int secondMaxEnergy = INT_MIN;
    for (int e : energy) {
        if (e > maxEnergy) {
            secondMaxEnergy = maxEnergy;
            maxEnergy = e;
        } else if (e > secondMaxEnergy) {
            secondMaxEnergy = e;
        }
    }
    return maxEnergy + secondMaxEnergy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of energy values. This is because we only need to make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum and second maximum energy values.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem, which is linear. We cannot do better than this because we must at least look at each energy value once to find the maximum energy boost.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the maximum and second maximum values in an array, and using this to solve a problem efficiently.
- Problem-solving patterns identified: Looking for ways to reduce the number of comparisons or iterations needed to solve a problem.
- Optimization techniques learned: Using a single pass through the array to find the maximum and second maximum energy values.
- Similar problems to practice: Finding the maximum sum of three or more elements in an array, or finding the maximum product of two or more elements.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, or not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with only one or two elements, or arrays with negative energy values.
- Performance pitfalls: Using a brute force approach that has a high time complexity, or using too much memory.
- Testing considerations: Testing the function with different input sizes and types, and checking for correct output in all cases.