## Moving Stones Until Consecutive
**Problem Link:** https://leetcode.com/problems/moving-stones-until-consecutive/description

**Problem Statement:**
- Input format and constraints: The problem involves three stones, each represented by an integer. The input is three integers `a`, `b`, and `c`, where `1 ≤ a < b < c ≤ 100`. The goal is to move these stones to consecutive positions.
- Expected output format: The output should be an array of two integers, representing the minimum number of moves required to move the stones to consecutive positions and the maximum number of moves required.
- Key requirements and edge cases to consider: The stones can only be moved to an empty space, and we cannot move a stone to a position that is occupied by another stone.
- Example test cases with explanations:
  - For input `a = 1, b = 2, c = 3`, the output should be `[0, 0]` because the stones are already in consecutive positions.
  - For input `a = 1, b = 3, c = 5`, the output should be `[1, 2]` because we can move one stone to an adjacent position in one move, and we can move two stones to non-adjacent positions in two moves.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible moves and calculate the minimum and maximum number of moves required.
- Step-by-step breakdown of the solution:
  1. Generate all possible positions for the stones.
  2. For each position, calculate the number of moves required to move the stones to consecutive positions.
  3. Keep track of the minimum and maximum number of moves required.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it involves trying all possible moves.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> numMovesStones(int a, int b, int c) {
    int minMoves = 2;
    int maxMoves = 0;
    // Try all possible positions
    for (int i = 1; i <= 100; i++) {
        for (int j = i + 1; j <= 100; j++) {
            for (int k = j + 1; k <= 100; k++) {
                int moves = 0;
                if (a != i) moves++;
                if (b != j) moves++;
                if (c != k) moves++;
                minMoves = min(minMoves, moves);
                maxMoves = max(maxMoves, moves);
            }
        }
    }
    return {minMoves, maxMoves};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of possible positions. In this case, $n = 100$.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum and maximum number of moves.
> - **Why these complexities occur:** The time complexity is cubic because we have three nested loops, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can move the stones to consecutive positions in at most two moves. We can do this by moving the middle stone to an adjacent position, and then moving the other two stones to consecutive positions.
- Detailed breakdown of the approach:
  1. Calculate the minimum number of moves required to move the stones to consecutive positions. If the stones are already in consecutive positions, the minimum number of moves is 0. Otherwise, if the gap between the first two stones is 1 or the gap between the last two stones is 1, the minimum number of moves is 1. Otherwise, the minimum number of moves is 2.
  2. Calculate the maximum number of moves required to move the stones to consecutive positions. The maximum number of moves is 2, because we can move the stones to consecutive positions in at most two moves.
- Proof of optimality: The optimal solution is optimal because it uses the minimum number of moves required to move the stones to consecutive positions.

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> numMovesStones(int a, int b, int c) {
    int minMoves = 2;
    if (b - a == 1 && c - b == 1) minMoves = 0;
    else if (b - a <= 2 || c - b <= 2) minMoves = 1;
    return {minMoves, 2};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only perform a constant number of operations.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum and maximum number of moves.
> - **Optimality proof:** The optimal solution is optimal because it uses the minimum number of moves required to move the stones to consecutive positions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of minimizing the number of moves required to move objects to a certain position.
- Problem-solving patterns identified: The problem requires the use of a greedy algorithm to find the minimum number of moves required.
- Optimization techniques learned: The problem demonstrates the use of optimization techniques to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve minimizing the number of moves required to move objects to a certain position, such as the "Minimize the Sum of Absolute Differences" problem.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is to use a brute force approach, which can result in a high time complexity.
- Edge cases to watch for: One edge case to watch for is when the stones are already in consecutive positions, in which case the minimum number of moves is 0.
- Performance pitfalls: One performance pitfall is to use a high time complexity algorithm, which can result in slow performance for large inputs.
- Testing considerations: One testing consideration is to test the solution with different inputs, including edge cases, to ensure that it produces the correct output.