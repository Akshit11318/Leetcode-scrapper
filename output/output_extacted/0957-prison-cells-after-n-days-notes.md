## Prison Cells After N Days
**Problem Link:** https://leetcode.com/problems/prison-cells-after-n-days/description

**Problem Statement:**
- Input format and constraints: The input is an array of 8 integers representing the initial state of the prison cells and an integer `n` representing the number of days.
- Expected output format: An array of 8 integers representing the state of the prison cells after `n` days.
- Key requirements and edge cases to consider: The state of each cell is determined by the state of its two neighbors on the previous day. If the two neighbors are the same, the cell becomes 1; otherwise, it becomes 0.
- Example test cases with explanations:
  - For example, given the initial state `[0,1,0,1,1,0,0,1]` and `n = 7`, the output should be `[0,0,1,1,0,0,0,0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the process day by day, updating the state of each cell based on the states of its neighbors.
- Step-by-step breakdown of the solution:
  1. Initialize the current state with the given initial state.
  2. For each day from 1 to `n`, calculate the next state based on the current state.
  3. Update the current state with the next state.
- Why this approach comes to mind first: It directly simulates the described process, making it straightforward to understand and implement.

```cpp
#include <vector>
#include <iostream>

std::vector<int> prisonAfterNDays(std::vector<int>& cells, int n) {
    std::vector<int> nextState(8);
    for (int day = 0; day < n; ++day) {
        for (int i = 1; i < 7; ++i) {
            nextState[i] = (cells[i - 1] == cells[i + 1]) ? 1 : 0;
        }
        nextState[0] = nextState[7] = 0; // Boundaries are always 0
        cells = nextState;
    }
    return cells;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days. This is because we iterate through each day once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the current and next states.
> - **Why these complexities occur:** The time complexity is linear due to the simulation of each day, and the space complexity is constant because we only need to keep track of the current and next states, regardless of the number of days.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognizing that the state of the cells will eventually cycle after a certain number of days. This is because there are only $2^8 = 256$ possible states for the cells, and after at most 256 days, the state must either repeat or become periodic.
- Detailed breakdown of the approach:
  1. Calculate the state of the cells for the first 256 days to find the cycle.
  2. Determine the length of the cycle.
  3. Use the cycle length to find the state of the cells after `n` days without simulating every day.
- Proof of optimality: This approach is optimal because it takes advantage of the periodic nature of the cell states, reducing the number of simulations needed from $n$ to at most 256.

```cpp
std::vector<int> prisonAfterNDays(std::vector<int>& cells, int n) {
    std::vector<int> seen;
    std::vector<int> current = cells;
    bool cycleFound = false;
    int cycleLength = 0;
    int days = 0;
    
    while (!cycleFound && days <= 100) {
        seen.push_back(hash(current));
        nextDay(current);
        days++;
        for (int i = 0; i < seen.size(); i++) {
            if (seen[i] == hash(current)) {
                cycleFound = true;
                cycleLength = days - i;
                break;
            }
        }
    }
    
    n = (n - 1) % cycleLength + 1;
    for (int i = 0; i < n; i++) {
        nextDay(cells);
    }
    
    return cells;
}

void nextDay(std::vector<int>& cells) {
    std::vector<int> nextState(8);
    for (int i = 1; i < 7; ++i) {
        nextState[i] = (cells[i - 1] == cells[i + 1]) ? 1 : 0;
    }
    nextState[0] = nextState[7] = 0; // Boundaries are always 0
    cells = nextState;
}

int hash(const std::vector<int>& cells) {
    int hash = 0;
    for (int i = 0; i < cells.size(); i++) {
        hash = hash * 2 + cells[i];
    }
    return hash;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only simulate at most 256 days to find the cycle, and then calculate the final state based on the cycle length.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the seen states and the current state.
> - **Optimality proof:** This approach is optimal because it minimizes the number of simulations needed by taking advantage of the periodic nature of the cell states.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, cycle detection, and periodicity.
- Problem-solving patterns identified: Looking for periodic behavior in problems that involve repeated operations.
- Optimization techniques learned: Using cycle detection to reduce the number of simulations needed.
- Similar problems to practice: Other problems involving simulation and periodic behavior.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when `n` is 0 or when the initial state is already in a cycle.
- Edge cases to watch for: The boundaries of the cells are always 0, and the cycle length may be less than 256.
- Performance pitfalls: Simulating every day without considering the periodic nature of the cell states.
- Testing considerations: Test the function with different initial states and values of `n` to ensure it handles all cases correctly.