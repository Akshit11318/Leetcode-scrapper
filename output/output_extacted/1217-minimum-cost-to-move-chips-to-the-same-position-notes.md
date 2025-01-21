## Minimum Cost to Move Chips to the Same Position

**Problem Link:** https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/description

**Problem Statement:**
- Input format and constraints: The problem involves an array of integers representing the positions of chips on a number line. The goal is to move all chips to the same position with minimum cost, where the cost of moving a chip is 0 if it's moved to an adjacent position (i.e., one unit away) and 1 otherwise.
- Expected output format: The function should return the minimum cost to move all chips to the same position.
- Key requirements and edge cases to consider: The input array can contain duplicate positions, and the number of chips at each position can vary. The function should handle these cases efficiently.
- Example test cases with explanations:
  - For the input `[1, 1000000000]`, the output should be `1` because we can move the chip at position 1 to position 1000000000 at a cost of 1.
  - For the input `[2, 2, 2, 3, 3]`, the output should be `2` because we can move the two chips at position 3 to position 2 at a cost of 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible positions and calculating the cost of moving all chips to each position.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible positions (from the minimum to the maximum position in the input array).
  2. For each position, calculate the cost of moving all chips to that position.
  3. Keep track of the minimum cost found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the iteration over all possible positions.

```cpp
int minCostToMoveChips(vector<int>& position) {
    int minCost = INT_MAX;
    for (int pos = *min_element(position.begin(), position.end()); 
         pos <= *max_element(position.begin(), position.end()); pos++) {
        int cost = 0;
        for (int chip : position) {
            cost += (abs(chip - pos) % 2 == 1) ? 1 : 0;
        }
        minCost = min(minCost, cost);
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of chips and $m$ is the range of positions. This is because we iterate over all possible positions and for each position, we iterate over all chips.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and the current position.
> - **Why these complexities occur:** The high time complexity occurs because we try all possible positions, which can be large if the range of positions is large. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can observe that the cost of moving a chip to a position is 0 if the chip is already at an even or odd position, and 1 otherwise. Therefore, we can simply count the number of chips at odd positions and the number of chips at even positions, and return the minimum of these two counts.
- Detailed breakdown of the approach:
  1. Initialize two counters, one for odd positions and one for even positions.
  2. Iterate over the input array and increment the corresponding counter for each chip.
  3. Return the minimum of the two counters.
- Proof of optimality: This approach is optimal because it directly calculates the minimum cost by counting the number of chips that need to be moved.

```cpp
int minCostToMoveChips(vector<int>& position) {
    int oddCount = 0, evenCount = 0;
    for (int chip : position) {
        if (chip % 2 == 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }
    return min(oddCount, evenCount);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of chips. This is because we only need to iterate over the input array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counters.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum cost by counting the number of chips that need to be moved, which is the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of observing patterns and simplifying the problem statement to find an optimal solution.
- Problem-solving patterns identified: The problem requires identifying the key insight that leads to the optimal solution, which is counting the number of chips at odd and even positions.
- Optimization techniques learned: The problem demonstrates the use of simple counting to optimize the solution.
- Similar problems to practice: Other problems that involve counting and pattern observation, such as counting the number of elements in an array that satisfy a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize counters or variables, or using incorrect logic to calculate the minimum cost.
- Edge cases to watch for: Handling cases where the input array is empty or contains only one element.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Testing the function with different input cases, including edge cases, to ensure that it produces the correct output.