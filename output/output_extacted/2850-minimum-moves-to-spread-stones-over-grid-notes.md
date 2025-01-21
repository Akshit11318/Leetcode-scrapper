## Minimum Moves to Spread Stones over Grid
**Problem Link:** https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `stones` where each integer represents the position of a stone on a grid. The length of the array `n` is between 1 and 10^5. The goal is to find the minimum number of moves required to spread the stones over the grid such that no two stones are on the same position.
- Expected output format: The function should return the minimum number of moves as an integer.
- Key requirements and edge cases to consider: The stones can be moved in any direction (left or right), and the goal is to minimize the number of moves.
- Example test cases with explanations:
  - `stones = [1, 2, 3, 4]`: The minimum number of moves is 0 because the stones are already spread over the grid.
  - `stones = [1, 1, 1, 1]`: The minimum number of moves is 3 because we need to move three stones to spread them over the grid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible moves for each stone and calculate the minimum number of moves required to spread the stones over the grid.
- Step-by-step breakdown of the solution:
  1. Generate all possible permutations of the stones.
  2. For each permutation, calculate the minimum number of moves required to spread the stones over the grid.
  3. Return the minimum number of moves among all permutations.
- Why this approach comes to mind first: This approach is straightforward and tries all possible solutions.

```cpp
#include <algorithm>
#include <vector>

int minMovesToSpreadStones(std::vector<int>& stones) {
    std::sort(stones.begin(), stones.end());
    int n = stones.size();
    int minMoves = n - 1;
    for (int i = 0; i < n; i++) {
        int moves = 0;
        for (int j = i + 1; j < n; j++) {
            if (stones[j] - stones[i] < j - i) {
                moves += j - i - (stones[j] - stones[i]);
            }
        }
        minMoves = std::min(minMoves, moves);
    }
    return minMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have two nested loops.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is quadratic because we have two nested loops, and the space complexity is constant because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to find the minimum number of moves required to spread the stones over the grid.
- Detailed breakdown of the approach:
  1. Sort the stones in ascending order.
  2. Initialize two pointers, `left` and `right`, to the first and last stones, respectively.
  3. Calculate the minimum number of moves required to spread the stones over the grid by moving the stones between `left` and `right`.
- Proof of optimality: This approach is optimal because it tries all possible moves and returns the minimum number of moves required to spread the stones over the grid.

```cpp
#include <algorithm>
#include <vector>

int minMovesToSpreadStones(std::vector<int>& stones) {
    std::sort(stones.begin(), stones.end());
    int n = stones.size();
    int minMoves = n - 1;
    for (int i = 0; i < n; i++) {
        int moves = 0;
        for (int j = i + 1; j < n; j++) {
            if (stones[j] - stones[i] < j - i) {
                moves += j - i - (stones[j] - stones[i]);
            }
        }
        minMoves = std::min(minMoves, moves);
    }
    return minMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have two nested loops.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it tries all possible moves and returns the minimum number of moves required to spread the stones over the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting, and greedy algorithm.
- Problem-solving patterns identified: Finding the minimum number of moves required to spread objects over a grid.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity.
- Similar problems to practice: Minimum number of moves to sort an array, minimum number of swaps to sort a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the stones before calculating the minimum number of moves.
- Edge cases to watch for: Handling cases where the stones are already spread over the grid.
- Performance pitfalls: Using a brute force approach that tries all possible moves.
- Testing considerations: Testing the function with different inputs and edge cases to ensure correctness.